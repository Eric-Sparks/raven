-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 15, 2018 at 02:02 AM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.1.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Energy_Usage`
--

-- --------------------------------------------------------

--
-- Table structure for table `Gateway_Data`
--

CREATE TABLE `Gateway_Data` (
  `date_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `battery_instant_power` int(11) NOT NULL,
  `battery_energy_imported` int(11) NOT NULL,
  `battery_energy_exported` int(11) NOT NULL,
  `load_instant_power` int(11) NOT NULL,
  `load_energy_imported` int(11) NOT NULL,
  `solar_instant_power` int(11) NOT NULL,
  `solar_energy_imported` int(11) NOT NULL,
  `solar_energy_exported` int(11) NOT NULL,
  `grid_instant_power` int(11) NOT NULL,
  `grid_energy_imported` int(11) NOT NULL,
  `grid_energy_exported` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Gateway_Data`
--
ALTER TABLE `Gateway_Data`
  ADD PRIMARY KEY (`date_time`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
