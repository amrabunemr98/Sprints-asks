@library('pipejenkins-shared') _
pipeline {
     agent any
    parameters {
        booleanParam(name:'Test', defaultValue: true, description:'this paramater help you to know project name')
        choice(name: 'namespace', choices:['Development','Testing','Production'], description: '' ) 
    }
    stages {
            stage('Check') {
                steps {
                    check()
                }
            }

            stage('Build') {
                steps {
                    build()
                }
            }

            stage('Test') {
                when {
                    expression{
                        params.Test == true 
                    }
                }
                steps {
                    test()
                }
            }
            
            stage('Deployment') {  
                steps {
                    dep()
                }
            }    
    }
}
