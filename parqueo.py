###########################
# Dina Monge Sandoval     #
# William Mata Rodriguez  #
# Fecha: 21/06/2022       #
# Proyecto 3: parqueo     #
###########################

from tkinter import *
from tkinter import messagebox

class MenuPrincipal:
    def __init__(self, master):
        self.master = master
        
        self.canvas_menu = Canvas(self.master, width=500,height=500, highlightthickness=0)
        self.canvas_menu.place(x=0,y=0)

        self.boton = Button(self.canvas_menu, text='Configuración', command=self.ventana_cambiar_configuracion)
        self.boton.place(x=175,y=20, width=150)
        
        self.boton = Button(self.canvas_menu, text='Cargar cajero', command=self.ventana_cambiar_cargar_cajero)
        self.boton.place(x=175,y=60, width=150)
        
        self.boton = Button(self.canvas_menu, text='Saldo del cajero', command=self.ventana_cambiar_saldo_cajero)
        self.boton.place(x=175,y=100, width=150)
        
        self.boton = Button(self.canvas_menu, text='Ingresos de dinero', command=self.ventana_cambiar_ingresos_dinero)
        self.boton.place(x=175,y=140, width=150)

        self.boton = Button(self.canvas_menu, text='Entrada de vehiculo', command=self.ventana_cambiar_entrada_vehiculo)
        self.boton.place(x=175,y=180, width=150)
        
        self.boton = Button(self.canvas_menu, text='Cajero del parqueo', command=self.ventana_cambiar_cajero_parqueo)
        self.boton.place(x=175,y=220, width=150)
        
        self.boton = Button(self.canvas_menu, text='Salida de vehículo', command=self.ventana_cambiar_salida_vehiculo)
        self.boton.place(x=175,y=260, width=150)
        
        self.boton = Button(self.canvas_menu, text='Ayuda')
        self.boton.place(x=175,y=300, width=150)

        self.boton = Button(self.canvas_menu, text='Acerca de', command=self.ventana_cambiar_acerca_de)
        self.boton.place(x=175,y=340, width=150)

    def ventana_cambiar_configuracion(self):
        self.canvas_menu.destroy()
        self.master.geometry('500x500')
        Configuracion(self.master)

