import psycopg2

# Database connection
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="estate",
    user="postgres",
    password="pass"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# # Create tables
# sql = """
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50),
#     email VARCHAR(50),
#     password VARCHAR(50)
# );
# """
# cur.execute(sql)

# # Populate table with dummy data
# data = """
# INSERT INTO users (name, email, password) VALUES
#     ('Alice', 'alice@example.com', 'password1'),
#     ('Bob', 'bob@example.com', 'password2'),
#     ('Charlie', 'charlie@example.com', 'password3');
# """
# cur.execute(data)

# Query table
cur.execute("SELECT * FROM users;")
result = cur.fetchall()
print(result)

# Close communication with the database
cur.close()
conn.close()
