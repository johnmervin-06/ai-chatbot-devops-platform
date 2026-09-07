variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.medium" # llama3.2:1b needs real RAM; t2.micro will swap/OOM
}

variable "key_name" {
  description = "Name of an existing EC2 key pair for SSH access"
  type        = string
}

variable "allowed_ssh_cidr" {
  description = "CIDR allowed to SSH in (lock this down to your own IP, not 0.0.0.0/0)"
  type        = string
}

variable "app_port" {
  description = "Port the Flask/gunicorn app listens on"
  type        = number
  default     = 5000
}
