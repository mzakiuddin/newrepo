pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                sh 'python3 sample.py >> output.txt'
                sh 'aws s3 cp output.txt s3://dcind-interns/jenkins/jenkinoutcheck.txt'
                sh 'aws s3 ls'
            }
        }
    }
}
