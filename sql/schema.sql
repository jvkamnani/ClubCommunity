CREATE DATABASE IF NOT EXISTS clubcommunity;
USE clubcommunity;

-- Table: club
CREATE TABLE IF NOT EXISTS `club` (
    `id` CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    `name` VARCHAR(80) NOT NULL,
    `description` VARCHAR(200)
) ENGINE=InnoDB;

-- Table: event
CREATE TABLE IF NOT EXISTS `event` (
    `id` CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    `name` VARCHAR(80) NOT NULL,
    `date` VARCHAR(20),
    `club_id` CHAR(36),
    FOREIGN KEY (`club_id`) REFERENCES `club`(`id`)
) ENGINE=InnoDB;

-- Table: user
CREATE TABLE IF NOT EXISTS `user` (
    `id` CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    `username` VARCHAR(80) NOT NULL UNIQUE,
    `email` VARCHAR(120) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- Table: sport
CREATE TABLE IF NOT EXISTS `sport` (
    `id` CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    `name` VARCHAR(80) NOT NULL UNIQUE,
    `image` LONGBLOB
) ENGINE=InnoDB; 