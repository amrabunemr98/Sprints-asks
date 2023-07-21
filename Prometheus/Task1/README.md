# Prometheus Task 1
## 1- What are the different HTTP status code and explain meaning of each of them?
- Informational: Server has received the request and is continuing to process it
- Successful: Request was successfully received, understood and accepted
- Redirection: Client must take additional action to complete the request
- Client Error: Request contains bad syntax or cannot be fulfilled
-----------------------------------------------
## 2- What database is used by Prometheus?
- TSDB (Time Series DataBase): Custom-built database that is optimized for storing and querying time-series data. It is designed to be highly scalable and performant, and it uses a compressed, in-memory format to store the time-series data
---------------------------------------
## 3- What is the differnece between different metrics types ( counter , gauge , histogram)?
- Counter: is a metric that represents a monotonically increasing value, used to track things like the number of requests received or the total number of errors that have occurred
- Gauge: is a metric that represents a value that can go up or down over time, used to track things like the amount of memory used or the number of active connections to a system
- Histogram: is a metric that represents the distribution of a set of values over time, used to track things like request latencies or response sizes
--------------------------------------------------------------
## 4- Install prometheus on your localhost or on server in any cloud provider:
### Prometheus running on port:9090:
![Screenshot from 2023-07-21 22-10-30](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/984d063b-5399-4219-a43d-ef7aaa02d04b)
------------------------------------
## Add any new target to prometheus.yaml file and apply any query on it using promql language:
### Add Node Exporter to prometheus.yml and running on port:9100:
![Screenshot from 2023-07-21 22-18-31](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/97636cf7-8b26-405b-876c-9c8d1de734e9)
![Screenshot from 2023-07-21 22-14-48](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/25c397d9-9cdd-4b06-97f1-9ec5cbf715d2)
![Screenshot from 2023-07-21 22-22-43](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/ce277bff-10ee-4d60-8452-4df9a4d98492)
------------------------------------------------
### Using Some query:
![Screenshot from 2023-07-21 22-31-16](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/131ab5aa-a52a-4edf-a311-5f086f99d484)
![Screenshot from 2023-07-21 22-37-59](https://github.com/amrabunemr98/Sprints-tasks/assets/128842547/e9ee247c-90be-42d1-9c5f-2ab7f7c49718)



