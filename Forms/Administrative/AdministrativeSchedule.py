from Validations.loadSubjects import *
from Validations.loadStudents import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeSchedule:
    def __init__(self, old_root,clave):
        h = 600
        w = 1300

        old_root.destroy()
        self.new_root = centerForm(w,h,"Consulta | Horario")
        self.clave = clave

        #Frames a usar, algo así como div b:
        topFrame = Frame(self.new_root, width=500, height=100)
        topFrame.grid(row=0,column=0,sticky=W,padx =20)
        leftTopFrame = Frame(topFrame, width=100, height=50)
        leftTopFrame.grid(row=0,column=0)
        rightTopFrame = Frame(topFrame, width=400, height=50)
        rightTopFrame.grid(row=0,column=1)

        bottomFrame = Frame(self.new_root, width=500, height=500)
        bottomFrame.grid(row=1,column=0)

        #selección
        subjectCveLB = Label(leftTopFrame, text="Matrícula:")
        subjectCveLB.grid(row=0, column=0,padx=20)
        self.subjectCveENY = Entry(leftTopFrame)
        self.subjectCveENY.grid(row=0, column=1)

        #Top Button
        selectButton = Button(leftTopFrame, text="Consultar", command=self.showScheduleForStudent)
        selectButton.grid(row = 0, column = 2)

        #primer tabla
        self.tbTopTreeView = ttk.Treeview(bottomFrame, height=14)
        self.tbTopTreeView.grid(row=1, column=0,padx = (40,40))

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

        spaceCveLB = Label(bottomFrame, text=" ")
        spaceCveLB.grid(row=2, column=0)
        #segunda tabla
        self.tbBottomTreeView = ttk.Treeview(bottomFrame, height=8)
        self.tbBottomTreeView.grid(row=3, column=0)

        self.tbBottomTreeView["columns"]=("Materia","Docente")
        self.tbBottomTreeView.column("#0",width=90)
        self.tbBottomTreeView.column("Materia",width=400)
        self.tbBottomTreeView.column("Docente",width=400)

        self.tbBottomTreeView.heading('#0',text='Clave')
        self.tbBottomTreeView.heading('Materia', text='Materia')
        self.tbBottomTreeView.heading('Docente', text='Docente')
        space2CveLB = Label(bottomFrame, text=" ")
        space2CveLB.grid(row=4, column=0)
        #Bottom buttons
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnAdministrativeHome)
        returnButton.grid(row = 5, column = 0, sticky=E, padx=(0,20))

        self.new_root.mainloop()

    def showScheduleForStudent(self):
        subject = self.subjectCveENY.get()
        if not subject:
            messagebox.showinfo("Aviso","Debes escribir la matrícula")
        elif not subject.isdigit():
            messagebox.showinfo("Aviso","La matrícula debe ser un número")
        else:
            self.tbTopTreeView.delete(*self.tbTopTreeView.get_children())
            self.tbBottomTreeView.delete(*self.tbBottomTreeView.get_children())
            schedule = loadStudentSchedule(subject)
            cont = 0
            if schedule.fetchone() == None:
                messagebox.showinfo("Aviso","El alumno no ha inscrito materias")
            else:
                for hour, monday, tuesday, whednesnday, thursdar, firday, saturday in schedule:
                    self.tbTopTreeView.insert('','0',cont,text=hour,values=(monday, tuesday, whednesnday, thursdar, firday, saturday))
                    cont += 1

                self.showSubjectsForStudent()

    def showSubjectsForStudent(self):
        subjects = loadSubjectsForStudent(self.subjectCveENY.get())
        type = 0

        for clave, materia, docente, aPaterno, aMaterno in subjects:
            nombre = docente +" " + aPaterno +" "+ aMaterno
            self.tbBottomTreeView.insert('','0',clave,text=clave,values=(materia,nombre))

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Administrative.AdministrativeAccess',None,None,['AdministrativeAccess'], 0)
        self.app = window.AdministrativeAccess(self.new_root,self.clave)
