import sys
from Validations.loadStudents import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class StudentSchedule:
    def __init__(self, old_root,clave):
        h = 600
        w = 1300
        old_root.destroy()
        self.new_root = centerForm(w,h,"Horario")
        self.clave = clave

        #Frames a usar, algo así como div b:
        topFrame = Frame(self.new_root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(self.new_root,width=500, height=100)
        bottomFrame.grid(row=1,column=0,sticky=E,padx=(0,50))
        #primer tabla
        style = ttk.Style(self.new_root)
        style.configure('Treeview', rowheight=50)
        self.tbTopTreeView = ttk.Treeview(topFrame, height=5)
        self.tbTopTreeView.grid(row=0, column=0,padx=(50,50),pady=(10,10))

        self.tbTopTreeView["columns"]=("Lunes","Martes","Miércoles","Jueves","Viernes","Sabado")
        self.tbTopTreeView.column("#0",width=170)
        self.tbTopTreeView.column("Martes",width=170)
        self.tbTopTreeView.column("Miércoles",width=170)
        self.tbTopTreeView.column("Jueves",width=170)
        self.tbTopTreeView.column("Viernes",width=170)
        self.tbTopTreeView.column("Sabado",width=170)

        self.tbTopTreeView.heading('#0',text='Hora')
        self.tbTopTreeView.heading('Lunes', text='Lunes')
        self.tbTopTreeView.heading('Martes', text='Martes')
        self.tbTopTreeView.heading('Miércoles', text='Miércoles')
        self.tbTopTreeView.heading('Jueves', text='Jueves')
        self.tbTopTreeView.heading('Viernes', text='Viernes')
        self.tbTopTreeView.heading('Sabado', text='Sábado')

        #segunda tabla
        self.tbBottomTreeView = ttk.Treeview(topFrame,height=5)
        self.tbBottomTreeView.grid(row=1, column=0,padx=(318,318),pady=(0,10))

        self.tbBottomTreeView["columns"]=("Grupo","Materia","Docente")
        self.tbBottomTreeView.column("#0",width=166)
        self.tbBottomTreeView.column("Grupo",width=166)
        self.tbBottomTreeView.column("Materia",width=166)
        self.tbBottomTreeView.column("Docente",width=166)

        self.tbBottomTreeView.heading('#0',text='Clave')
        self.tbBottomTreeView.heading('Grupo', text='Grupo')
        self.tbBottomTreeView.heading('Materia', text='Materia')
        self.tbBottomTreeView.heading('Docente', text='Docente')

        #Botones
        returnButton = Button(bottomFrame, text="Regresar", command= self.returnStudentHome)
        returnButton.grid(row = 1, column = 3)

        self.showStudentSchedule()
        self.new_root.mainloop()

    def showStudentSchedule(self):
        schedule = loadStudentSchedule(self.clave)
        subjects = loadAllStudentSubjects(self.clave)
        cont = 0

        for hour, monday, tuesday, whednesnday, thursdar, firday, saturday in schedule:
            self.tbTopTreeView.insert('','0',cont,text=hour,values=(monday, tuesday, whednesnday, thursdar, firday, saturday))
            cont += 1

        cont = 0
        for subject, groupClave, groupName, teacherName in subjects:
            self.tbBottomTreeView.insert('','0',cont,text=subject,values=(groupClave, groupName,teacherName))
            cont += 1

    def returnStudentHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Student.StudentAccess',None,None,['StudentAccess'], 0)
        self.app = window.StudentAccess(self.new_root,self.clave)
