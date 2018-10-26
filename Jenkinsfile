pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                sh 'python3 sample.py'
                sh 'aws s3 cp ./sample.py s3://dcind-interns/jenkins/jenkinoutcheck.txt'
                sh 'aws s3 ls'
            }
        }
    }
}
