resource "rockset_query_lambda" "top-rated" {
  name      = "top-rated-movies"
  workspace = rockset_workspace.blog.name
  sql {
    query = file("data/top-rated.sql")
  }
}

resource "rockset_query_lambda_tag" "stable" {
  name         = "stable"
  query_lambda = rockset_query_lambda.top-rated.name
  version      = var.stable_version == "" ? rockset_query_lambda.top-rated.version : var.stable_version
  workspace    = rockset_workspace.blog.name
}