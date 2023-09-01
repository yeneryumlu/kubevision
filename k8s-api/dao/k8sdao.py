from sqlalchemy import and_, orm, asc, desc, text
from db.base import session_factory
from db.model import Cluster, NodeMetric, Node, Namespace
from datetime import datetime
from entity.entities import ClusterEntity
import json
import logging

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

class K8sDAO(object):
    def get_all(self):
        session = session_factory()
        session.expire_on_commit = False
        db_clusters = session.query(Cluster).options(orm.joinedload(Cluster.nodes)).all()
        resp = []
        for cl in db_clusters:
            new_cl = ClusterEntity(cl.id, cl.name, cl.environment, cl.apiserver, cl.status, cl.version)
            resp.append(new_cl)
        session.close()
        return resp
        # for todo in self.todos:
        #     if todo["id"] == id:
        #         return todo
        # api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, name, environment, apiserver, token):
        session = session_factory()
        found_cluster = session.query(Cluster).filter(Cluster.name == name).first()
        if(not found_cluster):
            new_cl = Cluster(name=name, environment=environment, apiserver=apiserver, token=token, last_modified_time=datetime.now(), status="not ready", version="0")
            # obj = ClusterEntity(new_cl.id, new_cl.name, new_cl.environment, new_cl.apiserver, new_cl.status, new_cl.version)
            session.add(new_cl)
            session.commit()
            session.close()
            return True, "Cluster added successfully"
        else:
            logging.info("cluster named '" + name + "' is already in the database")
            session.close()
            return False, "cluster named '" + name + "' is already in the database"

    def get_cluster_detail(self, name):
        result = {}
        session = session_factory()
        db_cluster = session.query(Cluster).options(orm.joinedload(Cluster.nodes)).filter(
            and_(
                    Cluster.name == name
            )
        ).first()
        result["name"] = db_cluster.name
        result["environment"] = db_cluster.environment
        result["api_server"] = db_cluster.apiserver
        result["node_count"] = len(db_cluster.nodes)
        nodes = []
        for n in db_cluster.nodes:
            metric = session.query(NodeMetric).filter(
                and_(
                        NodeMetric.node_id == n.id
                )
            ).order_by(NodeMetric.created_date.desc()).first()
            nodes.append(
                {
                    "name": n.name,
                    "cpu_capacity": metric.cpu_capacity,
                    "memory_capacity": metric.memory_capacity,
                    "cpu_usage": metric.cpu_usage,
                    "memory_usage": metric.memory_usage,
                }
            )
        result["nodes"] = nodes
        session.close()
        return result
        
    def get_all_nodes(self):
        result = []
        session = session_factory()
        session.expire_on_commit = False
        db_nodes = session.query(Node).options(orm.joinedload(Node.cluster)).order_by(Node.name).all()
        for n in db_nodes:
            print(n.name)
            node = {}
            node["name"] = n.name
            node["cluster"] = n.cluster.name
            
            rs = session.execute(text("select nm.cpu_capacity, nm.memory_capacity from node_metric nm join node n on n.id = nm.node_id where n.name = '"+ n.name +"' order by created_date desc limit 1"))
            row = rs.fetchone()
            if row != None:
                node["cpu_capacity"] = row[0]
                node["memory_capacity"] = row[1]
            
            
            result.append(node)
        session.close()
        return result

    def get_all_namespaces(self):
        result = []
        session = session_factory()
        session.expire_on_commit = False
        db_namespaces = session.query(Namespace).order_by(Namespace.name).all()
        for n in db_namespaces:
            print(n.name)
            ns = {}
            ns["name"] = n.name
            
            rs = session.execute(text("select c.name from namespace n join cluster_namespace_association cna on cna.namespace_id = n.id join cluster c on c.id = cna.cluster_id where n.name = '" + n.name + "'"))
            clusters = [r[0] for r in rs]
            ns["clusterlist"] = ", ".join(clusters)
            
            result.append(ns)
        session.close()
        return result