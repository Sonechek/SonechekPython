-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Апр 16 2021 г., 15:53
-- Версия сервера: 8.0.22-0ubuntu0.20.04.2
-- Версия PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `soft0049_labrab`
--

-- --------------------------------------------------------

--
-- Структура таблицы `students`
--

CREATE TABLE `students` (
  `id` int NOT NULL,
  `nameStud` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `rating` int NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `date` date NOT NULL,
  `city` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `students`
--

INSERT INTO `students` (`id`, `nameStud`, `rating`, `gender`, `date`, `city`) VALUES
(1, 'Мишкин', 217, 1, '2002-08-23', 'Кунгур'),
(2, 'Бортич', 224, 0, '2002-06-03', 'Лысьва'),
(3, 'Деревянко', 182, 0, '2002-02-20', 'Оса'),
(4, 'Столбова', 194, 0, '2003-01-22', 'Кунгур'),
(5, 'Хомич', 205, 0, '2002-04-23', 'Кунгур'),
(6, 'Круглов', 191, 1, '2002-04-23', 'Березники'),
(7, 'Иванов', 192, 1, '2002-05-17', 'Кунгур'),
(8, 'Петров', 191, 1, '2002-11-25', 'Кунгур'),
(9, 'Сидоров', 196, 1, '2004-01-20', 'Кунгур'),
(10, 'Капустин', 196, 1, '2002-06-04', 'Кунгур'),
(11, 'Томатова', 201, 0, '2003-04-16', 'Кунгур'),
(12, 'Ежова', 214, 0, '2001-10-07', 'Лысьва'),
(13, 'Микова', 222, 0, '2001-10-07', 'Пермь'),
(14, 'Мамин', 199, 1, '2001-11-10', 'Пермь'),
(15, 'Комов', 195, 1, '2002-01-17', 'Пермь');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `students`
--
ALTER TABLE `students`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
