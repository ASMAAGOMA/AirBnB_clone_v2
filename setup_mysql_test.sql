--database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
--create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
--give select privilleges
GRANT SELECT ON performance_schema.* to 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
--give all privilleges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
