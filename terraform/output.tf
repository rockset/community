# Note that this displays the api key when you run terraform apply,
# so for production use it should be pushed into a secrets store.
output "apikey" {
  value     = rockset_api_key.query-only.key
  sensitive = true
}
