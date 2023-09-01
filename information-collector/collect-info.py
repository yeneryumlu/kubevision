import os
import time
from datetime import datetime
import k8s

cluster_name = os.getenv("cluster_name")

while True:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    version_info = k8s.get_cluster_version()
    nodes = k8s.get_all_nodes()
    namespaces = k8s.get_namespaces()
    node_usages = k8s.get_node_usages()
    
    for node in nodes:
        for usage in node_usages:
            if(node.get("name") == usage.get("name")):
                node["cpu_usage"] = usage.get("cpu_usage")
                node["memory_usage"] = usage.get("memory_usage")
    
    print("---result---")
    print({"version_info": version_info, "name": cluster_name, "nodes": nodes, "namespaces": namespaces})
    
    time.sleep(86400)
