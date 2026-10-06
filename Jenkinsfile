pipeline {
    agent any

    environment {
        APP_ENV     = 'production'
        APP_MESSAGE = 'Hello from my Jenkins + Docker app!'
        API_KEY     = credentials('api-key-id')
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Build') {
            steps { sh 'docker build -t envapp:${BUILD_NUMBER} .' }
        }

        stage('Test') {
            steps {
                sh '''
                  docker rm -f envapp-test || true
                  docker run -d --name envapp-test -e APP_ENV -e APP_MESSAGE -e API_KEY envapp:${BUILD_NUMBER}
                  sleep 4
                  docker exec envapp-test python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:5000/health').read())"
                '''
            }
            post {
                always { sh 'docker rm -f envapp-test || true' }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                  docker rm -f envapp || true
                  docker run -d --name envapp --restart unless-stopped -p 5000:5000 \
                    -e APP_ENV -e APP_MESSAGE -e API_KEY -e BUILD_NUMBER \
                    envapp:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success { echo 'Deployed! Open http://localhost:5000' }
        failure { echo 'Pipeline failed' }
        always  { sh 'docker image prune -f' }
    }
}