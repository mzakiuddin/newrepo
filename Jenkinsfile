pipeline {
    agent any
    stages {
        stage('RunScript') {
            steps {
                sh 'python3 cleaning.py' >> 'newout.csv'
                sh 'aws s3 cp newout.csv s3://dcind-interns/jenkins'
            }
        }
        stage('S3command'){
            steps{
                sh 'aws s3 ls'
            }
        }
    }
}
