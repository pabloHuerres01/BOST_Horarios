-- Crear base de datos
CREATE DATABASE IF NOT EXISTS bost_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE bost_db;

-- Tabla de empleados
CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    vacaciones_disponibles INT DEFAULT 0
);

-- Tabla de puestos (L1, L2, L3, PROVISION)
CREATE TABLE puestos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL UNIQUE
);

-- Tabla de meses
CREATE TABLE meses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    anio INT NOT NULL,
    mes INT NOT NULL,
    UNIQUE(anio, mes)
);

-- Tabla de días
CREATE TABLE dias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_dia INT NOT NULL,
    mes_id INT NOT NULL,
    FOREIGN KEY (mes_id) REFERENCES meses(id) ON DELETE CASCADE
);

-- Tabla de turnos (permite múltiples empleados por día y turno)
CREATE TABLE turnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dia_id INT NOT NULL,
    empleado_id INT NOT NULL,
    turno ENUM('mañana', 'tarde') NOT NULL,
    puesto_id INT NOT NULL,
    FOREIGN KEY (dia_id) REFERENCES dias(id) ON DELETE CASCADE,
    FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
    FOREIGN KEY (puesto_id) REFERENCES puestos(id)
);
