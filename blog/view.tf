resource rockset_view english-movies {
  name       = "english-movies"
  query      = file("data/view.sql")
  workspace  = rockset_workspace.blog.name
  depends_on = [rockset_alias.movies]
}
