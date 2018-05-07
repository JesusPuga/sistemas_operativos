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
