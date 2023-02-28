resource "time_sleep" "wait_30s" {
  depends_on      = [aws_iam_role.rockset]
  create_duration = "15s"
}

resource "rockset_s3_integration" "integration" {
  name         = var.bucket
  aws_role_arn = aws_iam_role.rockset.arn
  depends_on   = [time_sleep.wait_30s]
}

resource rockset_workspace blog {
  name = "blog"
}

resource "rockset_s3_collection" "movies" {
  name           = "movies-s3"
  workspace      = rockset_workspace.blog.name
  retention_secs = var.retention_secs
  source {
    format           = "json"
    integration_name = rockset_s3_integration.integration.name
    bucket           = var.bucket
    pattern          = "public/movies/*.json"
  }
}
#https
#2022-10-01T23:50:00.630375Z
#app/k8s-producti-apiserve-7bbfcb2efc/4d796a6a79177424
#70.132.18.81:27912
#10.0.40.238:8080
#0.000
#0.001
#0.000
#200
#200
#1028 524 "POST https://api.usw2a1.rockset.com:443/v1/receivers/kafka HTTP/1.1" "okhttp/3.9.1" ECDHE-RSA-AES128-GCM-SHA256 TLSv1.2 arn:aws:elasticloadbalancing:us-west-2:318212636800:targetgroup/k8s-producti-receiver-25d1dba86c/7ad56909ef107d6a "Root=1-6338d228-2887b4b0164d78fa32891ca0" "api.usw2a1.rockset.com" "session-reused" 2 2022-10-01T23:50:00.629000Z "forward" "-" "-" "10.0.40.238:8080" "200" "-" "-"
