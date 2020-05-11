pipeline {
    agent {
        docker { 
            image 'jenkins-agent:python-3.7' 
            args '--user jenkins'
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

        stage('Integration testing') {
            steps {
                sh 'bin/jdbcstats --file jdbc.log.test --output ttable --rows 10'
                sh 'bin/jdbcstats --file jdbc.log.test --output json --rows 5'
            }
        }
    }
}
