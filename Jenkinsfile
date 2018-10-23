pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                sh 'python3 sample.py'
                sh 'echo "Some Message" > some.txt'
                sh 'aws s3 ls'
            }
        }
    }
}
