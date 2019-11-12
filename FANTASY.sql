DROP DATABASE IF EXISTS `FANTASY`;
CREATE SCHEMA `FANTASY`;
USE `FANTASY`;

DROP TABLE IF EXISTS `league`;
CREATE TABLE `league` (
  `league_id` int(11) NOT NULL AUTO_INCREMENT,
  `country` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`league_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `football_club`;
CREATE TABLE `football_club` (
  `club_id` int(11) NOT NULL AUTO_INCREMENT,
  `club_name` varchar(20) NOT NULL,
  `club_crest` varchar(20) NOT NULL,
  `club_rating` varchar(20) NOT NULL,
  `league_id` int(11) NOT NULL,
  PRIMARY KEY (`club_id`),
  KEY `league_id` (`league_id`),
  CONSTRAINT `football_club_ibfk_1` FOREIGN KEY (`league_id`) REFERENCES `league` (`league_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `football_player`;
CREATE TABLE `football_player`(
	`player_id`  int(11) NOT NULL AUTO_INCREMENT,
	`price` int(11) NOT NULL,
	`club_id` int(11) NOT NULL,
	KEY `club_id` (`club_id`),
	 CONSTRAINT `football_player_ibfk_1` FOREIGN KEY (`club_id`) REFERENCES `football_club` (`club_id`),
	 `rating` int(11) NOT NULL, 
	 `country` varchar(25), 
	 `name` varchar(50), 
	 `age` int(11), 
	 PRIMARY KEY (`player_id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `User`;
CREATE TABLE `User` (
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `captain_player_id` int(11) NOT NULL,
  `current_total_points` int(11) NOT NULL,
  `money_left` int(11) NOT NULL,
  `dob` date DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `captain_player_id` (`captain_player_id`),
  CONSTRAINT `User_ibfk_1` FOREIGN KEY (`captain_player_id`) REFERENCES `football_player` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `private_league`;
CREATE TABLE `private_league` (
  `pl_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`pl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `user_pl_relation`;
CREATE TABLE `user_pl_relation` (
  `user_id` int(11) NOT NULL,
  `pl_id` int(11) NOT NULL,
  KEY `user_id` (`user_id`),
  KEY `pl_id` (`pl_id`),
  PRIMARY KEY (`user_id`,`pl_id`),
  CONSTRAINT `user_pl_relation_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `user_pl_relation_ibfk_2` FOREIGN KEY (`pl_id`) REFERENCES `private_league` (`pl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `user_club_relation`;
CREATE TABLE `user_club_relation` (
  `user_id` int(11) NOT NULL,
  `club_id` int(11) NOT NULL,
  KEY `user_id` (`user_id`),
  KEY `club_id` (`club_id`),
  PRIMARY KEY (`user_id`,`club_id`),
  CONSTRAINT `user_club_relation_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `user_club_relation_ibfk_2` FOREIGN KEY (`club_id`) REFERENCES `football_club` (`club_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `user_leagues_participated`;
CREATE TABLE `user_leagues_participated` (
  `user_id` int(11) NOT NULL,
  `league_id` int(11) NOT NULL,
  KEY `user_id` (`user_id`),
  KEY `league_id` (`league_id`),
  PRIMARY KEY (`user_id`,`league_id`),
  CONSTRAINT `user_leagues_participated_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `user_leagues_participated_ibfk_2` FOREIGN KEY (`league_id`) REFERENCES `league` (`league_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Best11`;
CREATE TABLE `Best11`(
	`match_week` int(11) NOT NULL,
	 PRIMARY KEY (`match_week`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Matches`;
CREATE TABLE `Matches` (
  `club_1_id` int(11) NOT NULL,
  `club_2_id` int(11) NOT NULL,
  `match_date` date DEFAULT NULL,
  `club_1_points` int(11) NOT NULL,
  `club_2_points` int(11) NOT NULL,
  `match_week` int(11) NOT NULL,
  KEY `club_1_id` (`club_1_id`),
  KEY `club_2_id` (`club_2_id`),
  KEY `match_week` (`match_week`),
  PRIMARY KEY (`club_1_id`,`club_2_id`,`match_week`),
  CONSTRAINT `Matches_ibfk_1` FOREIGN KEY (`club_1_id`) REFERENCES `football_club` (`club_id`),
  CONSTRAINT `Matches_ibfk_2` FOREIGN KEY (`club_2_id`) REFERENCES `football_club` (`club_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `user_player_relation`;
CREATE TABLE `user_player_relation` (
  `user_id` int(11) NOT NULL,
  `player_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`player_id`),
  KEY `user_id` (`user_id`),
  KEY `player_id` (`player_id`),
  CONSTRAINT `user_player_relation_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `user_player_relation_ibfk_2` FOREIGN KEY (`player_id`) REFERENCES `football_player` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `defender`;
CREATE TABLE `defender`(
	`player_id` int(11) NOT NULL,
	 KEY `player_id` (`player_id`),
	 CONSTRAINT `defender_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `football_player` (`player_id`),
	PRIMARY KEY (`player_id`), 
	`tackles` int(11) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `attacker`;
CREATE TABLE `attacker`(
	`player_id` int(11) NOT NULL,
	KEY `player_id` (`player_id`),
	CONSTRAINT `attacker_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `football_player` (`player_id`),
	PRIMARY KEY (`player_id`),
	`goals` int(11) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `midfielder`;
CREATE TABLE `midfielder`(
	`player_id` int(11) NOT NULL,
	 KEY `player_id` (`player_id`),
	 CONSTRAINT `midfielder_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `football_player` (`player_id`),
	 PRIMARY KEY(`player_id`),
	 `passes` int(11) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `goalkeeper`;
CREATE TABLE `goalkeeper`(
	`player_id` int(11) NOT NULL, 
	 KEY `player_id` (`player_id`),
	 CONSTRAINT `goalkeeper_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `football_player` (`player_id`),
	 `saves` int(11),
	 PRIMARY KEY(`player_id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `best11_def`;
CREATE TABLE `best11_def`(
	`match_week` int(11) NOT NULL, 
	`player_id` int(11) NOT NULL,
	KEY `player_id` (`player_id`),
	KEY `match_week` (`match_week`),
	PRIMARY KEY (`match_week`, `player_id`), 
	CONSTRAINT `best11_def_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `football_player` (`player_id`),
	CONSTRAINT `best11_def_ibfk_2` FOREIGN KEY (`match_week`) REFERENCES `Best11` (`match_week`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `best11_mid`;
CREATE TABLE `best11_mid`(
	`match_week` int(11) NOT NULL, 
	`player_id` int(11) NOT NULL,
	KEY `player_id` (`player_id`),
	KEY `match_week` (`match_week`),
	PRIMARY KEY (`match_week`, `player_id`), 
	CONSTRAINT `best11_mid_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `football_player` (`player_id`),
	CONSTRAINT `best11_mid_ibfk_2` FOREIGN KEY (`match_week`) REFERENCES `Best11` (`match_week`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `best11_att`; 
CREATE TABLE `best11_att`(
	`match_week` int(11) NOT NULL, 
	`player_id` int(11) NOT NULL,
	KEY `player_id` (`player_id`),
	KEY `match_week` (`match_week`),
	PRIMARY KEY (`match_week`, `player_id`), 
	CONSTRAINT `best11_att_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `football_player` (`player_id`),
	CONSTRAINT `best11_att_ibfk_2` FOREIGN KEY (`match_week`) REFERENCES `Best11` (`match_week`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `best11_gkp`; 
CREATE TABLE `best11_gkp`(
	`match_week` int(11) NOT NULL, 
	`player_id` int(11) NOT NULL,
	KEY `player_id` (`player_id`),
	KEY `match_week` (`match_week`),
	PRIMARY KEY (`match_week`, `player_id`), 
	CONSTRAINT `best11_gkp_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `football_player` (`player_id`),
	CONSTRAINT `best11_gkp_ibfk_2` FOREIGN KEY (`match_week`) REFERENCES `Best11` (`match_week`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;