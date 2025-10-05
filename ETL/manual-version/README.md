# Goodreads Books ETL Pipeline (Manual Version)

A **manual ETL pipeline** using Python and MySQL to extract, transform, and load the books data. This pipeline demonstrates how to process and load data into a MySQL database using Python scripts.

## Overview

This manual ETL pipeline performs the following steps:

- **Extract**: Loads the `books.csv` file from the `dataset/` folder into a Pandas DataFrame.
- **Transform**: Cleans and standardizes the data (e.g., handles missing values, parses `publication_date`).
- **Load**: Inserts the processed data into a MySQL database (`your_db`) using `mysql-connector-python`.


## Steps:
1. **Extract**  
   - Load `books.csv` into a Pandas DataFrame

2. **Transform**  
   - Clean and standardize the data  
   - Parse date columns (publication_date)  
   - Export cleaned data to `cleaned_books.csv`

3. **Load**  
   - Connect to MySQL using `mysql.connector`
   - Create the `books` table (if not present)
   - Load each row from the DataFrame into MySQL

##  How to Run:
#### 1. Install dependencies:

```bash
pip install -r requirements.txt
```

#### 2. Update Connection Details (e.g., username, password) in `connect` step of `clean_db.py`

#### 3. Run `clean_db.py` on terminal
    
> Note: <your_db> should be present in MySQL Workbench

> To run the manual version, make sure you also have the dataset folder.
