DROP TABLE IF EXISTS SELLERS CASCADE;

CREATE TABLE
    SELLERS (
        seller_id SERIAL PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        mobile VARCHAR(255)
    );

DROP TABLE IF EXISTS OFFERS CASCADE;

-- TODO: add FK

CREATE TABLE
    OFFERS (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        footer FLOAT,
        location VARCHAR(255),
        price INTEGER,
        price_per_meter INTEGER,
        number_of_rooms INTEGER,
        description TEXT,
        floor VARCHAR(255),
        rent INTEGER,
        remote_service BOOLEAN,
        form_of_ownership VARCHAR(255),
        finishing_condition VARCHAR(255),
        balcony_garden_terrace VARCHAR(255),
        parking_space VARCHAR(255),
        heating VARCHAR(255),
        market VARCHAR(255),
        advertiser_type VARCHAR(255),
        available_from VARCHAR(255),
        year_of_construction INTEGER,
        type_of_construction VARCHAR(255),
        windows VARCHAR(255),
        elevator BOOLEAN,
        media VARCHAR(255),
        security VARCHAR(255),
        equipment VARCHAR(255),
        additional_infromation VARCHAR(255),
        building_material VARCHAR(255),
        url VARCHAR(255)
    );

DROP TABLE IF EXISTS BUYERS CASCADE;

CREATE TABLE
    BUYERS (
        buyer_id SERIAL PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        mobile VARCHAR(255)
    );