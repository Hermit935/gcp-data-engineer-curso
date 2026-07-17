resource "google_container_cluster" "primary" {
    name      = "mi-cluster-gke"
    location  = "us-central1-a"
    initial_node_count = 1
    node_config {
        machine_type = "e2-medium" # GKE requiere un poco mas de ram
        oauth_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
    }
}