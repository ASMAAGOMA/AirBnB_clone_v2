--database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
--give select privilleges
GRANT SELECT ON performance_schema.* to 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
--give all privilleges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
