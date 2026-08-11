resource "google_storage_bucket" "auto_expire" {
    name                        = "mi-bucket-unico-935"
    location                    = "US"
    force_destroy               = true
    uniform_bucket_level_access = true

    lifecycle_rule {
        condition {
            age = 30
        }
        action {
            type = "Delete"
        }
    }
}