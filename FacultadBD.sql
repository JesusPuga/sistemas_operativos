CREATE TABLE Inscripcion (
	claveInscripcion BIGINT UNSIGNED AUTO_INCREMENT,
	fechaInscripcion TIMESTAMP,

	CONSTRAINT claveInscripcion_PK PRIMARY KEY (claveInscripcion)
);

CREATE TABLE Carrera (
	claveCarrera INT UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL,

	CONSTRAINT claveCarrera_PK PRIMARY KEY (claveCarrera)
);

CREATE TABLE Usuario (
	carnetUsuario INT UNSIGNED NOT NULL AUTO_INCREMENT,
	sexo CHAR(1),
	telefono CHAR(10),
	contrasenia CHAR(15),
	nombre VARCHAR(45) NOT NULL,
	apellidoPaterno VARCHAR(30) NOT NULL,
	apellidoMaterno VARCHAR(30) NOT NULL,
	tipoUsuario TINYINT NOT NULL,

	CONSTRAINT carnetUsuario_PK PRIMARY KEY (carnetUsuario)
);

CREATE TABLE Empleado (
	carnetEmpleado INT UNSIGNED NOT NULL PRIMARY KEY,
	tipoEmpleado VARCHAR(40) NOT NULL,

	CONSTRAINT carnetEmpleado_FK FOREIGN KEY (carnetEmpleado)
	REFERENCES Usuario(carnetUsuario)
	ON DELETE RESTRICT
	ON UPDATE CASCADE

);

