@library('pipejenkins-shared') _
pipeline {
     agent any
    parameters {
        booleanParam(name:'Test', defaultValue: true, description:'this paramater help you to know project name')
        choice(name: 'namespace', choices:['Development','Testing','Production'], description: '' ) 
    }
    stages {
            stage('check') {
                steps {
                    check()
                }
            }

            stage('build') {
                steps {
                    build()
                }
            }

            stage('test') {
                when {
                    expression{
                        params.Test == true 
                    }
                }
                steps {
                    test()
                }
            }
            
            stage('deployment') {  
                steps {
                    dep()
                }
            }    
    }
}
