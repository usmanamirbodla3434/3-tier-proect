pipeline {
    agent any
    stages {
        stage('Deploy to Remote Server') {
            steps {
                // 'remote-ssh-key' wahi ID hai jo abhi aapne banayi
                sshagent(['remote-ssh-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no root@192.168.100.43 "
                            cd /home/production-app &&
                            git pull origin main &&
                            docker-compose down &&
                            docker-compose up --build -d
                        "
                    '''
                }
            }
        }
    }
}
