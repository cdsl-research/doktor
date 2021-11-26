from kubernetes import client, config  # Kubernetesからclient,configを読み込む
import json
config.load_kube_config()  # kubernetesのConfigファイルを読み込む
api = client.CustomObjectsApi()
v1 = client.CoreV1Api()
resource = api.list_namespaced_custom_object(
    group="metrics.k8s.io",
    version="v1beta1",
    namespace="default",
    plural="pods")


def load():
    all_array = []
    #print(json.dumps(resource,ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': ')))
    for pod in resource["items"]:
        s = pod["metadata"]["name"], pod['containers'][0]["usage"]["cpu"].replace(
            'n', '')
        if 'replicas-deployment-66d67548c5' in s[0]:
            all_array.append(s)
            # print(s)
    min = None
    min_name = ""
    for container in all_array:
        if min is None:
            min_name = container[0]
            min = int(container[1])
        elif int(container[1]) < min:
            min = int(container[1])
            min_name = container[0]
    print(min_name, min)
    result = {}
    # Configs can be set in Configuration class directly or using helper utility
    ##print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        if 'replicas-deployment-66d67548c5' in i.metadata.name:
            result[i.metadata.name] = i.status.pod_ip
            ##print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    # min_name,result[min_name]を戻り値としてload()に返す
    return min_name, result[min_name]


print(load())
