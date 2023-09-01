import logging
from sqlalchemy import and_, select, text
from db.base import session_factory
from db.model import Cluster, Namespace, Node, NodeMetric
from datetime import datetime
from entity.entities import ClusterEntity
import json

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

class MetricsDAO(object):
    def create(self, cluster_name, version_info, nodes, namespaces):
        session = session_factory()
        
        found_cluster = session.query(Cluster).filter(Cluster.name == cluster_name).first()
        
        if not found_cluster:
            logging.info("cluster named '" + cluster_name + "' cannot be found.")
            return 404, "Cluster named '" + cluster_name + "' cannot be found."
        else:
            logging.debug("found cluster named '" + found_cluster.name + "'")
            found_cluster.status = "ready"
            found_cluster.version = version_info["major"] + "." + version_info["minor"]
            found_cluster.last_modified_time = datetime.now()
            session.commit()

        logging.debug("---namespaces---")
        for ns in namespaces:
            logging.debug("namespace: " + ns["name"])
            found_ns = session.query(Namespace).filter(Namespace.name == ns["name"]).first()
            if not found_ns:
                new_ns = Namespace(name=ns["name"])
                new_ns.clusters.append(found_cluster)
                session.add(new_ns)
                session.commit()
            else:
                logging.info("namespace '" + ns["name"] + "' already saved.")
                found = False
                for i in found_ns.clusters:
                    logging.debug("cluster_names: " + i.name + " - " + cluster_name)
                    if(i.name == cluster_name):
                        found = True
                if not found:
                    found_ns.clusters.append(found_cluster)
                    session.commit()
                    
        logging.debug("---nodes---")
        for node in nodes:
            logging.debug("node: " + node["name"])
            found_node = session.query(Node).filter(Node.name == node["name"]).first()
            if not found_node:
                logging.info("node named '" + node["name"] + "' will be created")
                new_node = Node(name=node["name"])
                new_node.cluster = found_cluster
                session.add(new_node)
                session.commit()
            else:
                logging.debug("node named '" + found_node.name + "' found")
                # check if node is connected to the cluster
                if( not (found_node.cluster.id == found_cluster.id)):
                    found_node.cluster_id = found_cluster.id
                    session.commit()

            logging.debug("---node metrics---")
            found_node = session.query(Node).filter(Node.name == node["name"]).first()
            if not found_node:
                logging.info("node named '" + node["name"] + "' cannot be found")
            else:
                found_metric = session.query(NodeMetric).filter(
                        and_(
                            NodeMetric.node_id == found_node.id,
                            NodeMetric.created_date == datetime.now().strftime("%Y-%m-%d")
                        )
                    ).first()
                if not found_metric:
                    logging.debug("new metric record will be created")
                    new_metric = NodeMetric(cpu_capacity=self.convert_cpu_capacity(node["cpu_capacity"]),
                                            memory_capacity=self.convert_memory(node["memory_capacity"]),
                                            cpu_usage=self.convert_cpu(node["cpu_usage"]),
                                            memory_usage=self.convert_memory(node["memory_usage"]))
                    new_metric.node_id = found_node.id
                    session.add(new_metric)
                    session.commit()
                else:
                    logging.info("metric for today has already been inserted")
        
        session.commit()
        session.close()
        return 201, "metrics created"

    def get_cluster_metrics(self):
        result = {
            "cpu_series": [],
            "memory_series": [],
            "categories": []
        }
        session = session_factory()
        rs = session.execute(text("select c.name, created_date, cpu_capacity, cpu_usage, memory_capacity, memory_usage from cluster_metrics cm  join cluster c on c.id = cm.cluster_id  where created_date BETWEEN NOW() - INTERVAL '8 DAYS' AND NOW() order by c.name, cm.created_date"))
        series = {}
        dates_list = []
        cluster_list = []
        for row in rs:
            cluster_name = row[0]
            created_date = row[1]
            cpu_capacity = row[2]
            cpu_usage = row[3]
            memory_capacity = row[4]
            memory_usage = row[5]
            
            if not cluster_name in cluster_list:
                cluster_list.append(cluster_name)
            if created_date not in dates_list:
                dates_list.append(created_date)
                result["categories"].append(created_date.strftime("%d/%m"))
            if series.get(cluster_name, {}) == {}:
                series[cluster_name] = {}
                series[cluster_name]["cpu_usage"] = [cpu_usage]
                series[cluster_name]["memory_usage"] = [memory_usage]
            else:
                series[cluster_name]["cpu_usage"].append(cpu_usage)
                series[cluster_name]["memory_usage"].append(memory_usage)

        for c in cluster_list:
            result["cpu_series"].append({"name":c, "data": series[c]["cpu_usage"]})
            result["memory_series"].append({"name":c, "data": series[c]["memory_usage"]})

        return result

    @staticmethod
    def convert_memory(inp: str):
        return int(inp.replace("Ki",""))/1000

    @staticmethod
    def convert_cpu(inp: str):
        return int(inp.replace("n",""))/1000000
    
    @staticmethod
    def convert_cpu_capacity(inp: str):
        return int(inp)*1000
