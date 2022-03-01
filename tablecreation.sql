SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- schema bookstore
-- -----------------------------------------------------

CREATE SCHEMA IF NOT EXISTS `bookstore` DEFAULT CHARACTER SET UTF8MB4 ;
USE `bookstore` ;

-- -----------------------------------------------------
-- table `bookstore`.`books`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `bookstore`.`books` (
  `bookid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `author` VARCHAR(45) NOT NULL,
  `genre` VARCHAR(45),
  `publisher` VARCHAR(45),
  `yop` YEAR,
  `price` DECIMAL NULL,
  `new` INT UNSIGNED,
  `used` INT UNSIGNED,
  PRIMARY KEY (`bookid`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- table `bookstore`.`customers`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `bookstore`.`customers` (
  `custid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `contact` CHAR(10) NOT NULL,
  `member` CHAR(1) NOT NULL,
  PRIMARY KEY (`custid`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- table `bookstore`.`vendors`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `bookstore`.`vendors` (
  `vendid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `contact` CHAR(10) NOT NULL,
  PRIMARY KEY (`vendid`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- table `bookstore`.`fromven`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `bookstore`.`fromven` (
  `transid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `vendid` INT UNSIGNED NOT NULL,
  `bookid` INT UNSIGNED NOT NULL,
  `copies` INT UNSIGNED NOT NULL,
  `cost` DECIMAL NULL,
  PRIMARY KEY (`transid`),
  FOREIGN KEY (vendid) REFERENCES vendors(vendid),
  FOREIGN KEY (bookid) REFERENCES books(bookid))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- table `bookstore`.`checkout`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `bookstore`.`checkout` (
  `transid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `custid` INT UNSIGNED NOT NULL,
  `bookid` INT UNSIGNED NOT NULL,
  `copies` INT UNSIGNED NOT NULL DEFAULT 1,
  `price` DECIMAL NULL,
  `discounted` DECIMAL NULL,
  PRIMARY KEY (`transid`),
  FOREIGN KEY (custid) REFERENCES customers(custid),
  FOREIGN KEY (bookid) REFERENCES books(bookid))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- table `bookstore`.`reserved`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `bookstore`.`reserved` (
  `resid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `custid` INT UNSIGNED NOT NULL,
  `bookid` INT UNSIGNED NOT NULL,
  `copies` INT UNSIGNED NOT NULL DEFAULT 1,
  `date` DATE NOT NULL,
  `fulfilled` CHAR(1) NOT NULL DEFAULT 'n', 
  PRIMARY KEY (`resid`),
  FOREIGN KEY (custid) REFERENCES customers(custid),
  FOREIGN KEY (bookid) REFERENCES books(bookid))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;