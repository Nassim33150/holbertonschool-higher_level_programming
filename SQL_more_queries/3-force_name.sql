-- Create a table named 'force_name' if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    -- Define a column 'id' of type INT
    id INT,
    -- Define a column 'name' of type VARCHAR(256) that cannot contain NULL values
    name VARCHAR(256) NOT NULL
);
