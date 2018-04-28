import sys
from AdministrativeAccess import *
from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    """ CREACIÓN DE LA VENTANA DE ACCESO AL SISTEMA"""

    #Declara ventana de aplicación
    root = Tk()

    #LLamado a la aplicación mediante la ventana de acceso al sistema
    #Access(root)

    AdministrativeAccess(root,5)# prueba de nueva ventana

    #Bucle de la aplicación
root.mainloop()
