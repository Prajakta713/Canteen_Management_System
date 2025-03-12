pipeline {
    agent any

    environment {
        // Set the directory for the virtual environment
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Prajakta713/Canteen_Management_System.git'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                script {
                    // Create virtual environment if it doesn't exist
                    if (!fileExists("${VENV_DIR}/Scripts/activate")) {
                        sh 'python -m venv ${VENV_DIR}'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies in the virtual environment
                    sh '''
                        ./${VENV_DIR}/Scripts/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest
                    sh '''
                        ./${VENV_DIR}/Scripts/activate
                        pytest --maxfail=1 --disable-warnings -q
                    '''
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                // Assuming you have a test report (XML format) generated, you can publish the test results
                junit '**/test-*.xml'  // Adjust path if needed
            }
        }

        stage('Deploy to Staging') {
            steps {
                script {
                    // Your deployment logic here
                    echo 'Deploying to staging environment...'
                }
            }
        }
    }

    post {
        always {
            // Clean up virtual environment after build
            cleanWs()
        }

        success {
            echo 'Build and tests passed successfully!'
        }

        failure {
            echo 'Build or tests failed. Please check the logs.'
        }
    }
}
