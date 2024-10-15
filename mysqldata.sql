-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: ecommerce
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

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
-- Table structure for table `analytics_category`
--

DROP TABLE IF EXISTS `analytics_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analytics_category`
--

LOCK TABLES `analytics_category` WRITE;
/*!40000 ALTER TABLE `analytics_category` DISABLE KEYS */;
INSERT INTO `analytics_category` VALUES (1,'Electronics','2024-10-10 08:27:26.525533','2024-10-10 08:27:26.525559'),(2,'Clothing','2024-10-10 08:27:26.528312','2024-10-10 08:27:26.528327'),(3,'Books','2024-10-10 08:27:26.530582','2024-10-10 08:27:26.530594'),(4,'Home Appliances','2024-10-10 08:32:19.273308','2024-10-10 08:32:19.273336'),(5,'Beauty','2024-10-10 08:32:19.275724','2024-10-10 08:32:19.275739'),(6,'Toys','2024-10-10 08:33:56.240254','2024-10-10 08:33:56.240280'),(7,'Fitness','2024-10-10 08:33:56.243058','2024-10-10 08:33:56.243073'),(8,'Pet Supplies','2024-10-10 08:34:21.444229','2024-10-10 08:34:21.444254'),(9,'Kitchen Appliances','2024-10-10 08:34:21.446381','2024-10-10 08:34:21.446394'),(10,'Office Supplies','2024-10-10 08:34:47.234315','2024-10-10 08:34:47.234343'),(11,'Sports','2024-10-10 08:34:47.236551','2024-10-10 08:34:47.236565');
/*!40000 ALTER TABLE `analytics_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analytics_customer`
--

DROP TABLE IF EXISTS `analytics_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `country` varchar(100) NOT NULL,
  `registration_date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analytics_customer`
--

LOCK TABLES `analytics_customer` WRITE;
/*!40000 ALTER TABLE `analytics_customer` DISABLE KEYS */;
INSERT INTO `analytics_customer` VALUES (1,'John Doe','john@example.com','US','2024-10-10','2024-10-10 08:27:26.552600','2024-10-10 08:27:26.552612'),(2,'Jane Smith','jane@example.com','UK','2024-10-10','2024-10-10 08:27:26.554605','2024-10-10 08:27:26.554615'),(3,'Alice Johnson','alice@example.com','US','2024-10-10','2024-10-10 08:32:19.294251','2024-10-10 08:32:19.294262'),(4,'Bob Brown','bob@example.com','UK','2024-10-10','2024-10-10 08:32:19.296219','2024-10-10 08:32:19.296232'),(5,'Charlie Green','charlie@example.com','US','2024-10-10','2024-10-10 08:33:56.261656','2024-10-10 08:33:56.261667'),(6,'Diana White','diana@example.com','UK','2024-10-10','2024-10-10 08:33:56.263692','2024-10-10 08:33:56.263705'),(7,'Evelyn Black','evelyn@example.com','CA','2024-10-10','2024-10-10 08:34:21.464288','2024-10-10 08:34:21.464299'),(8,'Frank Johnson','frank@example.com','AU','2024-10-10','2024-10-10 08:34:21.466314','2024-10-10 08:34:21.466330'),(9,'Grace Lee','grace@example.com','US','2024-10-10','2024-10-10 08:34:47.253819','2024-10-10 08:34:47.253829'),(10,'Henry King','henry@example.com','CA','2024-10-10','2024-10-10 08:34:47.255488','2024-10-10 08:34:47.255502');
/*!40000 ALTER TABLE `analytics_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analytics_inventory`
--

DROP TABLE IF EXISTS `analytics_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics_inventory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `last_restocked_date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`),
  CONSTRAINT `analytics_inventory_product_id_5c052cc1_fk_analytics_product_id` FOREIGN KEY (`product_id`) REFERENCES `analytics_product` (`id`),
  CONSTRAINT `analytics_inventory_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analytics_inventory`
--

LOCK TABLES `analytics_inventory` WRITE;
/*!40000 ALTER TABLE `analytics_inventory` DISABLE KEYS */;
INSERT INTO `analytics_inventory` VALUES (1,49,'2024-10-10','2024-10-10 08:27:26.547509','2024-10-10 08:27:26.562081',1),(2,1,'2024-10-11','2024-10-10 08:27:26.549248','2024-10-11 04:40:01.657604',2),(3,98,'2024-10-10','2024-10-10 08:27:26.550890','2024-10-10 08:27:26.569556',3),(4,29,'2024-10-10','2024-10-10 08:32:19.290459','2024-10-10 08:32:19.303596',4),(5,47,'2024-10-10','2024-10-10 08:32:19.292162','2024-10-10 08:32:19.311170',5),(6,98,'2024-10-10','2024-10-10 08:33:56.258018','2024-10-10 08:33:56.271344',6),(7,3,'2024-10-11','2024-10-10 08:33:56.259769','2024-10-11 04:39:41.012365',7),(8,58,'2024-10-10','2024-10-10 08:34:21.460572','2024-10-10 08:34:21.474132',8),(9,38,'2024-10-10','2024-10-10 08:34:21.462350','2024-10-10 08:34:21.481909',9),(10,198,'2024-10-10','2024-10-10 08:34:47.250347','2024-10-10 08:34:47.262392',10),(11,99,'2024-10-10','2024-10-10 08:34:47.252157','2024-10-10 08:34:47.266246',11);
/*!40000 ALTER TABLE `analytics_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analytics_order`
--

DROP TABLE IF EXISTS `analytics_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `order_date` date NOT NULL,
  `status` varchar(1) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `analytics_order_customer_id_33db038a_fk_analytics_customer_id` (`customer_id`),
  CONSTRAINT `analytics_order_customer_id_33db038a_fk_analytics_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `analytics_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analytics_order`
--

LOCK TABLES `analytics_order` WRITE;
/*!40000 ALTER TABLE `analytics_order` DISABLE KEYS */;
INSERT INTO `analytics_order` VALUES (1,'2020-01-30','C',719.98,'2024-10-10 08:27:26.556678','2024-10-11 04:56:04.971275',1),(2,'2023-10-05','C',34.98,'2024-10-10 08:27:26.558721','2024-10-11 04:55:18.406191',2),(3,'2023-02-21','C',529.98,'2024-10-10 08:32:19.297975','2024-10-11 04:55:44.615087',3),(4,'2024-10-10','C',59.98,'2024-10-10 08:32:19.299779','2024-10-10 08:32:19.299788',4),(5,'2024-10-01','C',64.98,'2024-10-10 08:33:56.265513','2024-10-11 04:06:44.340984',1),(6,'2023-10-10','C',39.99,'2024-10-10 08:33:56.267358','2024-10-11 04:55:03.401105',3),(7,'2024-10-10','C',139.98,'2024-10-10 08:34:21.468373','2024-10-10 08:34:21.468383',7),(8,'2024-10-10','C',89.99,'2024-10-10 08:34:21.470299','2024-10-10 08:34:21.470309',8),(9,'2024-10-10','C',42.98,'2024-10-10 08:34:47.257244','2024-10-11 04:06:31.605202',1),(10,'2024-10-10','C',29.99,'2024-10-10 08:34:47.259034','2024-10-10 08:34:47.259043',10);
/*!40000 ALTER TABLE `analytics_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analytics_orderitem`
--

DROP TABLE IF EXISTS `analytics_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `price_at_time_of_order` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `analytics_orderitem_order_id_64bf5325_fk_analytics_order_id` (`order_id`),
  KEY `analytics_orderitem_product_id_cd070313_fk_analytics_product_id` (`product_id`),
  CONSTRAINT `analytics_orderitem_order_id_64bf5325_fk_analytics_order_id` FOREIGN KEY (`order_id`) REFERENCES `analytics_order` (`id`),
  CONSTRAINT `analytics_orderitem_product_id_cd070313_fk_analytics_product_id` FOREIGN KEY (`product_id`) REFERENCES `analytics_product` (`id`),
  CONSTRAINT `analytics_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analytics_orderitem`
--

LOCK TABLES `analytics_orderitem` WRITE;
/*!40000 ALTER TABLE `analytics_orderitem` DISABLE KEYS */;
INSERT INTO `analytics_orderitem` VALUES (1,1,699.99,'2024-10-10 08:27:26.560439','2024-10-10 08:27:26.560451',1,1),(2,1,19.99,'2024-10-10 08:27:26.564392','2024-10-10 08:27:26.564410',1,2),(3,2,14.99,'2024-10-10 08:27:26.567912','2024-10-10 08:27:26.567924',2,3),(4,1,499.99,'2024-10-10 08:32:19.301670','2024-10-10 08:32:19.301684',3,4),(5,1,29.99,'2024-10-10 08:32:19.305817','2024-10-10 08:32:19.305829',3,5),(6,2,29.99,'2024-10-10 08:32:19.309494','2024-10-10 08:32:19.309506',4,5),(7,2,24.99,'2024-10-10 08:33:56.269340','2024-10-10 08:33:56.269355',5,6),(8,1,39.99,'2024-10-10 08:33:56.273568','2024-10-10 08:33:56.273581',5,7),(9,1,39.99,'2024-10-10 08:33:56.277622','2024-10-10 08:33:56.277634',6,7),(10,2,49.99,'2024-10-10 08:34:21.472259','2024-10-10 08:34:21.472271',7,8),(11,1,89.99,'2024-10-10 08:34:21.476476','2024-10-10 08:34:21.476487',7,9),(12,1,89.99,'2024-10-10 08:34:21.479992','2024-10-10 08:34:21.480002',8,9),(13,2,12.99,'2024-10-10 08:34:47.260708','2024-10-10 08:34:47.260719',9,10),(14,1,29.99,'2024-10-10 08:34:47.264530','2024-10-10 08:34:47.264543',10,11);
/*!40000 ALTER TABLE `analytics_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analytics_product`
--

DROP TABLE IF EXISTS `analytics_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `SKU` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `analytics_product_category_id_539dccaa_fk_analytics_category_id` (`category_id`),
  CONSTRAINT `analytics_product_category_id_539dccaa_fk_analytics_category_id` FOREIGN KEY (`category_id`) REFERENCES `analytics_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analytics_product`
--

LOCK TABLES `analytics_product` WRITE;
/*!40000 ALTER TABLE `analytics_product` DISABLE KEYS */;
INSERT INTO `analytics_product` VALUES (1,'Smartphone','Latest model smartphone with all the features.','SP123',699.99,'2024-10-10 08:27:26.536925','2024-10-10 08:27:26.536939',1),(2,'T-Shirt','Comfortable cotton t-shirt.','TS456',19.99,'2024-10-10 08:27:26.541629','2024-10-10 08:27:26.541645',2),(3,'Novel Book','Bestselling novel.','NB789',14.99,'2024-10-10 08:27:26.545634','2024-10-10 08:27:26.545648',3),(4,'Washing Machine','Energy-efficient washing machine.','WM001',499.99,'2024-10-10 08:32:19.282127','2024-10-10 08:32:19.282141',4),(5,'Moisturizer','Hydrating moisturizer for all skin types.','MO002',29.99,'2024-10-10 08:32:19.286385','2024-10-10 08:32:19.286401',5),(6,'Action Figure','Popular action figure from the latest movie.','AF003',24.99,'2024-10-10 08:33:56.249662','2024-10-10 08:33:56.249675',6),(7,'Yoga Mat','Eco-friendly yoga mat for all fitness levels.','YM004',39.99,'2024-10-10 08:33:56.253877','2024-10-10 08:33:56.253892',7),(8,'Dog Food','Premium dog food for healthy pets.','DF005',49.99,'2024-10-10 08:34:21.452491','2024-10-10 08:34:21.452505',8),(9,'Blender','High-performance blender for smoothies and soups.','BL006',89.99,'2024-10-10 08:34:21.456661','2024-10-10 08:34:21.456676',9),(10,'Notebook','Spiral-bound notebook for notes and sketches.','NB007',12.99,'2024-10-10 08:34:47.242301','2024-10-10 08:34:47.242316',10),(11,'Soccer Ball','Official size soccer ball for practice and games.','SB008',29.99,'2024-10-10 08:34:47.246689','2024-10-10 08:34:47.246706',11);
/*!40000 ALTER TABLE `analytics_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analytics_product_tags`
--

DROP TABLE IF EXISTS `analytics_product_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics_product_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `analytics_product_tags_product_id_tag_id_21301074_uniq` (`product_id`,`tag_id`),
  KEY `analytics_product_tags_tag_id_cee4b780_fk_analytics_tag_id` (`tag_id`),
  CONSTRAINT `analytics_product_ta_product_id_cc1f538a_fk_analytics` FOREIGN KEY (`product_id`) REFERENCES `analytics_product` (`id`),
  CONSTRAINT `analytics_product_tags_tag_id_cee4b780_fk_analytics_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `analytics_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analytics_product_tags`
--

LOCK TABLES `analytics_product_tags` WRITE;
/*!40000 ALTER TABLE `analytics_product_tags` DISABLE KEYS */;
INSERT INTO `analytics_product_tags` VALUES (1,1,1),(2,2,2),(3,4,3),(4,5,4),(5,6,5),(6,7,6),(7,8,7),(8,9,8),(9,10,9),(10,11,10);
/*!40000 ALTER TABLE `analytics_product_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analytics_tag`
--

DROP TABLE IF EXISTS `analytics_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analytics_tag`
--

LOCK TABLES `analytics_tag` WRITE;
/*!40000 ALTER TABLE `analytics_tag` DISABLE KEYS */;
INSERT INTO `analytics_tag` VALUES (1,'Sale','2024-10-10 08:27:26.532629','2024-10-10 08:27:26.532642'),(2,'New Arrival','2024-10-10 08:27:26.535065','2024-10-10 08:27:26.535080'),(3,'Discount','2024-10-10 08:32:19.277863','2024-10-10 08:32:19.277877'),(4,'Featured','2024-10-10 08:32:19.280218','2024-10-10 08:32:19.280232'),(5,'Bestseller','2024-10-10 08:33:56.245581','2024-10-10 08:33:56.245596'),(6,'Exclusive','2024-10-10 08:33:56.247667','2024-10-10 08:33:56.247681'),(7,'Trending','2024-10-10 08:34:21.448491','2024-10-10 08:34:21.448504'),(8,'Seasonal','2024-10-10 08:34:21.450620','2024-10-10 08:34:21.450635'),(9,'New Arrival','2024-10-10 08:34:47.238400','2024-10-10 08:34:47.238421'),(10,'Clearance','2024-10-10 08:34:47.240307','2024-10-10 08:34:47.240319');
/*!40000 ALTER TABLE `analytics_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add category',7,'add_category'),(26,'Can change category',7,'change_category'),(27,'Can delete category',7,'delete_category'),(28,'Can view category',7,'view_category'),(29,'Can add customer',8,'add_customer'),(30,'Can change customer',8,'change_customer'),(31,'Can delete customer',8,'delete_customer'),(32,'Can view customer',8,'view_customer'),(33,'Can add tag',9,'add_tag'),(34,'Can change tag',9,'change_tag'),(35,'Can delete tag',9,'delete_tag'),(36,'Can view tag',9,'view_tag'),(37,'Can add order',10,'add_order'),(38,'Can change order',10,'change_order'),(39,'Can delete order',10,'delete_order'),(40,'Can view order',10,'view_order'),(41,'Can add product',11,'add_product'),(42,'Can change product',11,'change_product'),(43,'Can delete product',11,'delete_product'),(44,'Can view product',11,'view_product'),(45,'Can add order item',12,'add_orderitem'),(46,'Can change order item',12,'change_orderitem'),(47,'Can delete order item',12,'delete_orderitem'),(48,'Can view order item',12,'view_orderitem'),(49,'Can add inventory',13,'add_inventory'),(50,'Can change inventory',13,'change_inventory'),(51,'Can delete inventory',13,'delete_inventory'),(52,'Can view inventory',13,'view_inventory'),(53,'Can add Token',14,'add_token'),(54,'Can change Token',14,'change_token'),(55,'Can delete Token',14,'delete_token'),(56,'Can view Token',14,'view_token'),(57,'Can add Token',15,'add_tokenproxy'),(58,'Can change Token',15,'change_tokenproxy'),(59,'Can delete Token',15,'delete_tokenproxy'),(60,'Can view Token',15,'view_tokenproxy');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$bUgkqBwlLijY9oqqk3CTxf$bYA2Cpp10ECCFcZHiIMaTS2jyL8x9Ukm4ucYW6rwJnI=',NULL,0,'newuser','','','l@gmail.com',0,1,'2024-10-10 08:27:58.412834'),(2,'pbkdf2_sha256$870000$0NoAQS9JNktYLlJzqeKEGR$WgIKpsDmqZuvAlfbapPsuu4MvkBpgABn5zRntf0COuw=','2024-10-11 04:05:05.448813',1,'Liju','','','l@gmail.com',1,1,'2024-10-11 04:04:29.731642');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-10-11 04:06:11.826672','5','Order object (5)',2,'[{\"changed\": {\"fields\": [\"Order date\"]}}]',10,2),(2,'2024-10-11 04:06:23.030685','6','Order object (6)',2,'[{\"changed\": {\"fields\": [\"Customer\"]}}]',10,2),(3,'2024-10-11 04:06:31.607245','9','Order object (9)',2,'[{\"changed\": {\"fields\": [\"Customer\"]}}]',10,2),(4,'2024-10-11 04:06:44.341904','5','Order object (5)',2,'[{\"changed\": {\"fields\": [\"Customer\"]}}]',10,2),(5,'2024-10-11 04:39:41.013108','7','Inventory object (7)',2,'[{\"changed\": {\"fields\": [\"Quantity\"]}}]',13,2),(6,'2024-10-11 04:40:01.658114','2','Inventory object (2)',2,'[{\"changed\": {\"fields\": [\"Quantity\"]}}]',13,2),(7,'2024-10-11 04:55:03.402076','6','Order object (6)',2,'[{\"changed\": {\"fields\": [\"Order date\"]}}]',10,2),(8,'2024-10-11 04:55:18.406891','2','Order object (2)',2,'[{\"changed\": {\"fields\": [\"Order date\"]}}]',10,2),(9,'2024-10-11 04:55:44.615855','3','Order object (3)',2,'[{\"changed\": {\"fields\": [\"Order date\"]}}]',10,2),(10,'2024-10-11 04:56:04.971886','1','Order object (1)',2,'[{\"changed\": {\"fields\": [\"Order date\"]}}]',10,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'analytics','category'),(8,'analytics','customer'),(13,'analytics','inventory'),(10,'analytics','order'),(12,'analytics','orderitem'),(11,'analytics','product'),(9,'analytics','tag'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(14,'authtoken','token'),(15,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-10 08:27:21.006761'),(2,'auth','0001_initial','2024-10-10 08:27:21.382889'),(3,'admin','0001_initial','2024-10-10 08:27:21.466440'),(4,'admin','0002_logentry_remove_auto_add','2024-10-10 08:27:21.472118'),(5,'admin','0003_logentry_add_action_flag_choices','2024-10-10 08:27:21.477647'),(6,'analytics','0001_initial','2024-10-10 08:27:21.815575'),(7,'contenttypes','0002_remove_content_type_name','2024-10-10 08:27:21.866940'),(8,'auth','0002_alter_permission_name_max_length','2024-10-10 08:27:21.903553'),(9,'auth','0003_alter_user_email_max_length','2024-10-10 08:27:21.918671'),(10,'auth','0004_alter_user_username_opts','2024-10-10 08:27:21.925399'),(11,'auth','0005_alter_user_last_login_null','2024-10-10 08:27:21.957734'),(12,'auth','0006_require_contenttypes_0002','2024-10-10 08:27:21.959477'),(13,'auth','0007_alter_validators_add_error_messages','2024-10-10 08:27:21.965338'),(14,'auth','0008_alter_user_username_max_length','2024-10-10 08:27:22.004468'),(15,'auth','0009_alter_user_last_name_max_length','2024-10-10 08:27:22.046659'),(16,'auth','0010_alter_group_name_max_length','2024-10-10 08:27:22.060108'),(17,'auth','0011_update_proxy_permissions','2024-10-10 08:27:22.069085'),(18,'auth','0012_alter_user_first_name_max_length','2024-10-10 08:27:22.110698'),(19,'authtoken','0001_initial','2024-10-10 08:27:22.160063'),(20,'authtoken','0002_auto_20160226_1747','2024-10-10 08:27:22.178260'),(21,'authtoken','0003_tokenproxy','2024-10-10 08:27:22.180827'),(22,'authtoken','0004_alter_tokenproxy_options','2024-10-10 08:27:22.205312'),(23,'sessions','0001_initial','2024-10-10 08:27:22.233694');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('6t4rbcsgowcg7qtdcpz9q6iikrjn89vd','.eJxVjEEOwiAQRe_C2pAphRFduvcMZJgBqRpISrsy3l2bdKHb_977LxVoXUpYe5rDJOqsjDr8bpH4keoG5E711jS3usxT1Juid9r1tUl6Xnb376BQL986Ds7bBCjIDuQUPViTnZAnQwZGtjCiyQMxkWdns2QEQHscnZeI2ar3B9wSN70:1sz6tl:uU6Pvd8CzjBz5QVg9veL9uepbC1bS2fY3C735zwvz4A','2024-10-25 04:05:05.451946');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-15 10:43:43
