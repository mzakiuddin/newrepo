pipeline {
    agent any
    stages {
        stage('RunScrapy') {
            steps {
                sh 'python3 a2zinc/a2zinc/spiders/ea2zin.py'
                sh 'cd a2zinc && scrapy crawl ea2zin -o ea2zinc.csv'                
            }
        }
        stage('S3command'){
            steps{
                sh 'aws s3 ls'
            }
        }
    }
}
