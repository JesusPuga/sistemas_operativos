from Validations.loadStudents import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeAddInscription:
    def __init__(self,old_root,clave,values):
        w = 300
        h = 100
        self.old_root = old_root
        self.clave = clave
        self.values = values

        self.new_root = centerForm(w,h,"Insertar Fecha de Inscripción | Administrativo")

        #Frames a usar, algo así como div b:
        mainFrame = Frame(self.new_root, width=300, height=75)
        mainFrame.grid(row=0,column=0,padx=(15,15),pady=(15,15))
        #Frames a usar, algo así como div b:
        insertFrame = Frame(self.new_root, width=300, height=15)
        insertFrame.grid(row=1,column=0,sticky=E)

        returnFrame = Frame(self.new_root,  width=300, height=15)
        returnFrame.grid(row=1,column=0,sticky=W)

        monthLBL = Label(mainFrame, text="Mes:")
        monthLBL.grid(row=0, column=0, sticky="W", padx=0, pady=0)
        self.monthCBX = ttk.Combobox(mainFrame, state="readonly",width=8)
        self.monthCBX.grid(row=0, column=1, sticky="W", padx=0, pady=5)
        self.monthCBX["values"] = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        self.monthCBX.current(0)
        self.monthCBX.bind("<<ComboboxSelected>>", self.loadInformation)

        dayLBL = Label(mainFrame, text="Día:")
        dayLBL.grid(row=0, column=2, sticky="W", padx=0, pady=0)
        self.dayCBX = ttk.Combobox(mainFrame, state="readonly",width=2)
        self.dayCBX.grid(row=0, column=3, sticky="e", padx=0, pady=0)

        hourLBL = Label(mainFrame, text="Hora:")
        hourLBL.grid(row=0, column=4, sticky="W", padx=0, pady=0)
        self.hourENY = Entry(mainFrame,width=2)
        self.hourENY.grid(row=0, column=5, sticky="W", padx=0, pady=5)
        minuteLBL = Label(mainFrame, text=":",width=1)
        minuteLBL.grid(row=0, column=6, sticky="W", padx=0, pady=0)
        self.minuteENV = Entry(mainFrame,width=2)
        self.minuteENV.grid(row=0, column=7, sticky="W", padx=0, pady=5)

        addButton = Button(insertFrame, text="Agregar", command=self.addInscription,height=1,width=4)
        addButton.grid(row = 1, column = 0,sticky=E,padx=(15,15))
        returnButton = Button(returnFrame, text="Regresar", command=self.returnAdministrativeHome,height=1,width=4)
        returnButton.grid(row = 1, column = 7,sticky=E,padx=(15,15))

        self.loadInformation(0)
        self.new_root.mainloop()

    def loadInformation(self,var):
        months = {"Enero":31,"Febrero":28,"Marzo":31,"Abril":30,"Mayo":31,"Junio":30,"Julio":31,"Agosto":31,"Septiembre":30,"Octubre":31,"Noviembre":30,"Diciembre":31}
        current =self.monthCBX.get()
        days = []

        for num in range(1,months[current]+1):
            days.append(num)

        self.dayCBX["values"] = days
        self.dayCBX.current(0)

    def addInscription(self):
        month = self.monthCBX.get()
        day = self.dayCBX.get()
        hour = self.hourENY.get()
        minute = self.minuteENV.get()

        if not hour.isdigit():
            messagebox.showinfo("Aviso","Escribe valores numéricos en las horas")
            self.hourENY.delete(0, END) #deletes the current value
            self.hourENY.insert(0, "") #inserts new value assigned by 2nd parameter
            return 0
        if not int(hour) < 24:
            messagebox.showinfo("Aviso","Escribe valores  menores 24 en las horas")
            self.hourENY.delete(0, END) #deletes the current value
            self.hourENY.insert(0, "") #inserts new value assigned by 2nd parameter
            return 0

        if not minute.isdigit():
            messagebox.showinfo("Aviso","Escribe valores numéricos en los minutos")
            self.minuteENV.delete(0, END) #deletes the current value
            self.minuteENV.insert(0, "") #inserts new value assigned by 2nd parameter
            return 0

        if not int(minute) < 60:
            messagebox.showinfo("Aviso","Escribe valores  menores 60 en las horas")
            self.minuteENV.delete(0, END) #deletes the current value
            self.minuteENV.insert(0, "") #inserts new value assigned by 2nd parameter
            return 0

        message = insertInscription(month,day,hour,minute)
        messagebox.showinfo("Aviso",message)
        self.returnAdministrativeHome()

    def returnAdministrativeHome(self):
        self.old_root.destroy()
        window = __import__('Forms.Administrative.AdministrativeAddStudent',None,None,['AdministrativeAddStudent'], 0)
        self.app = window.AdministrativeAddStudent(self.new_root,self.clave, self.values)
