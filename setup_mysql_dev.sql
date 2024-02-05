-- Check if the database exists
SELECT IF(
    EXISTS (
        SELECT SCHEMA_NAME
        FROM INFORMATION_SCHEMA.SCHEMATA
        WHERE SCHEMA_NAME = 'hbnb_dev_db'
    ),
    'Database exists',
    'Database does not exist'
);

-- Check if the user exists
SELECT IF(
    EXISTS (
        SELECT USER
        FROM mysql.user
        WHERE USER = 'hbnb_dev' AND HOST = 'localhost'
    ),
    'User exists',
    'User does not exist'
);

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
