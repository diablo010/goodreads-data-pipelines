import pandas as pd
import mysql.connector

def load_data():
    # Load the transformed data
    transformed_data_path = '/opt/airflow/dags/transformed_books.csv'         # airflow in docker container path
    df = pd.read_csv(transformed_data_path)
    
    # Establish connection to MySQL
    conn = mysql.connector.connect(
        host = "host.docker.internal",     # Airflow cannot resolve the hostname mysql-container inside the Docker network
                                           # special hostname that points to Windows host machine from inside Docker containers
        port=3307,                         #3306 is busy so 3307 is used
        user = "root",
        password = "your_pass",
        database = "your_db"
    )

    cursor = conn.cursor()

    # Drop table if exists
    cursor.execute("drop table if exists books;")

    # Create table if it does not exist
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

    # int may not work for isbn 
    # as the value may start at 0 and int will by default trim it

    # Insert data into the table
    for _, row in df.iterrows():

        # Convert publication_date into dateoject
        # as csv takes the input as str only
        pub_date = pd.to_datetime(row.get('publication_date'), errors='coerce')

        if pd.isnull(pub_date):
            pub_date = None
        else:
            pub_date = pub_date.date()  

        # Create a table to store data
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
            pub_date,
            row.get('publisher')
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("🔥Data loading completed successfully.")

if __name__ == "__main__":
    load_data()