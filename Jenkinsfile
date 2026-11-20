pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checkout completed.'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Python application...'
                sh 'python3 -m py_compile app/app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'python3 -m unittest discover -s app -p "test_*.py" -v'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t lab1-python-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application container...'
                sh '''
                    docker rm -f lab1-python-app || true
                    docker run -d --name lab1-python-app lab1-python-app:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD pipeline failed. Check the console output.'
        }
    }
}
