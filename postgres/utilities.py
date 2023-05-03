import psycopg2
import json


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


def populate_db(file_path, table):

    # Open file
    with open(file_path) as f:
        sample_data = json.load(f)

    conn = connect_to_db()

    cur = conn.cursor()

    # Load sample data
    with open('postgres/sample_data.json') as f:
        sample_data = json.load(f)

    # Populate table with sample data
    for offer in sample_data:
        print("Populating table...")
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

    # cur.execute("SELECT title, price FROM OFFERS;")
    # result = cur.fetchall()
    # print(result)
    # Close communication with the database
    cur.close()
    conn.commit()
    conn.close()
