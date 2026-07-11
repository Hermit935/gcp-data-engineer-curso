resource "google_compute_instance_template" "tpl" {
    name_prefix  = "app-tpl-"
    machine_type = "e2-micro"
    tags         = ["web-server"]
    disk {
        source_image  = "debian-cloud/debian-11"
    }
    network_interface {
        subnetwork = google_compute_subnetwork.subnet_us.id
    }
}

resource "google_compute_region_instance_group_manager" "mig" {
    name    = "app-mig"
    region  = "us-central1"
    base_instance_name = "app"
    version {
        instance_template = google_compute_instance_template.tpl.id
    }
    target_size = 2
}