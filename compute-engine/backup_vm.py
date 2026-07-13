import argparse
from google.cloud import compute_v1

def create_snapshot(project_id, disk_name, snapshot_name, zone):
    disk_client = compute_v1.DisksClient()
    disk = f"projects/{project_id}/zones/{zone}/disks/{disk_name}"
    snapshot = compute_v1.Snapshot(name=snapshot_name, source_disk=disk)

    snapclient = compute_v1.SnapshotsClient()
    op = snapclient.insert(project=project_id, snapshot_resource=snapshot)
    op.result()  # Wait for the operation to complete
    print(f"Snapshot '{snapshot_name}' created for disk '{disk_name}' in project '{project_id}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a snapshot of a disk in Google Cloud.")
    parser.add_argument("--project_id", required=True, help="Google Cloud project ID")
    parser.add_argument("--disk_name", required=True, help="Name of the disk to snapshot")
    parser.add_argument("--snapshot_name", required=True, help="Name of the snapshot to create")
    parser.add_argument("--zone", required=True, help="Zone where the disk is located")

    args = parser.parse_args()

    create_snapshot(args.project_id, args.disk_name, args.snapshot_name, args.zone)