# 📚 Goodreads ETL with Apache Airflow

An end-to-end ETL pipeline built using **Apache Airflow (in Docker)** to extract, transform, and load Goodreads book data into a **MySQL database**. The DAG is written using **TaskFlow API** for better readability and modularity.

## 🚀 Project Overview

This ETL pipeline performs the following steps:

- **Extract**: Reads a CSV file containing Goodreads data from the `/opt/airflow/dags/` directory.
- **Transform**: Cleans and formats the data (e.g., converts dates, handles missing values).
- **Load**: Inserts the processed data into a MySQL database (`your_db`) using `mysql-connector-python`.

## 🧰 Tech Stack

| Tool               | Purpose                        |
|--------------------|--------------------------------|
|   Docker Desktop   | Containerization environment   |
|   Apache Airflow   | Workflow orchestration         |
|   TaskFlow API     | DAG writing style in Airflow   |
|    MySQL Workbench | Visualize and verify data load |

## 📂 DAG Breakdown:
```python
extract() --> transform() --> load()
```

## ✅ DAG Features
- Written using `TaskFlow API (@task) decorators` for clean, modular logic.
- Retry mechanism (`retries=5` , `retry_delay=5 minutes`) for fault tolerance.
- Supports scheduling via `@daily` cron expression.

## ⚙️ How to Run the Project

#### 1. Install dependencies from `requirements.txt` 

#### 2. Start Airflow

```bash
docker compose up -d
```

#### 3. Run MySQL in Docker

```bash
docker run --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=yourpassword \
  -e MYSQL_DATABASE=your_db \
  -p 3307:3306 \
  -d mysql:8
```
> MySQL by default runs at `localhost:3306`, but, the port was occupied by other service. So, port `3307` is used.

#### 4. Update Connection Details (e.g., username, password) in `connect` step of `load.py`

#### 5. Trigger the DAG
- Enable and run `goodreads_dag` from the Airflow UI

> Note: Ensure that all files of this project folder are uploaded within the `dags/` folder of Dockerized Airflow container in your setup. And keep Docker Desktop running in background.
