pipeline {
    agent any

    environment {
        APP_ENV     = 'production'
        APP_MESSAGE = 'Hello from Jenkins and Docker'
        API_KEY     = credentials('api-key-id')
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Build') {
            steps { sh 'docker build -t envapp:${BUILD_NUMBER} .' }
        }

        stage('Run') {
            steps {
                sh 'docker run --rm -e APP_ENV -e APP_MESSAGE -e API_KEY envapp:${BUILD_NUMBER}'
            }
        }

        stage('Print secret test') {
            steps {
                echo "The key is: ${API_KEY}"
            }
        }
    }

    post {
        success { echo 'Pipeline succeeded' }
        failure { echo 'Pipeline failed' }
        always  { sh 'docker image prune -f' }
    }
}