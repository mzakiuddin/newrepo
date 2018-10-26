pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                sh 'python3 cleaning.py >> test.csv'
                sh 'aws s3 cp test.csv s3://dcind-interns/jenkins/cleaningscript.csv'
                sh 'aws s3 ls'
            }
        }
    }
}
