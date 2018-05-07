from Validations.loadSubjects import *
from Validations.loadStudents import *
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
        self.new_root.geometry('{}x{}'.format(1200, 600))
        self.new_root.resizable(0,0)
        # layout all of the main containers
        self.new_root.grid_rowconfigure(1, weight=1)
        self.new_root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(self.new_root, width=500, height=400)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(self.new_root, width=500, height=200)
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
        self.tbTopTreeView = ttk.Treeview(bottomFrame, height=5)
        self.tbTopTreeView.grid(row=1, column=0)

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
        subject = self.subjectCveENY.get()
        if not subject:
            messagebox.showinfo("Aviso","Debes escribir la matrícula")
        elif not subject.isdigit():
            messagebox.showinfo("Aviso","La matrícula debe ser un número")
        else:
            schedule = loadStudentSchedule(subject)
            cont = 0

            for hour, monday, tuesday, whednesnday, thursdar, firday, saturday in schedule:
                self.tbTopTreeView.insert('','0',cont,text=hour,values=(monday, tuesday, whednesnday, thursdar, firday, saturday))
                cont += 1

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
        window = __import__('Forms.Administrative.AdministrativeAccess',None,None,['AdministrativeAccess'], 0)
        self.app = window.AdministrativeAccess(self.new_root,self.clave)
