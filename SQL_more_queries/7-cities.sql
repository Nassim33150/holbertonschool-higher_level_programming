-- Create a database named 'hbtn_0d_usa' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create a table named 'cities' in the 'hbtn_0d_usa' database if it does not already exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);  
