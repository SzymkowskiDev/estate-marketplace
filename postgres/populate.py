import psycopg2
import utilities

# Create tables
utilities.create_tables()

# Populate database
utilities.populate_db(file_path="postgres/sample_data.json", table="OFFERS")
