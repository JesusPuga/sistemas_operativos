import sys
from Validaciones import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Inscription:
    def __init__(self, old_root, clave):
        old_root.destroy()
        self.new_root = Tk()
        self.clave = clave
        self.subject = None
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        self.new_root.title("Sistema de Inscripción | Inscripción")
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

        #créditos utilizados
        self.subjectCveLB = Label(counterFrame, text="Créditos utilizados: ")
        self.subjectCveLB.grid(row=0, column=0)
        ##espacio a la izquierda xD
        subject1CveLB = Label(counterFrame,
                                  text="""
                                  """)
        subject2CveLB = Label(counterFrame,
                                  text="""
                                  """)
        subject1CveLB.grid(row=0, column=1)
        subject2CveLB.grid(row=0, column=2)

        #configuración de tabla
        self.tableTreeView = ttk.Treeview(topFrame)
        self.tableTreeView.grid(row=0, column=0)

        self.tableTreeView["columns"]=("Materia","Semestre","Créditos")
        self.tableTreeView.column("#0",width=50)
        self.tableTreeView.column("Materia",width=270)
        self.tableTreeView.column("Semestre",width=80)
        self.tableTreeView.column("Créditos",width=80)

        self.tableTreeView.heading('#0',text='Clave')
        self.tableTreeView.heading('Materia', text='Materia')
        self.tableTreeView.heading('Semestre', text='Semestre')
        self.tableTreeView.heading('Créditos', text='Créditos')

        # Función para el double clic
        self.tableTreeView.bind("<Double-1>", self.onDoubleClick)

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
        subjects = findAvailableSubjects(self.clave)
        for cvMateria, nom, sem, creditos in subjects:
            self.tableTreeView.insert('','0',cvMateria,text=cvMateria,values=(nom,sem,creditos))

    def returnStudentHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('StudentAccess')
        self.app = window.StudentAccess(self.new_root, self.clave)

    def onDoubleClick(self, event):
        curItem = self.tableTreeView.item(self.tableTreeView.focus())
        self.subject = curItem["text"]

        if self.subject == None:
            messagebox.showinfo("Aviso","Selecciona una materia")
        else:
            window = __import__('GroupsInscription')
            self.app = window.GroupsInscription(self.new_root, self.clave, self.subject)
