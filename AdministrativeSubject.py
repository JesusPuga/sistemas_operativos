import sys
from AdministrativeAccess import *
from Validaciones import *
from loadSubjects import *
from loadStudents import *
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
        subjectCveLB = Label(topFrame, text="Materias:")
        subjectCveLB.grid(row=0, column=0)
        #subjectCveENY = Entry(topFrame)
        #subjectCveENY.grid(row=0, column=1)
        self.subjectCBX = ttk.Combobox(topFrame)
        self.subjectCBX.grid(row=0, column=1, sticky="e", padx=5, pady=5)
        self.showSubjects()

        #Top Button
        selectButton = Button(topFrame, text="Buscar:", command=self.showStudentsForSubject)
        selectButton.grid(row = 0, column = 2)

        #primer tabla
        self.tbTopTreeView = ttk.Treeview(bottomFrame)
        self.tbTopTreeView.grid(row=0, column=0)

        self.tbTopTreeView["columns"]=("Nombre","Apellido Paterno","Apellido Materno")
        self.tbTopTreeView.column("#0",width=120)
        self.tbTopTreeView.column("Nombre",width=120)
        self.tbTopTreeView.column("Apellido Paterno",width=120)
        self.tbTopTreeView.column("Apellido Materno",width=120)

        self.tbTopTreeView.heading('#0',text='Matrícula')
        self.tbTopTreeView.heading('Nombre', text='Nombre')
        self.tbTopTreeView.heading('Apellido Paterno', text='Apellido Paterno')
        self.tbTopTreeView.heading('Apellido Materno', text='Apellido Materno')


        #Bottom buttons
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnAdministrativeHome)
        returnButton.grid(row = 1, column = 0)

    def showSubjects(self):
        subjects = loadAllSubjects()
        mappedSubjects = []

        for subject in subjects:
            mappedSubjects.append(subject[0])

        self.subjectCBX["values"] = mappedSubjects
        self.subjectCBX.current(0)

    def showStudentsForSubject(self):
        self.tbTopTreeView.delete(*self.tbTopTreeView.get_children())
        students = loadStudentsForSubject(self.subjectCBX.get())

        for clave, nombre, appellidoPaterno, appelidoMaterno in students:
            self.tbTopTreeView.insert('','0',clave,text=clave,values=(clave,nombre,appellidoPaterno, appellidoPaterno))

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('AdministrativeAccess')
        self.app = window.AdministrativeAccess(Tk(),self.clave)
        self.root.destroy()
