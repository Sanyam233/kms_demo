export GOOGLE_APPLICATION_CREDENTIALS := ./kms-gcp-20241210.json

create:
	python3 create_encrypted_table.py

read:
	python3 read_encrypted_table.py

rewrite:
	python3 rewrite_encrypted_table.py

decrypt:
	python3 decrypt_table_col.py

show-gcp-service:
	bq show --encryption_service_account --project_id=vpc-1-439422