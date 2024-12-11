from google.cloud import bigquery
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

client = bigquery.Client()
TABLE_ID = "vpc-1-439422.kmsTest.Test2"
KMS_KEY=os.getenv("KMS_KEY")

def read_sql_file(path):
    with open(path, "r") as file:
        sql_query = file.read()
    return sql_query


def get_results(sql):
    job = client.query(sql)
    results = job.result()
    formatted_results = [dict(r) for r in results]
    return formatted_results


if __name__ == "__main__":
    sql = read_sql_file("./sql/decrypt.sql")

    results = get_results(sql)
    print("Decrypted Col Results:",results)