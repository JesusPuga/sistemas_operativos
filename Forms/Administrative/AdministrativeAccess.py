from Validations.userValidations import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeAccess:
    def __init__(self, old_root,clave):
        w = 500
        h = 300
        old_root.destroy()
        self.new_root = centerForm(w,h,"Sistema de Inscripción | Administrativo")
        self.clave = clave

        #Frames a usar, algo así como div b:
        leftFrame = Frame(self.new_root, width=100, height=100)
        leftFrame.grid(row=0,column=0)

        closeSessionFrame = Frame(self.new_root,  bg='gray2')
        closeSessionFrame.grid(row=1,column=0)

        rightFrame = Frame(self.new_root, bg='lavender', width=400, height=300)
        rightFrame.grid(row=0,column=1)

        #Botones
        scheduleButton = Button(leftFrame, text="Horario", command=self.openSchedule,height=1,width=4)
        scheduleButton.grid(row = 2, column = 0,pady=(10,10))
        subjectButton = Button(leftFrame, text="Materias", command=self.openSubjects,height=1,width=4)
        subjectButton.grid(row = 1, column = 0,pady=(10,0))
        insertButton = Button(leftFrame, text="Insertar\nAlumno", command=self.openAddStudent,height=2,width=4)
        insertButton.grid(row = 3, column = 0,pady=(10,100))
        sessionButton = Button(leftFrame, text="Cerrar Sesión", command=self.closeSession,height=1,width=8)
        sessionButton.grid(row = 4, column = 0,pady=(10,10), padx=(10,10))

        self.new_root.mainloop()

    def closeSession(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Access',None,None,['Access'], 0)
        self.app = window.Access(self.new_root)

    def openSubjects(self):
        window = __import__('Forms.Administrative.AdministrativeSubject',None,None,['AdministrativeSubject'], 0)
        self.app = window.AdministrativeSubject(self.new_root,self.clave)

    def openSchedule(self):
        window = __import__('Forms.Administrative.AdministrativeSchedule',None,None,['AdministrativeSchedule'], 0)
        self.app = window.AdministrativeSchedule(self.new_root,self.clave)

    def openAddStudent(self):
        window = __import__('Forms.Administrative.AdministrativeAddStudent',None,None,['AdministrativeAddStudent'], 0)
        self.app = window.AdministrativeAddStudent(self.new_root,self.clave)
