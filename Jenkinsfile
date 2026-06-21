pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t chatbot-backend:v1 backend/'
            }
        }

        stage('Security Scan') {
            steps {
                sh 'trivy image chatbot-backend:v1 || true'
            }
        }

        stage('Verify Image') {
            steps {
                sh 'docker images'
            }
        }
    }

    post {
        success {
            echo 'Build Successful'
        }

        failure {
            echo 'Build Failed'
        }
    }
}
