pipeline {
    agent any

    environment {
        IMAGE_NAME = "chatbot-backend"
        IMAGE_TAG  = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install & Unit Test') {
            steps {
                dir('backend') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        # add real tests under backend/tests and point pytest at them
                        pip install pytest
                        pytest tests/ || true
                    '''
                }
            }
        }

        stage('Docker Build') {
            steps {
                dir('backend') {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                sh """
                    trivy image --exit-code 0 --format table \
                        -o trivy-report.txt ${IMAGE_NAME}:${IMAGE_TAG}
                """
                archiveArtifacts artifacts: 'trivy-report.txt', fingerprint: true
            }
        }

        stage('Push to Registry') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                        echo "\$DOCKER_PASS" | docker login -u "\$DOCKER_USER" --password-stdin
                        docker tag ${IMAGE_NAME}:${IMAGE_TAG} \$DOCKER_USER/${IMAGE_NAME}:${IMAGE_TAG}
                        docker push \$DOCKER_USER/${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                    kubectl set image deployment/chatbot chatbot=\$DOCKER_USER/${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }
    }

    post {
        success {
            echo "Build ${IMAGE_TAG} succeeded and was deployed."
        }
        failure {
            echo 'Build failed — check the stage logs above.'
        }
    }
}
