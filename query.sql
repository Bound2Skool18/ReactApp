CREATE DATABASE IF NOT EXISTS your_database_name;

USE your_database_name; 

CREATE TABLE REP (
    rep_id VARCHAR(35),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address VARCHAR(100),
    city VARCHAR(50),
    state CHAR(2), 
    postal VARCHAR(10),
    cell_phone VARCHAR(15),
    commission NUMERIC(10, 2),
    rate NUMERIC(5, 4)
);
