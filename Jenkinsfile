DOCKER_IMAGE_NAME = 'bsfmundial'
HEROKU_DOCKER_URL = 'registry.heroku.com'
HEROKU_CREDENTIALS_ID = 'heroku_registry'
APP_VERSION = "${currentBuild.number}"

HEROKU_IMAGE_URL = "${HEROKU_DOCKER_URL}/${DOCKER_IMAGE_NAME}"
node {
    stage('Checkout') {
        checkout scm
        gitCommitHash = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()  
    }     
    
    stage('Docker build') {
        sh "docker build -t ${HEROKU_IMAGE_URL}/web ."
    }

    stage('Docker push on Heroku Registry') {
        docker.withRegistry("https://${HEROKU_DOCKER_URL}", HEROKU_CREDENTIALS_ID) {
            sh "docker push ${HEROKU_IMAGE_URL}/web"
            sh 'heroku container:release web -a bsfmundial'
        }
    }
    
    stage('Docker cleanup') {
        sh "docker rmi ${HEROKU_IMAGE_URL}/web"
    }
}   