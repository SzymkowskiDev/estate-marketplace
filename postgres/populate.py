import utilities

# Create tables
utilities.create_tables()

# Populate database
utilities.populate_offers_db(file_path="postgres/dummy_data/offers_data.json")
utilities.populate_buyers_db(file_path="postgres/dummy_data/buyers_data.json")
utilities.populate_sellers_db(file_path="postgres/dummy_data/sellers_data.json")

# Add randomly generated foreign key relations
conn = utilities.connect_to_db()
cur = conn.cursor()

sql = """
ALTER TABLE OFFERS ADD seller_id INT;
UPDATE OFFERS SET seller_id = FLOOR(RANDOM() * 3000) + 1;
ALTER TABLE OFFERS
ADD CONSTRAINT FK_OFFERS_SELLERS FOREIGN KEY (seller_id) REFERENCES SELLERS(seller_id);
"""

cur.execute(sql)
cur.close()
conn.commit()
conn.close()