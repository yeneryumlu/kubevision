from kubernetes import client, config
import json


def get_cluster_version():
    config.load_incluster_config()
    api = client.VersionApi()
    version_info = api.get_code()
    major_version = version_info.major
    minor_version = version_info.minor
    print("---version---")
    print("%s\t%s" % (major_version, minor_version))
    return {"major":major_version, "minor": minor_version}

def get_all_nodes():
    result = []
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    nodes = v1.list_node()
    print("---nodes---")
    # print(nodes)
    for node in nodes.items:
        name = node.metadata.name
        capacity = node.status.capacity
        cpu_capacity = capacity.get("cpu")
        memory_capacity = capacity.get("memory")
        print("%s\t%s\t%s" % (name, cpu_capacity, memory_capacity))
        result.append({"name": name, "cpu_capacity": cpu_capacity, "memory_capacity": memory_capacity})
    return result

def get_namespaces():
    result = []
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    nss = v1.list_namespace(watch=False)
    print("---namespaces---")
    # print(nss)
    for ns in nss.items:
        name = ns.metadata.name
        print("%s" % (name))
        result.append({"name": name})
    return result

def get_node_usages():
    result = []
    config.load_incluster_config()
    api = client.CustomObjectsApi()
    node_metrics = api.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "nodes")
    print("---metrics---")
    # print(node_metrics.get("items", []))
    for metric in node_metrics.get("items", []):
        name = metric.get("metadata", {}).get("name")
        cpu_usage = metric.get("usage", {}).get("cpu")
        memory_usage = metric.get("usage", {}).get("memory")
        print("%s\t%s\t%s" % (name, cpu_usage, memory_usage))
        result.append({"name": name, "cpu_usage": cpu_usage, "memory_usage": memory_usage})
    return result

def get_all_pods_in_all_namespaces():
    result = []
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False)
    print("---pods---")
    # print(pods)
    for pod in pods.items:
        ip = pod.status.pod_ip
        namespace = pod.metadata.namespace
        name = pod.metadata.name
        print("%s\t%s\t%s" % (ip, namespace, name))
        result.append({"name": name, "namespace": namespace, "ip": ip})
    return result
