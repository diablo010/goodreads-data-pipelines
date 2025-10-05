# SQL Analysis of Goodreads Book Data

This project demonstrates **data querying, aggregation, and insights extraction** of Goodreads book data using SQL.

## Overview

This analysis focuses on:

1. **Database Setup** – Create a `books` table in MySQL.
3. **Exploratory Queries** – Count, filter, and aggregate books, ratings, and publishers.
4. **Ranking & Grouping** – Use window functions and `GROUP BY` to find top books per publisher.
5. **Insights** – Identify patterns such as most popular publishers, books, and authors.

## How to Run

#### 1. Ensure the `books` table is created in your MySQL database.

> Load `cleaned_books.csv` dataset from ETL pipeline.

#### 2. Open and run the SQL scripts in `sql-analysis/goodreads_queries.sql` to reproduce the analysis.

> Note: Queries executed in Pandas and SQL are same. However, some results vary. For example, the date format in SQL is stricter whereas Pandas allows mixed date format.