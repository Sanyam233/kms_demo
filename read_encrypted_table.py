from google.cloud import bigquery

client = bigquery.Client()

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
    sql = read_sql_file("./sql/kms.sql")
    
    results = get_results(sql)
    print("Encrypted Table Results:", results)