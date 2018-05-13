import sys
from Forms.Student.Inscription import *
from Validations.loadSubjects import *
from Validations.addSubjectToSchedule import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class GroupsInscription:
    def __init__(self, old_root,clave, subject):
        h = 300
        w = 1300
        old_root.destroy()
        self.new_root = centerForm(w,h,"Sistema de Inscripción | Inscripción de grupos")
        self.clave = clave
        self.subject = subject

        #Frames a usar, algo así como div b:
        topFrame = Frame(self.new_root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(self.new_root, width=500, height=100)
        bottomFrame.grid(row=1,column=0,sticky=E,padx=(0,40))

        self.tableTreeView = ttk.Treeview(topFrame)
        self.tableTreeView.grid(row=0, column=0,padx=(40,40),pady=(30,15))

        self.tableTreeView["columns"]=("Grupo","Aula","Docente","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado")
        self.tableTreeView.column("#0",width=10)
        self.tableTreeView.column("Grupo",width=50)
        self.tableTreeView.column("Aula",width=50)
        self.tableTreeView.column("Docente",width=200)
        self.tableTreeView.column("Lunes",width=150)
        self.tableTreeView.column("Martes",width=150)
        self.tableTreeView.column("Miércoles",width=150)
        self.tableTreeView.column("Jueves",width=150)
        self.tableTreeView.column("Viernes",width=150)
        self.tableTreeView.column("Sábado",width=150)

        self.tableTreeView.heading('#0',text='')
        self.tableTreeView.heading('Grupo', text='Grupo')
        self.tableTreeView.heading('Aula', text='Aula')
        self.tableTreeView.heading('Docente', text='Docente')
        self.tableTreeView.heading('Lunes', text='Lunes')
        self.tableTreeView.heading('Martes', text='Martes')
        self.tableTreeView.heading('Miércoles', text='Miércoles')
        self.tableTreeView.heading('Jueves', text='Jueves')
        self.tableTreeView.heading('Viernes', text='Viernes')
        self.tableTreeView.heading('Sábado', text='Sábado')

        # Función para el double clic
        self.tableTreeView.bind("<Double-1>", self.onDoubleClick)

        returnButton = Button(bottomFrame, text="Regresar", command=self.returnInscription)
        returnButton.grid(row = 1, column = 3)

        ##carga información
        self.showAvailableTeachers()
        self.new_root.mainloop()

    def onDoubleClick(self, event):
        groupClave = self.tableTreeView.item(self.tableTreeView.focus())["values"][0]
        groupId = self.tableTreeView.item(self.tableTreeView.focus())["text"]
        message = addSubjectToSchedule(self.clave, groupId, groupClave, self.subject)
        messagebox.showinfo("Aviso",message)

        if not ("Horario empalmado " in message or "grupo lleno" in message):
            self.returnInscription()

    def showAvailableTeachers(self):
        subjects = loadAvailableGroups(self.subject)

        for idGrupo, claveGrupo, aula, docente, lunes, martes, miercoles, jueves, viernes, sabado in subjects:
            self.tableTreeView.insert('','0',idGrupo,text=idGrupo,values=(claveGrupo, aula, docente, lunes, martes, miercoles, jueves, viernes, sabado))


    def returnInscription(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Student.Inscription',None,None,['Inscription'], 0)
        self.app = window.Inscription(self.new_root, self.clave)
