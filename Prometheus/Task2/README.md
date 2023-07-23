# Prometheus Task 2
## 1- How do I trigger a Prometheus alert?
1. Define alerting rules: In Prometheus, i define alerting rules in a separate file called rules.yml or in the main configuration file, Each rule specifies a condition to be evaluated and a threshold to trigger an alert.
2. Reload Prometheus configuration: Once i have defined alerting rules, i need to reload the Prometheus configuration to make them active.
3. Configure alertmanager: I need to configure alertmanager to receive alerts from Prometheus and route them to the appropriate recipients, such as Slack.
4. Test the alert: Once i have defined alerting rules and configured alertmanager, i can test the alert by triggering the condition specified in the rule. This can be done by simulating the condition, such as by sending a test request to the server or by using the prometheus.
-----------------------------------------------
## 2- What is the difference between node exporter and mysql exporter ?
- Node Exporter: is a general-purpose exporter that collects system-level metrics from a host machine. It provides information on CPU usage, memory usage, disk usage, network traffic, and other system-level metrics.typically used to monitor the health and performance of a host machine.
- MySQL Exporter: is a specialized exporter that collects metrics from a MySQL database instance. It provides information on database performance, replication status, query execution, and other database-level metrics. MySQL Exporter can be used to monitor the health and performance of a MySQL database instance.
- ---------------------------------------
## 3- what is the maximum retention period to save data in Prometheus and how to increase it ?
- The maximum retention period to save data in Prometheus is determined by the size of the storage volume or disk space allocated for TSDB.
- To increase the retention period for Prometheus data so need to adjust the storage.tsdb.retention.time configuration parameter in the Prometheus configuration file.
----------------------------------------------------------------------------------
## 4- What are the different PromQL data types available in Prometheus Expression language?
- Matrices: are a collection of instant or range vectors that share the same metric name and set of labels. Matrices can be used to perform aggregations and calculations across multiple time-series data points.
- Scalars: are simple numeric values, such as integers or floating-point numbers so it can be used in arithmetic operations and comparisons.
- Strings: a sequence of characters enclosed in double quotes, can be used to match specific labels or filter results based on specific conditions.
------------------------------------------------------------------
## 5- How To calculate the average request duration over the last 5 minutes from a histogram ?
- will use rate() to calculate the average request duration during the last 5 minutes from a histogram called:
```
  rate(http_request_duration_seconds_sum[5m])
/
  rate(http_request_duration_seconds_count[5m])
```
-------------------------------------
## 6- What is Thanos Prometheus?
- An open-source project that extends the capabilities of Prometheus, a popular monitoring and alerting system. Thanos provides a way to store, query, and visualize Prometheus metrics data over long-term storage by integrating with object storage systems like AWS S3 and Google Cloud Storage.
- --------------------------
## 7- what is promtool and how i can use it ?
- A command-line tool provided by Prometheus that can be used to validate and alerting rules.
- Validating alerting rules: i can use promtool to validate your alerting rules file.
---------------------------------------
## 8- What types of Monitoring can be done via Grafana?
- Infrastructure monitoring: Grafana can be used to monitor the health and performance of my servers, network devices, and other infrastructure components-
- Application monitoring: Grafana can also be used to monitor the health and performance of my applications, including metrics such as response time and error rates.
- Database monitoring: Grafana can be used to monitor the performance of my databases, including metrics such as query execution times and connection counts.
---------------------------------------------------------
## 9- Can we see different Servers CPU comparison in Grafana?
- Yes, Grafana can be used to compare CPU usage across different servers using a variety of visualization techniques
