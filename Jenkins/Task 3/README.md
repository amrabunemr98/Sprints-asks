# Jenkins Task 3
## 1- What is the benefit of using master-slave architecture rather than building on master only ?
### - it allows you to scale out your build infrastructure as needed. By distributing the build load across multiple machines, you can ensure that your builds complete quickly and don't overwhelm the resources of the master machine. This also increases the reliability of your build system, as if the master machine fails, the build can continue on one of the slave machines without interruption.
----------------------------------------------
## 2- What is different between authorization and authentication ?
- Authentication: refers to the process of verifying the identity of a user or system. This typically involves the user or system providing some form of credentials, such as a username and password, which are then compared against a list of authorized users or stored in a secure database.
- Authorization: is the process of determining what actions an authenticated user or system is allowed to perform.
-------------------------------------------------------------------------------
## 3- make jenkins-shared-library and make your jenkinsfile which you used in lab2 to point to this library
### This is Link of [build.groovy](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/vars/Building.groovy) , [Check.groovy](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/vars/Checks.groovy) , [Test.groovy](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/vars/Tests.groovy) , [Deployment.groovy](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/vars/Depo.groovy) , [Jenkinsfile](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/Jenkinsfile)
![Screenshot from 2023-06-24 01-45-50](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/ea63ac8b-7ee0-408f-b784-580570b8469f)
![Screenshot from 2023-06-24 01-45-17](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/e7def45f-ce34-4839-abcb-3ccfdc589136)
![Screenshot from 2023-06-24 01-45-26](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/716d45f3-7b95-419b-a02d-ab852c7a847c)
![Screenshot from 2023-06-24 01-35-49](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/489d5581-0e80-4431-ba85-c63445d76938)
---------------------------------------------------

