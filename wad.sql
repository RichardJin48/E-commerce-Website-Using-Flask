-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: wad
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `buyers`
--

DROP TABLE IF EXISTS `buyers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buyers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_customer_id_uindex` (`id`),
  UNIQUE KEY `customer_username_uindex` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buyers`
--

LOCK TABLES `buyers` WRITE;
/*!40000 ALTER TABLE `buyers` DISABLE KEYS */;
INSERT INTO `buyers` VALUES (1,'richard','7a20603b2321e5ad941810026e02d280','1159798938@qq.com','13348970531','CDC');
/*!40000 ALTER TABLE `buyers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts`
--

DROP TABLE IF EXISTS `carts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carts` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `buyer_id` int unsigned NOT NULL,
  `product_id` int unsigned NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts`
--

LOCK TABLES `carts` WRITE;
/*!40000 ALTER TABLE `carts` DISABLE KEYS */;
INSERT INTO `carts` VALUES (6,1,2,1),(7,1,6,2);
/*!40000 ALTER TABLE `carts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Electronics'),(2,'Instruments'),(3,'Tools'),(4,'Clothes'),(5,'Other');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `buyer_id` int NOT NULL,
  `product_id` int NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `content` varchar(255) NOT NULL,
  `level` int DEFAULT NULL,
  `created_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `like_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,1,1,NULL,'Good!',NULL,'2023-05-09 16:29:07'),(2,1,1,NULL,'123',NULL,'2023-05-09 16:34:03'),(3,1,5,NULL,'Bad!',NULL,'2023-05-12 05:08:21');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `buyer_id` int NOT NULL,
  `product_id` int NOT NULL,
  `status` tinyint NOT NULL COMMENT '0.dislike; 1.like',
  PRIMARY KEY (`id`),
  UNIQUE KEY `like_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (19,1,1,1),(20,1,5,1),(21,1,2,1);
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `track` varchar(255) DEFAULT NULL,
  `created_time` timestamp NULL DEFAULT NULL,
  `send_time` timestamp NULL DEFAULT NULL,
  `arrive_time` timestamp NULL DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `buyer` varchar(100) DEFAULT NULL,
  `buyer_id` int NOT NULL,
  `vendor_id` int DEFAULT NULL,
  `product_id` int NOT NULL,
  `product` varchar(100) DEFAULT NULL,
  `price` decimal(8,2) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `histories_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'Completed','2023-05-11 11:36:30','2023-05-11 15:15:10','2023-05-11 15:15:22','CDC','richard',1,1,2,'Guitar',1000.00,1),(2,'Delivering','2023-05-11 12:33:18','2023-05-12 05:37:11','2023-05-13 05:37:00','CDC','richard',1,1,6,'Drill',400.00,4),(3,'Delivering','2023-05-12 03:58:39','2023-05-12 05:39:19',NULL,'CDUT','jzc',1,1,2,'Guitar',1234.00,1),(4,'Completed','2023-05-12 03:58:39','2023-05-12 04:24:22','2023-05-12 05:39:35','CDUT','jzc',1,1,5,'iPad',6912.00,2),(5,'Preparing','2023-05-12 03:58:39',NULL,NULL,'CDUT','jzc',1,1,1,'iPhone',9000.00,1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `vendor_id` int NOT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `price` decimal(8,2) NOT NULL,
  `likes` int NOT NULL DEFAULT '0',
  `dislikes` int NOT NULL DEFAULT '0',
  `category_id` int unsigned DEFAULT NULL,
  `modified_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `picture` varchar(255) DEFAULT NULL,
  `p_price` decimal(8,2) DEFAULT NULL,
  `p_start` timestamp NULL DEFAULT NULL,
  `p_end` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'iPhone 12',1,'This is an iPhone 12.',12345.00,1,0,1,'2023-05-21 12:11:00','/static/uploads/smartphone-apple-iphone-12-64gb-bianco.jpg',9000.00,'2023-05-11 02:53:00','2023-05-31 02:53:00'),(2,'Guitar',1,'This is an electric guitar.',1234.00,1,0,2,'2023-05-21 07:52:16','/static/uploads/GarageBand图标.png',1000.00,'2023-05-09 16:19:00','2023-05-30 16:19:00'),(4,'Apple',1,'This is an apple.',2.00,0,0,5,'2023-05-21 07:52:03','/static/uploads/屏幕截图 2023-05-12 122648.png',1.00,'2023-05-17 10:16:00','2023-06-11 10:16:00'),(5,'iPad Pro',1,'This is an iPad Pro.',3456.00,1,0,1,'2023-05-21 12:11:10','/static/uploads/屏幕截图 2023-05-21 155354.png',NULL,NULL,NULL),(6,'Drill',1,'This is a big drill',234.00,0,0,3,'2023-05-12 04:39:03','/static/uploads/R-C.jpg',199.00,'2023-05-11 10:16:00','2023-05-31 10:16:00'),(7,'Nike T-shirt',1,'This is a T-shirt.',100.00,0,0,4,'2023-05-21 13:25:29','/static/uploads/OIP-C.jpg',88.00,'2023-05-12 04:10:00','2023-06-01 04:10:00'),(8,'Small Drill',1,'This is a small drill.',123.00,0,0,3,'2023-05-12 05:06:42','/static/uploads/01e60e5c83bddba80120af9ac71a15.png@1280w_1l_2o_100sh.png',NULL,NULL,NULL),(9,'Screwdriver',1,'This is a screwdriver.',12.00,0,0,3,'2023-05-21 13:55:37','/static/uploads/b679d2d59aa24b9814d9e2efc02c4151.jpg',NULL,NULL,NULL),(10,'iPhone SE',1,'This is an iPhone SE.',2345.00,0,0,1,'2023-05-21 12:23:51','/static/uploads/屏幕截图 2023-05-21 202300.png',NULL,NULL,NULL),(11,'Hammer',1,'This is a hammer.',50.00,0,0,3,'2023-05-21 12:43:06','/static/uploads/屏幕截图 2023-05-21 204226.png',39.00,'2023-05-21 12:43:00','2023-06-09 12:43:00'),(12,'Nike Shoes',1,'This is Nike shoes.',400.00,0,0,4,'2023-05-21 13:25:18','/static/uploads/屏幕截图 2023-05-21 212406.png',379.00,'2023-05-16 13:24:00','2023-05-18 13:25:00'),(13,'Suit',1,'This is a Suit.',567.00,0,0,4,'2023-05-21 13:56:48','/static/uploads/suit.jpg',500.00,'2023-06-08 13:29:00','2023-06-10 13:29:00'),(14,'Violin',1,'This is a violin.',500.00,0,0,2,'2023-05-21 13:32:54','/static/uploads/屏幕截图 2023-05-21 213216.png',NULL,NULL,NULL),(15,'PSR-SX600',1,'This is a good keyboard instrument.',5678.00,0,0,2,'2023-05-21 13:44:55','/static/uploads/PSR-SX600.jpg',5000.00,'2023-05-19 13:44:00','2023-06-09 13:44:00'),(16,'PSR-SX900',1,'This is a professional keyboard instrument.',12345.00,0,0,2,'2023-05-21 13:45:50','/static/uploads/PSR-SX900.jpg',NULL,NULL,NULL),(17,'PSR-E373',1,'This is a cheap keyboard instrument.',999.00,0,0,2,'2023-05-21 13:46:27','/static/uploads/yamaha-psr-e373.jpg',NULL,NULL,NULL),(18,'Drums',1,'This is a drum kit.',5000.00,0,0,2,'2023-05-21 13:48:31','/static/uploads/drums.jpg',NULL,NULL,NULL),(19,'Nikon Camera',1,'This is a Nikon camera.',999.00,0,0,1,'2023-05-21 13:50:29','/static/uploads/camera.jpg',NULL,NULL,NULL),(20,'Bag',1,'This is a school bag.',555.00,0,0,5,'2023-05-21 13:53:51','/static/uploads/9711629498_1154317685.jpg',444.00,'2023-05-20 13:53:00','2023-06-11 13:53:00'),(21,'Air-condition',1,'This is an air-condition.',2000.00,0,0,5,'2023-05-21 14:01:02','/static/uploads/air-condition.jpg',1500.00,'2023-05-20 14:00:00','2023-06-04 14:00:00');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendors`
--

DROP TABLE IF EXISTS `vendors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_customer_id_uindex` (`id`),
  UNIQUE KEY `customer_username_uindex` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendors`
--

LOCK TABLES `vendors` WRITE;
/*!40000 ALTER TABLE `vendors` DISABLE KEYS */;
INSERT INTO `vendors` VALUES (1,'richard','7a20603b2321e5ad941810026e02d280','1159798938@qq.com','13348970531','CDC');
/*!40000 ALTER TABLE `vendors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-21 22:40:05
