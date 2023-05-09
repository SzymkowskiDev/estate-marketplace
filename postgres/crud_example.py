import psycopg2
import utilities

# Query table
conn = utilities.connect_to_db()
cur = conn.cursor()

cur.execute("SELECT id, seller_id, price FROM OFFERS LIMIT 10;")
result = cur.fetchall()
print(result)
# cur.close()
# conn.commit()
# conn.close()