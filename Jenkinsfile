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
                DOCKER_USERNAME = credentials('tktasci')
                DOCKER_PASSWORD = credentials('tk312598')
            }
            steps {
                sh """
                echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                docker tag addition-app $DOCKER_USERNAME/addition-app:latest
                docker push $DOCKER_USERNAME/addition-app:latest
                """
            }
        }
    }
}
