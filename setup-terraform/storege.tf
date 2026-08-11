resource "mi-bucket-unico-935" "auto-expire" {
    name                        = "mi-bucket-unico-935"
    location                    = "US"
    force_destroy               = true


    lifecycle_rule {
        condition {
            age = 30
        }
        action {
            type = "Delete"
        }
    }
}