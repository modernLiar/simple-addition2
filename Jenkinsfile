pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
        EMAIL_RECIPIENT = credentials('outlook-email')
    }
    stages {
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
        failure {
            script {
                // Get the name of the failed stage
                def failedStage = currentBuild.result == 'FAILURE' ? currentBuild.stageName : 'Unknown Stage'
                
                // Send an email with the failed stage information
                emailext (
                    subject: "Pipeline Failed: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
                    body: """
                    The pipeline has failed at stage: ${failedStage}.

                    Job: ${env.JOB_NAME}
                    Build Number: ${env.BUILD_NUMBER}
                    Build URL: ${env.BUILD_URL}
                    """,
                    to: "${env.EMAIL_RECIPIENT}"
                )
            }
        }
    }
}

    
