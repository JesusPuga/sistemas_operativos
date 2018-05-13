import sys
from Validations.loadStudents import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class StudentAccess:
    def __init__(self, old_root, clave):
        h = 300
        w = 500
        old_root.destroy()
        self.new_root = centerForm(w,h,"Sistema de Inscripción | Alumno")
        self.clave = clave

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
            inscriptionButton = Button(leftFrame, text="Inscribir", state=DISABLED, command= self.openInscription,height=1,width=4)
            deleteButton = Button(leftFrame, text="Eliminar", state=DISABLED, command= self.openDeleteSubject,height=1,width=4)

        elif estatus == 'REINGRESO':
            inscriptionButton = Button(leftFrame, text="Inscribir", command= self.openInscription,height=1,width=4)
            deleteButton = Button(leftFrame, text="Eliminar", command= self.openDeleteSubject,height=1,width=4)


        inscriptionButton.grid(row = 1, column = 0,pady=(10,0))
        deleteButton.grid(row = 2, column = 0,pady=(10,0))
        scheduleButton = Button(leftFrame, text="Horario", command= self.openSchedule,height=1,width=4)
        scheduleButton.grid(row = 3, column = 0,pady=(10,100))
        sessionButton = Button(leftFrame, text="Cerrar Sesión", command= self.quit,height=1,width=8)
        sessionButton.grid(row = 4, column = 0,pady=(10,10), padx=(10,10))


    def quit(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Access',None,None,['Access'], 0)
        self.app = window.Access(self.new_root)

    def openDeleteSubject(self):
        window = __import__('Forms.Student.EraseSubject',None,None,['EraseSubject'], 0)
        self.app = window.EraseSubject(self.new_root,self.clave)

    def openInscription(self):
        window = __import__('Forms.Student.Inscription',None,None,['Inscription'], 0)
        self.app = window.Inscription(self.new_root,self.clave)

    def openSchedule(self):
        window = __import__('Forms.Student.StudentSchedule',None,None,['StudentSchedule'], 0)
        self.app = window.StudentSchedule(self.new_root,self.clave)
