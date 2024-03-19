-- Check if the user 'user_0d_1'@'localhost' exists in the MySQL user table
SET @user_exists = (SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost');

-- If the user does not exist, create the user and grant all privileges
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'; 
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
END IF;
