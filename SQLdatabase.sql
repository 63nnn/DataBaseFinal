DROP DATABASE `flower_shop`;

CREATE DATABASE `flower_shop`;
USE `flower_shop`;

CREATE TABLE `flowers`(
	`fnumber` VARCHAR(16) PRIMARY KEY NOT NULL,
    `fname` VARCHAR(16),
    `supplier` VARCHAR(16) NULL,
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
    `Email` VARCHAR(25),
    `age` INT,
    `photo` LONGBLOB,
    `VIPdiscount` DECIMAL(3,2),
    `address` VARCHAR(25) NULL
);
DESCRIBE `customer`;

CREATE TABLE `supplier`(
	`sname` VARCHAR(16) NOT NULL,
    `snumber` VARCHAR(10) PRIMARY KEY NOT NULL,
    `phone` VARCHAR(16) NOT NULL,
    `Email` VARCHAR(25),
    `in_charge` VARCHAR(16),
    `address` VARCHAR(25) NOT NULL
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
    `real_delivery` DATE NULL,
    PRIMARY KEY(`cnumber`,`fnumber`)
);
DESCRIBE `purchase`;

CREATE TABLE `stable_customer`(
	`cname` VARCHAR(16),
    `cnumber` VARCHAR(10) PRIMARY KEY,
    `birthday` DATE,
    `phone` VARCHAR(16),
    `Email` VARCHAR(25),
    `age` INT,
    `photo` LONGBLOB,
    `VIPdiscount` DECIMAL(3,2),
    `address` VARCHAR(25)
);
DESCRIBE `stable_customer`;

-- ALTER TABLE `flowers`
-- ADD FOREIGN KEY (`snumber`)
-- REFERENCES `supplier`(`snumber`) ON DELETE SET NULL;

INSERT INTO `flowers` VALUES("09-876-0543-2","玫瑰花","南海苗圃",20,"束",6.00,120.00,"二樓花房","2018-11-20");
INSERT INTO `flowers` VALUES("30-342-2354-3","繡球花","南海苗圃",120,"盆",2.00,240.00,"三樓花房","2018-12-11");
INSERT INTO `flowers` VALUES("74-345-3222-4","天堂鳥","北風花市",300,"盆",7.00,2100.00,"二樓花房","2018-12-13");
INSERT INTO `customer` VALUES("胡謅鄒","B123456789","2000-11-13","04-2345-6666","321@gmail.com" ,20,"photo",0.82,"台中市台灣大道四段一七二七號");
INSERT INTO `supplier` VALUES("地海苗圃","52994484","04-2359-0121","221@gmail.com","王海東","台中市台灣大道14號");
INSERT INTO `purchase` VALUES("水仙花","B187654321","09-878-0540-2","北海苗園", 30, 15.00, 450.00, 369.00,"2018-10-31","2018-11-02",NULL);

SELECT * FROM `flowers` WHERE `fnumber` = "09-876-0543-2" AND `fname` = "玫瑰花";


SELECT * FROM `flowers`;
SELECT * FROM `customer`;
SELECT * FROM `supplier`;
SELECT * FROM `purchase`;
SELECT * FROM `stable_customer`;

SELECT * FROM `supplier` WHERE `sname` = "地海苗圃";