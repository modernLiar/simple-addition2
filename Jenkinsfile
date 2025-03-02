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
                sh """
                echo "Logging in to Docker Hub..."
                echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                """
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t addition-app .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    // def commitHash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    def versionController = 1
                    def buildNumber = env.BUILD_NUMBER
                    def imageTag = "v${versionController}.${buildNumber}"

                    echo "Tagging the Docker image..."
                    sh """
                        docker tag addition-app $DOCKER_USERNAME/addition-app:latest
                        docker tag addition-app $DOCKER_USERNAME/addition-app:${imageTag}

                        echo "Pushing the Docker image to Docker Hub..."
                        docker push $DOCKER_USERNAME/addition-app:latest
                        docker push $DOCKER_USERNAME/addition-app:${imageTag}
                    """
                }
            }
        }

        stage('Create Container in the Host Machine'){
            steps{
                script{
                    def CONTAINER_ID = env.BUILD_NUMBER

                    sh """
                    echo 'Pulling the latest image for building container...'
                    docker pull $DOCKER_USERNAME/addition-app:latest
                    echo 'Building the container with the latest image'
                    docker run -d --name addition-container-${CONTAINER_ID} $DOCKER_USERNAME/addition-app:latest
                    """    
                }
                
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
                    from: 'tahakeremtasci@gmail.com',
                    replyTo: 'tahakeremtasci@gmail.com',
                    mimeType: 'text/html',
                    // attachmentsPattern: 'a.txt' # Uncomment this line if you have a file you want to attach
                )
            }
        }


    }
}
    
