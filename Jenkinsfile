#!/usr/bin/env groovy

pipeline {
    agent any
    environment{
        server_ip        =   ""
        home_directory   =   "/home/olexandr"
    }
    stages {
        stage('Move py script to server'){
            steps{
                script{
                    sh "scp auto_run.py olexandr@${server_ip}:${home_directory}"
                }
            }
        }
        stage{
            steps('Enshure pip & python3 is present'){
                script{
                    sh """
                    sudo apt install -y python3 && \
                    sudo apt install python3-pip
                    """
                }
            }
        }
    }
    post {
        always {
            sh "python3 auto_run.py"
        }
    }
}
