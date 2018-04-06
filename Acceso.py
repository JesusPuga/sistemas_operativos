import sys
import tkinter
from tkinter import *
from tkinter import ttk

class Access:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Acceso")
        root.resizable(0,0)


        frame = Frame(root, width=500, heigh=300)
        frame.grid(row=0,column=0, padx=(150,150), pady=(150,100))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0,weight=1)


        """ CREACIÓN DEL FORMULARIO DE ACCESO"""

        #Campo Tipo Usuario
        tipoUsuarioLBL = Label(frame, text="Tipo de Usuario:")
        tipoUsuarioLBL.grid(row=0, column=0, sticky="e", padx=5, pady=5)

        tipoUsuarioCBX = ttk.Combobox(frame)
        tipoUsuarioCBX.grid(row=0, column=1, sticky="e", padx=5, pady=5)
        tipoUsuarioCBX["values"] = ["Alumno", "Docente", "Administrativo"]

        #Campo Usuario
        usuarioLB = Label(frame, text="Usuario:")
        usuarioLB.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        usuarioENY = Entry(frame)
        usuarioENY.grid(row=1, column=1, sticky="e", padx=5, pady=5)

        #Campo Contraseña
        contraseniaLB = Label(frame, text="Contraseña:")
        contraseniaLB.grid(row=2, column=0, sticky="e", padx=5, pady=5)

        contraseniaENY = Entry(frame)
        contraseniaENY.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        contraseniaENY.config(show="*")

        #Botón Ingresar
        Button(root, text="Ingresar")

class StudentAccess:
    def __init__(self, root):
        self.root = root
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

        #Botones
        inscriptionButton = Button(leftFrame, text="Ingresar")
        inscriptionButton.grid(row = 1, column = 0)
        scheduleButton = Button(leftFrame, text="Horario")
        scheduleButton.grid(row = 2, column = 0)
        sessionButton = Button(leftFrame, text="Sesión")
        sessionButton.grid(row = 3, column = 0)

class AdministrativeAccess:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Administrativo")
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

        #Botones
        scheduleButton = Button(leftFrame, text="Horario")
        scheduleButton.grid(row = 2, column = 0)
        subjectButton = Button(leftFrame, text="Materias")
        subjectButton.grid(row = 1, column = 0)
        sessionButton = Button(leftFrame, text="Sesión")
        sessionButton.grid(row = 3, column = 0)

class Inscription:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Inscripción")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root, bg='lavender', width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        subjectListENY = Entry(topFrame)
        subjectListENY.grid(row=0, column=0)
        #selección
        subjectCveLB = Label(bottomFrame, text="Clave de materia:")
        subjectCveLB.grid(row=0, column=0)
        subjectCveENY = Entry(bottomFrame)
        subjectCveENY.grid(row=0, column=1)

        #Botones
        selectButton = Button(bottomFrame, text="Seleccionar")
        selectButton.grid(row = 0, column = 2)
        returnButton = Button(bottomFrame, text="Regresar")
        returnButton.grid(row = 1, column = 3)

class GroupsInscription:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Inscripción de grupos")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root, bg='lavender', width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        subjectListENY = Entry(topFrame)
        subjectListENY.grid(row=0, column=0)
        #selección
        subjectCveLB = Label(bottomFrame, text="Grupo:")
        subjectCveLB.grid(row=0, column=0)
        subjectCveENY = Entry(bottomFrame)
        subjectCveENY.grid(row=0, column=1)

        #Botones
        selectButton = Button(bottomFrame, text="Inscribir")
        selectButton.grid(row = 0, column = 2)
        returnButton = Button(bottomFrame, text="Regresar")
        returnButton.grid(row = 1, column = 3)


if __name__ == '__main__':
    """ CREACIÓN DE LA VENTANA DE ACCESO AL SISTEMA"""

    #Declara ventana de aplicación
    root = Tk()

    aplicacion = GroupsInscription(root)# prueba de nueva ventana

    #Bucle de la aplicación
    root.mainloop()
