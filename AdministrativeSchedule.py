from Validaciones import *
from loadStudents import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeSchedule:
    def __init__(self, old_root,clave):
        old_root.destroy()
        self.new_root = Tk()
        self.clave = clave
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        self.new_root.title("Consulta | Horario")
        self.new_root.geometry('{}x{}'.format(500, 350))
        self.new_root.resizable(0,0)
        # layout all of the main containers
        self.new_root.grid_rowconfigure(1, weight=1)
        self.new_root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(self.new_root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(self.new_root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        #selección
        subjectCveLB = Label(topFrame, text="Matrícula:")
        subjectCveLB.grid(row=0, column=0)
        self.subjectCveENY = Entry(topFrame)
        self.subjectCveENY.grid(row=0, column=1)

        #Top Button
        selectButton = Button(topFrame, text="Consultar", command=self.showScheduleForStudent)
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
        self.tbBottomTreeView = ttk.Treeview(bottomFrame, height=5)
        self.tbBottomTreeView.grid(row=2, column=0)

        self.tbBottomTreeView["columns"]=("Materia","Docente")
        self.tbBottomTreeView.column("#0",width=90)
        self.tbBottomTreeView.column("Materia",width=210)
        self.tbBottomTreeView.column("Docente",width=200)

        self.tbBottomTreeView.heading('#0',text='Clave')
        self.tbBottomTreeView.heading('Materia', text='Materia')
        self.tbBottomTreeView.heading('Docente', text='Docente')

        #Bottom buttons
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnAdministrativeHome)
        returnButton.grid(row = 3, column = 0)

        self.new_root.mainloop()

    def showScheduleForStudent(self):
        if not self.subjectCveENY.get():
            messagebox.showinfo("Aviso","Debes escribir la matrícula")
        elif not self.subjectCveENY.get().isdigit():
            messagebox.showinfo("Aviso","La matrícula debe ser un número")
        else:
            ##Método de Memo vv:
            self.showSubjectsForStudent()

    def showSubjectsForStudent(self):
        self.tbBottomTreeView.delete(*self.tbBottomTreeView.get_children())
        subjects = loadSubjectsForStudent(self.subjectCveENY.get())
        type = 0

        for clave, materia, docente, aPaterno, aMaterno in subjects:
            nombre = docente +" " + aPaterno +" "+ aMaterno
            self.tbBottomTreeView.insert('','0',clave,text=clave,values=(materia,nombre))

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('AdministrativeAccess')
        self.app = window.AdministrativeAccess(self.new_root,self.clave)
