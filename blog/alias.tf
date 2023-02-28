resource rockset_alias movies {
  collections = ["${rockset_workspace.blog.name}.${rockset_s3_collection.movies.name}"]
  name        = "movies"
  workspace   = rockset_workspace.blog.name
}
