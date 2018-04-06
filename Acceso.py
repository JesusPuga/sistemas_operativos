import sys
import tkinter
from tkinter import *
from tkinter import ttk

class Acceso:
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


        tipoUsuarioCBX = ttk.Combobox(frame)
        tipoUsuarioCBX.grid(row=0, column=1, sticky="e", padx=5, pady=5)
        tipoUsuarioCBX["values"] = ["Alumno", "Docente", "Administrativo"]

        #Campo Usuario
        usuarioLB = Label(frame, text="Usuario:")
        usuarioLB.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        usuarioENY = Entry(frame)
        usuarioENY.grid(row=1, column=1, sticky="e", padx=5, pady=5)

        #Campo Contraseña
        contraseniaLB = Label(frame, text="Contraseña:")
        contraseniaLB.grid(row=2, column=0, sticky="e", padx=5, pady=5)

        contraseniaENY = Entry(frame)
        contraseniaENY.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        contraseniaENY.config(show="*")

        #Botón Ingresar
        Button(root, text="Ingresar")


if __name__ == '__main__':
    """ CREACIÓN DE LA VENTANA DE ACCESO AL SISTEMA"""

    #Declara ventana de aplicación
    root = Tk()

    aplicacion = Acceso(root)

    #Bucle de la aplicación
    root.mainloop()
