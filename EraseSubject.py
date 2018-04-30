import sys
from StudentAccess import *
from Validaciones import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class EraseSubject:
    def __init__(self, old_root, clave):
        old_root.destroy()
        self.new_root = Tk()
        self.clave = clave
        self.subject = None
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        self.new_root.title("Sistema de Inscripción | Dar de baja")
        self.new_root.geometry('{}x{}'.format(600, 300))
        self.new_root.resizable(0,0)
        # layout all of the main containers
        self.new_root.grid_rowconfigure(1, weight=1)
        self.new_root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        counterFrame = Frame(self.new_root, width=500, height=50)
        counterFrame.grid(row=0,column=0)
        topFrame = Frame(self.new_root, width=500, height=200)
        topFrame.grid(row=1,column=0)
        bottomFrame = Frame(self.new_root, width=500, height=100)
        bottomFrame.grid(row=2,column=0)

        #configuración de tabla
        self.tableTreeView = ttk.Treeview(topFrame)
        self.tableTreeView.grid(row=0, column=0)
        self.tableTreeView["columns"]=("Materia")
        self.tableTreeView.column("#0",width=50)
        self.tableTreeView.column("Materia",width=500)

        self.tableTreeView.heading('#0',text='Clave')
        self.tableTreeView.heading('Materia', text='Materia')

        # Función para borrar con doble clic
        self.tableTreeView.bind("<Double-1>", self.deleteSubject)

        ##en prueba, creo que es pa' los datos xD
        ysb = ttk.Scrollbar(orient="vertical", command= self.tableTreeView.yview)
        xsb = ttk.Scrollbar(orient="horizontal", command= self.tableTreeView.xview)
        self.tableTreeView['yscroll'] = ysb.set
        self.tableTreeView['xscroll'] = xsb.set

        #Cargar inf en tabla
        self.showAvailableSubjects()

        #Botones
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnStudentHome)
        returnButton.grid(row = 0, column = 1)

        self.new_root.mainloop()

    def showAvailableSubjects(self):
        subjects = simpleShowRegisteredSubject(self.clave)

        for cvMateria, nom, grupo in subjects:
            self.tableTreeView.insert('','0',text=cvMateria, value=(nom,grupo))

    def deleteSubject(self, event):
        curItem = self.tableTreeView.item(self.tableTreeView.focus())
        subjectClave = curItem['text']
        IDGrupo = curItem['values'][1]
        eraseSubject(self.clave,IDGrupo,subjectClave)
        self.showAvailableSubjects()                            #LLAMADO A LA FUNCIÓN DE BORRADO EN LA BASE DE DATOS
        EraseSubject(self.new_root, self.clave)


    def returnStudentHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('StudentAccess')
        self.app = window.StudentAccess(self.new_root, self.clave)
