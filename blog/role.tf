resource rockset_role read-only {
  name = "blog-read-only"
  privilege {
    action        = "EXECUTE_QUERY_LAMBDA_WS"
    cluster       = "*ALL*"
    resource_name = rockset_workspace.blog.name
  }
}

resource "rockset_api_key" "ql-only" {
  name = "blog-ql-only"
  role = rockset_role.read-only.name
}

resource "aws_ssm_parameter" "api-key" {
  name  = "/rockset/blog/apikey"
  type  = "SecureString"
  value = rockset_api_key.ql-only.key
}
