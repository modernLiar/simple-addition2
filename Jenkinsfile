// pipeline {
//     agent any

//     environment {
//         RECIPIENTS = 'flxschmidt969@gmail.com'
//     }

//     stages {
//         stage('Build') {
//             steps {
//                 echo 'Building...'
//             }
//         }

//         stage('Test') {
//             steps {
//                 echo 'Running tests...'
//             }
//         }

//         stage('Deploy') {
//             steps {
//                 echo 'Deploying application...'
//             }
//         }
//     }

//     post {
//         always {
//             script {
//                 try {
//                     emailext subject: "Jenkins Build ${currentBuild.currentResult}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
//                              body: "The build ${env.BUILD_NUMBER} for job '${env.JOB_NAME}' has completed with status: ${currentBuild.currentResult}.\nCheck console output at ${env.BUILD_URL}",
//                              to: "${RECIPIENTS}"
//                     echo "Email sent successfully"
//                 } catch (Exception e) {
//                     echo "Failed to send email: ${e.getMessage()}"
//                     error("Email notification failed")
//                 }
//             }
//         }
//     }
// }





// ************************************************************************************************************


pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
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
        success {
            emailext (
                subject: "${JOB_NAME} - Build #${BUILD_NUMBER} - SUCCESS",
                body: "The pipeline has completed successfully.",
                to: 'flxschmidt969@gmail.com',
                from: 'tahakeremtasci@gmail.com',
                replyTo: 'tahakeremtasci@gmail.com',
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                subject: "${JOB_NAME} - Build #${BUILD_NUMBER} - FAILURE",
                body: "The pipeline has failed.",
                to: 'flxschmidt969@gmail.com',
                from: 'tahakeremtasci@gmail.com',
                replyTo: 'tahakeremtasci@gmail.com'
                mimeType: 'text/html'
            )
        }
    }


}

    
