pipeline {
    agent any
    stages {
        stage('RunScrapy') {
            steps {
                sh 'a2zinc/a2zinc/spiders/ea2zin.py'
                sh 'scrapy crawl ea2zin -o ea2zinc.csv'
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
