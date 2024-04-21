pipeline {
    agent any

    stages {
        stage('Cloning Git') {
          steps {
              git credentialsId: 'GitCred', url: 'https://github.com/srilatha333/cicd.git'
         }
        }
        stage('Deploy App') {
          steps {
            script {
              kubernetesDeploy(configs: "deployment.yaml", kubeconfigId: "docker-desktop")
            }
          }
        }
    }
}