CREATE TABLE Alumno (
	carnetAlumno INT UNSIGNED NOT NULL PRIMARY KEY,
	estatus VARCHAR (30) NOT NULL,
	claveCarrera INT UNSIGNED ZEROFILL NOT NULL,
	claveInscripcion BIGINT UNSIGNED,

	CONSTRAINT carnetAlumno_FK FOREIGN KEY (carnetAlumno)
	REFERENCES Usuario(carnetUsuario)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT claveCarrera_FK FOREIGN KEY (claveCarrera)
	REFERENCES Carrera(claveCarrera)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT claveInscripcion_FK FOREIGN KEY (claveInscripcion)
	REFERENCES Inscripcion(claveInscripcion)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Materia (
	claveMateria INT UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL,
	creditos TINYINT NOT NULL,
	semestre TINYINT NOT NULL,
	claveCarrera INT UNSIGNED NOT NULL,

	CONSTRAINT claveMateria_PK PRIMARY KEY (claveMateria),

	CONSTRAINT claveCarreraMateria_FK FOREIGN KEY (claveCarrera)
	REFERENCES Carrera(claveCarrera)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Materia_Seriada (
	claveMateria INT UNSIGNED  NOT NULL,
	claveMateriaSeriada INT UNSIGNED  NOT NULL,

	CONSTRAINT claveMateria_PK PRIMARY KEY (claveMateria, claveMateriaSeriada),

	CONSTRAINT claveMateria_FK FOREIGN KEY (claveMateria)
	REFERENCES Materia(claveMateria)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT claveMateriaSeriada_FK FOREIGN KEY (claveMateriaSeriada)
	REFERENCES Materia(claveMateria)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Oportunidad (
	IDOportunidad BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	calificacion TINYINT DEFAULT NULL,
	numOportunidad TINYINT NOT NULL,
	carnetAlumno INT UNSIGNED NOT NULL,
	claveMateria INT UNSIGNED ZEROFILL NOT NULL,

	CONSTRAINT IDOportunidad_PK PRIMARY KEY (IDOportunidad),

	CONSTRAINT carnetAlumnoOportunidad_FK FOREIGN KEY (carnetAlumno)
	REFERENCES Alumno(carnetAlumno)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT claveMateriaOportunidad_FK FOREIGN KEY (claveMateria)
	REFERENCES Materia(claveMateria)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Grupo (
	IDGrupo  BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	claveGrupo TINYINT ZEROFILL,
	aula INT ZEROFILL,
	capacidad TINYINT,
	contador TINYINT,
	perdio DATE,
	carnetEmpleado INT UNSIGNED NOT NULL,
	claveMateria INT UNSIGNED ZEROFILL NOT NULL,

	CONSTRAINT IDGrupo_PK PRIMARY KEY (IDGrupo),

	CONSTRAINT carnetEmpleadoG_FK FOREIGN KEY (carnetEmpleado)
	REFERENCES Empleado(carnetEmpleado)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT claveMateriaGrupo_FK FOREIGN KEY (claveMateria)
	REFERENCES Materia(claveMateria)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Horario (
	IDHorario BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	dia CHAR(10) NOT NULL,
	horaInicio TIME NOT NULL,
	horaFin TIME NOT NULL,
	claveGrupo BIGINT UNSIGNED NOT NULL,

	CONSTRAINT Horario_PK PRIMARY KEY (IDHorario),

	CONSTRAINT claveGrupo_FK FOREIGN KEY (claveGrupo)
	REFERENCES Grupo(IDGrupo)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Alumno_Grupo (
	claveGrupo  BIGINT UNSIGNED NOT NULL,
	carnetAlumno INT UNSIGNED NOT NULL,

	CONSTRAINT claveAlumnoGrupo_PK PRIMARY KEY (claveGrupo, carnetAlumno),

	CONSTRAINT claveGrupoRel_FK FOREIGN KEY (claveGrupo)
	REFERENCES Grupo(IDGrupo)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT carnetAlumnoRel_FK FOREIGN KEY (carnetAlumno)
	REFERENCES Alumno(carnetAlumno)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

INSERT INTO `Carrera` (`claveCarrera`, `nombre`) VALUES
(001, 'CIENCIAS DE LA COMPUTACIÓN');

INSERT INTO `Materia` (`claveMateria`, `nombre`, `creditos`, `numeroSemestre`, `claveCarrera`) VALUES
(001, 'MATEMÁTICAS I', 1, 1, 1),
(002, 'FUNDAMENTOS DE ELECTROMAGNETISMO', 1, 1, 1),
(003, 'FUNDAMENTOS DE ALGORITMOS', 1, 1, 1),
(004, 'ARQUITECTURA DE COMPUTADORAS', 1, 1, 1),
(005, 'PROGRAMACIÓN ESTRUCTURADA', 1, 1, 1),
(006, 'MATEMÁTICAS II', 1, 2, 1),
(007, 'SISTEMAS ELECTRÓNICOS', 1, 2, 1),
(008, 'FUNDAMENTOS DE REDES', 1, 2, 1),
(009, 'BASE DE DATOS', 1, 2, 1),
(010, 'PROGRAMACIÓN ORIENTADA A OBJETOS', 1, 2, 1),
(011, 'FUNDAMENTOS DE ESTADÁSTICA', 1, 2, 1),
(012, 'MATEMÁTICAS DISCRETAS', 1, 3, 1),
(013, 'CIRCUITOS DIGITALES', 1, 3, 1),
(014, 'ESTRUCTURA DE DATOS', 1, 3, 1),
(015, 'ANÁLISIS DE SISTEMAS', 1, 3, 1),
(016, 'TEORÍA DE AUTÁMATAS', 1, 3, 1),
(017, 'ANÁLISIS NUMÉRICO', 1, 3, 1),
(018, 'ADMINISTRACIÓN DE PROYECTOS', 1, 4, 1),
(019, 'SISTEMAS OPERATIVOS', 1, 4, 1),
(020, 'ADMINSTRACIÓN DE REDES', 1, 4, 1),
(021, 'MODELOS ESTADÍSTICOS', 1, 4, 1),
(022, 'SISTEMAS EMBEBIDOS', 1, 4, 1),
(023, 'MINERÍA DE DATOS', 1, 4, 1),
(024, 'SISTEMAS DISTRIBUIDOS', 1, 5, 1),
(025, 'INTELIGENCIA ARTIFICIAL', 1, 5, 1),
(026, 'BIG DATA', 1, 5, 1),
(027, 'REDES NEURONALES', 1, 5, 1),
(028, 'SERVICIO SOCIAL', 1, 5, 1);
