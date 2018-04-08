CREATE TABLE Inscripcion (
	claveInscripcion BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	fechaInscripcion TIMESTAMP,

	CONSTRAINT claveInscripcion_PK PRIMARY KEY (claveInscripcion)
);

CREATE TABLE Carrera (
	claveCarrera INT UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL,

	CONSTRAINT claveCarrera_PK PRIMARY KEY (claveCarrera)
);

CREATE TABLE Oportunidad (
	IDOportunidad BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	calificacion TINYINT NOT NULL,
	numOportunidad TINYINT NOT NULL,

	CONSTRAINT IDOportunidad_PK PRIMARY KEY (IDOportunidad)
);

CREATE TABLE Materia (
	claveMateria INT UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL,
	creditos TINYINT NOT NULL,
	numeroSemestre TINYINT NOT NULL,
	claveCarrera INT UNSIGNED NOT NULL,

	CONSTRAINT claveMateria_PK PRIMARY KEY (claveMateria),

	CONSTRAINT claveCarrera_FK FOREIGN KEY (claveCarrera)
	REFERENCES Carrera(claveCarrera)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
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
	claveCarrera INT UNSIGNED NULL,
	claveInscripcion BIGINT UNSIGNED NULL,

	CONSTRAINT carnetUsuario_PK PRIMARY KEY (carnetUsuario),

	CONSTRAINT claveCarreraU_FK FOREIGN KEY (claveCarrera)
	REFERENCES Carrera(claveCarrera)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT claveInscripcionU_FK FOREIGN KEY (claveInscripcion)
	REFERENCES Inscripcion(claveInscripcion)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Alumno (
	carnetAlumno INT UNSIGNED NOT NULL PRIMARY KEY,
	estatus VARCHAR (30) NOT NULL,

	CONSTRAINT carnetAlumno_FK FOREIGN KEY (carnetAlumno)
	REFERENCES Usuario(carnetUsuario)
	ON DELETE RESTRICT
	ON UPDATE CASCADE

);

CREATE TABLE Empleado (
	carnetEmpleado INT UNSIGNED NOT NULL PRIMARY KEY,
	tipoEmpleado VARCHAR(40) NOT NULL,

	CONSTRAINT carnetEmpleado_FK FOREIGN KEY (carnetEmpleado)
	REFERENCES Usuario(carnetUsuario)
	ON DELETE RESTRICT
	ON UPDATE CASCADE

);

CREATE TABLE Grupo (
	IDGrupo  BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	claveGrupo TINYINT ZEROFILL,
	aula INT ZEROFILL,
	carnetEmpleado INT UNSIGNED NOT NULL,
	contador TINYINT,
	claveEmpleado INT UNSIGNED NOT NULL,

	CONSTRAINT IDGrupo_PK PRIMARY KEY (IDGrupo),

	CONSTRAINT carnetEmpleadoG_FK FOREIGN KEY (claveEmpleado)
	REFERENCES Usuario(carnetUsuario)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Horario (
	claveHorario BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	dia CHAR(10) NOT NULL,
	horaInicio TIME NOT NULL,
	horaFin TIME NOT NULL,
	claveMateria INT UNSIGNED NOT NULL,
	claveOportunidad BIGINT UNSIGNED NOT NULL,
	claveGrupo BIGINT UNSIGNED NOT NULL,

	CONSTRAINT claveHorario_PK PRIMARY KEY (claveHorario),

	CONSTRAINT claveMateria_FK FOREIGN KEY (claveMateria)
	REFERENCES Materia(claveMateria)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT claveOportunidad_FK FOREIGN KEY (claveOportunidad)
	REFERENCES Oportunidad(IDOportunidad)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT claveGrupo_FK FOREIGN KEY (claveGrupo)
	REFERENCES Grupo(IDGrupo)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Usuario_Horario (
	carnetAlumno  INT UNSIGNED NOT NULL,
	claveHorario BIGINT UNSIGNED NOT NULL,
	periodo VARCHAR(40) NOT NULL,

	CONSTRAINT claveUsuarioHorario_PK PRIMARY KEY (carnetAlumno, claveHorario),

	CONSTRAINT carnetAlumnoH_FK FOREIGN KEY (carnetAlumno)
	REFERENCES Usuario(carnetUsuario)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT claveHorario_FK FOREIGN KEY (claveHorario)
	REFERENCES Horario(claveHorario)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

INSERT INTO `Carrera` (`claveCarrera`, `nombre`) VALUES
(001, 'CIENCIAS DE LA COMPUTACIÓN');

INSERT INTO `Inscripcion` (`claveInscripcion`, `fechaInscripcion`) VALUES
(1, '2018-04-07 15:30:00'),
(2, '2018-04-07 14:30:00');

INSERT INTO `Materia` (`claveMateria`, `nombre`, `creditos`, `numeroSemestre`, `claveCarrera`) VALUES
(001, 'MATEMÁTICAS I', 1, 1, 1),
(002, 'FUNDAMENTOS DE ELECTROMAGNETISMO', 1, 1, 1),
(003, 'FUNDAMENTOS DE ALGORITMOS', 1, 1, 1),
(004, 'ARQUITECTURA DE COMPUTADORAS', 1, 1, 1),
(005, 'PROGRAMACIÓN ESTRUCTURADA', 1, 1, 1),
(006, 'MATEMÁTICAS II', 1, 2, 1),
(007, 'SISTEMAS ELECTRÓNICOS', 1, 2, 1),
(008, 'FUNDAMENTOS DE REDES', 1, 2, 1),
(009, 'PROGRAMACIÓN ORIENTADA A OBJETOS', 1, 2, 1),
(010, 'FUNDAMENTOS DE ESTADÁSTICA', 1, 2, 1),
(011, 'MATEMÁTICAS DISCRETAS', 1, 3, 1),
(012, 'CIRCUITOS DIGITALES', 1, 3, 1),
(013, 'ESTRUCTURA DE DATOS', 1, 3, 1),
(014, 'ANÁLISIS DE SISTEMAS', 1, 3, 1),
(015, 'TEORÍA DE AUTÁMATAS', 1, 3, 1),
(016, 'ANÁLISIS NUMÉRICO', 1, 3, 1),
(017, 'ADMINISTRACIÓN DE PROYECTOS', 1, 4, 1),
(018, 'SISTEMAS OPERATIVOS', 1, 4, 1),
(019, 'ADMINSTRACIÓN DE REDES', 1, 4, 1),
(020, 'MODELOS ESTADÍSTICOS', 1, 4, 1),
(021, 'SISTEMAS EMBEBIDOS', 1, 4, 1),
(022, 'MINERÍA DE DATOS', 1, 4, 1),
(023, 'SISTEMAS DISTRIBUIDOS', 1, 5, 1),
(024, 'INTELIGENCIA ARTIFICIAL', 1, 5, 1),
(025, 'BIG DATA', 1, 5, 1);
