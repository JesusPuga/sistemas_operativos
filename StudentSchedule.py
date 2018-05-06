import sys
from Validaciones import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class StudentSchedule:
    def __init__(self, old_root,clave):
        old_root.destroy()
        self.new_root = Tk()
        self.clave = clave
        #Se define el nombre de la ventana y se restringe el tamaño de la misma
        self.new_root.title("Horario")
        self.new_root.geometry('{}x{}'.format(1300, 600))
        self.new_root.resizable(0,0)
        # layout all of the main containers
        self.new_root.grid_rowconfigure(1, weight=1)
        self.new_root.grid_columnconfigure(0, weight=1)


        #Frames a usar, algo así como div b:
        topFrame = Frame(self.new_root, width=500, height=200)
        topFrame.grid(row=0,column=0)

        bottomFrame = Frame(self.new_root,width=500, height=100)
        bottomFrame.grid(row=1,column=0)
        #primer tabla
        style = ttk.Style(self.new_root)
        style.configure('Treeview', rowheight=50)
        self.tbTopTreeView = ttk.Treeview(topFrame, height=5)
        self.tbTopTreeView.grid(row=0, column=0)

        self.tbTopTreeView["columns"]=("Lunes","Martes","Miércoles","Jueves","Viernes","Sabado")
        self.tbTopTreeView.column("#0",width=170)
        self.tbTopTreeView.column("Martes",width=170)
        self.tbTopTreeView.column("Miércoles",width=170)
        self.tbTopTreeView.column("Jueves",width=170)
        self.tbTopTreeView.column("Viernes",width=170)
        self.tbTopTreeView.column("Sabado",width=170)

        self.tbTopTreeView.heading('#0',text='Hora')
        self.tbTopTreeView.heading('Lunes', text='Lunes')
        self.tbTopTreeView.heading('Martes', text='Martes')
        self.tbTopTreeView.heading('Miércoles', text='Miércoles')
        self.tbTopTreeView.heading('Jueves', text='Jueves')
        self.tbTopTreeView.heading('Viernes', text='Viernes')
        self.tbTopTreeView.heading('Sabado', text='Sábado')

        #segunda tabla
        self.tbBottomTreeView = ttk.Treeview(topFrame,height=5)
        self.tbBottomTreeView.grid(row=1, column=0)

        self.tbBottomTreeView["columns"]=("Grupo","Materia","Docente")
        self.tbBottomTreeView.column("#0",width=166)
        self.tbBottomTreeView.column("Grupo",width=166)
        self.tbBottomTreeView.column("Materia",width=166)
        self.tbBottomTreeView.column("Docente",width=166)

        self.tbBottomTreeView.heading('#0',text='Clave')
        self.tbBottomTreeView.heading('Grupo', text='Grupo')
        self.tbBottomTreeView.heading('Materia', text='Materia')
        self.tbBottomTreeView.heading('Docente', text='Docente')

        #Botones
        returnButton = Button(bottomFrame, text="Regresar", command= self.returnStudentHome)
        returnButton.grid(row = 1, column = 3)

        self.showStudentSchedule()
        self.new_root.mainloop()


    def orderSchedule(self,materia,dia,horario,horaInicio,horaFin):
        if dia == 'LUNES':
            horario['LUNES']= materia + '\n' + str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'MARTES':
            horario['MARTES'] = materia + '\n' + str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'MIÉRCOLES':
            horario['MIERCOLES'] = materia + '\n' + str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'JUEVES':
            horario['JUEVES'] = materia + '\n' + str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'VIERNES':
            horario['VIERNES'] = materia + '\n' + str(horaInicio)  + ' - ' +str(horaFin)
        if dia == 'SÁBADO':
            horario['SABADO'] = materia + '\n' + str(horaInicio)  + ' - ' +str(horaFin)

        return horario


    def showStudentSchedule(self):
        claveMateria = []
        materias = findStudentSchedule(self.clave)
        index = 0
        contador = 0
        """Este primer iterador solo obtiene primeros valores para poder hacer comparaciones posteriores"""
        for materiaClave, grupoClave, materia, docente, dia, horaInicio, horaFin, in materias:
            claveMateria.append(materiaClave)
            break

        """Con este segundo iterador sabremos cuantos grupos existen y su ID"""
        for materiaClave, grupoClave, materia, docente, dia, horaInicio, horaFin, in materias:
            if materiaClave != claveMateria[contador]:
                contador +=1
                claveMateria.append(materiaClave)
        """Con este segundo iterador guardaremos los datos de los n grupos"""
        contador=0
        horario = {'CLAVE':'','GRUPO':'','MATERIA':'','DOCENTE':'','LUNES':'', 'MARTES':'','MIERCOLES':'', 'JUEVES':'', 'VIERNES':'', 'SABADO':''}
        for materiaClave, grupoClave, materia, docente, dia, horaInicio, horaFin, in materias:
            if materiaClave != claveMateria[contador]:
                self.tbBottomTreeView.insert('','0',index,text=horario['CLAVE'],values=(horario['GRUPO'],horario['MATERIA'],horario['DOCENTE']))
                self.tbTopTreeView.insert('','0',index,text=horario['LUNES'],values=(horario['MARTES'],horario['MIERCOLES'],horario['JUEVES'],horario['VIERNES'],horario['SABADO']))
                contador +=1
                index +=1
                horario = {'CLAVE':'','GRUPO':'','MATERIA':'','DOCENTE':'','LUNES':'', 'MARTES':'','MIERCOLES':'', 'JUEVES':'', 'VIERNES':'', 'SABADO':''}
                horario['CLAVE']= materiaClave
                horario = self.orderSchedule(materia,dia,horario,horaInicio,horaFin)
            else:
                if materiaClave == claveMateria[contador]:
                    horario['CLAVE']= materiaClave
                    horario['GRUPO']=grupoClave
                    horario['MATERIA']=materia
                    horario['DOCENTE']=docente
                    horario = self.orderSchedule(materia,dia,horario,horaInicio,horaFin)

        self.tbTopTreeView.insert('','0',index,text=horario['LUNES'],values=(horario['MARTES'],horario['MIERCOLES'],horario['JUEVES'],horario['VIERNES'],horario['SABADO']))
        self.tbBottomTreeView.insert('','0',index,text=horario['CLAVE'],values=(horario['GRUPO'],horario['MATERIA'],horario['DOCENTE']))





    def returnStudentHome(self):
        ##Add validations to return or close and open the other window
        window = __import__('StudentAccess')
        self.app = window.StudentAccess(self.new_root,self.clave)
