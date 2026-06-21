AI Chatbot DevOps Project Report
1. Introduction

This project demonstrates the implementation of a simple AI Chatbot application using DevOps practices. The chatbot backend was developed using Flask, containerized using Docker, automated with Jenkins, provisioned using Terraform, and deployed on an AWS EC2 instance. Monitoring and logging were configured using Amazon CloudWatch.

2. Objectives
Develop a chatbot backend using Flask.
Create a simple frontend interface.
Containerize the application using Docker.
Implement CI/CD using Jenkins.
Provision infrastructure using Terraform.
Deploy the application on AWS EC2.
Configure monitoring using Amazon CloudWatch.
Maintain the source code using Git and GitHub.
3. Tools Used
Tool	Purpose
Python	Backend development
Flask	REST API
HTML	Frontend
Git & GitHub	Version control
Docker	Containerization
Jenkins	CI/CD pipeline
Terraform	Infrastructure as Code
AWS EC2	Deployment
Amazon CloudWatch	Monitoring
Ubuntu	Operating System
4. Architecture Diagram
                    User
                      |
                      v
              Frontend (HTML)
                      |
                      v
               Flask Backend API
                      |
                      v
                    Docker
                      |
                      v
                Jenkins CI/CD
                      |
                      v
                Terraform IaC
                      |
                      v
                AWS EC2 Instance
                      |
                      v
                 CloudWatch
5. Day-wise Implementation
Day 1: Git and GitHub Setup
Created GitHub repository.
Configured branches.
Performed commits and pushes.
Day 2: Backend Development
Created Flask application.
Added /chat endpoint.
Tested API locally.
Day 3: Frontend Development
Developed chatbot interface using HTML.
Connected frontend with backend.
Day 4: Dockerization
Created Dockerfile.
Built Docker image.
Ran Docker containers.
Day 5: Jenkins CI/CD
Installed Jenkins.
Created Jenkins pipeline.
Automated build process.
Day 6: Terraform
Initialized Terraform.
Created infrastructure configuration.
Executed:
terraform init
terraform validate
terraform plan
terraform apply
Day 7: Kubernetes

Skipped.

Day 8: AWS Lex

Skipped.

Day 9: Monitoring and Logging
Created CloudWatch dashboard.
Configured CPU utilization monitoring.
Created log group.
Created alarm for CPU usage.
Day 10: Documentation
Prepared project report.
Collected screenshots.
Documented architecture and implementation.
6. Screenshots

Include screenshots of:

GitHub repository.
Branches and commit history.
Flask backend execution.
Frontend interface.
Docker containers.
Docker images.
Jenkins pipeline.
Terraform commands.
EC2 instance.
CloudWatch dashboard.
CPU utilization graph.
Log group.
Alarm configuration.
7. GitHub Repository Link
https://github.com/johnmervin-06/ai-chatbot-devops-platform
8. Deployment Link
http://43.205.210.101:5000/chat

Response:

{
  "message": "Hello from AI Chatbot"
}
9. Conclusion

The AI Chatbot DevOps project successfully demonstrated the integration of software development and DevOps practices. The application was containerized using Docker, automated using Jenkins, provisioned with Terraform, deployed on AWS EC2, and monitored using Amazon CloudWatch. This project provided practical experience with modern DevOps tools and cloud technologies.

