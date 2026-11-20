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

        stage('Deploy') {
            steps {
                echo 'Deploying sample application...'
                sh 'python3 app/app.py'
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
