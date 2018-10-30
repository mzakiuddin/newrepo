pipeline {
    agent any
    stages {
        stage('RunScrapy') {
            steps {
                sh 'python3 a2zinc/a2zinc/spiders/ea2zin.py'
                sh 'cd a2zinc && scrapy crawl ea2zin -o s3://dcind-interns/jenkins-scrapy/ea2zinc.csv'                
            }
        }
       
    }
}
