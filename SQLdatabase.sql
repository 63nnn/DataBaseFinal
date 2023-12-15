DROP DATABASE `flower_shop`;

CREATE DATABASE `flower_shop`;
USE `flower_shop`;

CREATE TABLE `flowers`(`fnumber` VARCHAR(16) PRIMARY KEY, `fname` VARCHAR(16),
    `supplier` VARCHAR(16),
    `amount` INT,
    `unit` VARCHAR(4),
	`unit_price` DECIMAL(10,2),
    `total_price` DECIMAL(10,2),
    `location` VARCHAR(20),
    `purchase_date` DATE
);
DESCRIBE `flowers`;

CREATE TABLE `customer`(
	`cname` VARCHAR(16),
    `cnumber` VARCHAR(10) PRIMARY KEY,
    `birthday` DATE,
    `phone` VARCHAR(16),
    `Email` VARCHAR(42),
    `address` VARCHAR(42),
    `age` INT,
    `photo` LONGBLOB,
    `VIPdiscount` DECIMAL(3,2)
);
DESCRIBE `customer`;

CREATE TABLE `supplier`(
	`sname` VARCHAR(16),
    `snumber` VARCHAR(10) PRIMARY KEY,
    `phone` VARCHAR(16),
    `address` VARCHAR(42),
    `in_charge` VARCHAR(16)
);
DESCRIBE `supplier`;

CREATE TABLE `purchase`(
	`fname` VARCHAR(16),
    `cnumber` VARCHAR(10) PRIMARY KEY,
    `fnumber` VARCHAR(16) ,
    `sname` VARCHAR(16),
    `pur_amount` INT,
    `unit_price` DECIMAL(10,2),
    `total_price` DECIMAL(10,2),
    `discount_price` DECIMAL(10,2),
    `pur_date` DATE,
    `exp_delivery` DATE,
    `real_delivery` DATE
);
DESCRIBE `purchase`;


