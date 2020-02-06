pipeline {
	agent {
	  label "${params.testbed}"
	}
    environment {
        INTERFACE = 'pcan'
        BODY=3
        CHASSIS1=4
        CHASSIS2=2
        THERMAL=1
        icebuild="${params.icebuild}"
    }
	stages {
        stage("Git Pull") {
            steps {
                echo "Git pull"
                git branch: "${params.testbranch}", changelog: false, credentialsId: '47bde6d4-64ce-4f13-9645-17e0167063cb', poll: false, url: 'git@gitlab.com:bytonccs/ui-ux/sqa-ice.git'
            }
        }
        stage("Install") {
            steps {
                sh '''if [ ! -d "venv" ]; then
                    virtualenv -p /usr/bin/python3 venv
                fi
                . venv/bin/activate
                pip install -r ./setup/requirements.txt'''
            }
        }
        stage("Test") {
            steps {
                sh ". venv/bin/activate && python auto_launch.py -u -i ${params.tags} -e ${params.untags} -b ${params.testbed} -o alex.zhao@byton.com"
            }
        }
	}
    post {
        always("Clean up") {
            echo 'clean up our workspace'
            cleanWs()
        }
    }
}
