pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                sh 'chmod +x sample.py'
                sh './sample.py'
                echo "Some Message" > /home/osboxes/Downloads/some.txt
            }
        }
    }
}
