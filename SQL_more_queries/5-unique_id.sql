-- Create a table named 'unique_id' if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    -- Define a column 'id' of type INT with a default value of 1 and a UNIQUE constraint
    id INT DEFAULT 1 UNIQUE,
    -- Define a column 'name' of type VARCHAR(256) that cannot contain NULL values
    name VARCHAR(256) NOT NULL
);
