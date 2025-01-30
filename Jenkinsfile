pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
    }
    stages {
        stage('Test Email') {
            steps {
                script {
                    emailext (
                        subject: "Test Email from Jenkins",
                        body: "If you receive this, Jenkins email works!",
                        to: 'flxschmidt969@gmail.com',
                        from: 'jenkins@example.com',
                        replyTo: 'jenkins@example.com',
                        mimeType: 'text/html'
                    )
                }
            }
        }
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/modernLiar/simple-addition2.git'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                sh '''
                echo "Logging in to Docker Hub..."
                echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t addition-app .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh '''
                echo "Tagging the Docker image..."
                docker tag addition-app $DOCKER_USERNAME/addition-app:latest
                echo "Pushing the Docker image to Docker Hub..."
                docker push $DOCKER_USERNAME/addition-app:latest
                '''
            }
        }
    }
    post {
        success {
            emailext (
                subject: "${JOB_NAME} - Build #${BUILD_NUMBER} - SUCCESS",
                body: "The pipeline has completed successfully.",
                to: 'flxschmidt969@gmail.com',
                from: 'jenkins@example.com',
                replyTo: 'jenkins@example.com',
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                subject: "${JOB_NAME} - Build #${BUILD_NUMBER} - FAILURE",
                body: "The pipeline has failed.",
                to: 'flxschmidt969@gmail.com',
                from: 'jenkins@example.com',
                replyTo: 'jenkins@example.com',
                mimeType: 'text/html'
            )
        }
    }


}

    
