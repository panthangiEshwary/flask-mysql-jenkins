pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo '📥 Cloning...'
                git branch: 'main', url: 'https://github.com/yourusername/flask-mysql-jenkins.git'
            }
        }

        stage('Build and Run with Docker Compose') {
            steps {
                echo '🐳 Running Docker Compose...'
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }
    }
}

