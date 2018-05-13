DELIMITER $$
CREATE PROCEDURE borradoGrupo(IN carnetAlumno INT, IN claveGrupo BIGINT, IN claveMateria INT)
BEGIN
      DELETE FROM Alumno_Grupo WHERE Alumno_Grupo.claveGrupo = claveGrupo AND Alumno_Grupo.carnetAlumno = carnetAlumno;
      BEGIN
        DECLARE numeroOportunidad INT;
        SET numeroOportunidad = (SELECT Oportunidad.IDOportunidad FROM Oportunidad WHERE Oportunidad.claveMateria = claveMateria AND Oportunidad.carnetAlumno = carnetAlumno ORDER BY Oportunidad.numOportunidad DESC LIMIT 1);

        DELETE FROM Oportunidad WHERE Oportunidad.IDOportunidad = numeroOportunidad;
      END;
      BEGIN
        UPDATE Grupo SET contador = contador - 1 WHERE Grupo.IDGrupo = claveGrupo;
      END;
  END$$
DELIMITER ;
