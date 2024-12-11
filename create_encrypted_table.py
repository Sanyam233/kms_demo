from google.cloud import bigquery
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

client = bigquery.Client()
TABLE_ID = "project.dataset.table"
KMS_KEY=os.getenv("KMS_KEY")

def create_gbq_table():
    schema = [
        bigquery.SchemaField("x", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("y", "STRING", mode="NULLABLE")
    ]

    kms_encryption_config = bigquery.EncryptionConfiguration(kms_key_name=KMS_KEY)
    table = bigquery.Table(TABLE_ID, schema=schema)
    table.encryption_configuration = kms_encryption_config
    table = client.create_table(table)


def insert_rows():
    rows_to_insert = [
        {"x": "x1", "y": "y1"},
        {"x": "x2", "y": "y2"},
        {"x": "x3", "y": "y3"}
    ]

    errors = client.insert_rows_json(TABLE_ID, rows_to_insert)
    if errors:
        print(f"Errors while inserting rows: {errors}")
    else:
        print("Data inserted successfully.")


if __name__ == "__main__":
    # Create an encrypted BQ table
    create_gbq_table()

    # Insert some dummy data
    insert_rows()
