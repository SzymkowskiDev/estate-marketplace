DROP TABLE IF EXISTS OFFERS;

CREATE TABLE
    OFFERS (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        footer VARCHAR(255),
        location VARCHAR(255),
        price VARCHAR(255),
        price_per_meter VARCHAR(255),
        number_of_rooms INTEGER,
        description TEXT,
        floor VARCHAR(255),
        rent VARCHAR(255),
        remote_service VARCHAR(255),
        form_of_ownership VARCHAR(255),
        finishing_condition VARCHAR(255),
        balcony_garden_terrace VARCHAR(255),
        parking_space VARCHAR(255),
        heating VARCHAR(255),
        market VARCHAR(255),
        advertiser_type VARCHAR(255),
        available_from VARCHAR(255),
        year_of_construction VARCHAR(255),
        type_of_construction VARCHAR(255),
        windows VARCHAR(255),
        elevator VARCHAR(255),
        media VARCHAR(255),
        security VARCHAR(255),
        equipment VARCHAR(255),
        additional_infromation VARCHAR(255),
        building_material VARCHAR(255),
        url VARCHAR(255)
    );