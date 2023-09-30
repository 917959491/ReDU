DROP TABLE IF EXISTS `peoplewebdata_result`;



CREATE TABLE `peoplewebdata_result` (
      `mid` VARCHAR(40) NOT NULL,
      `result` INT(11) NOT NULL,
      `pred` INT(11) NOT NULL,
      PRIMARY KEY(`mid`)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

