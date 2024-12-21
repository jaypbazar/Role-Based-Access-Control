-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 21, 2024 at 06:10 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `se_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `lotName` varchar(50) NOT NULL,
  `bookingDate` date NOT NULL,
  `timeStarted` time NOT NULL,
  `timeEnded` time NOT NULL,
  `ClientID` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`lotName`, `bookingDate`, `timeStarted`, `timeEnded`, `ClientID`) VALUES
('Lot IP005', '2024-12-28', '11:51:00', '23:51:00', '221008049');

-- --------------------------------------------------------

--
-- Table structure for table `parking_lots`
--

CREATE TABLE `parking_lots` (
  `name` varchar(50) NOT NULL,
  `latitude1` decimal(20,15) NOT NULL,
  `longitude1` decimal(20,15) NOT NULL,
  `latitude2` decimal(20,15) NOT NULL,
  `longitude2` decimal(20,15) NOT NULL,
  `status` enum('available','reserved','occupied','') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parking_lots`
--

INSERT INTO `parking_lots` (`name`, `latitude1`, `longitude1`, `latitude2`, `longitude2`, `status`) VALUES
('Lot IP001', 13.405581896431616, 123.376980411010430, 13.405542932132011, 123.377003632488180, 'available'),
('Lot IP002', 13.405578721330884, 123.377037160100240, 13.405538584414021, 123.377063369921250, 'occupied'),
('Lot IP003', 13.405574546229933, 123.377093486488480, 13.405531886491611, 123.377120979130370, 'available'),
('Lot IP004', 13.405552334217062, 123.377228187395890, 13.405510065346709, 123.377252327276540, 'available'),
('Lot IP005', 13.405535288577386, 123.377277137709480, 13.405493019707033, 123.377301277590130, 'reserved'),
('Lot IP006', 13.405526242936998, 123.377326723605140, 13.405484974066645, 123.377350863485790, 'available');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` varchar(255) NOT NULL,
  `FIrstName` varchar(255) NOT NULL,
  `MiddleName` varchar(255) NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `Role` enum('admin','employee','student') NOT NULL,
  `CspcEmail` varchar(255) NOT NULL,
  `PhoneNumber` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `ProfilePhoto` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `FIrstName`, `MiddleName`, `LastName`, `Role`, `CspcEmail`, `PhoneNumber`, `Password`, `ProfilePhoto`) VALUES
('12345678', 'John Michael', '', 'Dela Cruz', 'employee', 'john.delacruz@cspc.edu.ph', '09981234567', '43163b58711f9de5d6a726a36bba65e35d874b3a1ef689c004b3fb9b938ad34e', ''),
('202312345', 'Maria Clara', 'Ibarra', 'Santos', 'student', 'maria.clara@cspc.edu.ph', '09171234567', '2a966c8e3833f9876d847cfb242d4fcb224d759fadd8b1e1a0a189d0eaa8bcbc', ''),
('202312678', 'Angela Marie', '', 'Cruz', 'student', 'angela.cruz@cspc.edu.ph', '09181234678', '33686c65cb8f7d691f2aa3ea3952148690f3214da435ea822ed913f24da9c285', ''),
('202398765', 'Joseph', 'Luis', 'Ramirez', 'student', 'joseph.ramirez@cspc.edu.ph', '09091234567', 'faf8e8f1a32e4e9e454b61c56f025e9a798f17b219d7a6bf3a0bbdf48606ce03', ''),
('221008049', 'Jayp', 'Surara', 'Bazar', 'admin', 'jabazar@my.cspc.edu.ph', '09725974622', 'ddb293b5b47020df66a30f184d03d312b0a485d9e6e2b2315c09d567e3c34a02', 'static/img/221008049_profile.jpg'),
('231004168', 'Alfredo', 'Obrero', 'Sasota', 'student', 'alsasota@my.cspc.edu.ph', '09923051944', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'static/img/231004168_profile.jpg'),
('98765432', 'Christine Joy', 'Perez', 'Gonzales', 'employee', 'christine.gonzales@cspc.edu.ph', '09351234987', 'e17d8d2fd76e926c1a1343a0f674f0e6cd5fb746c77b71a7f95fcc00458fba0f', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`lotName`),
  ADD KEY `fk_studentID` (`ClientID`);

--
-- Indexes for table `parking_lots`
--
ALTER TABLE `parking_lots`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bookings`
--
ALTER TABLE `bookings`
  ADD CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`lotName`) REFERENCES `parking_lots` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_studentID` FOREIGN KEY (`ClientID`) REFERENCES `users` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
