DROP TABLE IF EXISTS `weibodata_result`;



CREATE TABLE `weibodata_result` (
      `mid` VARCHAR(40) NOT NULL,
      `result` INT(11) NOT NULL,
      `pred` INT(11) NOT NULL,
      PRIMARY KEY(`mid`)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

