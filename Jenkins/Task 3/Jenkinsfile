@Library('pipejenkins-shared') _
pipeline {
     agent any
    parameters {
        booleanParam(name:'Test', defaultValue: true, description:'this paramater help you to know project name')
        choice(name: 'namespace', choices:['Development','Testing','Production'], description: '' ) 
    }
    stages {
            stage('check') {
                steps {
                    Checks()
                }
            }

            stage('build') {
                steps {
                    Building()
                }
            }

            stage('test') {
                when {
                    expression{
                        params.Test == true 
                    }
                }
                steps {
                    Tests()
                }
            }
            
            stage('deployment') {  
                steps {
                    Depo()
                }
            }    
    }
}
