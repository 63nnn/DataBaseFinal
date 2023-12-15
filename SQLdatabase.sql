DROP DATABASE `flower_shop`;

CREATE DATABASE `flower_shop`;
USE `flower_shop`;

CREATE TABLE `flowers`(
	`fnumber` VARCHAR(16) PRIMARY KEY NOT NULL,
    `fname` VARCHAR(16),
    `supplier` VARCHAR(16) NULL,
    `snumber` VARCHAR(10) NULL,
    `amount` INT NOT NULL,
    `unit` VARCHAR(4) NOT NULL,
	`unit_price` DECIMAL(10,2) NOT NULL,
    `total_price` DECIMAL(10,2),
    `location` VARCHAR(20) NOT NULL,
    `purchase_date` DATE
);
DESCRIBE `flowers`;

CREATE TABLE `customer`(
	`cname` VARCHAR(16) NOT NULL,
    `cnumber` VARCHAR(10) PRIMARY KEY NOT NULL,
    `birthday` DATE,
    `phone` VARCHAR(16) NOT NULL,
    `Email` VARCHAR(42),
    `address` VARCHAR(42) NULL,
    `age` INT,
    `photo` LONGBLOB,
    `VIPdiscount` DECIMAL(3,2)
);
DESCRIBE `customer`;

CREATE TABLE `supplier`(
	`sname` VARCHAR(16) NOT NULL,
    `snumber` VARCHAR(10) PRIMARY KEY NOT NULL,
    `phone` VARCHAR(16) NOT NULL,
    `address` VARCHAR(42) NOT NULL,
    `in_charge` VARCHAR(16)
);
DESCRIBE `supplier`;

CREATE TABLE `purchase`(
	`fname` VARCHAR(16) NOT NULL,
    `cnumber` VARCHAR(10),
    `fnumber` VARCHAR(16),
    `sname` VARCHAR(16),
    `pur_amount` INT NOT NULL,
    `unit_price` DECIMAL(10,2),
    `total_price` DECIMAL(10,2),
    `discount_price` DECIMAL(10,2),
    `pur_date` DATE,
    `exp_delivery` DATE,
    `real_delivery` DATE,
    PRIMARY KEY(`cnumber`,`fnumber`)
);
DESCRIBE `purchase`;

CREATE TABLE `stable_customer`(
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
DESCRIBE `stable_customer`;

ALTER TABLE `flowers`
ADD FOREIGN KEY (`snumber`)
REFERENCES `supplier`(`snumber`) ON DELETE SET NULL;




