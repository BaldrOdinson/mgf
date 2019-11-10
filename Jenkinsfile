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
        stage("update jenkins build info for html") {
            steps {
                echo " ============== update build number in file =================="
                dir ('test_app/core/build_info') {
                  sh 'echo ${BUILD_NUMBER} > build_no.txt'
                }
            }
        }
        stage("create docker image") {
            steps {
                echo " ============== start building image =================="
                dir ('docker/toolbox') {
                  sh 'docker build --no-cache -t sheroukhov/mgf_app:${BUILD_NUMBER} . '
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
        stage("docker push") {
                steps {
                    echo " ============== start pushing image =================="
                    sh '''
                    docker push sheroukhov/mgf_app:${BUILD_NUMBER}
                    '''
                }
        }
    }
}
