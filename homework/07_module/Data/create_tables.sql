CREATE TABLE card_holder (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE credit_card (
    card VARCHAR(20) PRIMARY KEY,
    cardholder_id INT REFERENCES card_holder(id),
);

CREATE TABLE merchant_category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE merchant (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    id_merchant_category INT REFERENCES merchant_category(id),
);

CREATE TABLE transaction (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP,
    amount NUMERIC,
    card VARCHAR(20) REFERENCES credit_card(card),
    id_merchant INT REFERENCES merchant(id),
);