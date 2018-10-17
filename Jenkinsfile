pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                sh 'chmod +x sample.py'
                sh './sample.py'
                sh 'echo "Some Message" > some.txt'
            }
        }
    }
}
