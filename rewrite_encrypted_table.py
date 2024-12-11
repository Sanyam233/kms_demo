from google.cloud import bigquery
import os
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

# Initialize the BigQuery client
client = bigquery.Client()
TABLE_ID = "vpc-1-439422.kmsTest.Test1"
NEW_TABLE_ID = "vpc-1-439422.kmsTest.Test3"
KMS_KEY=os.getenv("KMS_KEY")# Set the query

query = f"SELECT x, y FROM `{TABLE_ID}`"


# Configure encryption settings
job_config = bigquery.QueryJobConfig(
    destination=NEW_TABLE_ID,
    destination_encryption_configuration=bigquery.EncryptionConfiguration(
        kms_key_name=KMS_KEY
    ),
)

query_job = client.query(query, job_config=job_config)
results = query_job.result()

print("Query executed and results written with encryption.")