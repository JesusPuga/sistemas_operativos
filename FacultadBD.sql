CREATE TABLE Inscripcion (
	claveInscripcion BIGINT UNSIGNED AUTO_INCREMENT,
	fechaInscripcion TIMESTAMP,

	CONSTRAINT claveInscripcion_PK PRIMARY KEY (claveInscripcion)
);

CREATE TABLE Carrera (
	claveCarrera INT UNSIGNED NOT NULL AUTO_INCREMENT,
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
	claveCarrera INT UNSIGNED  NOT NULL,
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
	claveMateria INT UNSIGNED  NOT NULL AUTO_INCREMENT,
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
	claveMateria INT UNSIGNED  NOT NULL,

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
	claveGrupo TINYINT ,
	aula INT,
	capacidad TINYINT,
	contador TINYINT,
	periodo DATE,
	carnetEmpleado INT UNSIGNED NOT NULL,
	claveMateria INT UNSIGNED  NOT NULL,

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
	horaInicio TIME NOT NULL,
	horaFin TIME NOT NULL,
	claveGrupo BIGINT UNSIGNED NOT NULL,

	CONSTRAINT Horario_PK PRIMARY KEY (IDHorario),

	CONSTRAINT claveGrupo_FK FOREIGN KEY (claveGrupo)
	REFERENCES Grupo(IDGrupo)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE Dia (
	IDDia TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
	dia CHAR(10) NOT NULL,

	CONSTRAINT IDDia_PK PRIMARY KEY (IDDia)
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

CREATE TABLE Dia_Horario (
	IDDia  TINYINT UNSIGNED NOT NULL,
	IDHorario BIGINT UNSIGNED NOT NULL,

	CONSTRAINT claveAlumnoGrupo_PK PRIMARY KEY (IDDia, IDHorario),

	CONSTRAINT IDDiaRel_FK FOREIGN KEY (IDDIa)
	REFERENCES Dia(IDDia)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT IDHorarioRel_FK FOREIGN KEY (IDHorario)
	REFERENCES Horario(IDHorario)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

/*CREACIÓN DE LOS DÍAS*/
INSERT INTO Dia (dia) VALUES
('LUNES'),
('MARTES'),
('MIÉRCOLES'),
('JUEVES'),
('VIERNES'),
('SÁBADO');

/* CREACIÓN DE LA CARRERA */
INSERT INTO Carrera (claveCarrera, nombre) VALUES
(001, 'CIENCIAS DE LA COMPUTACIÓN');

 /* CREACIÓN DE LA MATERIAS PARA LA CARRERA DE CIENCIAS DE LA COMPUTACIÓN*/
INSERT INTO Materia (claveMateria, nombre, creditos, semestre, claveCarrera) VALUES
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

 /*MATERIAS SERIADAS*/
INSERT INTO Materia_Seriada (claveMateria, claveMateriaSeriada) VALUES
(1, 6),
(2, 7),
(5, 10);

/* CREACIÓN DE ALUMNOS (EJEMPLO)*/
INSERT INTO Inscripcion (claveInscripcion, fechaInscripcion) VALUES
(1, '2018-04-07 15:30:00'),
(2, '2018-04-07 14:30:00');

INSERT INTO Usuario (carnetUsuario, sexo, telefono, contrasenia, nombre, apellidoPaterno, apellidoMaterno, tipoUsuario) VALUES
(001, 'H', 5512345678, 'unodostres', 'Francisco', 'Gutierrez', 'Quinza', 1),
(002, 'H', 7772345678, 123, 'Jose', 'Martinez', 'Diaz', 1),
(003, 'M', 7572345678, 'unotres', 'Angelica', 'Lopez', 'Garza', 1);

INSERT INTO Alumno (carnetAlumno, estatus, claveCarrera, claveInscripcion) VALUES
(1, 'Estudiando',1,1),
(2, 'Estudiando',1,2),
(3, 'Estudiando',1,1);

/*CREACIÓN DE EMPLEADOS (EJEMPLO)*/
INSERT INTO Usuario (carnetUsuario, sexo, telefono, contrasenia, nombre, apellidoPaterno, apellidoMaterno, tipoUsuario) VALUES
(004, 'H', 7752345678, 'contra', 'Noe', 'Espinoza', 'Perez', 2),
(005, 'M', 7372345678, 'senia', 'Aracely', 'Gomez', 'Trujillo', 2);

INSERT INTO Empleado (carnetEmpleado, tipoEmpleado) VALUES
(4, 'Docente'),
(5, 'Administrativo');

/* CREACIÓN DE LOS GRUPOS*/

/*PRIMER SEMESTRE*/

/*GRUPOS*/
INSERT INTO Grupo (claveGrupo, aula, capacidad, contador, periodo, carnetEmpleado, claveMateria) VALUES
(01,104,1,0,'180116',4,1),	/*MATEMÁTICAS I*/
(01,104,1,0,'180116',4,2),	/*FUNDAMENTOS	DE ELECTROMAGNETISMO*/
(01,104,1,0,'180116',4,3),	/*FUNDAMENTOS DE ALGORITMOS*/
(01,104,1,0,'180116',4,4),	/*ARQUITECTURA DE COMPUTADORAS*/
(01,104,1,0,'180116',4,5);	/*PROGRAMACIÓN ESTRUCTURADA*/

INSERT INTO Horario (horaInicio, horaFin, claveGrupo) VALUES
(150000,160000,1),	/*MATEMÁTICAS I*/
(180000,190000,2),	/*FUNDAMENTOS DE ELECTROMAGNETISMO*/
(160000,170000,3),	/*FUNDAMENTOS DE COMPUTADORAS*/
(160000,180000,4),	/*ARQUITECTURA DE COMPUTADORAS*/
(170000,180000,5);	/*PROGRAMACIÓN ESTRUCTURADA*/

INSERT INTO Dia_Horario(IDDIa, IDHorario) VALUES
/*MATEMÁTICAS I*/
(1,1),
(3,1),
(4,1),
(5,1),
 /*FUNDAMENTOS DE ELECTROMAGNETISMO*/
(1,2),
(3,2),
(4,2),
(5,2),
/*FUNDAMENTOS DE ALGORITMOS*/
(1,3),
(3,3),
(5,3),
/*ARQUITECTURA DE COMPUTADORAS*/
(2,4),
(4,4),
/*PROGRAMACIÓN ESTRUCTURADA*/
(1,5),
(3,5),
(5,5);

/*SEGUNDO SEMESTRE*/
/*GRUPOS*/
INSERT INTO Grupo (claveGrupo, aula, capacidad, contador, periodo, carnetEmpleado, claveMateria) VALUES
(01,409,1,0,'180116',4,6),
(01,408,1,0,'180116',4,7),
(01,409,1,0,'180116',4,8),
(01,409,1,0,'180116',4,9),
(01,411,1,0,'180116',4,10),
(01,409,1,0,'180116',4,11),
(02,407,1,0,'180116',4,6),
(02,407,1,0,'180116',4,8),
(02,407,1,0,'180116',4,11);

INSERT INTO Horario (horaInicio, horaFin, claveGrupo) VALUES
(170000,180000,6),	/*MATEMÁTICAS II*/
(150000,180000,7),	/*SISTEMAS ELECTRÓNICOS*/
(160000,170000,8),	/*FUNDAMENTOS DE REDES*/
(140000,150000,9),	/*BASES DE DATOS*/
(180000,210000,10),	/*PROGRAMACIÓN ORIENTADA A OBJETOS*/
(110000,120000,11),	/*MATEMÁTICAS II*/
(70000,100000,12),	/*FUNDAMENTOS DE REDES*/
(150000,180000,13);	/*FUNDAMENTOS DE ESTADÁSTICA*/


INSERT INTO Dia_Horario(IDDIa, IDHorario) VALUES
/*MATEMÁTICAS II*/
(1,6),
(3,6),
(5,6),
/*SISTEMAS ELECTRÓNICOS*/
(4,7),
/*FUNDAMENTOS DE REDES*/
(1,8),
(3,8),
(5,8),
/*BASES DE DATOS*/
(1,9),
(2,9),
(3,9),
(4,9),
(5,9),
/*PROGRAMACIÓN ORIENTADA A OBJETOS*/
(1,10),
/*MATEMÁTICAS II*/
(1,11),
(3,11),
(5,11),
/*FUNDAMENTOS DE REDES*/
(6,12),
/*FUNDAMENTOS DE ESTADÁSTICA*/
(2,13);

/*AÑADIENDO ALUMNOS A MATERIAS */
/*NOTA: SI SE AÑADE UNA OPORTUNIDAD SE DEBE AGREGAR EN LA RELACION ALUMNO_GRUPO*/
INSERT INTO `Alumno_Grupo` (`claveGrupo`, `carnetAlumno`) VALUES
(1, 1),
(1, 2),
(2, 1);

INSERT INTO Oportunidad (IDOportunidad, calificacion, numOportunidad, carnetAlumno, claveMateria) VALUES
(1, 69, 1, 1, 0000000001),
(2, 80, 1, 1, 0000000002),
(3, 80, 1, 2, 0000000001);
