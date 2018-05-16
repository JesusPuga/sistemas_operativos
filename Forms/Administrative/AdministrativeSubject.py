import sys
from Validations.loadSubjects import *
from Validations.loadStudents import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeSubject:
    def __init__(self, old_root,clave):
        h = 350
        w = 600
        old_root.destroy()
        self.new_root = centerForm(w,h,"Consulta | Alumnos por materia")
        self.clave = clave

        #Frames a usar, algo así como div b:
        topFrame = Frame(self.new_root, width=500, height=200)
        topFrame.grid(row=0,column=0, sticky=W, padx=(55,0))

        bottomFrame = Frame(self.new_root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        #selección
        subjectCveLB = Label(topFrame, text="Materias:")
        subjectCveLB.grid(row=0, column=0)
        self.subjectCBX = ttk.Combobox(topFrame, state="readonly")
        self.subjectCBX.grid(row=0, column=1, sticky="e", padx=5, pady=5)
        self.subjectCBX.bind("<<ComboboxSelected>>", self.showSubjectGroups)

        groupCveLB = Label(topFrame, text="Grupos:")
        groupCveLB.grid(row=1, column=0)
        self.groupCBX = ttk.Combobox(topFrame, state="readonly")
        self.groupCBX.grid(row=1, column=1, sticky="e", padx=5, pady=5)
        self.showSubjects()

        #Top Button
        selectButton = Button(topFrame, text="Buscar", command=self.showStudentsForSubject)
        selectButton.grid(row = 0, column = 2)

        #primer tabla
        self.tbTopTreeView = ttk.Treeview(bottomFrame)
        self.tbTopTreeView.grid(row=0, column=0,padx=(55,55),pady=(15,15))

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
        returnButton.grid(row = 1, column = 0,sticky=E, padx=(0,15))

        self.new_root.mainloop()


    def showSubjects(self):
        subjects = loadAllSubjects()
        mappedSubjects = []

        for subject in subjects:
            mappedSubjects.append(subject[0])

        self.subjectCBX["values"] = mappedSubjects
        self.subjectCBX.current(0)
        #Carga los grupos de la materia seleccionada
        self.showSubjectGroups(self.subjectCBX.get())


    def showSubjectGroups(self, var):
        groups = loadSubjectGroups(self.subjectCBX.get())
        mappedGroups = []

        for group in groups:
            mappedGroups.append(group[0])
        if groups.fetchone() != None:
            self.groupCBX["values"] = mappedGroups
            self.groupCBX.current(0)
        else:
            self.groupCBX["values"] = []

    def showStudentsForSubject(self):
        self.tbTopTreeView.delete(*self.tbTopTreeView.get_children())
        group = self.groupCBX.get()

        if group == "":
            messagebox.showinfo("Aviso","No hay grupos disponibles para esta materia")
        else:
            students = loadStudentsForGroup(group, self.subjectCBX.get())

            if students.fetchone() == None:
                messagebox.showinfo("Aviso","No hay alumnos inscritos")
            else:
                for clave, nombre, appellidoPaterno, appelidoMaterno in students:
                    self.tbTopTreeView.insert('','0',clave,text=clave,values=(nombre,appellidoPaterno, appellidoPaterno))

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Administrative.AdministrativeAccess',None,None,['AdministrativeAccess'], 0)
        self.app = window.AdministrativeAccess(self.new_root,self.clave)
