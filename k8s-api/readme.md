



# to run postgresql db
docker run --name k8s-db -e POSTGRES_PASSWORD=*** -d -p 5432:5432 -v $HOME/docker/volumes/k8sdb:/var/lib/postgresql/data postgres

# to stop 
docker start k8s-db

# to start again
docker start k8s-db


# to build and push container image
docker build . -t yeneryumlu/k8s-api:x.y.z
docker push yeneryumlu/k8s-api:x.y.z









