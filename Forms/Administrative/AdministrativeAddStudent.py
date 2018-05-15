from Validations.loadStudents import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeAddStudent:
    def __init__(self, old_root,clave):
        w = 500
        h = 350
        old_root.destroy()
        self.new_root = centerForm(w,h,"Insertar Alumno | Administrativo")
        self.clave = clave

        #Frames a usar, algo así como div b:
        rightFrame = Frame(self.new_root, bg='gray', width=500, height=200)
        rightFrame.grid(row=0,column=1)
                #Frames a usar, algo así como div b:
        leftFrame = Frame(self.new_root, bg='gray', width=500, height=100)
        leftFrame.grid(row=1,column=1)

        nameLBL = Label(rightFrame, text="Nombre:")
        nameLBL.grid(row=0, column=0, sticky="W", padx=0, pady=0)
        self.nameENY = Entry(rightFrame)
        self.nameENY.grid(row=0, column=1, sticky="W", padx=0, pady=5)

        appPaternoLBL = Label(rightFrame, text="Apellido Paterno:")
        appPaternoLBL.grid(row=1, column=0, sticky="W", padx=0, pady=0)
        self.appPaternoENY = Entry(rightFrame)
        self.appPaternoENY.grid(row=1, column=1, sticky="W", padx=0, pady=5)

        appMaternoLBL = Label(rightFrame, text="Apellido Materno:")
        appMaternoLBL.grid(row=2, column=0, sticky="W", padx=0, pady=0)
        self.appMaternoENY = Entry(rightFrame)
        self.appMaternoENY.grid(row=2, column=1, sticky="W", padx=0, pady=5)

        telefonoLBL = Label(rightFrame, text="Teléfono:")
        telefonoLBL.grid(row=3, column=0, sticky="W", padx=0, pady=0)
        self.telefonoENY = Entry(rightFrame)
        self.telefonoENY.grid(row=3, column=1, sticky="W", padx=0, pady=5)

        sexoLBL = Label(rightFrame, text="Sexo:")
        sexoLBL.grid(row=4, column=0, sticky="W", padx=0, pady=0)
        self.sexoENY = Entry(rightFrame)
        self.sexoENY.grid(row=4, column=1, sticky="W", padx=0, pady=5)

        contraseniaLBL = Label(rightFrame, text="Contraseña:")
        contraseniaLBL.grid(row=5, column=0, sticky="W", padx=0, pady=0)
        self.contraseniaENY = Entry(rightFrame)
        self.contraseniaENY.grid(row=5, column=1, sticky="W", padx=0, pady=5)

        estatusLBL = Label(rightFrame, text="Estatus:")
        estatusLBL.grid(row=6, column=0, sticky="W", padx=0, pady=0)
        self.estatusCBX = ttk.Combobox(rightFrame, state="readonly")
        self.estatusCBX.grid(row=6, column=1, sticky="W", padx=0, pady=5)
        self.estatusCBX["values"] = ["PRIMER INGRESO","REINGRESO"]
        self.estatusCBX.current(0)

        carreraLBL = Label(rightFrame, text="Carrera:")
        carreraLBL.grid(row=7, column=0, sticky="W", padx=0, pady=0)
        self.carreraCBX = ttk.Combobox(rightFrame, state="readonly")
        self.carreraCBX.grid(row=7, column=1, sticky="W", padx=0, pady=5)

        inscripcionLBL = Label(rightFrame, text="Inscripcion:")
        inscripcionLBL.grid(row=8, column=0, sticky="W", padx=0, pady=0)
        self.inscripcionCBX = ttk.Combobox(rightFrame, state="readonly")
        self.inscripcionCBX.grid(row=8, column=1, sticky="e", padx=0, pady=0)

        agregarButton = Button(rightFrame, text="Agregar", command=self.openCalendar,height=1,width=4)
        agregarButton.grid(row = 8, column = 2,padx=(0,0))

        insertButton = Button(leftFrame, text="Insertar", command=self.addStudent,height=1,width=4)
        insertButton.grid(row = 1, column = 0,pady=(10,10))

        scheduleButton = Button(leftFrame, text="Regresar", command=self.returnAdministrativeHome,height=1,width=4)
        scheduleButton.grid(row = 2, column = 0,pady=(10,10))

        self.showInformation()

        self.new_root.mainloop()

    def showInformation(self):
        careers = loadAllCareers()
        mappedCareers = []
        if careers.fetchone() != None:
            for career in careers:
                mappedCareers.append(career)
            self.carreraCBX["values"] = mappedCareers[0]
            self.carreraCBX.current(0)

        datesInscription = loadAvailableDatesInscription()
        mappedDatesInscription = []
        if datesInscription.fetchone() != None:
            for dateInscription in datesInscription:
                mappedDatesInscription.append(dateInscription)
            self.inscripcionCBX["values"] = mappedDatesInscription[0]
            self.inscripcionCBX.current(0)


    def openCalendar(self):
        return 0

    def addStudent(self):
        name = self.nameENY.get()
        lastName = self.appPaternoENY.get()
        lastName2 = self.appMaternoENY.get()
        cel = self.telefonoENY
        status =  self.estatusCBX.get()
        inscriptionClave = self.inscripcionCBX.get()
        sex = self.sexoENY.get()
        password = self.contraseniaENY
        ##validate inputs

        insertStudent(status, inscriptionClave,sex,cel, password, name, lastName, lastName2):

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Administrative.AdministrativeAccess',None,None,['AdministrativeAccess'], 0)
        self.app = window.AdministrativeAccess(self.new_root,self.clave)
