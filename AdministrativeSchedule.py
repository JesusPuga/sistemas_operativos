from Validaciones import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeSchedule:
    def __init__(self, root,clave):
        self.root = root
        self.clave = clave
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Consulta | Horario")
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
        selectButton = Button(topFrame, text="Consultar")
        selectButton.grid(row = 0, column = 2)

        #primer tabla
        tbTopTreeView = ttk.Treeview(bottomFrame, height=5)
        tbTopTreeView.grid(row=1, column=0)

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
        tbBottomTreeView = ttk.Treeview(bottomFrame, height=5)
        tbBottomTreeView.grid(row=2, column=0)

        tbBottomTreeView["columns"]=("Materia","Docente")
        tbBottomTreeView.column("#0",width=166)
        tbBottomTreeView.column("Materia",width=166)
        tbBottomTreeView.column("Docente",width=166)

        tbBottomTreeView.heading('#0',text='Clave')
        tbBottomTreeView.heading('Materia', text='Materia')
        tbBottomTreeView.heading('Docente', text='Docente')

        #Bottom buttons
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnAdministrativeHome)
        returnButton.grid(row = 1, column = 3)

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('AdministrativeAccess')
        self.app = window.AdministrativeAccess(Tk(),self.clave)
        self.root.destroy()
