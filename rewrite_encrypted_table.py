from google.cloud import bigquery

# Initialize the BigQuery client
client = bigquery.Client()
TABLE_ID = "vpc-1-439422.kmsTest.Test1"
NEW_TABLE_ID = "vpc-1-439422.kmsTest.Test3"
KMS_KEY="projects/vpc-1-439422/locations/us/keyRings/us-test/cryptoKeys/us-test-key"
# Set the query
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