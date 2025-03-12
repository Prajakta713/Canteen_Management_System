pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Python39' // Set to your Python version
        PATH = "${env.PYTHON_HOME}\\Scripts:${env.PYTHON_HOME}:${env.PATH}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Prajakta713/Canteen_Management_System.git'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                script {
                    // Create a virtual environment and activate it
                    sh 'python -m venv venv'
                    sh '.\\venv\\Scripts\\activate'  // Windows (or `source venv/bin/activate` on Linux/Mac)
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    sh '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run Django tests
                    sh '.\\venv\\Scripts\\activate && python manage.py test'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit '**/test-*.xml'  // Publish JUnit-compatible test results
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging environment'
                // Add your deployment steps here
            }
        }
    }

    post {
        success {
            echo 'Build and tests succeeded!'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}
