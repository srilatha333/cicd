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
              dockerImage = docker.build("srilatha333/nginx:$BUILD_NUMBER")
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
