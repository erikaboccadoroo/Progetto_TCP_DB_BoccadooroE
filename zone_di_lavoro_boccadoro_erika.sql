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
-- Struttura della tabella `zone_di_lavoro_boccadoro_erika`
--

CREATE TABLE `zone_di_lavoro_boccadoro_erika` (
  `id_zona` int(11) NOT NULL,
  `nome_zona` varchar(100) NOT NULL,
  `numero_clienti` int(11) NOT NULL,
  `id_dipendente` int(11) NOT NULL,
  `progetto_zona` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `zone_di_lavoro_boccadoro_erika`
--

INSERT INTO `zone_di_lavoro_boccadoro_erika` (`id_zona`, `nome_zona`, `numero_clienti`, `id_dipendente`, `progetto_zona`) VALUES
(1, 'Help Desk', 15, 3, 'Intelligenza artificiare per la soluzione di problemi'),
(3, 'Help Desk', 28, 9, 'Creazione database per archivio contratti 2008/2009');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zone_di_lavoro_boccadoro_erika`
--
ALTER TABLE `zone_di_lavoro_boccadoro_erika`
  ADD PRIMARY KEY (`id_zona`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zone_di_lavoro_boccadoro_erika`
--
ALTER TABLE `zone_di_lavoro_boccadoro_erika`
  MODIFY `id_zona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
