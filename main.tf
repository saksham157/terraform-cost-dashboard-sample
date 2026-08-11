provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c101f26f147fa7fd"
  instance_type = "t3.medium"
}

resource "aws_s3_bucket" "assets" {
  bucket = "cost-dashboard-sample-assets-saksham"
}

resource "aws_db_instance" "main" {
  identifier           = "cost-dashboard-sample-db"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  allocated_storage    = 20
  username             = "admin"
  password             = "changeme123!"
  skip_final_snapshot  = true
}