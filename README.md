# Real-time Data Streaming Pipeline | End-to-End Data Engineering Project

## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [Steps](#steps)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
---
## 🪄 Introduction
This project serves as a comprehensive guide to building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. Everything is containerized using Docker for ease of deployment and scalability.

---

## ⚡ System Architecture

![System Architecture](https://github.com/ahmedashraffcih/Real-time-Data-Streaming-Pipeline/blob/main/imgs/Data%20engineering%20architecture.png)

The project is designed with the following components:

- **Data Source**: We use `randomuser.me` API to generate random user data for our pipeline.
- **Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
- **Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
- **Apache Spark**: For data processing with its master and worker nodes.
- **Cassandra**: Where the processed data will be stored.
---
## 📜 Steps

- Setting up a data pipeline with Apache Airflow
- Real-time data streaming with Apache Kafka
- Distributed synchronization with Apache Zookeeper
- Data processing techniques with Apache Spark
- Data storage solutions with Cassandra and PostgreSQL
- Containerizing your entire data engineering setup with Docker
---
## 🔧 Technologies

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker
---
## 💿 Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/ahmedashraffcih/Real-time-Data-Streaming-Pipeline.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Real-time-Data-Streaming-Pipeline
    ```

3. Run Docker Compose to spin up the services:
    ```bash
    docker-compose up
    ```
---
## ✨ Contribution

Contributions and feedback are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.


To contribute to this project, see the GitHub documentation on **[creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)**.

---

## 👏 Support

Give a ⭐️ if you like this project!
___________________________________

<p>&copy; 2024 Ahmed Ashraf</p>