import sys
from AdministrativeAccess import *
from Validaciones import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeSubject:
    def __init__(self, root,clave):
        self.root = root
        self.clave = clave
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Consulta | Alumnos por materia")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        #selección
        subjectCveLB = Label(topFrame, text="Matrícula:")
        subjectCveLB.grid(row=0, column=0)
        subjectCveENY = Entry(topFrame)
        subjectCveENY.grid(row=0, column=1)

        #Top Button
        selectButton = Button(topFrame, text="Buscar:")
        selectButton.grid(row = 0, column = 2)

        #primer tabla
        tbTopTreeView = ttk.Treeview(bottomFrame)
        tbTopTreeView.grid(row=0, column=0)

        tbTopTreeView["columns"]=("Nombre","Apellido Paterno","Apellido Materno")
        tbTopTreeView.column("#0",width=120)
        tbTopTreeView.column("Nombre",width=120)
        tbTopTreeView.column("Apellido Paterno",width=120)
        tbTopTreeView.column("Apellido Materno",width=120)

        tbTopTreeView.heading('#0',text='Matrícula')
        tbTopTreeView.heading('Nombre', text='Nombre')
        tbTopTreeView.heading('Apellido Paterno', text='Apellido Paterno')
        tbTopTreeView.heading('Apellido Materno', text='Apellido Materno')


        #Bottom buttons
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnAdministrativeHome)
        returnButton.grid(row = 1, column = 0)


    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        self.app = AdministrativeAccess(Tk(),self.clave)
        self.root.destroy()
