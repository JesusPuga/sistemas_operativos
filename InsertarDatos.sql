##Datos RANDOM para crear validaciones

INSERT INTO `Oportunidad` (`IDOportunidad`, `calificacion`, `numOportunidad`) VALUES
(1, 100, 1),
(2, 50, 1);

INSERT INTO `Usuario` (`carnetUsuario`, `sexo`,`telefono`,`contrasenia`,`nombre`,`apellidoPaterno`,`apellidoMaterno`,`tipoUsuario`,`claveCarrera`,`claveInscripcion`) VALUES
(1, 'M', '83918207','password',"User","userAppelidoP", "userAppelidoM",1,1,1),
(2, 'F', '83918208','password',"User","userAppelidoP", "userAppelidoM",2,1,1),
(3, 'M', '83918209','password',"User","userAppelidoP", "userAppelidoM",3,1,1);

INSERT INTO `Alumno` (`carnetAlumno`, `estatus`) VALUES
(1, 'estatus1'),
(2, 'estatus2');


INSERT INTO `Empleado` (`carnetEmpleado`, `tipoEmpleado`) VALUES
(1, 'Administrativo'),
(2, 'Docente');

INSERT INTO `Grupo` (`IDGrupo`, `claveGrupo`,`aula`,`carnetEmpleado`,`contador`,`claveEmpleado`) VALUES
(1, 1, 1, 1, 1, 1),
(2, 1, 1, 1, 1, 1);

INSERT INTO `Horario` (`claveHorario`, `dia`,`horaInicio`,`horaFin`,`claveMateria`,`claveOportunidad`,`claveGrupo`) VALUES
(1, 1, '15:30:00', '16:30:00', 1, 1, 1),
(2, 1, '17:30:00', '18:30:00', 1, 1, 1);
