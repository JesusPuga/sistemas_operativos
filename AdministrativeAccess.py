from Validaciones import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeAccess:
    def __init__(self, root,clave):
        self.root = root
        self.clave = clave
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
        scheduleButton = Button(leftFrame, text="Horario", command=self.openSchedule)
        scheduleButton.grid(row = 2, column = 0)
        subjectButton = Button(leftFrame, text="Materias", command=self.openSubjects)
        subjectButton.grid(row = 1, column = 0)
        sessionButton = Button(leftFrame, text="Cerrar Sesión", command=self.closeSession)
        sessionButton.grid(row = 3, column = 0)

    def closeSession(self):
        ##Add validations to return or close and open the other window
        window = __import__('Acceso')
        self.app = window.Access(Tk())
        self.root.destroy()

    def openSubjects(self):
        window = __import__('AdministrativeSubject')
        self.app = window.AdministrativeSubject(Tk(),self.clave)
        self.root.destroy()

    def openSchedule(self):
        window = __import__('AdministrativeSchedule')
        self.app = window.AdministrativeSchedule(Tk(),self.clave)
        self.root.destroy()
