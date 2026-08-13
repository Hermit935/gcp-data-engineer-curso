terraform destroy -auto-approve


gcloud sql instances delete my-sql-instance --quiet
gcloud functions delete function-prueba --region=us-central1 --quiet
gcloud run services delete mi-servicio-run --region=us-central1 --quiet
gcloud containers clusters delete mi-cluster-gke --zone=us-central1-a --quiet