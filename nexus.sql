-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 02. Nov 2026 um 19:26
-- Server-Version: 10.4.32-MariaDB
-- PHP-Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `nexus`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `chats`
--

CREATE TABLE `chats` (
  `chatid` int(11) NOT NULL,
  `chatname` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `chats`
--

INSERT INTO `chats` (`chatid`, `chatname`, `created_at`) VALUES
(1, 'Allgemein', '2026-11-01 13:52:50'),
(2, 'Chat 2', '2026-11-01 15:13:24'),
(3, 'Gaming', '2026-11-01 16:34:58'),
(4, 'Test', '2026-11-01 16:36:07'),
(5, 'Geil', '2026-11-01 16:41:04'),
(6, 'TestChat', '2026-11-01 18:00:03'),
(7, 'fdsf', '2026-11-01 18:00:59'),
(8, 'sdff', '2026-11-01 18:01:23'),
(9, 'dsfsd', '2026-11-01 18:01:37'),
(10, 'fdsf', '2026-11-01 18:03:02'),
(11, 'ffdsf', '2026-11-01 18:03:59'),
(12, 'dasds', '2026-11-01 18:05:01'),
(20, 'Test2', '2026-11-01 18:55:58');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `chat_members`
--

CREATE TABLE `chat_members` (
  `chatid` int(11) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `chat_members`
--

INSERT INTO `chat_members` (`chatid`, `userid`) VALUES
(1, 1),
(6, 1),
(6, 2),
(6, 3),
(7, 1),
(7, 2),
(7, 3),
(8, 1),
(8, 2),
(8, 3),
(9, 1),
(9, 2),
(10, 1),
(10, 2),
(11, 1),
(12, 1),
(20, 1),
(20, 2),
(20, 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `messages`
--

CREATE TABLE `messages` (
  `messageid` int(11) NOT NULL,
  `chatid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `content` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `messages`
--

INSERT INTO `messages` (`messageid`, `chatid`, `userid`, `content`, `created_at`) VALUES
(1, 1, 1, 'Hallo Welt', '2026-11-01 13:52:59'),
(2, 1, 1, 'Test Nachricht', '2026-11-01 14:07:19'),
(3, 1, 1, 'Test123', '2026-11-01 14:40:47'),
(4, 1, 1, 'Läuft es?', '2026-11-01 15:04:31'),
(6, 2, 1, 'Nachricht aus Chat 2', '2026-11-01 15:13:46'),
(7, 1, 1, 'Test 1', '2026-11-01 15:34:12'),
(8, 2, 1, 'Hallo, wie geht es?', '2026-11-01 15:39:10');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `users`
--

CREATE TABLE `users` (
  `userid` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `users`
--

INSERT INTO `users` (`userid`, `username`, `password_hash`, `created_at`) VALUES
(1, 'Tilo', 'test', '2026-11-01 13:52:46'),
(2, 'Max', 'test123', '2026-11-01 17:22:40'),
(3, 'Anna', 'test123', '2026-11-01 17:22:40'),
(4, 'Lukas', 'test123', '2026-11-01 17:22:40'),
(5, 'Sophie', 'test123', '2026-11-01 17:22:40'),
(6, 'Ben', 'test123', '2026-11-01 17:22:40');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `chats`
--
ALTER TABLE `chats`
  ADD PRIMARY KEY (`chatid`);

--
-- Indizes für die Tabelle `chat_members`
--
ALTER TABLE `chat_members`
  ADD PRIMARY KEY (`chatid`,`userid`),
  ADD KEY `fk_members_user` (`userid`);

--
-- Indizes für die Tabelle `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`messageid`),
  ADD KEY `fk_messages_chat` (`chatid`),
  ADD KEY `fk_messages_user` (`userid`);

--
-- Indizes für die Tabelle `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `chats`
--
ALTER TABLE `chats`
  MODIFY `chatid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT für Tabelle `messages`
--
ALTER TABLE `messages`
  MODIFY `messageid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT für Tabelle `users`
--
ALTER TABLE `users`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `chat_members`
--
ALTER TABLE `chat_members`
  ADD CONSTRAINT `fk_members_chat` FOREIGN KEY (`chatid`) REFERENCES `chats` (`chatid`),
  ADD CONSTRAINT `fk_members_user` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`);

--
-- Constraints der Tabelle `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `fk_messages_chat` FOREIGN KEY (`chatid`) REFERENCES `chats` (`chatid`),
  ADD CONSTRAINT `fk_messages_user` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
