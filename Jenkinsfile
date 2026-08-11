pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Terraform Plan') {
            steps {
                sh 'terraform init'
                sh 'terraform plan -out=tfplan'
            }
        }

        stage('Infracost Breakdown') {
            steps {
                withCredentials([string(credentialsId: 'infra-cost-api-key', variable: 'INFRACOST_API_KEY')]) {
                    sh 'infracost breakdown --path . --format json --out-file infracost-output.json'
                }
            }
        }

        stage('Push to Postgres') {
            steps {
                sh '''
                    source venv/bin/activate
                    python3 push_cost.py
                '''
            }
        }
    }
}