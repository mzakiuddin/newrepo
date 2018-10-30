pipeline {
    agent any
    stages {
        stage('RunScript') {
            steps {
                sh 'python3 cleaning.py'
                sh 'aws s3 cp popoutput.csv s3://dcind-interns/jenkins/'
                
            }
        }
        stage('S3command'){
            steps{
                sh 'aws s3 ls'
            }
        }
    }
}
