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
        always {
            script {
                def jobName = env.JOB_NAME
                def buildNumber = env.BUILD_NUMBER
                def pipelineStatus = currentBuild.result ?: 'UNKNOWN'
                def bannerColor = pipelineStatus.toUpperCase() == 'SUCCESS' ? 'green' : 'red'

                def body = """<html>
                    <body>
                        <div style="border: 4px solid ${bannerColor}; padding: 10px;">
                            <h2>${jobName} - Build ${buildNumber}</h2>
                            <div style="background-color: ${bannerColor}; padding: 10px;">
                                <h3 style="color: white;">Pipeline Status: 
                                    ${pipelineStatus.toUpperCase()}</h3>
                            </div>
                            <p>Check the <a href="${BUILD_URL}">console output</a>.</p>
                        </div>
                    </body>
                </html>"""

                emailext (
                    subject: "${jobName} - Build ${buildNumber} - ${pipelineStatus}",
                    body: body,
                    to: 'flxschmidt969@gmail.com',
                    from: 'jenkins@example.com',
                    replyTo: 'jenkins@example.com',
                    mimeType: 'text/html',
                    // attachmentsPattern: 'a.txt' # Uncomment this line if you have a file you want to attach
                )
            }
        }


    }
}
    
