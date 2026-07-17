kubectl create deployment nginx-app --image=nginx:latest
kubectl expose deployment nginx-app --type=LoadBalancer --port 80 --target-port 80
kubectl get services
kubectl get pods