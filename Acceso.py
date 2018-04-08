import sys
from tkinter import *
from tkinter import ttk

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
        userButton = Button(frame, text="Ingresar", command= self.quit)
        userButton.grid(row = 3, column = 2)

    def quit(self):
        ##Add validations to return or close and open the other window
        new_root = Tk()
        self.app = StudentAccess(new_root)
        self.app = AdministrativeAccess(new_root)
        self.root.destroy()

class StudentAccess:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Alumno")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        leftFrame = Frame(root, width=100, height=100)
        leftFrame.grid(row=0,column=0)

        closeSessionFrame = Frame(root,  bg='gray2',)
        closeSessionFrame.grid(row=1,column=0)

        rightFrame = Frame(root, bg='lavender', width=400, height=300)
        rightFrame.grid(row=0,column=1)

        #Botones
        inscriptionButton = Button(leftFrame, text="Ingresar", command= self.openInscription)
        inscriptionButton.grid(row = 1, column = 0)
        scheduleButton = Button(leftFrame, text="Horario", command= self.openSchedule)
        scheduleButton.grid(row = 2, column = 0)
        sessionButton = Button(leftFrame, text="Cerrar Sesión", command= self.quit)
        sessionButton.grid(row = 3, column = 0)

    def quit(self):
        ##Add validations to return or close and open the other window
        self.app = Access(Tk())
        self.root.destroy()

    def openInscription(self):
        self.app = Inscription(Tk())
        self.root.destroy()

    def openSchedule(self):
        self.app = StudentSchedule(Tk())
        self.root.destroy()

class AdministrativeAccess:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Administrativo")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        leftFrame = Frame(root, width=100, height=100)
        leftFrame.grid(row=0,column=0)

        closeSessionFrame = Frame(root,  bg='gray2',)
        closeSessionFrame.grid(row=1,column=0)

        rightFrame = Frame(root, bg='lavender', width=400, height=300)
        rightFrame.grid(row=0,column=1)

        #Botones
        scheduleButton = Button(leftFrame, text="Horario", command=self.openSchedule)
        scheduleButton.grid(row = 2, column = 0)
        subjectButton = Button(leftFrame, text="Materias", command=self.openSubjects)
        subjectButton.grid(row = 1, column = 0)
        sessionButton = Button(leftFrame, text="Cerrar Sesión", command=self.closeSession)
        sessionButton.grid(row = 3, column = 0)

    def closeSession(self):
        ##Add validations to return or close and open the other window
        self.app = Access(Tk())
        self.root.destroy()

    def openSubjects(self):
        self.app = AdministrativeSubject(Tk())
        self.root.destroy()

    def openSchedule(self):
        self.app = AdministrativeSchedule(Tk())
        self.root.destroy()

class Inscription:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Inscripción")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)
        bottomFrame = Frame(root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        tableTreeView = ttk.Treeview(topFrame)
        tableTreeView.grid(row=0, column=0)

        tableTreeView["columns"]=("Materia","Semestre","Créditos")
        tableTreeView.column("#0",width=120)
        tableTreeView.column("Materia",width=120)
        tableTreeView.column("Semestre",width=120)
        tableTreeView.column("Créditos",width=120)

        tableTreeView.heading('#0',text='Clave')
        tableTreeView.heading('Materia', text='Materia')
        tableTreeView.heading('Semestre', text='Semestre')
        tableTreeView.heading('Créditos', text='Créditos')

        ##en prueba, creo que es pa' los datos xD
        ysb = ttk.Scrollbar(orient="vertical", command= tableTreeView.yview)
        xsb = ttk.Scrollbar(orient="horizontal", command= tableTreeView.xview)
        tableTreeView['yscroll'] = ysb.set
        tableTreeView['xscroll'] = xsb.set
        tableTreeView.insert('','0','item1',text="0xD",values=("1","2","3"))

        #selección
        subjectCveLB = Label(bottomFrame, text="Clave de materia:")
        subjectCveLB.grid(row=0, column=0)
        subjectCveENY = Entry(bottomFrame)
        subjectCveENY.grid(row=0, column=1)

        #Botones
        selectButton = Button(bottomFrame, text="Seleccionar")
        selectButton.grid(row = 0, column = 2)
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnStudentHome)
        returnButton.grid(row = 1, column = 3)

    def returnStudentHome(self):
        ##Add validations to return or close and open the other window
        self.app = Access(Tk())
        self.root.destroy()

class GroupsInscription:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Inscripción de grupos")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        tableTreeView = ttk.Treeview(topFrame)
        tableTreeView.grid(row=0, column=0)

        tableTreeView["columns"]=("Aula","Docente","Días(l-v)")
        tableTreeView.column("#0",width=120)
        tableTreeView.column("Aula",width=120)
        tableTreeView.column("Docente",width=120)
        tableTreeView.column("Días(l-v)",width=120)

        tableTreeView.heading('#0',text='Grupo')
        tableTreeView.heading('Aula', text='Aula')
        tableTreeView.heading('Docente', text='Docente')
        tableTreeView.heading('Días(l-v)', text='Días(l-v)')

        #selección
        subjectCveLB = Label(bottomFrame, text="Grupo:")
        subjectCveLB.grid(row=0, column=0)
        subjectCveENY = Entry(bottomFrame)
        subjectCveENY.grid(row=0, column=1)

        #Botones
        selectButton = Button(bottomFrame, text="Inscribir")
        selectButton.grid(row = 0, column = 2)
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnInscription)
        returnButton.grid(row = 1, column = 3)

    def returnInscription(self):
        ##Add validations to return or close and open the other window
        self.app = Inscription(Tk())
        self.root.destroy()

