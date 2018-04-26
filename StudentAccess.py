import sys
from Inscription import *
from EraseSubject import *
from StudentSchedule import *
from Validaciones import *
from Acceso import *
from tkinter import *
from tkinter import ttk

class StudentAccess:
    def __init__(self, root, clave):
        self.root = root
        self.clave = clave
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Alumno")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        leftFrame = Frame(root, width=100, height=100)
        leftFrame.grid(row=0,column=0)

        closeSessionFrame = Frame(root,  bg='gray2',)
        closeSessionFrame.grid(row=1,column=0)

        rightFrame = Frame(root, bg='lavender', width=400, height=300)
        rightFrame.grid(row=0,column=1)

        #REVISAR ESTATUS DE ALUMNO
        query= """SELECT Alumno.estatus FROM Alumno WHERE Alumno.carnetAlumno = %s"""
        result = con.execute_query(query,(clave,),True)

        #CAPTURA DEL CONTENIDO DE LA CONSULTA. SE GUARDA EL ESTATUS DEL ALUMNO ("PRIMER INGRESO", "REINGRESO", "NO INSCRITO")"
        for x in result: estatus=x[0]

        #Botones
        if estatus == 'PRIMER INGRESO':
            inscriptionButton = Button(leftFrame, text="Inscribir", state=DISABLED, command= self.openInscription)
            inscriptionButton.grid(row = 1, column = 0)
            scheduleButton = Button(leftFrame, text="Horario", command= self.openSchedule)
            scheduleButton.grid(row = 2, column = 0)
            sessionButton = Button(leftFrame, text="Cerrar Sesión", command= self.quit)
            sessionButton.grid(row = 3, column = 0)
        elif estatus == 'REINGRESO':
            inscriptionButton = Button(leftFrame, text="Inscribir", command= self.openInscription)
            inscriptionButton.grid(row = 1, column = 0)
            scheduleButton = Button(leftFrame, text="Horario", command= self.openSchedule)
            scheduleButton.grid(row = 2, column = 0)
            sessionButton = Button(leftFrame, text="Cerrar Sesión", command= self.quit)
            sessionButton.grid(row = 3, column = 0)


    def quit(self):
        ##Add validations to return or close and open the other window
        self.app = Access(Tk())
        self.root.destroy()

    def openInscription(self):
        self.app = Inscription(Tk(),self.clave)
        self.root.destroy()

    def openSchedule(self):
        self.app = StudentSchedule(Tk())
        self.root.destroy()
