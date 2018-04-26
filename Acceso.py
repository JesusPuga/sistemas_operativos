import sys
from StudentAccess import *
from AdministrativeAccess import *
from Validaciones import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Access:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Acceso")
        root.resizable(0,0)

        frame = Frame(root, width=500, heigh=300)
        frame.grid(row=0,column=0, padx=(150,150), pady=(150,100))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0,weight=1)


        """ CREACIÓN DEL FORMULARIO DE ACCESO"""

        #Campo Tipo Usuario
        tipoUsuarioLBL = Label(frame, text="Tipo de Usuario:")
        tipoUsuarioLBL.grid(row=0, column=0, sticky="e", padx=5, pady=5)

        self.tipoUsuarioCBX = ttk.Combobox(frame)
        self.tipoUsuarioCBX.grid(row=0, column=1, sticky="e", padx=5, pady=5)
        self.tipoUsuarioCBX["values"] = ["Alumno","Docente", "Administrativo"]
        self.tipoUsuarioCBX.current(0)

        self.tipoUsuarioErrorLBL = Label(frame, text="")
        self.tipoUsuarioErrorLBL.grid(row=0, column=2, sticky="e", padx=5, pady=5)

        #Campo Usuario
        usuarioLB = Label(frame, text="Usuario:")
        usuarioLB.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        self.usuarioENY = Entry(frame)
        self.usuarioENY.grid(row=1, column=1, sticky="e", padx=5, pady=5)

        self.usuarioErrorLBL = Label(frame, text="")
        self.usuarioErrorLBL.grid(row=1, column=2, sticky="e", padx=5, pady=5)

        #Campo Contraseña
        contraseniaLB = Label(frame, text="Contraseña:")
        contraseniaLB.grid(row=2, column=0, sticky="e", padx=5, pady=5)

        self.contraseniaENY = Entry(frame)
        self.contraseniaENY.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        self.contraseniaENY.config(show="*")

        self.contraseniaErrorLBL = Label(frame, text="")
        self.contraseniaErrorLBL.grid(row=2, column=2, sticky="e", padx=5, pady=5)

        #Botón Ingresar
        userButton = Button(frame, text="Ingresar", command= self.validateInput)
        userButton.grid(row = 3, column = 2)

    def validateInput(self):
        ##type, user, password
        clave =self.usuarioENY.get()
        result = validateUser(self.tipoUsuarioCBX.get(), clave,self.contraseniaENY.get())
        self.contraseniaErrorLBL["text"] = ""
        self.usuarioErrorLBL["text"] =  ""
        self.tipoUsuarioErrorLBL["text"] = ""

        if result == "ok":
            new_root = Tk()
            if self.tipoUsuarioCBX.get() == "Administrativo":
                self.app = AdministrativeAccess(new_root,clave)                 #CLASE QUE MANDA A LLAMAR LA VENTANA DE ADMINISTRATIVO
            elif self.tipoUsuarioCBX.get() == "Alumno":
                self.app = StudentAccess(new_root, clave)                       #CLASE QUE CONTIENE LA FUNCIOANLIDAD DE ALUMNO
            self.root.destroy()
        else:
            messagebox.showwarning("Error",result)
