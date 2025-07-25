import pandas as pd

def extract_data():
    
    # Load data from csv into dataframe
    input_path = '/opt/airflow/dags/books.csv'         # airflow in docker container path
    df = pd.read_csv(input_path)                       

    # Save the extracted data as a CSV
    output_path = '/opt/airflow/dags/extracted_books.csv'         # airflow in docker container path
    df.to_csv(output_path, index=False)
    
    print(f"🔥 Data extraction completed !\n"
          f"Combined data saved at: {output_path}")

if __name__ == "__main__":
    extract_data()