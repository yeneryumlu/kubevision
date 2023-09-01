

# to create test clusters
apply instructions from kind-docs.md

# to create postgresql in master(alpha) cluster
kubectl aply -f posgresql-deployment.yaml

# to create k8s-api in master(alpha) cluster
kubectl aply -f k8s-api-deployment.yaml

# to create collectors in all clusters
kubectl aply -f collector-deployment.yaml

