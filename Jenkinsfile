pipeline {
    agent any

    stages {
        stage('Cloning Git') {
          steps {
              git credentialsId: 'GitCred', url: 'https://github.com/srilatha333/cicd.git'
         }
        }
        stage('Building image') {
          steps{
            script {
              dockerImage = docker.build("https://hub.docker.com/repositories/srilatha333/nginx:latest")
            }
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
