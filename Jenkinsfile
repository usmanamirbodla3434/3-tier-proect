pipeline {
    agent any
    stages {
        stage('Deploy to Remote Server') {
            steps {
                sshagent(['remote-ssh-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no root@192.168.100.43 "
                            # Folder banayein agar nahi hai
                            mkdir -p /home/production-app &&
                            cd /home/production-app &&
                            
                            # Agar git setup nahi hai to clone karein, warna pull karein
                            if [ ! -d .git ]; then
                                git clone https://github.com/usmanamirbodla3434/3-tier-proect.git .
                            else
                                git pull origin main
                            fi &&
                            
                            # Docker containers ko restart karein
                            docker-compose down || true &&
                            docker-compose up --build -d
                        "
                    '''
                }
            }
        }
    }
}
