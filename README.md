# 📚 Goodreads Data Project

This repository contains multiple projects showcasing **data engineering workflows** and analysis using Goodreads book data.  
<br/>
It includes ETL pipelines, Pandas analysis, and SQL analysis to demonstrate end-to-end data handling, cleaning, transformation, and insights extraction.


##  Project Overview

- **Dataset**: Goodreads Books Dataset (`books.xlsx` or `books.csv`)
- **Tools**:
  - Python, Pandas
  - MySQL, MySQL Workbench
  - Apache Airflow (Docker)

##  Database Schema

| Column               | Data Type     |
|----------------------|---------------|
| book_id              | int           |
| title                | varchar(255)  |
| authors              | text          |
| average_rating       | float         |
| isbn                 | varchar(20)   |
| isbn13               | varchar(20)   |
| language_code        | varchar(15)   |
| num_pages            | int           |
| ratings_count        | int           |
| text_reviews_count   | int           |
| publication_date     | date          |
| publisher            | varchar(255)  |

## ETL Pipeline Versions

### 🔸 Version 1 : Manual ETL (No Automation)

A simple script-based pipeline using Python and MySQL.

Refer [README.md](https://github.com/diablo010/goodreads-etl-pipeline/blob/main/ETL/manual-version/README.md) from `manual-version` folder.

---

### 🔹 Version 2 : Automated ETL with Apache Airflow + Docker

A production-style version using Apache Airflow inside Docker to orchestrate the workflow.

Refer [README.md](https://github.com/diablo010/goodreads-etl-pipeline/blob/main/ETL/airflow-version/README.md) from `airflow-version` folder.

## Analysis

### 🔸 1 : Pandas Analysis

A Jupyter Notebook-based analysis using Python and Pandas for data cleaning, exploration, and visualization.

Refer [README.md](https://github.com/diablo010/goodreads-etl-pipeline/blob/main/Analysis/pandas-analysis/README.md) from `pandas-analysis` folder.

---

### 🔹 2 : SQL Analysis

A SQL-based analysis on the dataset to answer business questions, aggregations, and insights.

Refer [README.md](https://github.com/diablo010/goodreads-etl-pipeline/blob/main/Analysis/sql-analysis/README.md) from `sql-analysis` folder.
