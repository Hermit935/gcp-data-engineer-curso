gcloud container clusters get-credentials mi-cluster-gke --zone us-central1-a
gcloud components install gke-gcloud-auth-plugin
gcloud components install kubectl
kubectl get nodes
kubectl get namespaces