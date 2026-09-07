output "instance_public_ip" {
  description = "Public IP of the chatbot EC2 instance"
  value       = aws_instance.chatbot.public_ip
}

output "chatbot_url" {
  description = "URL to reach the chatbot once the container is running"
  value       = "http://${aws_instance.chatbot.public_ip}:${var.app_port}"
}
