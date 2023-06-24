# Jenkins Task 3
## 1- What is the benefit of using master-slave architecture rather than building on master only ?
### - It allows you to scale out your build infrastructure as needed. By distributing the build load across multiple machines, you can ensure that your builds complete quickly and don't overwhelm the resources of the master machine. This also increases the reliability of your build system, as if the master machine fails, the build can continue on one of the slave machines without interruption.
----------------------------------------------
## 2- What is different between authorization and authentication ?
- Authentication: refers to the process of verifying the identity of a user or system. This typically involves the user or system providing some form of credentials, such as a username and password, which are then compared against a list of authorized users or stored in a secure database.
- Authorization: is the process of determining what actions an authenticated user or system is allowed to perform.
-------------------------------------------------------------------------------
## 3- Make jenkins-shared-library and make your jenkinsfile which you used in lab2 to point to this library:
### This is Link of [Build.groovy](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/vars/Building.groovy) , [Check.groovy](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/vars/Checks.groovy) , [Test.groovy](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/vars/Tests.groovy) , [Deployment.groovy](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/vars/Depo.groovy) , [Jenkinsfile](https://github.com/amrabunemr98/Sprints-tasks/blob/main/Jenkins/Task%203/Jenkinsfile)
![Screenshot from 2023-06-24 01-45-50](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/ea63ac8b-7ee0-408f-b784-580570b8469f)
![Screenshot from 2023-06-24 01-45-17](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/e7def45f-ce34-4839-abcb-3ccfdc589136)
![Screenshot from 2023-06-24 01-45-26](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/716d45f3-7b95-419b-a02d-ab852c7a847c)
![Screenshot from 2023-06-24 01-35-49](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/489d5581-0e80-4431-ba85-c63445d76938)
---------------------------------------------------
## 4- Try to make new slave as container or ec2 server and configure master to use it:
### - launch EC2 instance and enable port 22 (ssh):
![Screenshot from 2023-06-25 01-36-06](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/6975731b-a9c1-42ee-8e76-6ef6819daf6e)
----------------------------------
### - Adding ssh of jenkins and instance EC2 so it can connect EC2 through jenkins root and run ec2-slave:
![Screenshot from 2023-06-25 01-37-49](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/86aba59c-0385-409a-9ac4-49cc75f3a7eb)
![Screenshot from 2023-06-25 01-39-32](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/ac7e798a-22d6-4e6c-80f7-dc2920d63aab)
![Screenshot from 2023-06-25 02-08-36](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/846be58a-a74d-414b-b4b6-30a63439a367)
![Screenshot from 2023-06-25 01-39-04](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/0c435249-2a41-4df3-bc8c-5f8454867340)
![Screenshot from 2023-06-25 01-38-36](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/83c99f09-00f9-42bd-8e53-bb68519d62f9)


