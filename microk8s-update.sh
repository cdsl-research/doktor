microk8s kubectl delete -f service/docker-web
microk8s kubectl delete -f service/docker-upload
microk8s kubectl delete -f service/docker-search

microk8s kubectl apply -f service/docker-web
microk8s kubectl apply -f service/docker-upload
microk8s kubectl apply -f service/docker-search