import psycopg2
import json
import random
import string
from faker import Faker

def connect_to_db():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="estate",
        user="postgres",
        password="pass"
    )

    return conn


def create_tables():

    conn = connect_to_db()
    cur = conn.cursor()

    # Create tables
    with open('postgres/estate.sql', 'r') as f:
        sql = f.read()
    cur.execute(sql)

    # Close communication with the database
    cur.close()
    conn.commit()
    # conn.close()


def populate_offers_db(file_path):

    # Open file
    with open(file_path) as f:
        sample_data = json.load(f)

    conn = connect_to_db()

    cur = conn.cursor()

    # Populate table with sample data
    for offer in sample_data:
        print("Populating 'OFFERS' table...")
        sql = """
        INSERT INTO OFFERS (
            title,
            footer,
            location,
            price,
            price_per_meter,
            number_of_rooms,
            description,
            floor,
            rent,
            remote_service,
            form_of_ownership,
            finishing_condition,
            balcony_garden_terrace,
            parking_space,
            heating,
            market,
            advertiser_type,
            available_from,
            year_of_construction,
            type_of_construction,
            windows,
            elevator,
            media,
            security,
            equipment,
            additional_infromation,
            building_material,
            url
        ) VALUES (
            %(title)s,
            %(footer)s,
            %(location)s,
            %(price)s,
            %(price_per_meter)s,
            %(number_of_rooms)s,
            %(description)s,
            %(floor)s,
            %(rent)s,
            %(remote_service)s,
            %(form_of_ownership)s,
            %(finishing_condition)s,
            %(balcony_garden_terrace)s,
            %(parking_space)s,
            %(heating)s,
            %(market)s,
            %(advertiser_type)s,
            %(available_from)s,
            %(year_of_construction)s,
            %(type_of_construction)s,
            %(windows)s,
            %(elevator)s,
            %(media)s,
            %(security)s,
            %(equipment)s,
            %(additional_infromation)s,
            %(building_material)s,
            %(url)s
        );
        """
        cur.execute(sql, offer)

    # Close communication with the database
    cur.close()
    conn.commit()
    conn.close()


def generate_data(num_records, file_path):
    fake = Faker()
    data = []
    for i in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        mobile = ''.join(random.choices(string.digits, k=10))
        record = {"first_name": first_name, "last_name": last_name, "email": email, "mobile": mobile}
        data.append(record)

    with open(file_path, 'w') as f:
        json.dump(data, f)


def populate_buyers_db(file_path):

    # Open file
    with open(file_path) as f:
        sample_data = json.load(f)

    conn = connect_to_db()

    cur = conn.cursor()

    # Populate table with sample data
    for offer in sample_data:
        print("Populating 'BUYERS' table...")
        sql = """
        INSERT INTO BUYERS (
            first_name,
            last_name,
            email,
            mobile
        ) VALUES (
            %(first_name)s,
            %(last_name)s,
            %(email)s,
            %(mobile)s
        );
        """
        cur.execute(sql, offer)

    # Close communication with the database
    cur.close()
    conn.commit()
    conn.close()


def populate_sellers_db(file_path):

    # Open file
    with open(file_path) as f:
        sample_data = json.load(f)

    conn = connect_to_db()

    cur = conn.cursor()

    # Populate table with sample data
    for offer in sample_data:
        print("Populating 'SELLERS' table...")
        sql = """
        INSERT INTO SELLERS (
            first_name,
            last_name,
            email,
            mobile
        ) VALUES (
            %(first_name)s,
            %(last_name)s,
            %(email)s,
            %(mobile)s
        );
        """
        cur.execute(sql, offer)

    # Close communication with the database
    cur.close()
    conn.commit()
    conn.close()