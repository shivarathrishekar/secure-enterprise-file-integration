pipeline {
    agent any

    stages {
        stage('Validate SFTP File') {
            steps {
                echo 'Validating SFTP received file'
                sh 'test -f /app/data/transactions-to-send.csv'
                sh 'rm -f "$WORKSPACE/error.log"'
                sh 'FILE_PATH=/app/data/transactions-to-send.csv LOG_PATH="$WORKSPACE/error.log" python3 /app/monitor.py'
            }
        }

        stage('Check Error Log') {
            steps {
                sh 'if [ -s "$WORKSPACE/error.log" ]; then cat "$WORKSPACE/error.log"; else echo "No validation errors"; fi'
            }
        }

        stage('Process Transactions') {
            steps {
                sh 'OUTPUT_FILE="$WORKSPACE/transactions-processed.csv" python3 /app/process_transactions.py'
                sh 'cat "$WORKSPACE/transactions-processed.csv"'
            }
        }
    }

    post {
        success {
            echo 'SFTP integration workflow completed successfully'
        }
        failure {
            echo 'SFTP integration workflow failed'
        }
    }
}