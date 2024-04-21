pipeline {
    agent any

    stages {
        stage('Cloning Git') {
          steps {
              git credentialsId: 'GitCred', url: 'https://github.com/srilatha333/cicd.git'
         }
        }
        stage('Build') {
            steps {
                echo 'Building.'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing.'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying.**'
            }
        }
    }
}
