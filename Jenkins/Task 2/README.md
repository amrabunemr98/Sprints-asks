# Jenkins Task 2
## 1- What is Jenkins pipeline ?
### Jenkins Pipeline is a powerful tool that can help you automate your software delivery process continuous integrating pipelines into Jenkins. It can be used to automate a wide range of tasks, including:
- Building your code
- Running unit tests
- Deploying your code to a staging environment
- Creating a release and deploy it
-----------------------------------------------------------
## 2- What scripting language is Jenkins pipeline syntax based on ?
- Groovy scripting Language
--------------------------------------------------------
## 3- What are the different ways to trigger pipeline ?
- Polling SCM
- Build Triggers
- Webhooks
- Manually
---------------------------------------------------------------
## 4- What is different between parameter and jenkins env variable ?
- Parameters: are values that are passed into the pipeline at runtime. They are typically used to configure the pipeline, such as the branch to build or the environment to deploy to. Parameters can be set in the Jenkins UI, in a Jenkinsfile, or through the Jenkins CLI
- Environment variables: are values that are set in the Jenkins environment. They are typically used to store sensitive data, such as passwords or API keys. Environment variables can be set in the Jenkins configuration, in a Jenkinsfile, or through the Jenkins CLI
-------------------------------------------------------
## 5- What is organization folder job and what is used for ?
- Type of folder that automatically creates multi-branch pipelines for all the repositories in a GitHub of company,By using organization folder jobs in Jenkins, company can automate the CI/CD process for multiple projects. This can save time and effort, and it can also help to improve the quality of code
----------------------------------------
## 6- Create jenkins pipeline for your repo and use script file (jenkinsfile) to write pipeline syntax, include parameter functions and env variable in it
![Screenshot from 2023-06-21 21-59-10](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/170e1a32-9536-474f-a55a-4f82b22691ae)
![Screenshot from 2023-06-21 21-59-22](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/9823befd-2ae9-4345-af8b-53802d9464a1)
![Screenshot from 2023-06-21 21-59-33](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/2d5062d0-a6e4-4fe6-8ffe-f745b12fbceb)
![Screenshot from 2023-06-21 21-59-49](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/d04925d1-2c1b-4a80-ab1f-7f951ce6fc40)
![Screenshot from 2023-06-21 22-00-33](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/bb5efead-ebe3-4fec-a83b-bbeb297b6c99)
------------------------------------------------
## 7- Create another multibranch pipeline and filter branches to contain only (main , dev , test )













