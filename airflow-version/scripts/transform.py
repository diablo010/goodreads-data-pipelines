import pandas as pd

def transform_data():
    # Step 1: Load the extracted data
    data_path = '/opt/airflow/dags/extracted_books.csv'         # airflow in docker container path
    df = pd.read_csv(data_path)

    # Step 2: Handle missing values
    if 'publication_date' in df.columns:
        df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')
        
    # Save the transformed data
    output_path = '/opt/airflow/dags/transformed_books.csv'         # airflow in docker container path
    df.to_csv(output_path, index=False)

    print(f"🔥Data transformation completed and saved at: {output_path}")

if __name__ == "__main__":
    transform_data()