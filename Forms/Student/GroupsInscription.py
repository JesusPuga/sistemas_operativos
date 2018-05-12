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
        h = 1500
        w = 300
        old_root.destroy()
        self.new_root = centerForm(h,w,"Sistema de Inscripción | Inscripción de grupos")
        self.clave = clave
        self.subject = subject

        #Frames a usar, algo así como div b:
        topFrame = Frame(self.new_root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(self.new_root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        self.tableTreeView = ttk.Treeview(topFrame)
        self.tableTreeView.grid(row=0, column=0)

        self.tableTreeView["columns"]=("Grupo","Aula","Docente","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado")
        self.tableTreeView.column("#0",width=10)
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

    def orderSchedule(self,dia,horario,horaInicio,horaFin):
        if dia == 'LUNES':
            horario['LUNES']= str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'MARTES':
            horario['MARTES'] = str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'MIÉRCOLES':
            horario['MIERCOLES'] = str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'JUEVES':
            horario['JUEVES'] = str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'VIERNES':
            horario['VIERNES'] = str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'SÁBADO':
            horario['SABADO'] = str(horaInicio)  + ' - ' +str(horaFin)

        return horario

    def showAvailableTeachers(self):
        groupsID = []
        groups = loadAvailableGroups(self.subject)
        index = 0
        contador = 0
        """Este primer iterador solo obtiene primeros valores para poder hacer comparaciones posteriores"""
        for grupoClave, aula, docente, dia, horaInicio, horaFin, claveMateria, IDGrupo in groups:
            groupsID.append(IDGrupo)
            break

        """Con este segundo iterador sabremos cuantos grupos existen y su ID"""
        for grupoClave, aula, docente, dia, horaInicio, horaFin, claveMateria, IDGrupo in groups:
            if IDGrupo != groupsID[contador]:
                contador +=1
                groupsID.append(IDGrupo)
        """Con este segundo iterador guardaremos los datos de los n grupos"""
        contador=0
        lastIDGroup = 0
        horario = {'GRUPO':'','AULA':'','DOCENTE':'','LUNES':'', 'MARTES':'','MIERCOLES':'', 'JUEVES':'', 'VIERNES':'', 'SABADO':''}
        for grupoClave, aula, docente, dia, horaInicio, horaFin, claveMateria, IDGrupo in groups:
            if IDGrupo != groupsID[contador]:
                self.tableTreeView.insert('','0',index,text=IDGrupo,values=(horario['GRUPO'],horario['AULA'], horario['DOCENTE'],horario['LUNES'],horario['MARTES'],horario['MIERCOLES'],horario['JUEVES'],horario['VIERNES'],horario['SABADO']))
                contador +=1
                index +=1
                horario = {'GRUPO':'','AULA':'','DOCENTE':'','LUNES':'', 'MARTES':'','MIERCOLES':'', 'JUEVES':'', 'VIERNES':'', 'SABADO':''}
                horario['GRUPO']= grupoClave
                horario = self.orderSchedule(dia,horario,horaInicio,horaFin)
            elif IDGrupo == groupsID[contador]:
                horario['GRUPO']= grupoClave
                horario['AULA']=aula
                horario['DOCENTE']=docente
                horario = self.orderSchedule(dia,horario,horaInicio,horaFin)
                lastIDGroup  = IDGrupo

        self.tableTreeView.insert('','0',index,text=lastIDGroup,values=(horario['GRUPO'],horario['AULA'], horario['DOCENTE'],horario['LUNES'],horario['MARTES'],horario['MIERCOLES'],horario['JUEVES'],horario['VIERNES'],horario['SABADO']))

    def returnInscription(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Student.Inscription',None,None,['Inscription'], 0)
        self.app = window.Inscription(self.new_root, self.clave)
