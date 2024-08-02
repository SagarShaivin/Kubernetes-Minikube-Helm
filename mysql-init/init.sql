CREATE DATABASE IF NOT EXISTS pyapplicationdb;
USE pyapplicationdb;

CREATE USER IF NOT EXISTS 'admin'@'%' IDENTIFIED BY 'admin@123';
GRANT ALL PRIVILEGES ON pyapplicationdb.* TO 'admin'@'%';
FLUSH PRIVILEGES;

-- Create a sample table and insert data
CREATE TABLE IF NOT EXISTS random_words (
    id INT AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(255) NOT NULL
);

INSERT INTO random_words (word) VALUES ('example');
