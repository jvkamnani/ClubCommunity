CREATE DATABASE IF NOT EXISTS clubcommunity;
USE clubcommunity;

-- Table: club
CREATE TABLE IF NOT EXISTS `club` (
    `id` CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    `name` VARCHAR(80) NOT NULL,
    `description` VARCHAR(200)
) ENGINE=InnoDB;

-- Table: club_sport (association table)
CREATE TABLE IF NOT EXISTS `club_sport` (
    `club_id` CHAR(36),
    `sport_id` CHAR(36),
    PRIMARY KEY (`club_id`, `sport_id`),
    FOREIGN KEY (`club_id`) REFERENCES `club`(`id`),
    FOREIGN KEY (`sport_id`) REFERENCES `sport`(`id`)
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

-- Form Template Table
CREATE TABLE IF NOT EXISTS form_template (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    name TEXT NOT NULL,
    description TEXT,
    club_id CHAR(36) NOT NULL,
    FOREIGN KEY (club_id) REFERENCES club(id)
);

-- Form Field Table
CREATE TABLE IF NOT EXISTS form_field (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    template_id CHAR(36) NOT NULL,
    label TEXT NOT NULL,
    field_type TEXT NOT NULL,
    is_required BOOLEAN NOT NULL DEFAULT 0,
    options TEXT,
    `order` INTEGER,
    validation TEXT,
    FOREIGN KEY (template_id) REFERENCES form_template(id)
); 