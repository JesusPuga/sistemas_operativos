import sys
from Validations.userValidations import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Access:
    def __init__(self, old_root):
        w = 500
        h = 300
        old_root.destroy()
        self.new_root = centerForm(w,h,"Sistema de Inscripción | Acceso")

        frame = Frame(self.new_root, width=w, heigh=h)
        frame.grid(row=0,column=0, padx=(70,70), pady=(90,90))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0,weight=1)

        """ CREACIÓN DEL FORMULARIO DE ACCESO"""

        #Campo Tipo Usuario
        tipoUsuarioLBL = Label(frame, text="Tipo de Usuario:")
        tipoUsuarioLBL.grid(row=0, column=0, sticky="e", padx=5, pady=5)

        self.tipoUsuarioCBX = ttk.Combobox(frame, state="readonly")
        self.tipoUsuarioCBX.grid(row=0, column=1, sticky="e", padx=5, pady=5)
        self.tipoUsuarioCBX["values"] = ["Alumno","Docente", "Administrativo"]
        self.tipoUsuarioCBX.current(0)

        #Campo Usuario
        usuarioLB = Label(frame, text="Usuario:")
        usuarioLB.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        self.usuarioENY = Entry(frame)
        self.usuarioENY.grid(row=1, column=1, sticky="e", padx=5, pady=5)

        #Campo Contraseña
        contraseniaLB = Label(frame, text="Contraseña:")
        contraseniaLB.grid(row=2, column=0, sticky="e", padx=5, pady=5)

        self.contraseniaENY = Entry(frame)
        self.contraseniaENY.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        self.contraseniaENY.config(show="*")

        #Botón Ingresar
        userButton = Button(frame, text="Ingresar", command= self.validateInput)
        userButton.grid(row = 3, column = 2, padx=5, pady=5)

        self.new_root.mainloop()

    def validateInput(self):
        ##type, user, password
        clave =self.usuarioENY.get()
        result = validateUser(self.tipoUsuarioCBX.get(), clave,self.contraseniaENY.get())

        if result == "ok":
            window = None
            if self.tipoUsuarioCBX.get() == "Administrativo":
                window = __import__('Forms.Administrative.AdministrativeAccess',None,None,['AdministrativeAccess'], 0)
                self.app = window.AdministrativeAccess(self.new_root,clave)                 #CLASE QUE MANDA A LLAMAR LA VENTANA DE ADMINISTRATIVO
            elif self.tipoUsuarioCBX.get() == "Alumno":
                window = __import__('Forms.Student.StudentAccess',None,None,['StudentAccess'], 0)
                self.app = window.StudentAccess(self.new_root, clave)  #CLASE QUE CONTIENE LA FUNCIOANLIDAD DE ALUMNO
            else:
                messagebox.showwarning("Aviso","Proceso no disponible shavo, pícale a otra opción")
                return 0
        else:
            messagebox.showwarning("Error",result)
