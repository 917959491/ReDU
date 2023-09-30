DROP TABLE IF EXISTS `twitterdata_result`;



CREATE TABLE `twitterdata_result` (
      `mid` VARCHAR(80) NOT NULL,
      `result` INT(11) NOT NULL,
      `pred` INT(11) NOT NULL,
      PRIMARY KEY(`mid`)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

