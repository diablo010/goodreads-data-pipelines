# 📚 Goodreads ETL Project

This repository contains two versions of an end-to-end **ETL pipeline** that processes Goodreads book data into a MySQL database.

## 🧩 Project Overview

- **📂 Dataset**: Goodreads Books Dataset (`books.xlsx` or `books.csv`)
- **⚙️ Tools**:
  - Python, Pandas
  - MySQL, MySQL Workbench
  - Apache Airflow (Docker)

## 🗃️ Database Schema

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

## 🔀 ETL Pipeline Versions

### 🔸 Version 1: Manual ETL (No Automation)

A simple script-based pipeline using Python and MySQL.

#### ✅ Steps:
1. **Extract**  
   - Load `books.xlsx` into a Pandas DataFrame

2. **Transform**  
   - Clean and standardize the data  
   - Parse date columns (publication_date)  
   - Export cleaned data to `cleaned_books.csv`

3. **Load**  
   - Connect to MySQL using `mysql.connector`
   - Create the `books` table (if not present)
   - Load each row from the DataFrame into MySQL

#### 🏃‍♀️ How to Run:
- Install dependencies:

```bash
pip install -r requirements.txt
```

- Update Connection Details (e.g., username, password) in `connect` step of `clean_db.py`

- Run `clean_db.py` on terminal
    
> Note: <your_db> should be present in MySQL Workbench

---

### 🔹 Version 2: Automated ETL with Apache Airflow + Docker

A production-style version using Apache Airflow inside Docker to orchestrate the workflow.

Refer [README.md](https://github.com/diablo010/goodreads-etl-pipeline/blob/main/airflow-version/README.md) from `airflow-version` folder.
