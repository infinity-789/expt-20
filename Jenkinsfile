pipeline {

    agent any

    stages {
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }

        stage ('Run tests') {

            steps {
                bat '"C:\\Users\\Abhay\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest.exe" --junitxml=pytest.xml'
            }
        }

        stage ('Build') {
            steps {
                bat 'docker build -t python-app .'
            }
        }

        stage ('Cleanup old container') {
            steps {
                bat 'docker rm -f python-app || exit 0'
            }
        }

        stage ('Run Container') {
            steps {
                bat 'docker run -d -p 5020:5020 --name python-app python-app'
            }
        }
    }

    post {
        always {
            junit 'pytest.xml'
        }
    }
}