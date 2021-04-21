kubectl delete -f service/docker-web
kubectl delete -f service/docker-upload
kubectl delete -f service/docker-search

kubectl apply -f service/docker-web
kubectl apply -f service/docker-upload
kubectl apply -f service/docker-search