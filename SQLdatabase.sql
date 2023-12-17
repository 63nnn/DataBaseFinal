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


INSERT INTO `flowers` VALUES("08-878-0540-2","水仙花","北海苗圃",20,"束",15.00,750.00,"一樓花房","2018-10-30");
INSERT INTO `flowers` VALUES("09-876-0543-2","玫瑰花","南海苗圃",20,"束",6.00,120.00,"二樓花房","2018-11-20");
INSERT INTO `flowers` VALUES("09-156-5486-1","繡球花","南海苗圃",30,"束",20.00,600.00,"二樓花房","2018-12-20");
INSERT INTO `flowers` VALUES("74-345-3222-4","天堂鳥","北風花市",300,"盆",7.00,2100.00,"二樓花房","2018-12-13");
INSERT INTO `flowers` VALUES("07-165-1654-4","仙人掌","東海苗圃",25,"盆",10.00,250.00,"五樓花房","2019-11-02");
INSERT INTO `flowers` VALUES("07-165-4546-6","檜木苗","東海苗圃",5,"株",1000.00,5000.00,"五樓花房","2019-05-05");
INSERT INTO `flowers` VALUES("07-165-4849-3","馬鞭草","東海苗圃",100,"盆",5.00,500.00,"五樓花房","2018-10-20");
INSERT INTO `flowers` VALUES("07-165-6564-5","薄荷","東海苗圃",50,"盆",10.00,500.00,"五樓花房","2018-10-31");
INSERT INTO `flowers` VALUES("08-346-5485-5","鬱金香","北海苗圃",10,"束",60.00,600.00,"一樓花房","2019-10-30");

INSERT INTO `customer` VALUES("胡謅鄒","B123456789","2000-11-13","04-2345-6666","321@gmail.com" ,20,"photo",0.82,"台中市台灣大道四段一七二七號");
INSERT INTO `customer` VALUES("張三","B198765432","2001-10-30","04-5461-7915","121@gmail.com" ,22,"photo",0.82,"台中市台灣大道三段三百二十號");
INSERT INTO `customer` VALUES("李四","B154876236","1999-1-12","04-4854-2154","021@gmail.com" ,24,"photo",0.82,"台中市台灣大道四段兩百五十號");
INSERT INTO `customer` VALUES("王一","A164872166","2000-5-5","04-4566-4562","331@gmail.com" ,23,"photo",0.82,"台中市台灣大道五段二十七號");
INSERT INTO `customer` VALUES("劉二","C158716214","2000-1-2","04-2636-1654","421@gmail.com" ,23,"photo",0.82,"台中市玉門路一七二七號");
INSERT INTO `customer` VALUES("孔十","J216455547","1955-8-10","04-4596-4494","621@gmail.com" ,68,"photo",0.82,"台中市遊園南路三段六十一號");
INSERT INTO `customer` VALUES("林與","A264848464","2001-4-5","04-6454-1649","721@gmail.com" ,22,"photo",0.82,"台中市中科路一段五百七十號");
INSERT INTO `customer` VALUES("黃湘","O223456789","2000-11-13","03-1578-6895","321@gmail.com" ,30,"photo",0.82,"台中市台灣大道四段一七二七號");

INSERT INTO `supplier` VALUES("南海苗圃","C312345678","04-2359-0121","221@gmail.com","王海東","台中市台灣大道14號");
INSERT INTO `supplier` VALUES("東海苗圃","C286342445","04-5668-2665","551@gmail.com","陳花","台中市台灣大道21號");
INSERT INTO `supplier` VALUES("北海苗圃","C066288510","04-1465-6554","177@gmail.com","王海東","台中市西屯路112號");
INSERT INTO `supplier` VALUES("太平洋苗圃","C493524515","04-6495-1265","221@gmail.com","林加龍","台中市中科路66號");
INSERT INTO `supplier` VALUES("黑海苗圃","C391684210","04-6556-1351","261@gmail.com","委於","台中市向上路一段17號");

INSERT INTO `purchase` VALUES("水仙花","B123456789","09-878-0540-2","北海苗園", 10, 15.00, 150.00, 123.00,"2018-10-30","2018-11-02","2018-11-02");
INSERT INTO `purchase` VALUES("仙人掌","B198765432","07-165-1654-4","東海苗圃", 20, 10.00, 200.00, 164.00,"2019-11-02","2019-11-03",NULL);
INSERT INTO `purchase` VALUES("檜木苗","B154876236","07-165-4546-6","東海苗圃", 2, 1000.00, 2000.00, 1640.00,"2019-05-05","2019-05-07","2019-05-07");
INSERT INTO `purchase` VALUES("馬鞭草","A164872166","07-165-4849-3","東海苗圃", 50, 5.00, 250.00, 205.00,"2018-10-20","2018-10-21","2018-10-22");
INSERT INTO `purchase` VALUES("薄荷","C158716214","07-165-6564-5","東海苗圃", 30, 10.00, 300.00, 246.00,"2018-10-31","2018-11-01",NULL);
INSERT INTO `purchase` VALUES("繡球花","B123456789","09-156-5486-1","南海苗圃", 30, 20.00, 600.00, 492.00,"2018-12-20","2018-12-21","2018-12-21");
INSERT INTO `purchase` VALUES("玫瑰花","J216455547","08-878-0540-2","南海苗圃", 20, 6.00, 120.00, 98.00,"2018-11-20","2018-11-21",NULL);

SELECT * FROM `flowers`;
SELECT * FROM `customer`;
SELECT * FROM `supplier`;
SELECT * FROM `purchase`;
SELECT * FROM `stable_customer`;



