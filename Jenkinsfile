pipeline {
    agent any
    stages {
        stage('Deploy to Remote Server') {
            steps {
                sshagent(['remote-ssh-key']) {
                    sh '''
                        # 1. Remote machine par folder agar nahi hai to banana
                        ssh -o StrictHostKeyChecking=no root@192.168.100.43 "mkdir -p /home/production-app"
                        
                        # 2. Jenkins workspace se sara code remote machine par copy karna
                        # Ismein GitHub ki zaroorat nahi kyunke Jenkins ke paas code pehle hi aa chuka hai
                        scp -o StrictHostKeyChecking=no -r ./* root@192.168.100.43:/home/production-app/
                        
                        # 3. Remote par Docker chalana
                        ssh -o StrictHostKeyChecking=no root@192.168.100.43 "
                            cd /home/production-app &&
                            (docker-compose down || true) &&
                            docker-compose up --build -d
                        "
                    '''
                }
            }
        }
    }
}
