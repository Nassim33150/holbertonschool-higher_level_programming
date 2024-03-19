-- Create a new database 'hbtn_0d_2' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create a new user 'user_0d_2'@'localhost' with the specified password if the user does not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges on all tables in the 'hbtn_0d_2' database to the user 'user_0d_2'@'localhost'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
