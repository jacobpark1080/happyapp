CREATE DATABASE `happyapp` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE `happyapp`;

CREATE TABLE IF NOT EXISTS `monday` (
  `restID` int(11) DEFAULT NULL,
  `stime` decimal(10,2) DEFAULT NULL,
  `etime` decimal(10,2) DEFAULT NULL,
  `drink` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
  `food` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `monday` (`restID`, `stime`, `etime`, `drink`, `food`) VALUES(101, 18.00, 19.00, 'drink','food');