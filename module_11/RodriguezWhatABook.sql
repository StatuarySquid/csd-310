CREATE DATABASE  IF NOT EXISTS `whatabook` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `whatabook`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: whatabook
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS book;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE book (
  book_id int NOT NULL AUTO_INCREMENT,
  book_name varchar(200) NOT NULL,
  author varchar(200) NOT NULL,
  details varchar(500) DEFAULT NULL,
  PRIMARY KEY (book_id)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES book WRITE;
/*!40000 ALTER TABLE book DISABLE KEYS */;
INSERT INTO book VALUES (1,'Meditations','Marcus Aurelius','A life-changing collection of philosophical and spiritual thoughts from Marcus Aurelius, a Stoic and the former Roman Emperor.'),(2,'The War of Art','Steven Pressfield','Pressfield prepares and inspires creatives to survive and thrive the challenging journey to produce good work in the face of resistance.'),(3,'Awaken The Giant Within','Tony Robbins','A comprehensive and invaluable guide to mastering your mind, body, emotions, and finances from leading life and business strategist Tony Robbins.'),(4,'The Power of Habit','Charles Duhigg','A digestible, comprehensive, and transformative guide to understanding why habits exist, how they work, and how you can change then.'),(5,'Thinking Fast And Slow','Daniel Kahneman','An engaging and comprehensive introduction to the psychology of decision making and judgment by one of the pioneers in the field.'),(6,'How To Lie With Statistics','Darrell Huff','A great reminder of the basic principles of statistics and how they are often violated in the data we use.'),(7,'When Breath Becomes Air','Paul Kalanithi','While dying of lung cancer, neurosurgeon Paul Kalanithi confronts the unanswerable and difficult question of what makes life meaningful.'),(8,'Zen and The Art of Motorcycle Maintenance','Robert Pirsig','Through an entrancing narrative of a man on a summer motorcycle trip with his son, Pirsig takes us on a deeply philosophical journey that explores society, values, and life’s big questions.'),(9,'Shoe Dog','Phil Knight','This is the inspiring story of Phil Knight, the founder of Nike, and his struggles, victories, and lesson learned while building a billion dollar shoe giant');
/*!40000 ALTER TABLE book ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS store;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE store (
  store_id int NOT NULL,
  locale varchar(500) NOT NULL,
  PRIMARY KEY (store_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES store WRITE;
/*!40000 ALTER TABLE store DISABLE KEYS */;
INSERT INTO store VALUES (1,'123 St York NE 68467');
/*!40000 ALTER TABLE store ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS user;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  user_id int NOT NULL AUTO_INCREMENT,
  first_name varchar(75) NOT NULL,
  last_name varchar(75) NOT NULL,
  PRIMARY KEY (user_id)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES user WRITE;
/*!40000 ALTER TABLE user DISABLE KEYS */;
INSERT INTO user VALUES (1,'Juan','Rodriguez'),(2,'Mayra','Cerritos'),(3,'Tommy','Hill');
/*!40000 ALTER TABLE user ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wishlist`
--

DROP TABLE IF EXISTS wishlist;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE wishlist (
  wishlist_id int NOT NULL AUTO_INCREMENT,
  user_id int NOT NULL,
  book_id int NOT NULL,
  PRIMARY KEY (wishlist_id),
  KEY book_id_idx (wishlist_id) /*!80000 INVISIBLE */,
  KEY book_id_idx1 (book_id),
  KEY user_id_idx (user_id),
  CONSTRAINT book_id FOREIGN KEY (book_id) REFERENCES book (book_id),
  CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES `user` (user_id)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlist`
--

LOCK TABLES wishlist WRITE;
/*!40000 ALTER TABLE wishlist DISABLE KEYS */;
INSERT INTO wishlist VALUES (1,1,5),(2,2,4),(3,2,2),(4,1,7),(5,3,6),(6,2,7),(7,1,8),(8,3,9),(9,3,1);
/*!40000 ALTER TABLE wishlist ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-06 16:30:38
