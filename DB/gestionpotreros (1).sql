-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-02-2024 a las 21:36:22
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestionpotreros`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fertilizantes`
--

CREATE TABLE `fertilizantes` (
  `idfertilizante` int(11) NOT NULL,
  `nombrefertilizante` varchar(150) DEFAULT NULL,
  `categoria` varchar(150) DEFAULT NULL,
  `proveedor` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lotes`
--

CREATE TABLE `lotes` (
  `idlote` int(11) NOT NULL,
  `nombre` varchar(150) DEFAULT NULL,
  `idpotrero` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `lotes`
--

INSERT INTO `lotes` (`idlote`, `nombre`, `idpotrero`) VALUES
(1, '2-1', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `potreros`
--

CREATE TABLE `potreros` (
  `idpotrero` int(11) NOT NULL,
  `potrero_nombre` varchar(150) DEFAULT NULL,
  `zona` varchar(255) DEFAULT NULL,
  `area` decimal(10,0) DEFAULT NULL,
  `promediodias` int(11) DEFAULT NULL,
  `tipopastura` varchar(150) DEFAULT NULL,
  `estado` varchar(150) DEFAULT NULL,
  `coordenada` text NOT NULL,
  `observacion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `potreros`
--

INSERT INTO `potreros` (`idpotrero`, `potrero_nombre`, `zona`, `area`, `promediodias`, `tipopastura`, `estado`, `coordenada`, `observacion`) VALUES
(1, 'Potrero54', 'Delirio', 12, 0, '[value-6]', 'Descanso/Recuperacion', '', ''),
(2, 'Potrero2', 'Delirio', 3, 25, 'Estrella', 'Descanso/Recuperacion', '', ''),
(3, 'Potrero3', 'Delirio', 12, 23, 'Estrella', 'Descanso/Recuperacion', '', ''),
(4, 'Potrero 4', 'Delirio', 12, 23, 'Estrella', 'Ocupado', '', ''),
(5, 'Potrero 5', 'Pata de Loma', 2, 23, 'Estrella', 'Descanso/Recuperacion', '', ''),
(6, 'Potrero 6', 'Pata de Loma', 3, 23, 'Estrella', 'Descanso/Recuperacion', '123321432f', 'Este es un nuevo potrero'),
(7, 'Potrero 1', 'Pata de Loma', 2, 25, 'Caiman', 'Descanso/Recuperacion', '638637', 'Todo cool'),
(8, 'chancho', 'Deliro', 2, 123, 'oscura', 'Ocupado/Consumo', '123321432f', 'Chancho es Hacker y baho');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registrofertilizacion`
--

CREATE TABLE `registrofertilizacion` (
  `idregistrofertilizacion` int(11) NOT NULL,
  `idpotrero` int(11) DEFAULT NULL,
  `idfertilizante` int(11) DEFAULT NULL,
  `cantidad` decimal(10,0) DEFAULT NULL,
  `fechafertilizacion` date DEFAULT NULL,
  `fecharefertilizacion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registrosrotacion`
--

CREATE TABLE `registrosrotacion` (
  `idregistro` int(11) NOT NULL,
  `idpotrero` int(11) DEFAULT NULL,
  `entradasalida` varchar(100) DEFAULT NULL,
  `fecharotacion` date DEFAULT NULL,
  `posiblereingreso` date DEFAULT NULL,
  `estado` varchar(150) DEFAULT NULL,
  `idlote` int(11) DEFAULT NULL,
  `oservacion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `fullname`) VALUES
(0, 'DILAN', 'pbkdf2:sha256:600000$9n2vrKTDuY8BL1Dt$dd30686e053226fc844d47f3d59beec0bb9eebcd6c6ef486a714736de75191d5', 'Dilan Adrian Zapata Ortiz');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `fertilizantes`
--
ALTER TABLE `fertilizantes`
  ADD PRIMARY KEY (`idfertilizante`);

--
-- Indices de la tabla `lotes`
--
ALTER TABLE `lotes`
  ADD PRIMARY KEY (`idlote`),
  ADD KEY `fk_lote_potrero` (`idpotrero`);

--
-- Indices de la tabla `potreros`
--
ALTER TABLE `potreros`
  ADD PRIMARY KEY (`idpotrero`);

--
-- Indices de la tabla `registrofertilizacion`
--
ALTER TABLE `registrofertilizacion`
  ADD PRIMARY KEY (`idregistrofertilizacion`),
  ADD KEY `idpotrero` (`idpotrero`),
  ADD KEY `idfertilizante` (`idfertilizante`);

--
-- Indices de la tabla `registrosrotacion`
--
ALTER TABLE `registrosrotacion`
  ADD PRIMARY KEY (`idregistro`),
  ADD KEY `idpotrero` (`idpotrero`),
  ADD KEY `idlote` (`idlote`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `fertilizantes`
--
ALTER TABLE `fertilizantes`
  MODIFY `idfertilizante` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `lotes`
--
ALTER TABLE `lotes`
  MODIFY `idlote` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `potreros`
--
ALTER TABLE `potreros`
  MODIFY `idpotrero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `registrofertilizacion`
--
ALTER TABLE `registrofertilizacion`
  MODIFY `idregistrofertilizacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `registrosrotacion`
--
ALTER TABLE `registrosrotacion`
  MODIFY `idregistro` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `lotes`
--
ALTER TABLE `lotes`
  ADD CONSTRAINT `fk_lote_potrero` FOREIGN KEY (`idpotrero`) REFERENCES `potreros` (`idpotrero`);

--
-- Filtros para la tabla `registrofertilizacion`
--
ALTER TABLE `registrofertilizacion`
  ADD CONSTRAINT `registrofertilizacion_ibfk_1` FOREIGN KEY (`idpotrero`) REFERENCES `potreros` (`idpotrero`),
  ADD CONSTRAINT `registrofertilizacion_ibfk_2` FOREIGN KEY (`idfertilizante`) REFERENCES `fertilizantes` (`idfertilizante`);

--
-- Filtros para la tabla `registrosrotacion`
--
ALTER TABLE `registrosrotacion`
  ADD CONSTRAINT `registrosrotacion_ibfk_1` FOREIGN KEY (`idpotrero`) REFERENCES `potreros` (`idpotrero`),
  ADD CONSTRAINT `registrosrotacion_ibfk_2` FOREIGN KEY (`idlote`) REFERENCES `lotes` (`idlote`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
