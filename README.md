# 📚 Goodreads ETL Project

A simple end-to-end **ETL pipeline** that extracts, cleans, and loads data from a Goodreads dataset into a MySQL database — followed by SQL queries to gain insights.

## 🧩 Project Overview

- **📂 Dataset**: Goodreads Books Dataset
- **⚙️ Tools**: Python, Pandas, MySQL, MySQL Workbench
- **💡 Goal**: Load and explore book metadata like ratings, authors, and publication details

## ⚙️ ETL Steps

### 1. **Extract**
- Load raw `books.xlsx` into a Pandas DataFrame

### 2. **Transform**
- Parse date columns (`publication_date`)
- Handle missing values
- Export cleaned data to `cleaned_books.csv`

### 3. **Load**
- Connect to MySQL using `mysql.connector`
- Create a table `books`
- Load each row from the DataFrame into MySQL

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

To run this project,
- install requirements from `requirements.txt`
- update in Load step of `clean_db.py`
- run `clean_db.py` on terminal

**And you are good to go! 💪**
    
> Note: `<your_db>` should be present in MySQL Workbench
