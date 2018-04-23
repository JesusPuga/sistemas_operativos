import sys
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
                self.app = AdministrativeAccess(new_root,clave)
            elif self.tipoUsuarioCBX.get() == "Alumno":
                self.app = StudentAccess(new_root, clave)
            self.root.destroy()
        else:
            messagebox.showwarning("Error",result)

class StudentAccess:
    def __init__(self, root, clave):
        self.root = root
        self.clave = clave
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

        #REVISAR ESTATUS DE ALUMNO
        query= """SELECT Alumno.estatus FROM Alumno WHERE Alumno.carnetAlumno = %s"""
        result = con.execute_query(query,(clave,),True)

        #CAPTURA DEL CONTENIDO DE LA CONSULTA. SE GUARDA EL ESTATUS DEL ALUMNO ("PRIMER INGRESO", "REINGRESO", "NO INSCRITO")"
        for x in result: estatus=x[0]

        #Botones
        if estatus == 'PRIMER INGRESO':
            inscriptionButton = Button(leftFrame, text="Inscribir", state=DISABLED, command= self.openInscription)
            inscriptionButton.grid(row = 1, column = 0)
            scheduleButton = Button(leftFrame, text="Horario", command= self.openSchedule)
            scheduleButton.grid(row = 2, column = 0)
            sessionButton = Button(leftFrame, text="Cerrar Sesión", command= self.quit)
            sessionButton.grid(row = 3, column = 0)
        elif estatus == 'REINGRESO':
            inscriptionButton = Button(leftFrame, text="Inscribir", command= self.openInscription)
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
        self.app = Inscription(Tk(),self.clave)
        self.root.destroy()

    def openSchedule(self):
        self.app = StudentSchedule(Tk())
        self.root.destroy()

class AdministrativeAccess:
    def __init__(self, root,clave):
        self.root = root
        self.clave = clave
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
        self.app = Access(Tk(),self.clave)
        self.root.destroy()

    def openSubjects(self):
        self.app = AdministrativeSubject(Tk(),self.clave)
        self.root.destroy()

    def openSchedule(self):
        self.app = AdministrativeSchedule(Tk(),self.clave)
        self.root.destroy()

