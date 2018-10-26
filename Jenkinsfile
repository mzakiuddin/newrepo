pipeline {
    agent any
    stages {
        stage('RunScript') {
            steps {
                sh 'python3 cleaning.py'  >> 'pop.csv'
                
                sh 'echo cleaning.py'
            }
        }
        stage('S3command'){
            steps{
                sh 'aws s3 ls'
            }
        }
    }
}
