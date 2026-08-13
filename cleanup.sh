terraform destroy -auto-approve


gcloud sql instances delete my-instance-sql --quiet
gcloud functions delete funcion-prueba --region us-central1 --quiet
gcloud run services delete mi-servicio-run --region us-central1-a --quiet
gcloud container clusters delete mi-cluster-gke --zone us-central1-a --quiet