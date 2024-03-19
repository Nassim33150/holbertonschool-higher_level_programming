-- Create a table named 'id_not_null' if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    -- Define a column 'id' of type INT with a default value of 1
    id INT DEFAULT 1,
    -- Define a column 'name' of type VARCHAR(256) that cannot contain NULL values
    name VARCHAR(256) NOT NULL
);
