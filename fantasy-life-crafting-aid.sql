-- MySQL dump 10.13  Distrib 5.6.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: fantasy_life_crafting_aid
-- ------------------------------------------------------
-- Server version	5.6.28-0ubuntu0.15.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ingredients`
--

DROP TABLE IF EXISTS `ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingredients` (
  `ingredients_id` int(11) NOT NULL,
  `ingredients_name` varchar(45) DEFAULT NULL,
  `ingredients_description` varchar(45) DEFAULT NULL,
  `ingredients_found` varchar(45) DEFAULT NULL,
  `ingredients_rarity` int(11) DEFAULT '0',
  PRIMARY KEY (`ingredients_id`),
  KEY `idx_ingredients_ingredients_id` (`ingredients_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
INSERT INTO `ingredients` VALUES (1,'Castele Copper','Common Castele Copper ore.','East Castele, East Grassy Plains',0),(2,'Plains Iron','Used to make many weapons and armor.','East Grassy Plains, West Grassy Plains',1),(3,'Port Puerto Silver','Port Puerto abounds with this ore.','Tortuga Archipelago',2),(4,'Al Maajik Gold','Precious ore mined in the Al Maajik area.','Al Maajik, Aridian Desert',3),(5,'Platinum Ore','Rare metal found on the top of Mount Snowpeak','Mount Snowpeak Summit',4);
/*!40000 ALTER TABLE `ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lives`
--

DROP TABLE IF EXISTS `lives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lives` (
  `lives_id` int(11) NOT NULL,
  `lives_title` varchar(45) DEFAULT NULL,
  `lives_description` varchar(45) DEFAULT NULL,
  `lives_main_image` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`lives_id`),
  KEY `idx_lives_lives_id` (`lives_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lives`
--

LOCK TABLES `lives` WRITE;
/*!40000 ALTER TABLE `lives` DISABLE KEYS */;
/*!40000 ALTER TABLE `lives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes` (
  `recipes_id` int(11) NOT NULL,
  `recipes_name` varchar(45) DEFAULT NULL,
  `recipes_description` varchar(45) DEFAULT NULL,
  `recipes_image` varchar(45) DEFAULT NULL,
  `recipes_ingredients` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`recipes_id`),
  KEY `idx_recipes_recipes_id` (`recipes_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-02-09 10:56:57
