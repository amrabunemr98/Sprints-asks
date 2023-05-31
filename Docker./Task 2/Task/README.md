# Docker Task 2
## 1- Run an instance of nginx:alpine with a name nginx and map port 8080 on the container to 3828 on the host:
![Screenshot from 2023-05-27 02-22-29](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/47984155-6ea2-4b71-96a5-6481a965c810)
## 2- Create ubuntu image and check the size of it:
![Screenshot from 2023-05-27 02-23-55](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/00712861-967c-4f84-a8d3-17dd33fa914f)
## 3- Run a container named blue-app using image KodeKloud/simple-webapp and set the environmet variable APP_COLOR to blue. make the app available on port 38282 on the host. the app listens on port 8080:
![Screenshot from 2023-05-27 02-50-01](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/698acd1a-6529-4fab-8cf2-7ad51f847a8a)
![Screenshot from 2023-05-27 02-49-56](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/e71da03b-5607-4ced-bd93-04d4b5f9141e)
## 4- Deploy a mysql database using the mysql image and name it mysql-db. set the database password to use db_pass123 then inspect it to check the value:
![Screenshot from 2023-05-27 02-55-46](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/eb2337a6-5557-4b78-82e8-9c45d9878219)
![Screenshot from 2023-05-27 02-57-32](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/1dd38958-ee46-487a-8581-c352bdbf82bd)
## 5- Pull the code from https://github.com/sabreensalama/simple-flask-app/tree/main and create a docker file for this flask app:
![Screenshot from 2023-05-29 00-34-15](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/01013ce3-fd29-4e9d-843a-d72cd0994423)
![Screenshot from 2023-05-29 00-34-46](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/4f7cf8bd-979c-4b57-a931-887dec2d50f5)
![Screenshot from 2023-05-29 00-34-36](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/721fc73b-3b09-43fe-832b-a548fbaee408)
## 6- Create a volume called mysql_data, run a mysql container again, but this time map a volume to the container so that the data stored by the container is stored at /opt/data on the host. use the same name : mysql-db and same password : db_pass123 as before. Mysql stores data at /var/lib/mysql inside the container:
![Screenshot from 2023-05-27 04-08-32](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/49a47a10-1a7f-4ae6-ac3e-65a28160e078)
