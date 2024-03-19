-- Create a database named 'hbtn_0d_usa' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create a table named 'states' in the 'hbtn_0d_usa' database if it does not already exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    -- Define a column 'id' of type INT with a UNIQUE constraint, PRIMARY KEY constraint, NOT NULL, and AUTO_INCREMENT property
    id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    -- Define a column 'name' of type VARCHAR(256) that cannot contain NULL values
    name VARCHAR(256) NOT NULL
);
