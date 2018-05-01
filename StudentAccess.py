import sys
from Validaciones import *
from Acceso import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class StudentAccess:
    def __init__(self, old_root, clave):
        old_root.destroy()
        self.new_root = Tk()
        self.clave = clave
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        self.new_root.title("Sistema de Inscripción | Alumno")
        self.new_root.geometry('{}x{}'.format(500, 300))
        self.new_root.resizable(0,0)
        # layout all of the main containers
        self.new_root.grid_rowconfigure(1, weight=1)
        self.new_root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        leftFrame = Frame(self.new_root, width=100, height=100)
        leftFrame.grid(row=0,column=0)

        closeSessionFrame = Frame(self.new_root,  bg='gray2',)
        closeSessionFrame.grid(row=1,column=0)

        rightFrame = Frame(self.new_root, bg='lavender', width=400, height=300)
        rightFrame.grid(row=0,column=1)

        estatus =  loadStudentStatus(clave)

        #Botones
        if estatus == 'PRIMER INGRESO':
            inscriptionButton = Button(leftFrame, text="Inscribir", state=DISABLED, command= self.openInscription)
        elif estatus == 'REINGRESO':
            inscriptionButton = Button(leftFrame, text="Inscribir", command= self.openInscription)

        inscriptionButton.grid(row = 1, column = 0)
        scheduleButton = Button(leftFrame, text="Horario", command= self.openSchedule)
        scheduleButton.grid(row = 2, column = 0)
        sessionButton = Button(leftFrame, text="Cerrar Sesión", command= self.quit)
        sessionButton.grid(row = 3, column = 0)


    def quit(self):
        ##Add validations to return or close and open the other window
        window = __import__('Acceso')
        self.app = window.Access(self.new_root)

    def openInscription(self):
        window = __import__('Inscription')
        self.app = window.Inscription(self.new_root,self.clave)

    def openSchedule(self):
        window = __import__('StudentSchedule')
        self.app = window.StudentSchedule(self.new_root,self.clave)
