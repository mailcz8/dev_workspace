pipeline {
	agent {
	  label "${params.test_bed_info}"
	}
    environment {
        INTERFACE = 'value'
    }
	stages {
        stage("Git Pull") {
            steps {
                echo "Git pull"
                git branch: "${params.testbranch}", changelog: false, credentialsId: 'ID_Info', poll: false, url: 'git@<reple_name_address>'
            }
        }
        stage("Install") {
            steps {
                sh '''if [ ! -d "venv" ]; then
                    virtualenv -p /usr/bin/python3 venv
                fi
                . venv/bin/activate
                pip install -r ./config/setup/requirements.txt'''
            }
        }
        stage("Test") {
            steps {
                sh ". venv/bin/activate && <script_name> -u -i ${params.tags} -e ${params.untags} -b ${params.testbed}"
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
