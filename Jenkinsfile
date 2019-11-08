#!groovy
// Run docker build
properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
        }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage("create docker image") {
            steps {
                echo " ============== start building image =================="
                dir ('docker/toolbox') {
                  sh 'docker build -t sheroukhov/mgf_app:latest . '
                }
            }
        }
    stage("docker login") {
            steps {
                echo " ============== docker login =================="
                withCredentials([usernamePassword(credentialsId: 'dockerhub_sheroukhov', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh """
                    docker login -u $USERNAME -p $PASSWORD
                    """
                }
            }
        }
    tage("docker push") {
            steps {
                echo " ============== start pushing image =================="
                sh '''
                docker push sheroukhov/mgf_app:latest
                '''
            }
        }
    }
}
