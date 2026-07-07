gcloud iam service-accounts create dev-developer --display-name="Deployer SA"

# Asignar rol, (Principio de menor privilegio) 
gcloud projects add-iam-policy-binding gcp-engineer-curso --member="serviceAccount:dev-developer@gcp-engineer-curso.iam.gserviceaccount.com" --role="roles/compute.viewer"