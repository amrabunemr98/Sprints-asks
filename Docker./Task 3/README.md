# Docker Task 3
## Problem 1:
### Create 2 bridge network, "network1" with subnet 192.168.0.0/24 & "network2" with subnet 10.5.0.0/24 and Run 2 containers "container1 , container2" and attach them to network1. & Run container "container3" and attach it to network2:
![Screenshot from 2023-05-31 01-51-46](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/7be2eb3e-65b2-4acd-841d-98f24f94283d)
![Screenshot from 2023-05-31 01-54-24](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/2168c01c-2ee5-41bb-a01a-4a3b3085264e)
![Screenshot from 2023-05-31 02-00-58](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/c2756393-10a0-47bb-8463-6097bb1e3517)
![Screenshot from 2023-05-31 02-04-22](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/1d4e93cf-c05f-49cc-b1af-4cf26e374fa8)
### Make sure that the containers at different network can’t ping each other:
![Screenshot from 2023-05-31 02-07-28](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/ae619266-7f8e-487b-9152-255402bdcb4f)
## Problem 2:
- Create the static html file
- Write Dockerfile to build image based on httpd to host the html file and
- specify the following
- Copy the html file.
- Copy a new configuration file to listen on port 9999 instead of 80
- Open the port 9999 in the container
- Add environment variable CONTAINER with value docker . 
- Add startup command to echo the variable
![Screenshot from 2023-05-31 02-07-28](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/406da4ce-803b-4490-b628-f6f9494e1ff8)
![Screenshot from 2023-05-31 02-27-45](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/18878f93-52db-4490-bf7f-d8b0d0ac2a9b)
![Screenshot from 2023-05-31 02-30-10](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/172cfe3d-70f9-4eb4-a8b2-52724b5b941c)
![Screenshot from 2023-05-31 02-32-26](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/6977a0b2-2dfd-4022-bb30-0573a55fb78d)
## Problem 3:
### Create a docker compose to up mysql container,  https://github.com/sabreensalama/dockerize-node-app-task which depend on mysqldb. Add volume for mysqldb:
![Screenshot from 2023-05-31 03-16-37](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/f5ef848c-e466-41f9-bbf5-5c760016ea77)
![Screenshot from 2023-05-31 03-16-52](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/feef5c89-850e-4fa7-b783-3038cd284f25)
## Problem5:
### Use docker compose to deploy ghost platform (image: ghost:1-alpine)(Ghost is a free and open source blogging platform written in JavaScript) Use mysql database instead of sqlite:
![Screenshot from 2023-05-31 03-56-23](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/b6304615-3170-4e8e-8e38-1b0cff86b314)
![Screenshot from 2023-05-31 03-42-38](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/f2fdb348-2049-4a38-8e26-18feccc217ea)
![Screenshot from 2023-05-31 04-01-04](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/3c946d29-de65-423d-a8e0-b19a110aba6a)

 
  
