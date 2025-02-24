CREATE DATABASE la_Reina_Huevo_db;
USE la_Reina_Huevo_db;

-- Crear la tabla galpon primero
CREATE TABLE galpon (
  id_galpon INT AUTO_INCREMENT PRIMARY KEY,
  numero_Galpon INT,
  numero_aves INT
);

-- Tabla de Condiciones Ambientales
CREATE TABLE CondicionesAmbientales (
  id_CondicionesAmbientales INT AUTO_INCREMENT PRIMARY KEY,
  fecha DATE NOT NULL,
  temperatura DECIMAL(5, 2),
  humedad DECIMAL(5, 2),
  ventilacion VARCHAR(50), -- Cambiado a VARCHAR
  iluminacion VARCHAR(50), -- Cambiado a VARCHAR
  id_galpon INT,
  FOREIGN KEY (id_galpon) REFERENCES galpon(id_galpon)
);

-- Tabla de aves
CREATE TABLE aves (
  ave_id INT AUTO_INCREMENT PRIMARY KEY,
  raza VARCHAR(255),
  fecha_nacimiento DATE NOT NULL,
  fecha_llegada DATE NOT NULL,
  origen VARCHAR(255) NOT NULL,
  total_aves INT,
  id_galpon INT,
  FOREIGN KEY (id_galpon) REFERENCES galpon(id_galpon)
);

-- Tabla de mortalidad
CREATE TABLE mortalidad (
  mortalidad_id INT AUTO_INCREMENT PRIMARY KEY,
  numero_galpon INT,
  estado_salud VARCHAR(255) NOT NULL,
  fecha_muerte DATE,
  causa_muerte VARCHAR(255),
  numero_aves INT,
  id_galpon INT,
  FOREIGN KEY (id_galpon) REFERENCES galpon(id_galpon)
);

-- Tabla de pesaje
CREATE TABLE pesaje (
  pesaje_id INT PRIMARY KEY AUTO_INCREMENT,
  numero_ave INT,
  estado_salud VARCHAR(255) NOT NULL,
  peso INT NOT NULL,
  fecha_Pesaje DATE NOT NULL,
  id_galpon INT,
  FOREIGN KEY (id_galpon) REFERENCES galpon(id_galpon)
);

-- Tabla de vacunacion
CREATE TABLE vacunacion (
  vacunacion_id INT PRIMARY KEY AUTO_INCREMENT,
  nombre_Vacuna VARCHAR(255) NOT NULL,
  fecha DATE NOT NULL,
  id_galpon INT,
  FOREIGN KEY (id_galpon) REFERENCES galpon(id_galpon)
);

-- Tabla de huevos
CREATE TABLE huevos (
  huevo_id INT PRIMARY KEY AUTO_INCREMENT,
  fecha_puesta DATE NOT NULL,
  peso_huevo DECIMAL(5, 2) NOT NULL,
  calidad_huevo INT NOT NULL,
  total_huevo INT NOT NULL,
  id_galpon INT,
  FOREIGN KEY (id_galpon) REFERENCES galpon(id_galpon)
);

-- Tabla de alimentos
CREATE TABLE alimentos (
  alimento_id INT PRIMARY KEY AUTO_INCREMENT,
  marca_Alimento VARCHAR(255) NOT NULL,
  etapa_alimento VARCHAR(255) NOT NULL,
  fecha_consumo DATE NOT NULL,
  cantidad_kg INT NOT NULL,
  id_galpon INT,
  FOREIGN KEY (id_galpon) REFERENCES galpon(id_galpon)
);
 
-- Tabla de Clima
CREATE TABLE Clima (
  id INT AUTO_INCREMENT PRIMARY KEY,
  fecha DATE NOT NULL,
  temperatura DECIMAL(5, 2),
  precipitacion DECIMAL(5, 2)
);
