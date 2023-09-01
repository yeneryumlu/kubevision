




## create test cluster
kind create cluster --config=cluster-install/kind-alpha.yaml
kind create cluster --config=cluster-install/kind-delta.yaml
kind create cluster --config=cluster-install/kind-lambda.yaml
kind create cluster --config=cluster-install/kind-theta.yaml

## install metrics server to all of the clusters
kubectl apply -f https://raw.githubusercontent.com/pythianarora/total-practice/master/sample-kubernetes-code/metrics-server.yaml

## get all pods
kubectl get pods -A

## create api token for all the clusters
kubectl create clusterrolebinding cluster_admin_role_binding --clusterrole=cluster-admin --serviceaccount=default:default
cat << EOF | kubectl create -f -
apiVersion: v1
kind: Secret
metadata:
  name: default-token
  namespace: default
  annotations:
    kubernetes.io/service-account.name: default
type: kubernetes.io/service-account-token
EOF

kubectl get secrets -o jsonpath="{.items[?(@.metadata.annotations['kubernetes\.io/service-account\.name']=='default')].data.token}" | base64 --decode


# to delete clusters
kind delete cluster --name alpha
kind delete cluster --name delta
kind delete cluster --name lambda
kind delete cluster --name theta





