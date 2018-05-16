from Validations.loadStudents import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeAddStudent:
    def __init__(self, old_root,clave,values = {}):
        w = 430
        h = 350
        old_root.destroy()
        self.new_root = centerForm(w,h,"Insertar Alumno | Administrativo")
        self.values = values
        self.clave = clave

        #Frames a usar, algo así como div b:
        mainFrame = Frame(self.new_root, width=500, height=200)
        mainFrame.grid(row=0,column=0,padx=(40,40),pady=(20,20))
        #Frames a usar, algo así como div b:
        insertFrame = Frame(self.new_root, width=500, height=75)
        insertFrame.grid(row=1,column=0,sticky=E)

        returnFrame = Frame(self.new_root,  width=500, height=75)
        returnFrame.grid(row=2,column=0,sticky=W)

        nameLBL = Label(mainFrame, text="Nombre:")
        nameLBL.grid(row=0, column=0, sticky="W", padx=0, pady=0)
        self.nameENY = Entry(mainFrame)
        self.nameENY.grid(row=0, column=1, sticky="W", padx=0, pady=5)

        appPaternoLBL = Label(mainFrame, text="Apellido Paterno:")
        appPaternoLBL.grid(row=1, column=0, sticky="W", padx=0, pady=0)
        self.appPaternoENY = Entry(mainFrame)
        self.appPaternoENY.grid(row=1, column=1, sticky="W", padx=0, pady=5)

        appMaternoLBL = Label(mainFrame, text="Apellido Materno:")
        appMaternoLBL.grid(row=2, column=0, sticky="W", padx=0, pady=0)
        self.appMaternoENY = Entry(mainFrame)
        self.appMaternoENY.grid(row=2, column=1, sticky="W", padx=0, pady=5)

        telefonoLBL = Label(mainFrame, text="Teléfono:")
        telefonoLBL.grid(row=3, column=0, sticky="W", padx=0, pady=0)
        self.telefonoENY = Entry(mainFrame)
        self.telefonoENY.grid(row=3, column=1, sticky="W", padx=0, pady=5)

        sexoLBL = Label(mainFrame, text="Sexo:")
        sexoLBL.grid(row=4, column=0, sticky="W", padx=0, pady=0)
        self.radio = StringVar()
        self.radio.set("M")
        self.mradio = Radiobutton(mainFrame, text="M", variable=self.radio , value="M")
        self.mradio.grid(row=4, column=1, sticky="W", padx=(0,10), pady=5)

        self.fradio = Radiobutton(mainFrame, text="F", variable=self.radio , value="F")
        self.fradio.grid(row=4, column=1, sticky="E", padx=(0,90), pady=5)

        contraseniaLBL = Label(mainFrame, text="Contraseña:")
        contraseniaLBL.grid(row=5, column=0, sticky="W", padx=0, pady=0)
        self.contraseniaENY = Entry(mainFrame)
        self.contraseniaENY.grid(row=5, column=1, sticky="W", padx=0, pady=5)
        self.contraseniaENY.config(show="*")

        carreraLBL = Label(mainFrame, text="Carrera:")
        carreraLBL.grid(row=7, column=0, sticky="W", padx=0, pady=0)
        self.carreraCBX = ttk.Combobox(mainFrame, state="readonly")
        self.carreraCBX.grid(row=7, column=1, sticky="W", padx=0, pady=5)

        inscripcionLBL = Label(mainFrame, text="Inscripcion:")
        inscripcionLBL.grid(row=8, column=0, sticky="W", padx=0, pady=0)
        self.inscripcionCBX = ttk.Combobox(mainFrame, state="readonly")
        self.inscripcionCBX.grid(row=8, column=1, sticky="e", padx=0, pady=0)

        agregarButton = Button(mainFrame, text="Agregar \nFecha", command=self.openAddInscription,height=2,width=4)
        agregarButton.grid(row = 8, column = 2,padx=(10,0))

        insertButton = Button(insertFrame, text="Insertar", command=self.addStudent,height=1,width=4)
        insertButton.grid(row = 1, column = 0,padx=(0,40),sticky=W)

        scheduleButton = Button(returnFrame, text="Regresar", command=self.returnAdministrativeHome,height=1,width=4)
        scheduleButton.grid(row = 2, column = 0,sticky=E,padx=(40,10))

        self.showInformation()

        self.new_root.mainloop()

    def showInformation(self):
        careers = loadAllCareers()
        mappedCareers = []
        if careers.fetchone() != None:
            for career in careers:
                mappedCareers.append(career[0])
            self.carreraCBX["values"] = mappedCareers
            self.carreraCBX.current(0)

        datesInscription = loadAvailableDatesInscription()
        mappedDatesInscription = []
        for dateInscription in datesInscription:
            mappedDatesInscription.append(dateInscription[0])
        self.inscripcionCBX["values"] = mappedDatesInscription
        if  mappedDatesInscription :
            self.inscripcionCBX.current(0)

        if self.values:
            self.loadOldValues()

    def loadValues(self):
        self.values = {"name":self.nameENY.get(),
                       "lastName":self.appPaternoENY.get(),
                       "lastName2":self.appMaternoENY.get(),
                       "cel": self.telefonoENY.get(),
                       "inscriptionClave": self.inscripcionCBX.get(),
                       "sex": self.radio.get(),
                       "password":self.contraseniaENY.get()
                      }

    def loadOldValues(self):
        self.contraseniaENY.delete(0, END) #deletes the current value
        self.contraseniaENY.insert(0, self.values["password"]) #inserts new value assigned by 2nd parameter
        self.nameENY.delete(0, END) #deletes the current value
        self.nameENY.insert(0, self.values["name"]) #inserts new value assigned by 2nd parameter
        self.appPaternoENY.delete(0, END) #deletes the current value
        self.appPaternoENY.insert(0, self.values["lastName"]) #inserts new value assigned by 2nd parameter
        self.appMaternoENY.delete(0, END) #deletes the current value
        self.appMaternoENY.insert(0, self.values["lastName2"]) #inserts new value assigned by 2nd parameter
        self.telefonoENY.delete(0, END) #deletes the current value
        self.telefonoENY.insert(0, self.values["cel"]) #inserts new value assigned by 2nd parameter
        if self.values["password"] != "":
            self.contraseniaENY.insert(0, END) #inserts new value assigned by 2nd parameter
            self.contraseniaENY.insert(0, self.values["password"]) #inserts new value assigned by 2nd parameter

        self.radio.set(self.values["sex"])

    def openAddInscription(self):
        self.loadValues()
        window = __import__('Forms.Administrative.AdministrativeAddInscription',None,None,['AdministrativeAddInscription'], 0)
        self.app = window.AdministrativeAddInscription(self.new_root,self.clave,self.values)

    def addStudent(self):
        self.loadValues()
        if self.values["name"] == "":
            messagebox.showinfo("Aviso","Debes escribir el nombre")
            return 0

        if self.values["lastName"] == "":
            messagebox.showinfo("Aviso","Debes escribir el apellido paterno")
            return 0

        if self.values["lastName2"] == "":
            messagebox.showinfo("Aviso","Debes escribir el apellido materno")
            return 0

        if self.values["cel"] == "":
            messagebox.showinfo("Aviso","Debes escribir el teléfono")
            return 0

        if self.values["inscriptionClave"] == "":
            messagebox.showinfo("Aviso","Debes seleccionar la hora de inscipción")
            return 0

        if self.values["password"] == "":
            messagebox.showinfo("Aviso","Debes escribir la contraseña")
            return 0

        message = insertStudent(self.values["inscriptionClave"],self.radio.get(),self.values["cel"],
                                self.values["password"], self.values["name"],
                                self.values["lastName"], self.values["lastName2"])
        messagebox.showinfo("Aviso",message)
        self.reopenAddStudent()

    def reopenAddStudent(self):
        window = __import__('Forms.Administrative.AdministrativeAddStudent',None,None,['AdministrativeAddStudent'], 0)
        self.app = window.AdministrativeAddStudent(self.new_root,self.clave)

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Administrative.AdministrativeAccess',None,None,['AdministrativeAccess'], 0)
        self.app = window.AdministrativeAccess(self.new_root,self.clave)
