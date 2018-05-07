import sys
from Validations.loadStudents import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class StudentSchedule:
    def __init__(self, old_root,clave):
        old_root.destroy()
        self.new_root = Tk()
        self.clave = clave
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        self.new_root.title("Horario")
        self.new_root.geometry('{}x{}'.format(1300, 600))
        self.new_root.resizable(0,0)
        # layout all of the main containers
        self.new_root.grid_rowconfigure(1, weight=1)
        self.new_root.grid_columnconfigure(0, weight=1)


        #Frames a usar, algo así como div b:
        topFrame = Frame(self.new_root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(self.new_root,width=500, height=100)
        bottomFrame.grid(row=1,column=0)
        #primer tabla
        style = ttk.Style(self.new_root)
        style.configure('Treeview', rowheight=50)
        self.tbTopTreeView = ttk.Treeview(topFrame, height=5)
        self.tbTopTreeView.grid(row=0, column=0)

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
        self.tbBottomTreeView.grid(row=1, column=0)

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