class StudentSchedule:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Horario")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root,width=500, height=100)
        bottomFrame.grid(row=1,column=0)
        #primer tabla
        tbTopTreeView = ttk.Treeview(topFrame, height=5)
        tbTopTreeView.grid(row=0, column=0)

        tbTopTreeView["columns"]=("Martes","Miércoles","Jueves")
        tbTopTreeView.column("#0",width=120)
        tbTopTreeView.column("Martes",width=120)
        tbTopTreeView.column("Miércoles",width=120)
        tbTopTreeView.column("Jueves",width=120)

        tbTopTreeView.heading('#0',text='Lunes')
        tbTopTreeView.heading('Martes', text='Martes')
        tbTopTreeView.heading('Miércoles', text='Miércoles')
        tbTopTreeView.heading('Jueves', text='Jueves')

        #segunda tabla
        tbBottomTreeView = ttk.Treeview(topFrame,height=5)
        tbBottomTreeView.grid(row=1, column=0)

        tbBottomTreeView["columns"]=("Materia","Docente")
        tbBottomTreeView.column("#0",width=166)
        tbBottomTreeView.column("Materia",width=166)
        tbBottomTreeView.column("Docente",width=166)

        tbBottomTreeView.heading('#0',text='Clave')
        tbBottomTreeView.heading('Materia', text='Materia')
        tbBottomTreeView.heading('Docente', text='Docente')

        #Botones
        returnButton = Button(bottomFrame, text="Regresar", command= self.returnStudentHome)
        returnButton.grid(row = 1, column = 3)

    def returnStudentHome(self):
        ##Add validations to return or close and open the other window
        self.app = Access(Tk())
        self.root.destroy()

class AdministrativeSchedule:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Consulta | Horario")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        #selección
        subjectCveLB = Label(topFrame, text="Matrícula:")
        subjectCveLB.grid(row=0, column=0)
        subjectCveENY = Entry(topFrame)
        subjectCveENY.grid(row=0, column=1)

        #Top Button
        selectButton = Button(topFrame, text="Consultar")
        selectButton.grid(row = 0, column = 2)

        #primer tabla
        tbTopTreeView = ttk.Treeview(bottomFrame, height=5)
        tbTopTreeView.grid(row=1, column=0)

        tbTopTreeView["columns"]=("Martes","Miércoles","Jueves")
        tbTopTreeView.column("#0",width=120)
        tbTopTreeView.column("Martes",width=120)
        tbTopTreeView.column("Miércoles",width=120)
        tbTopTreeView.column("Jueves",width=120)

        tbTopTreeView.heading('#0',text='Lunes')
        tbTopTreeView.heading('Martes', text='Martes')
        tbTopTreeView.heading('Miércoles', text='Miércoles')
        tbTopTreeView.heading('Jueves', text='Jueves')

        #segunda tabla
        tbBottomTreeView = ttk.Treeview(bottomFrame, height=5)
        tbBottomTreeView.grid(row=2, column=0)

        tbBottomTreeView["columns"]=("Materia","Docente")
        tbBottomTreeView.column("#0",width=166)
        tbBottomTreeView.column("Materia",width=166)
        tbBottomTreeView.column("Docente",width=166)

        tbBottomTreeView.heading('#0',text='Clave')
        tbBottomTreeView.heading('Materia', text='Materia')
        tbBottomTreeView.heading('Docente', text='Docente')

        #Bottom buttons
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnAdministrativeHome)
        returnButton.grid(row = 1, column = 3)

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        self.app = AdministrativeAccess(Tk())
        self.root.destroy()

class AdministrativeSubject:
    def __init__(self, root):
        self.root = root
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Consulta | Alumnos por materia")
        root.geometry('{}x{}'.format(500, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        #selección
        subjectCveLB = Label(topFrame, text="Matrícula:")
        subjectCveLB.grid(row=0, column=0)
        subjectCveENY = Entry(topFrame)
        subjectCveENY.grid(row=0, column=1)

        #Top Button
        selectButton = Button(topFrame, text="Buscar:")
        selectButton.grid(row = 0, column = 2)

        #primer tabla
        tbTopTreeView = ttk.Treeview(bottomFrame)
        tbTopTreeView.grid(row=0, column=0)

        tbTopTreeView["columns"]=("Nombre","Apellido Paterno","Apellido Materno")
        tbTopTreeView.column("#0",width=120)
        tbTopTreeView.column("Nombre",width=120)
        tbTopTreeView.column("Apellido Paterno",width=120)
        tbTopTreeView.column("Apellido Materno",width=120)

        tbTopTreeView.heading('#0',text='Matrícula')
        tbTopTreeView.heading('Nombre', text='Nombre')
        tbTopTreeView.heading('Apellido Paterno', text='Apellido Paterno')
        tbTopTreeView.heading('Apellido Materno', text='Apellido Materno')

        #Bottom buttons
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnAdministrativeHome)
        returnButton.grid(row = 1, column = 0)

    def returnAdministrativeHome(self):
        ##Add validations to return or close and open the other window
        self.app = AdministrativeAccess(Tk())
        self.root.destroy()


if __name__ == '__main__':
    """ CREACIÓN DE LA VENTANA DE ACCESO AL SISTEMA"""

    #Declara ventana de aplicación
    root = Tk()

    aplicacion = StudentSchedule(root)# prueba de nueva ventana

    #Bucle de la aplicación
    root.mainloop()
