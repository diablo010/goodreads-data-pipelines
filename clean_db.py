import pandas as pd
import mysql.connector

# Step 1: Extract
df = pd.read_excel("D:\\resume projects\\Goodreads-Books-Analysis\\dataset\\books.xlsx")

# Step 2: Try converting the date column (if it exists)
if 'publication_date' in df.columns:
    df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')

# Save the cleaned data as a CSV
df.to_csv("D:\\resume projects\\Goodreads-Books-Analysis\\dataset\\cleaned_books.csv", index=False)

print("✅ Done! Cleaned file saved.")

# Step 3: Load
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "192837",
    database = "books_db"
)

cursor = conn.cursor()

cursor.execute("drop table if exists books;")

cursor.execute("""
create table if not exists books (
    book_id int,
    title varchar(255),
    authors text,
    average_rating float,
    isbn varchar(20),
    isbn13 varchar(20),    
    language_code varchar(15),
    num_pages int,
    ratings_count int,
    text_reviews_count int,       
    publication_date date,
    publisher varchar(255)
)
""")

# int may not work as the value may start at 0 and int will by default trim it

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
        insert into books (book_id, 
                           title, 
                           authors, 
                           average_rating, 
                           isbn, 
                           isbn13, 
                           language_code, 
                           num_pages, 
                           ratings_count, 
                           text_reviews_count, 
                           publication_date, 
                           publisher)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row.get('book_id'),
        row.get('title'),
        row.get('authors'),
        row.get('average_rating'),
        row.get('isbn'),
        row.get('isbn13'),
        row.get('language_code'), 
        row.get('num_pages'),
        row.get('ratings_count'),
        row.get('text_reviews_count'),
        row.get('publication_date').date(),
        row.get('publisher')
    ))


conn.commit()
cursor.close()
conn.close()

print("🔥ETL complete!")