/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS player;
CREATE TABLE `player` (
  `player_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(75) NOT NULL,
  `last_name` varchar(75) NOT NULL,
  `team_id` int NOT NULL,
  PRIMARY KEY (`player_id`),
  KEY `fk_team` (`team_id`),
  CONSTRAINT `fk_team` FOREIGN KEY (`team_id`) REFERENCES `team` (`team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS team;
CREATE TABLE `team` (
  `team_id` int NOT NULL AUTO_INCREMENT,
  `team_name` varchar(75) NOT NULL,
  `mascot` varchar(75) NOT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO player(player_id,first_name,last_name,team_id) VALUES('1','\'Thorin\'','\'Oakenshield\'','1'),('2','\'Bilbo\'','\'Baggins\'','1'),('3','\'Frodo\'','\'Baggins\'','1'),('4','\'Saruman\'','\'The White\'','2'),('5','\'Angmar\'','\'Witch-king\'','2'),('6','\'Azog\'','\'The Defiler\'','2');
INSERT INTO team(team_id,team_name,mascot) VALUES('1','\'Team Gandalf\'','\'White Wizards\''),('2','\'Team Sauron\'','\'Orcs\'');