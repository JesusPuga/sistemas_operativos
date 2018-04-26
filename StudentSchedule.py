import sys
from StudentAccess import *
from Validaciones import *
from tkinter import *
from tkinter import ttk

class StudentSchedule:
    def __init__(self, root,clave):
        self.root = root
        self.clave = clave
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Horario")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root,width=500, height=100)
        bottomFrame.grid(row=1,column=0)
        #primer tabla
        tbTopTreeView = ttk.Treeview(topFrame, height=5)
        tbTopTreeView.grid(row=0, column=0)

        tbTopTreeView["columns"]=("Martes","Miércoles","Jueves")
        tbTopTreeView.column("#0",width=120)
        tbTopTreeView.column("Martes",width=120)
        tbTopTreeView.column("Miércoles",width=120)
        tbTopTreeView.column("Jueves",width=120)

        tbTopTreeView.heading('#0',text='Lunes')
        tbTopTreeView.heading('Martes', text='Martes')
        tbTopTreeView.heading('Miércoles', text='Miércoles')
        tbTopTreeView.heading('Jueves', text='Jueves')

        #segunda tabla
        tbBottomTreeView = ttk.Treeview(topFrame,height=5)
        tbBottomTreeView.grid(row=1, column=0)

        tbBottomTreeView["columns"]=("Materia","Docente")
        tbBottomTreeView.column("#0",width=166)
        tbBottomTreeView.column("Materia",width=166)
        tbBottomTreeView.column("Docente",width=166)

        tbBottomTreeView.heading('#0',text='Clave')
        tbBottomTreeView.heading('Materia', text='Materia')
        tbBottomTreeView.heading('Docente', text='Docente')

        #Botones
        returnButton = Button(bottomFrame, text="Regresar", command= self.returnStudentHome)
        returnButton.grid(row = 1, column = 3)

    def returnStudentHome(self):
        ##Add validations to return or close and open the other window
        self.app = StudentAccess(Tk(),self.clave)
        self.root.destroy()
