pipeline {
    agent any
    stages {
        stage('RunScrapy') {
            steps {
                sh 'python3 a2zinc/a2zinc/spiders/ea2zin.py'
                sh 'aws s3 cp ea2zinc.csv s3://dcind-interns/jenkins-scrapy/'
                
            }
        }
        stage('S3command'){
            steps{
                sh 'aws s3 ls'
            }
        }
    }
}
