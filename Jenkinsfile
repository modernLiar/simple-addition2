pipeline {
    agent any
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
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t addition-app .'
            }
        }
        stage('Push to Docker Hub') {
            environment {
                DOCKER_USERNAME = credentials('docker-username')
                DOCKER_PASSWORD = credentials('docker-password')
            }
            steps {
                sh """
                echo "DOCKER_USERNAME: $DOCKER_USERNAME"
                echo "Logging in to Docker Hub..."
                echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                echo "Tagging the Docker image..."
                docker tag addition-app $DOCKER_USERNAME/addition-app:latest
                echo "Pushing the Docker image to Docker Hub..."
                docker push $DOCKER_USERNAME/addition-app:latest
                """
            }
        }
    }
}
