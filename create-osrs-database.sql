DROP DATABASE IF EXISTS osrs;
CREATE DATABASE osrs;
USE osrs;

SET NAMES utf8mb4;
SET character_set_client = utf8mb4;

CREATE TABLE total_player_counts (
	`datetime` DATETIME,
    player_count MEDIUMINT UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE world_player_counts (
    `datetime` DATETIME,
	world SMALLINT UNSIGNED NOT NULL,
    player_count MEDIUMINT UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
