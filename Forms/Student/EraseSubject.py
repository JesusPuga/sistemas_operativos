import sys
from Validations.loadSubjects import *
from Forms.centerForm import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class EraseSubject:
    def __init__(self, old_root, clave):
        h = 300
        w = 600
        old_root.destroy()
        self.new_root = centerForm(w,h,"Sistema de Inscripción | Dar de baja")
        self.clave = clave
        self.subject = None

        topFrame = Frame(self.new_root, width=500, height=200)
        topFrame.grid(row=1,column=0)
        bottomFrame = Frame(self.new_root, width=500, height=100)
        bottomFrame.grid(row=2,column=0,sticky=E,padx=(0,30))

        #configuración de tabla
        self.tableTreeView = ttk.Treeview(topFrame)
        self.tableTreeView.grid(row=0, column=0,padx=(25,25),pady=(15,15))
        self.tableTreeView["columns"]=("Materia")
        self.tableTreeView.column("#0",width=50)
        self.tableTreeView.column("Materia",width=500)

        self.tableTreeView.heading('#0',text='Clave')
        self.tableTreeView.heading('Materia', text='Materia')

        # Función para borrar con doble clic
        self.tableTreeView.bind("<Double-1>", self.deleteSubject)

        ##en prueba, creo que es pa' los datos xD
        ysb = ttk.Scrollbar(orient="vertical", command= self.tableTreeView.yview)
        xsb = ttk.Scrollbar(orient="horizontal", command= self.tableTreeView.xview)
        self.tableTreeView['yscroll'] = ysb.set
        self.tableTreeView['xscroll'] = xsb.set

        #Cargar inf en tabla
        self.showAvailableSubjects()

        #Botones
        returnButton = Button(bottomFrame, text="Regresar", command=self.returnStudentHome)
        returnButton.grid(row = 0, column = 1)

        self.new_root.mainloop()

    def showAvailableSubjects(self):
        self.tableTreeView.delete(*self.tableTreeView.get_children())
        subjects = loadRegisteredSubjects(self.clave)

        for cvMateria, nom, grupo in subjects:
            self.tableTreeView.insert('','0',text=cvMateria, value=(nom,grupo))

    def deleteSubject(self, event):
        '''Función que borra un grupo inscrito mediante el evento doble clic

        Parametros:
            event           -   Tipo de evento que acciona la función. En ese caso <Double-1> , para doble clic

        Variables:
            curItem         -   Contiene los registros de la fila del elemento seleccionado con doble clic
            subjectClave    -   Contiene la clave de la materia obtenido mediante la función
                                simpleShowRegisteredSubject() en el método showAvailableSubjects()
            IDGrupo         -   Contiene el IDGrupo (no su clave, véase Nota)
                                obtenido mediante la función simpleShowRegisteredSubject() en método showAvailableSubjects()

            Nota: El IDGrupo en el modelo de base de datos, es el registro llave que permite alamacenar n cantidad de grupos
            independiente de la materia, la claveGrupo es el registro que permite alamcenar para una materia n cantidad de grupos
        '''

        curItem = self.tableTreeView.item(self.tableTreeView.focus())
        subjectClave = curItem['text']
        IDGrupo = curItem['values'][1]

        #LLAMADO A LA FUNCIÓN DE BORRADO EN LA BASE DE DATOS
        eraseSubject(self.clave,IDGrupo,subjectClave)
        messagebox.showinfo("Aviso","Materia Eliminada")

        #DESPUÉS DE EJECUTAR EL BORRADO, SE VUELVE A DESPLEGAR LA VISTA ACTUALIZADA
        self.showAvailableSubjects()

    def returnStudentHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('Forms.Student.StudentAccess',None,None,['StudentAccess'], 0)
        self.app = window.StudentAccess(self.new_root, self.clave)
