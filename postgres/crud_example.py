import psycopg2
import utilities

# Query table
conn = utilities.connect_to_db()
cur = conn.cursor()
cur.execute("SELECT title FROM OFFERS;")
result = cur.fetchall()
print(result)
