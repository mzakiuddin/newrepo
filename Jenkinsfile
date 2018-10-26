pipeline {
    agent any
    stages {
        stage('RunScript') {
            steps {
                sh 'python3 cleaning.py >> test.csv'
            }
        }
        stage('ToS3'){
            steps{
                sh 'aws s3 cp test.csv s3://dcind-interns/jenkins/cleaningscript.csv'
            }
        }
        stage('S3command'){
            steps{
                sh 'aws s3 ls'
            }
        }
    }
}
