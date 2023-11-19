-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 18, 2023 alle 15:24
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5atepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendenti_erika_boccadoro`
--

CREATE TABLE `dipendenti_erika_boccadoro` (
  `id` int(11) NOT NULL,
  `nome` varchar(20) DEFAULT NULL,
  `cognome` varchar(20) DEFAULT NULL,
  `posizione_lavorativa` varchar(20) NOT NULL,
  `data_assunzione` varchar(20) DEFAULT NULL,
  `data_nascita` date DEFAULT NULL,
  `mail` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `dipendenti_erika_boccadoro`
--

INSERT INTO `dipendenti_erika_boccadoro` (`id`, `nome`, `cognome`, `posizione_lavorativa`, `data_assunzione`, `data_nascita`, `mail`) VALUES
(3, 'martina', 'rossi', 'pulizie', '23 gennaio 2013', '1995-02-03', 'rossi.m@gmail.com'),
(8, 'Sumi', 'Hamil', 'Ingegnere Informatic', '2000 gennaio 7', '1985-11-25', 'samillo@gmail.com'),
(9, 'hamran', 'singh', 'graphic designer', '11 maggio 1999', '1970-04-07', 'mala.hamr@gmail.com');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_erika_boccadoro`
--
ALTER TABLE `dipendenti_erika_boccadoro`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_erika_boccadoro`
--
ALTER TABLE `dipendenti_erika_boccadoro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
