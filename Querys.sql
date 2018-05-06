DELIMITER $$
CREATE PROCEDURE borradoGrupo(IN carnetAlumno INT, IN claveGrupo BIGINT, IN claveMateria INT)
BEGIN
      DELETE FROM Alumno_Grupo WHERE Alumno_Grupo.claveGrupo = claveGrupo AND Alumno_Grupo.carnetAlumno = carnetAlumno;
      BEGIN
        DECLARE numeroOportunidad INT;
        SET numeroOportunidad = (SELECT Oportunidad.IDOportunidad FROM Oportunidad WHERE Oportunidad.claveMateria = claveMateria AND Oportunidad.carnetAlumno = carnetAlumno ORDER BY Oportunidad.numOportunidad DESC LIMIT 1);

        DELETE FROM Oportunidad WHERE Oportunidad.claveMateria = claveMateria AND Oportunidad.numOportunidad = numeroOportunidad AND Oportunidad.carnetAlumno = carnetAlumno;
      END;
      BEGIN
        UPDATE Grupo SET contador = contador - 1 WHERE Grupo.IDGrupo = claveGrupo;
      END;
  END$$
DELIMITER ;



SELECT Materia.claveMateria, Grupo.claveGrupo, Materia.nombre,CONCAT(Usuario.nombre,' ',Usuario.apellidoPaterno) AS Nombre, Dia.dia, Horario.horaInicio, Horario.horaFin
FROM Materia
INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND Grupo.periodo = "180116"
INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo
INNER JOIN Alumno ON Alumno.carnetAlumno = Alumno_Grupo.carnetAlumno
INNER JOIN Usuario ON Usuario.carnetUsuario = Grupo.carnetEmpleado
INNER JOIN Horario ON Horario.claveGrupo = Alumno_Grupo.claveGrupo
INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario
INNER JOIN Dia ON Dia.IDDia = Dia_Horario.IDDia
WHERE Alumno.carnetAlumno = 2


SELECT  CONCAT(H.horaInicio,' - ',H.horaFin) Hora,
        MAX(CASE WHEN H.dia = 'Lunes' THEN H.nombre ELSE '' END) Lunes,
        MAX(CASE WHEN H.dia = 'Martes' THEN H.nombre ELSE '' END) Martes,
        MAX(CASE WHEN H.dia = 'Miercoles' THEN H.nombre ELSE '' END) Miercoles,
        MAX(CASE WHEN H.dia = 'Jueves' THEN H.nombre ELSE '' END) Jueves,
        MAX(CASE WHEN H.dia = 'Viernes' THEN H.nombre ELSE '' END) Viernes,
        MAX(CASE WHEN H.dia = 'Sabado' THEN H.nombre ELSE '' END) Sabado
FROM (SELECT Materia.claveMateria, Grupo.claveGrupo, Materia.nombre,CONCAT(Usuario.nombre,' ',Usuario.apellidoPaterno) AS Docente, Dia.dia, Horario.horaInicio, Horario.horaFin
        FROM Materia
        INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND Grupo.periodo = "180116"
        INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo
        INNER JOIN Alumno ON Alumno.carnetAlumno = Alumno_Grupo.carnetAlumno
        INNER JOIN Usuario ON Usuario.carnetUsuario = Grupo.carnetEmpleado
        INNER JOIN Horario ON Horario.claveGrupo = Alumno_Grupo.claveGrupo
        INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario
        INNER JOIN Dia ON Dia.IDDia = Dia_Horario.IDDia
        WHERE Alumno.carnetAlumno = 2) AS H
GROUP BY CONCAT(Horario.horaInicio,' - ',Horario.horaFin)
ORDER BY CONCAT(Horario.horaInicio,' - ',Horario.horaFin) ASC