class Inscription:
    def __init__(self, root, clave):
        self.root = root
        self.clave = clave
        self.subject = None
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Inscripción")
        root.geometry('{}x{}'.format(600, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        counterFrame = Frame(root, width=500, height=50)
        counterFrame.grid(row=0,column=0)
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=1,column=0)
        bottomFrame = Frame(root, width=500, height=100)
        bottomFrame.grid(row=2,column=0)

        #créditos utilizados
        self.subjectCveLB = Label(counterFrame, text="Créditos utilizados: ")
        self.subjectCveLB.grid(row=0, column=0)
        ##espacio a la izquierda xD
        subject1CveLB = Label(counterFrame,
                                  text="""
                                  """)
        subject2CveLB = Label(counterFrame,
                                  text="""
                                  """)
        subject1CveLB.grid(row=0, column=1)
        subject2CveLB.grid(row=0, column=2)

        #configuración de tabla
        self.tableTreeView = ttk.Treeview(topFrame)
        self.tableTreeView.grid(row=0, column=0)

        self.tableTreeView["columns"]=("Materia","Semestre","Créditos")
        self.tableTreeView.column("#0",width=50)
        self.tableTreeView.column("Materia",width=270)
        self.tableTreeView.column("Semestre",width=80)
        self.tableTreeView.column("Créditos",width=80)

        self.tableTreeView.heading('#0',text='Clave')
        self.tableTreeView.heading('Materia', text='Materia')
        self.tableTreeView.heading('Semestre', text='Semestre')
        self.tableTreeView.heading('Créditos', text='Créditos')

        # Función para el double clic
        self.tableTreeView.bind("<Double-1>", self.onDoubleClick)

        ##en prueba, creo que es pa' los datos xD
        ysb = ttk.Scrollbar(orient="vertical", command= self.tableTreeView.yview)
        xsb = ttk.Scrollbar(orient="horizontal", command= self.tableTreeView.xview)
        self.tableTreeView['yscroll'] = ysb.set
        self.tableTreeView['xscroll'] = xsb.set

        #Cargar inf en tabla
        self.showAvailableSubjects()


        #selección, checar, para usar es necesario obtener el id en la tb
        #subjectCveLB = Label(bottomFrame, text="Materia:")
        #subjectCveLB.grid(row=0, column=0)
        ##self.subjectCveENY = Entry(bottomFrame)
        #self.subjectCveENY.grid(row=0, column=1)

        #Botones

        returnButton = Button(bottomFrame, text="Regresar", command=self.returnStudentHome)
        returnButton.grid(row = 0, column = 1)

    def showAvailableSubjects(self):
        subjects = findAvailableSubjects(self.clave)
        for cvMateria, nom, sem, creditos in subjects:
            self.tableTreeView.insert('','0',cvMateria,text=cvMateria,values=(nom,sem,creditos))

    def returnStudentHome(self):
        ##Add validations to return or close and open the other window
        self.app = StudentAccess(Tk(), self.clave)
        self.root.destroy()

    def onDoubleClick(self, event):
        cursoItem = self.tableTreeView.focus()
        self.subject = self.tableTreeView.item(cursoItem)["values"][0]
        if self.subject == None:
            self.erroMsgLB["text"] = "Selecciona una materia"
        else:
            self.app = GroupsInscription(Tk(), self.clave, self.subject)
            self.root.destroy()


class GroupsInscription:
    def __init__(self, root,clave, subject):
        self.root = root
        self.clave = clave
        self.subject = subject
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        root.title("Sistema de Inscripción | Inscripción de grupos")
        root.geometry('{}x{}'.format(1100, 300))
        root.resizable(0,0)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Frames a usar, algo así como div b:
        topFrame = Frame(root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(root, width=500, height=100)
        bottomFrame.grid(row=1,column=0)

        self.tableTreeView = ttk.Treeview(topFrame)
        self.tableTreeView.grid(row=0, column=0)

        ##se hará dinámicamente
        self.tableTreeView["columns"]=("Grupo","Aula","Docente","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado")
        self.tableTreeView.column("#0",width=10)
        self.tableTreeView.column("Aula",width=50)
        self.tableTreeView.column("Docente",width=200)
        self.tableTreeView.column("Lunes",width=100)
        self.tableTreeView.column("Martes",width=100)
        self.tableTreeView.column("Miércoles",width=100)
        self.tableTreeView.column("Jueves",width=100)
        self.tableTreeView.column("Viernes",width=100)
        self.tableTreeView.column("Sábado",width=100)

        self.tableTreeView.heading('#0',text='')
        self.tableTreeView.heading('Grupo', text='Grupo')
        self.tableTreeView.heading('Aula', text='Aula')
        self.tableTreeView.heading('Docente', text='Docente')
        self.tableTreeView.heading('Lunes', text='Lunes')
        self.tableTreeView.heading('Martes', text='Martes')
        self.tableTreeView.heading('Miércoles', text='Miércoles')
        self.tableTreeView.heading('Jueves', text='Jueves')
        self.tableTreeView.heading('Viernes', text='Viernes')
        self.tableTreeView.heading('Sábado', text='Sábado')

        #selección
        subjectCveLB = Label(bottomFrame, text="Grupo:")
        subjectCveLB.grid(row=0, column=0)
        subjectCveENY = Entry(bottomFrame)
        subjectCveENY.grid(row=0, column=1)

        #Botones
        selectButton = Button(bottomFrame, text="Inscribir", command = self.addToSchedule)
        selectButton.grid(row = 0, column = 2)
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnInscription)
        returnButton.grid(row = 1, column = 3)

        ##carga información
        self.showAvailableTeachers()

    def addToSchedule(self):
        return False

    def showAvailableTeachers(self):
        teachers = findAvailableTeachers(self.subject)
        index = 1
        for grupo, aula, docente, horarios in teachers:
            self.tableTreeView.insert('','0',index,text=index,values=(grupo,aula,docente,horarios))
            index += 1

    def selectItem(self):
        curItem = self.tableTreeView.focus()
        print(self.tableTreeView.item(curItem))

    def returnInscription(self):
        ##Add validations to return or close and open the other window
        self.app = Inscription(Tk(), self.clave)
        self.root.destroy()

class StudentSchedule:
    def __init__(self, root,clave):
        self.root = root
        self.clave = clave
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
        self.app = StudentAccess(Tk(),self.clave)
        self.root.destroy()

class AdministrativeSchedule:
    def __init__(self, root,clave):
        self.root = root
        self.clave = clave
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
        self.app = AdministrativeAccess(Tk(),self.clave)
        self.root.destroy()

class AdministrativeSubject:
    def __init__(self, root,clave):
        self.root = root
        self.clave = clave
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
        self.app = AdministrativeAccess(Tk(),self.clave)
        self.root.destroy()


if __name__ == '__main__':
    """ CREACIÓN DE LA VENTANA DE ACCESO AL SISTEMA"""

    #Declara ventana de aplicación
    root = Tk()

    #LLamado a la aplicación mediante la ventana de acceso al sistema
    app = Access(root)

    #aplicacion = Inscription(root,2)# prueba de nueva ventana

    #Bucle de la aplicación
root.mainloop()
