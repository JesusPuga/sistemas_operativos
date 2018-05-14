from Validations.userValidations import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AdministrativeAddStudent:
    def __init__(self, old_root,clave):
        w = 500
        h = 300
        old_root.destroy()
        self.new_root = centerForm(w,h,"Insertar Alumno | Administrativo")
        self.clave = clave

        #Frames a usar, algo así como div b:
        leftFrame = Frame(self.new_root, width=100, height=100)
        leftFrame.grid(row=0,column=0)

        closeSessionFrame = Frame(self.new_root,  bg='gray2')
        closeSessionFrame.grid(row=1,column=0)

        rightFrame = Frame(self.new_root, bg='lavender', width=400, height=300)
        rightFrame.grid(row=0,column=1)

        #Botones
        scheduleButton = Button(leftFrame, text="Regresar", command=self.returnAdministrativeHome,height=1,width=4)
        scheduleButton.grid(row = 2, column = 0,pady=(10,100))

        self.new_root.mainloop()

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Administrative.AdministrativeAccess',None,None,['AdministrativeAccess'], 0)
        self.app = window.AdministrativeAccess(self.new_root,self.clave)
