import sys
from Inscription import *
from Validaciones import *
from tkinter import *
from tkinter import ttk


class GroupsInscription:
    def __init__(self, root,clave, subject):
        self.root = root
        self.clave = clave
        self.subject = subject
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Inscripción de grupos")
        root.geometry('{}x{}'.format(1100, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        self.tableTreeView = ttk.Treeview(topFrame)
        self.tableTreeView.grid(row=0, column=0)

        ##se hará dinámicamente
        self.tableTreeView["columns"]=("Grupo","Aula","Docente","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado")
        self.tableTreeView.column("#0",width=10)
        self.tableTreeView.column("Aula",width=50)
        self.tableTreeView.column("Docente",width=200)
        self.tableTreeView.column("Lunes",width=100)
        self.tableTreeView.column("Martes",width=100)
        self.tableTreeView.column("Miércoles",width=100)
        self.tableTreeView.column("Jueves",width=100)
        self.tableTreeView.column("Viernes",width=100)
        self.tableTreeView.column("Sábado",width=100)

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

        #selección
        subjectCveLB = Label(bottomFrame, text="Grupo:")
        subjectCveLB.grid(row=0, column=0)
        subjectCveENY = Entry(bottomFrame)
        subjectCveENY.grid(row=0, column=1)

        #Botones
        selectButton = Button(bottomFrame, text="Inscribir", command = self.addToSchedule)
        selectButton.grid(row = 0, column = 2)
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnInscription)
        returnButton.grid(row = 1, column = 3)

        ##carga información
        self.showAvailableTeachers()

    def addToSchedule(self):
        return False

    def showAvailableTeachers(self):
        teachers = findAvailableTeachers(self.subject)
        index = 1
        for grupo, aula, docente, horarios in teachers:
            self.tableTreeView.insert('','0',index,text=index,values=(grupo,aula,docente,horarios))
            index += 1

    def selectItem(self):
        curItem = self.tableTreeView.focus()
        print(self.tableTreeView.item(curItem))

    def returnInscription(self):
        ##Add validations to return or close and open the other window
        self.app = Inscription(Tk(), self.clave)
        self.root.destroy()
