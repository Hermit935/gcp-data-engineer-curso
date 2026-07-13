gcloud compute instances list
gcloud compute instances describe servidor-web-1
python3 backup_vm.py --project_id gcp-engineer-curso --disk_name servidor-web-1  --snapshot_name snapshot-servidor-web-1 --zone  us-central1-a