resource "google_monitoring_uptime_check_config" "http" {
    display_name = "http-uptime-check"
    timeout      = "10s"
    period       = "60s"

    http_check {
        path = "/"
        port = 80
    }

    monitored_resource {
        type = "uptime_url"
        labels = {
            project_id = "gcp-engineer-curso"
            host       = "10.0.1.2" 
        }
    }
}