class Configuracion:
    def __init__(self, master):
        
        self.master = master
        self.master.geometry('500x500')
        self.canvas_configuracion = Canvas(self.master, width=500,height=500, highlightthickness=0)
        self.canvas_configuracion.place(x=0,y=0)
        self.label_configuracion = Label(self.canvas_configuracion, text='PARQUEO - CONFIGURACION')
        self.label_configuracion.place(x=10,y=10)
        
        self.label = Label(self.canvas_configuracion, text='Cantidad de espacios en el parqueo (entero >=1)')
        self.label.place(x=10,y=30)
        self.entrada_espacio = Entry(self.canvas_configuracion)
        self.entrada_espacio.place(x=440, y=30, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Precio por hora (flotante con máximo 2 decimales >=0)')
        self.label.place(x=10,y=70)
        self.entrada_precio = Entry(self.canvas_configuracion)
        self.entrada_precio.place(x=440, y=70, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Pago mínimo (flotante con máximo 2 decimales >=0)')
        self.label.place(x=10,y=110)
        self.entrada_pago = Entry(self.canvas_configuracion)
        self.entrada_pago.place(x=440, y=110, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Correo electrónico del supervisor')
        self.label.place(x=10,y=150)
        self.entrada_correo = Entry(self.canvas_configuracion)
        self.entrada_correo.place(x=340, y=150, width=150)
        
        self.label = Label(self.canvas_configuracion, text='Minutos máximos para salir después del pago (entero >=0)')
        self.label.place(x=10,y=190)
        self.entrada_minuto_salir = Entry(self.canvas_configuracion)
        self.entrada_minuto_salir.place(x=440, y=190, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Tipos de moneda (máximo 3 tipos, enteros >= 0):')
        self.label.place(x=10,y=230)
        self.entrada_cantidad_monedas = Entry(self.canvas_configuracion)
        self.entrada_cantidad_monedas.place(x=440, y=230, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Moneda 1, la de menor denominación (ejemplo 50)')
        self.label.place(x=10,y=250)
        self.entrada_monedas1 = Entry(self.canvas_configuracion)
        self.entrada_monedas1.place(x=440, y=250, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Moneda 2, denominación siguiente a la anterior (ejemplo 100)')
        self.label.place(x=10,y=270)
        self.entrada_monedas2 = Entry(self.canvas_configuracion)
        self.entrada_monedas2.place(x=440, y=270, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Moneda 3, denominación siguiente a la anterior (ejemplo 500)')
        self.label.place(x=10,y=290)
        self.entrada_monedas3 = Entry(self.canvas_configuracion)
        self.entrada_monedas3.place(x=440, y=290, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Tipos de billetes (máximo 5 tipos, enteros >= 0):')
        self.label.place(x=10,y=330)
        self.entrada_cantidad_billetes = Entry(self.canvas_configuracion)
        self.entrada_cantidad_billetes.place(x=440, y=330, width=50)

        self.label = Label(self.canvas_configuracion, text='Billete 1, el de menor denominación (ejemplo 1000)')
        self.label.place(x=10,y=350)
        self.entrada_billetes1 = Entry(self.canvas_configuracion)
        self.entrada_billetes1.place(x=440, y=350, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Billete 2, denominación siguiente a la anterior (ejemplo 2000)')
        self.label.place(x=10,y=370)
        self.entrada_billetes2 = Entry(self.canvas_configuracion)
        self.entrada_billetes2.place(x=440, y=370, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Billete 3, denominación siguiente a la anterior (ejemplo 5000)')
        self.label.place(x=10,y=390)
        self.entrada_billetes3 = Entry(self.canvas_configuracion)
        self.entrada_billetes3.place(x=440, y=390, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Billete 4, denominación siguiente a la anterior (ejemplo 10000)')
        self.label.place(x=10,y=410)
        self.entrada_billetes4 = Entry(self.canvas_configuracion)
        self.entrada_billetes4.place(x=440, y=410, width=50)
        
        self.label = Label(self.canvas_configuracion, text='Billete 5, denominación siguiente a la anterior (ejemplo 20000)')
        self.label.place(x=10,y=430)
        self.entrada_billetes5 = Entry(self.canvas_configuracion)
        self.entrada_billetes5.place(x=440, y=430, width=50)
        
        self.boton = Button(self.canvas_configuracion, text='Ok', command=self.guardar_configuracion)
        self.boton.place(x=145,y=465, width=100)
        self.boton = Button(self.canvas_configuracion, text='Cancelar', command=self.ventana_cambiar_menu)
        self.boton.place(x=250,y=465, width=100)

    def guardar_configuracion(self):
        f = open('configuración.dat', 'w')
        espacio = self.entrada_espacio.get()
        if int(espacio) <1:
            return messagebox.showerror('Error', 'La cantidad de espacio debe de ser mayor o igual a 1')
        precio = self.entrada_precio.get()
        if float(precio) <0:
            return messagebox.showerror('Error', 'El pago minimo debe de ser mayor o igual a 0')
        pago = self.entrada_pago.get()
        if float(pago) <0:
            return messagebox.showerror('Error', 'La precio debe de ser mayor o igual a 0')
        correo = self.entrada_correo.get()
        minutos_salir = self.entrada_minuto_salir.get()
        if int(minutos_salir) <0:
            return messagebox.showerror('Error', 'Los minutos maximos para salir deben de ser mayor o igual a 0')
        cantidad_monedas = self.entrada_cantidad_monedas.get()
        if int(cantidad_monedas) <0 or int(cantidad_monedas)>3:
            return messagebox.showerror('Error', 'Los tipos de monedas deben de ser mayor o igual a 0 y menor o igual 3')
        monedas1 = self.entrada_monedas1.get()
        if int(monedas1) <0:
            return messagebox.showerror('Error', 'Las monedas deben de ser mayor o igual a 0')
        monedas2 = self.entrada_monedas2.get()
        if int(monedas2) <0:
            return messagebox.showerror('Error', 'Las monedas deben de ser mayor o igual a 0')
        monedas3 = self.entrada_monedas3.get()
        if int(monedas3) <0:
            return messagebox.showerror('Error', 'Las monedas deben de ser mayor o igual a 0')
        cantidad_billetes = self.entrada_cantidad_billetes.get()
        if int(cantidad_billetes) <0 or int(cantidad_billetes)>5:
            return messagebox.showerror('Error', 'Los tipos de billetes deben de ser mayor o igual a 0 y menor o igual 3')
        billetes1 = self.entrada_billetes1.get()
        if int(billetes1) <0:
            return messagebox.showerror('Error', 'Los billetes deben de ser mayor o igual a 0')
        billetes2 = self.entrada_billetes2.get()
        if int(billetes2) <0:
            return messagebox.showerror('Error', 'Los billetes deben de ser mayor o igual a 0')
        billetes3 = self.entrada_billetes3.get()
        if int(billetes3) <0:
            return messagebox.showerror('Error', 'Los billetes deben de ser mayor o igual a 0')
        billetes4 = self.entrada_billetes4.get()
        if int(billetes4) <0:
            return messagebox.showerror('Error', 'Los billetes deben de ser mayor o igual a 0')
        billetes5 = self.entrada_billetes5.get()
        if int(billetes5) <0:
            return messagebox.showerror('Error', 'Los billetes deben de ser mayor o igual a 0')
        f.writelines([espacio+'\n', precio+'\n', pago+'\n', correo+'\n', minutos_salir+'\n', cantidad_monedas+'\n', monedas1+'\n', monedas2+'\n', monedas3+'\n', cantidad_billetes+'\n', billetes1+'\n', billetes2+'\n', billetes3+'\n', billetes4+'\n', billetes5+'\n'])
        f.close()
         
    def ventana_cambiar_menu(self):
        self.canvas_configuracion.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master) 

window = Tk()
MenuPrincipal(window)
window.title('Proyecto')
window.geometry('500x500')
window.mainloop()