CREATE DATABASE flaskdocker;

USE flaskdocker;

CREATE TABLE `flaskdocker`.`facts` (
    `id` INT NOT NULL AUTO_INCREMENT, `fact` VARCHAR(10000), PRIMARY KEY (ID)
);