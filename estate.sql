CREATE TABLE
    users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );

CREATE TABLE
    properties (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price NUMERIC NOT NULL,
        user_id INTEGER REFERENCES users(id)
    );