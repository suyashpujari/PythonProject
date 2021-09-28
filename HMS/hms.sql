-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 28, 2021 at 08:43 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hms`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `id` int(3) NOT NULL,
  `doc_name` varchar(15) NOT NULL,
  `pat_name` varchar(15) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`id`, `doc_name`, `pat_name`, `date`, `time`) VALUES
(4, 'Vardhan', 'Shrinivas', '9/29/21', '10:30 AM'),
(5, 'Kanti', 'Abhishek', '9/29/21', '11:30 AM'),
(6, 'Vardhan', 'Ram', '9/30/21', '8:15 PM');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `id` int(3) NOT NULL,
  `name` varchar(30) NOT NULL,
  `specialization` varchar(25) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`id`, `name`, `specialization`, `contact`, `address`) VALUES
(4, 'Sumit', 'ENT', '9865327845', 'Pune'),
(5, 'Vardhan', 'Surgeon', '8754213250', 'Solapur'),
(6, 'Kanti', 'Surgeon', '9865321245', 'Solapur'),
(7, 'Chaitali', 'Anesthesiology', '7946131622', 'Jabbalpur'),
(8, 'Rohan', 'Neruosurgeon', '8765321245', 'Solapur'),
(9, 'Vikram', 'Cardiologists', '9832124585', 'Aurangabad'),
(10, 'Dimple', 'Immunologists', '8765324589', 'Nagpur'),
(13, 'Rohit', 'Family Physician', '8789545621', 'Delhi');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `id` int(3) NOT NULL,
  `name` varchar(30) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`id`, `name`, `gender`, `contact`, `address`) VALUES
(7, 'Karan', ' Male', '7845128956', 'Mumbai'),
(8, 'Nikita', ' Female', '7889455612', 'Mumbai'),
(9, 'Shrinivas', ' Male', '8754213265', 'Pune'),
(10, 'Pooja', ' Female', '7845986512', 'Solan'),
(11, 'Abhishek', ' Male', '9832654512', 'Kolhapur'),
(12, 'Ram', ' Male', '8754986512', 'Dhule'),
(13, 'Nikhil', ' Male', '8765451298', 'Dhule');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
