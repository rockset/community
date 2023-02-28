data rockset_account current {}

resource "aws_iam_policy" "rockset-s3-integration" {
  name   = var.rockset_role_name
  policy = templatefile("${path.module}/data/policy.json", {
    bucket = var.bucket
    prefix = var.bucket_prefix
  })
}

resource "aws_iam_role" "rockset" {
  name               = var.rockset_role_name
  assume_role_policy = data.aws_iam_policy_document.rockset-trust-policy.json
}

data "aws_iam_policy_document" "rockset-trust-policy" {
  statement {
    sid     = ""
    effect  = "Allow"
    actions = [
      "sts:AssumeRole"
    ]
    principals {
      identifiers = [
        "arn:aws:iam::${data.rockset_account.current.account_id}:root"
      ]
      type = "AWS"
    }
    condition {
      test   = "StringEquals"
      values = [
        data.rockset_account.current.external_id
      ]
      variable = "sts:ExternalId"
    }
  }
}

resource "aws_iam_role_policy_attachment" "rockset_s3_integration" {
  role       = aws_iam_role.rockset.name
  policy_arn = aws_iam_policy.rockset-s3-integration.arn
}