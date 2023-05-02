import psycopg2
import utilities

# Create tables
utilities.create_tables()

# # Populate database
utilities.populate_db(file_path='src/sample_data.json', table='OFFERS')

# # Query table
conn = utilities.connect_to_db()
cur = conn.cursor()
cur.execute("SELECT title FROM OFFERS;")
result = cur.fetchall()
print(result)
