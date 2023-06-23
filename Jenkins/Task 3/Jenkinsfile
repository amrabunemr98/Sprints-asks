@library('pipejenkins-shared') _
def gv
pipeline {
     agent any
    parameters {
        booleanParam(name:'Test', defaultValue: true, description:'this paramater help you to know project name')
        choice(name: 'namespace', choices:['Development','Testing','Production'], description: '' ) 
    }
    stages {
            stage('check') {
                steps {
                    script {
                        gv.checkapp
                    }
                }
            }

            stage('build') {
                steps {
                    script {
                        gv.buildapp
                    }
                }
            }

            stage('test') {
                when {
                    expression{
                        params.Test == true 
                    }
                }
                steps {
                    script {
                        gv.testapp 
                    }
                }
            }
            
            stage('deployment') {  
                steps {
                    script {
                      gv.deploymentapp  
                    }
                }
            }    
    }
}
