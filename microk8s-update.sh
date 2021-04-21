microk8s kubectl delete -f service/website
microk8s kubectl delete -f service/upload
microk8s kubectl delete -f service/search

microk8s kubectl apply -f service/website
microk8s kubectl apply -f service/upload
microk8s kubectl apply -f service/search