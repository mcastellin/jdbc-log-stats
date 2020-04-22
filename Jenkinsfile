pipeline {
    agent {
        docker { 
            image 'python:3.7-stretch' 
            args '--user root'
        }
    }
    environment {
        shortCommit = env.GIT_COMMIT.take(7)
    }

    stages {
        stage('Application Lint & Test') {
            steps {
                sh 'make setup install'
                sh 'make lint'
                sh 'make test'
            }
        }
    }
}
