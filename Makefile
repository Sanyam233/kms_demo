export GOOGLE_APPLICATION_CREDENTIALS := ./service-key.json

create:
	python3 create_encrypted_table.py

read:
	python3 read_encrypted_table.py

rewrite:
	python3 rewrite_encrypted_table.py

decrypt:
	python3 decrypt_table_col.py
