###########################
# Dina Monge Sandoval     #
# William Mata Rodriguez  #
# Fecha: 21/06/2022       #
# Proyecto 3: parqueo     #
###########################

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

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
        
        self.boton = Button(self.canvas_menu, text='Ayuda', command=self.ventana_cambiar_ayuda)
        self.boton.place(x=175,y=300, width=150)

        self.boton = Button(self.canvas_menu, text='Acerca de', command=self.ventana_cambiar_acerca_de)
        self.boton.place(x=175,y=340, width=150)

        self.boton = Button(self.canvas_menu, text='Salir', command=self.ventana_cambiar_salir)
        self.boton.place(x=175,y=380, width=150)
        
    def ventana_cambiar_configuracion(self):
        self.canvas_menu.destroy()
        self.master.geometry('500x500')
        Configuracion(self.master)
    def ventana_cambiar_cargar_cajero(self):
        self.canvas_menu.destroy()
        self.master.geometry('500x500')
        CargarCajero(self.master)
    def ventana_cambiar_saldo_cajero(self):
        self.canvas_menu.destroy()
        self.master.geometry('500x500')
        SaldoCajero(self.master)
    def ventana_cambiar_ingresos_dinero(self):
        self.canvas_menu.destroy()
        self.master.geometry('500x500')
        IngresosDinero(self.master)
    def ventana_cambiar_entrada_vehiculo(self):
        self.canvas_menu.destroy()
        self.master.geometry('500x500')
        EntradaVehiculo(self.master)
    def ventana_cambiar_cajero_parqueo(self):
        self.canvas_menu.destroy()
        self.master.geometry('500x500')
        CajeroParqueo(self.master)
    def ventana_cambiar_salida_vehiculo(self):
        self.canvas_menu.destroy()
        self.master.geometry('500x500')
        SalidaVehiculo(self.master)
    def ventana_cambiar_ayuda(self):
        ruta = 'manual_de_usuario_parqueo.pdf'
        os.system(ruta)
    def ventana_cambiar_acerca_de(self):
        self.canvas_menu.destroy()
        self.master.geometry('500x500')
        AcercaDe(self.master)
    def ventana_cambiar_salir(self):
        self.master.destroy()

        
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
        
        self.label = Label(self.canvas_configuracion, text='Tipos de moneda (Monedas de CR):')
        self.label.place(x=10,y=230)

        
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
        
        self.label = Label(self.canvas_configuracion, text='Tipos de billetes (Billetes de CR):')
        self.label.place(x=10,y=330)

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
        monedas1 = self.entrada_monedas1.get()
        if int(monedas1) <0:
            return messagebox.showerror('Error', 'Las monedas deben de ser mayor o igual a 0')
        monedas2 = self.entrada_monedas2.get()
        if int(monedas2) <0:
            return messagebox.showerror('Error', 'Las monedas deben de ser mayor o igual a 0')
        monedas3 = self.entrada_monedas3.get()
        if int(monedas3) <0:
            return messagebox.showerror('Error', 'Las monedas deben de ser mayor o igual a 0')
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
        # Monedas
        if int(monedas1) > int(monedas2):
            return messagebox.showerror('Error', 'La moneda 1 debe ser menor a la moneda 2')
        if int(monedas1) > int(monedas3):
            return messagebox.showerror('Error', 'La moneda 1 debe ser menor a la moneda 3')
        if int(monedas2) > int(monedas3):
            return messagebox.showerror('Error', 'La moneda 2 debe ser menor a la moneda 3')

        # Billetes
        if int(billetes1) > int(billetes2):
            return messagebox.showerror('Error', 'El billete 1 debe ser menor a el billete 2')
        if int(billetes1) > int(billetes3):
            return messagebox.showerror('Error', 'El billete 1 debe ser menor a el billete 3')
        if int(billetes1) > int(billetes4):
            return messagebox.showerror('Error', 'El billete 1 debe ser menor a el billete 4')
        if int(billetes1) > int(billetes5):
            return messagebox.showerror('Error', 'El billete 1 debe ser menor a el billete 5')

        if int(billetes2) > int(billetes3):
            return messagebox.showerror('Error', 'El billete 2 debe ser menor a el billete 3')
        if int(billetes2) > int(billetes4):
            return messagebox.showerror('Error', 'El billete 2 debe ser menor a el billete 4')
        if int(billetes2) > int(billetes5):
            return messagebox.showerror('Error', 'El billete 2 debe ser menor a el billete 5')

        if int(billetes3) > int(billetes4):
            return messagebox.showerror('Error', 'El billete 3 debe ser menor a el billete 4')
        if int(billetes3) > int(billetes5):
            return messagebox.showerror('Error', 'El billete 3 debe ser menor a el billete 5')
        
        if int(billetes4) > int(billetes5):
            return messagebox.showerror('Error', 'El billete 4 debe ser menor a el billete 5')

            
        f.writelines([espacio+'\n', precio+'\n', pago+'\n', correo+'\n', minutos_salir+'\n', monedas1+'\n', monedas2+'\n', monedas3+'\n', billetes1+'\n', billetes2+'\n', billetes3+'\n', billetes4+'\n', billetes5+'\n'])
        f.close()
         
    def ventana_cambiar_menu(self):
        self.canvas_configuracion.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

 
class CargarCajero:
    def __init__(self, master):

        f = open('configuración.dat','r')

        conf = []    
        for line in f:
            conf.append(line[:-1])
        f.close()

        f = open('cajero.dat','r')
        cajero = eval(f.read())
       
        self.master = master
        self.master.geometry('800x400')
        self.canvas_cargar = Canvas(self.master, width=500,height=500, highlightthickness=0)
        self.canvas_cargar.place(x=0,y=0)
        self.label_cargar = Label(self.canvas_cargar, text='PARQUEO - CARGAR CAJERO')
        self.label_cargar.grid(row=0,column=0)
        
        self.label_cargar = Label(self.canvas_cargar, text='SALDO ANTES DE LA CARGA')
        self.label_cargar.grid(row=1,column=1,columnspan=3)
        self.label_cargar = Label(self.canvas_cargar, text='          CARGA')
        self.label_cargar.grid(row=1,column=4,columnspan=3)
        self.label_cargar = Label(self.canvas_cargar, text='                                       SALDO')
        self.label_cargar.grid(row=1,column=9,columnspan=3)
        
        self.label_cargar = Label(self.canvas_cargar, text='DENOMINACIÓN')
        self.label_cargar.grid(row=2,column=0)
        self.label_denominacion_monedast1 = Label(self.canvas_cargar, text='Monedas de '+conf[5])
        self.label_denominacion_monedast1.grid(row=3,column=0)
        self.label_denominacion_monedast2 = Label(self.canvas_cargar, text='Monedas de '+conf[6])
        self.label_denominacion_monedast2.grid(row=4,column=0)
        self.label_denominacion_monedast3 = Label(self.canvas_cargar, text='Monedas de '+conf[7])
        self.label_denominacion_monedast3.grid(row=5,column=0)
        self.label_denominacion_total_monedas = Label(self.canvas_cargar, text='TOTAL DE MONEDAS')
        self.label_denominacion_total_monedas.grid(row=6,column=0)
        self.label_denominacion_espacio1 = Label(self.canvas_cargar, text='')
        self.label_denominacion_espacio1.grid(row=7,column=0)
        self.label_denominacion_billetest1 = Label(self.canvas_cargar, text='Billetes de '+conf[8])
        self.label_denominacion_billetest1.grid(row=8,column=0)
        self.label_denominacion_billetest2 = Label(self.canvas_cargar, text='Billetes de '+conf[9])
        self.label_denominacion_billetest2.grid(row=9,column=0)
        self.label_denominacion_billetest3 = Label(self.canvas_cargar, text='Billetes de '+conf[10])
        self.label_denominacion_billetest3.grid(row=10,column=0)
        self.label_denominacion_billetest4 = Label(self.canvas_cargar, text='Billetes de '+conf[11])
        self.label_denominacion_billetest4.grid(row=11,column=0)
        self.label_denominacion_billetest5 = Label(self.canvas_cargar, text='Billetes de '+conf[12])
        self.label_denominacion_billetest5.grid(row=12,column=0)
        self.label_denominacion_total_billetes = Label(self.canvas_cargar, text='TOTAL DE BILLETES')
        self.label_denominacion_total_billetes.grid(row=13,column=0)
        self.label_denominacion_espacio2 = Label(self.canvas_cargar, text='')
        self.label_denominacion_espacio2.grid(row=14,column=0)
        self.label_denominacion_total_cajero = Label(self.canvas_cargar, text='TOTAL DEL CAJERO')
        self.label_denominacion_total_cajero.grid(row=15,column=0)

        self.label_cargar = Label(self.canvas_cargar, text='CANTIDAD')
        self.label_cargar.grid(row=2,column=1)
        self.label_antescargar_cantidad_monedast1 = Label(self.canvas_cargar, text=cajero[conf[5]])
        self.label_antescargar_cantidad_monedast1.grid(row=3,column=1)
        self.label_antescargar_cantidad_monedast2 = Label(self.canvas_cargar, text=cajero[conf[6]])
        self.label_antescargar_cantidad_monedast2.grid(row=4,column=1)
        self.label_antescargar_cantidad_monedast3 = Label(self.canvas_cargar, text=cajero[conf[7]])
        self.label_antescargar_cantidad_monedast3.grid(row=5,column=1)
        self.label_antescargar_cantidad_total_monedas = Label(self.canvas_cargar, text=cajero[conf[5]]+cajero[conf[6]]+cajero[conf[7]])
        self.label_antescargar_cantidad_total_monedas.grid(row=6,column=1)
        self.label_antescargar_cantidad_espacio1 = Label(self.canvas_cargar, text='')
        self.label_antescargar_cantidad_espacio1.grid(row=7,column=1)
        self.label_antescargar_cantidad_billetest1 = Label(self.canvas_cargar, text=cajero[conf[8]])
        self.label_antescargar_cantidad_billetest1.grid(row=8,column=1)
        self.label_antescargar_cantidad_billetest2 = Label(self.canvas_cargar, text=cajero[conf[9]])
        self.label_antescargar_cantidad_billetest2.grid(row=9,column=1)
        self.label_antescargar_cantidad_billetest3 = Label(self.canvas_cargar, text=cajero[conf[10]])
        self.label_antescargar_cantidad_billetest3.grid(row=10,column=1)
        self.label_antescargar_cantidad_billetest4 = Label(self.canvas_cargar, text=cajero[conf[11]])
        self.label_antescargar_cantidad_billetest4.grid(row=11,column=1)
        self.label_antescargar_cantidad_billetest5 = Label(self.canvas_cargar, text=cajero[conf[12]])
        self.label_antescargar_cantidad_billetest5.grid(row=12,column=1)
        self.label_antescargar_cantidad_total_billetes = Label(self.canvas_cargar, text=cajero[conf[8]]+cajero[conf[9]]+cajero[conf[10]]+cajero[conf[11]]+cajero[conf[12]])
        self.label_antescargar_cantidad_total_billetes.grid(row=13,column=1)
        
        self.label_cargar = Label(self.canvas_cargar, text='TOTAL')
        self.label_cargar.grid(row=2,column=2)
        self.label_antescargar_total_monedast1 = Label(self.canvas_cargar, text=cajero[conf[5]]*int(conf[5]))
        self.label_antescargar_total_monedast1.grid(row=3,column=2)
        self.label_antescargar_total_monedast2 = Label(self.canvas_cargar, text=cajero[conf[6]]*int(conf[6]))
        self.label_antescargar_total_monedast2.grid(row=4,column=2)
        self.label_antescargar_total_monedast3 = Label(self.canvas_cargar, text=cajero[conf[7]]*int(conf[7]))
        self.label_antescargar_total_monedast3.grid(row=5,column=2)
        self.label_antescargar_total_total_monedas = Label(self.canvas_cargar, text=cajero[conf[5]]*int(conf[5])+cajero[conf[6]]*int(conf[6])+cajero[conf[7]]*int(conf[7]))
        self.label_antescargar_total_total_monedas.grid(row=6,column=2)
        self.label_antescargar_total_espacio1 = Label(self.canvas_cargar, text='')
        self.label_antescargar_total_espacio1.grid(row=7,column=2)
        self.label_antescargar_total_billetest1 = Label(self.canvas_cargar, text=cajero[conf[8]]*int(conf[8]))
        self.label_antescargar_total_billetest1.grid(row=8,column=2)
        self.label_antescargar_total_billetest2 = Label(self.canvas_cargar, text=cajero[conf[9]]*int(conf[9]))
        self.label_antescargar_total_billetest2.grid(row=9,column=2)
        self.label_antescargar_total_billetest3 = Label(self.canvas_cargar, text=cajero[conf[10]]*int(conf[10]))
        self.label_antescargar_total_billetest3.grid(row=10,column=2)
        self.label_antescargar_total_billetest4 = Label(self.canvas_cargar, text=cajero[conf[11]]*int(conf[11]))
        self.label_antescargar_total_billetest4.grid(row=11,column=2)
        self.label_antescargar_total_billetest5 = Label(self.canvas_cargar, text=cajero[conf[12]]*int(conf[12]))
        self.label_antescargar_total_billetest5.grid(row=12,column=2)
        self.label_antescargar_total_total_billetes = Label(self.canvas_cargar, text=cajero[conf[8]]*int(conf[8])+cajero[conf[9]]*int(conf[9])+cajero[conf[10]]*int(conf[10])+cajero[conf[11]]*int(conf[11])+cajero[conf[12]]*int(conf[12]))
        self.label_antescargar_total_total_billetes.grid(row=13,column=2)

        self.label_cargar = Label(self.canvas_cargar, text='  CANTIDAD')
        self.label_cargar.grid(row=2,column=4)
        
        self.label_carga_cantidad_monedast1 = tk.Entry(self.canvas_cargar)
        self.label_carga_cantidad_monedast1.insert(0,0)
        self.label_carga_cantidad_monedast1.grid(row=3,column=4)

        self.label_carga_cantidad_monedast2 = tk.Entry(self.canvas_cargar)
        self.label_carga_cantidad_monedast2.insert(0,0)
        self.label_carga_cantidad_monedast2.grid(row=4,column=4)

        self.label_carga_cantidad_monedast3 = tk.Entry(self.canvas_cargar)
        self.label_carga_cantidad_monedast3.insert(0,0)
        self.label_carga_cantidad_monedast3.grid(row=5,column=4)

    
        self.label_carga_cantidad_total_monedas = Label(self.canvas_cargar, text='0')
        self.label_carga_cantidad_total_monedas.grid(row=6,column=4)
        
        self.label_carga_cantidad_espacio1 = Label(self.canvas_cargar, text='')
        self.label_carga_cantidad_espacio1.grid(row=7,column=4)

        self.label_carga_cantidad_billetest1 = tk.Entry(self.canvas_cargar)
        self.label_carga_cantidad_billetest1.insert(0,0)
        self.label_carga_cantidad_billetest1.grid(row=8,column=4)

        self.label_carga_cantidad_billetest2 = tk.Entry(self.canvas_cargar)
        self.label_carga_cantidad_billetest2.insert(0,0)
        self.label_carga_cantidad_billetest2.grid(row=9,column=4)

        self.label_carga_cantidad_billetest3 = tk.Entry(self.canvas_cargar)
        self.label_carga_cantidad_billetest3.insert(0,0)
        self.label_carga_cantidad_billetest3.grid(row=10,column=4)

        self.label_carga_cantidad_billetest4 = tk.Entry(self.canvas_cargar)
        self.label_carga_cantidad_billetest4.insert(0,0)
        self.label_carga_cantidad_billetest4.grid(row=11,column=4)

        self.label_carga_cantidad_billetest5 = tk.Entry(self.canvas_cargar)
        self.label_carga_cantidad_billetest5.insert(0,0)
        self.label_carga_cantidad_billetest5.grid(row=12,column=4)
        

        self.label_carga_cantidad_total_billetes = Label(self.canvas_cargar, text='0')
        self.label_carga_cantidad_total_billetes.grid(row=13,column=4)

        self.label_cargar = Label(self.canvas_cargar, text='     ')
        self.label_cargar.grid(row=2,column=5)

        self.label_cargar = Label(self.canvas_cargar, text='  TOTAL')
        self.label_cargar.grid(row=2,column=6)
        self.label_carga_total_monedast1 = Label(self.canvas_cargar, text='0')
        self.label_carga_total_monedast1.grid(row=3,column=6)
        self.label_carga_total_monedast2 = Label(self.canvas_cargar, text='0')
        self.label_carga_total_monedast2.grid(row=4,column=6)
        self.label_carga_total_monedast3 = Label(self.canvas_cargar, text='0')
        self.label_carga_total_monedast3.grid(row=5,column=6)
        self.label_carga_total_total_monedas = Label(self.canvas_cargar, text='0')
        self.label_carga_total_total_monedas.grid(row=6,column=6)
        self.label_carga_total_espacio1 = Label(self.canvas_cargar, text='')
        self.label_carga_total_espacio1.grid(row=7,column=6)
        self.label_carga_total_billetest1 = Label(self.canvas_cargar, text='0')
        self.label_carga_total_billetest1.grid(row=8,column=6)
        self.label_carga_total_billetest2 = Label(self.canvas_cargar, text='0')
        self.label_carga_total_billetest2.grid(row=9,column=6)
        self.label_carga_total_billetest3 = Label(self.canvas_cargar, text='0')
        self.label_carga_total_billetest3.grid(row=10,column=6)
        self.label_carga_total_billetest4 = Label(self.canvas_cargar, text='0')
        self.label_carga_total_billetest4.grid(row=11,column=6)
        self.label_carga_total_billetest5 = Label(self.canvas_cargar, text='0')
        self.label_carga_total_billetest5.grid(row=12,column=6)
        self.label_carga_total_total_billetes = Label(self.canvas_cargar, text='0')
        self.label_carga_total_total_billetes.grid(row=13,column=6)

        self.label_cargar = Label(self.canvas_cargar, text='    CANTIDAD')
        self.label_cargar.grid(row=2,column=10)
        self.label_saldo_cantidad_monedast1 = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_monedast1.grid(row=3,column=10)
        self.label_saldo_cantidad_monedast2 = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_monedast2.grid(row=4,column=10)
        self.label_saldo_cantidad_monedast3 = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_monedast3.grid(row=5,column=10)
        self.label_saldo_cantidad_total_monedas = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_total_monedas.grid(row=6,column=10)
        self.label_saldo_cantidad_espacio1 = Label(self.canvas_cargar, text='')
        self.label_saldo_cantidad_espacio1.grid(row=7,column=10)
        self.label_saldo_cantidad_billetest1 = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_billetest1.grid(row=8,column=10)
        self.label_saldo_cantidad_billetest2 = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_billetest2.grid(row=9,column=10)
        self.label_saldo_cantidad_billetest3 = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_billetest3.grid(row=10,column=10)
        self.label_saldo_cantidad_billetest4 = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_billetest4.grid(row=11,column=10)
        self.label_saldo_cantidad_billetest5 = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_billetest5.grid(row=12,column=10)
        self.label_saldo_cantidad_total_billetes = Label(self.canvas_cargar, text='0')
        self.label_saldo_cantidad_total_billetes.grid(row=13,column=10)

        self.label_cargar = Label(self.canvas_cargar, text='TOTAL')
        self.label_cargar.grid(row=2,column=12)
        self.label_saldo_total_monedast1 = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_monedast1.grid(row=3,column=12)
        self.label_saldo_total_monedast2 = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_monedast2.grid(row=4,column=12)
        self.label_saldo_total_monedast3 = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_monedast3.grid(row=5,column=12)
        self.label_saldo_total_total_monedas = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_total_monedas.grid(row=6,column=12)
        self.label_saldo_total_espacio1 = Label(self.canvas_cargar, text='')
        self.label_saldo_total_espacio1.grid(row=7,column=12)
        self.label_saldo_total_billetest1 = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_billetest1.grid(row=8,column=12)
        self.label_saldo_total_billetest2 = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_billetest2.grid(row=9,column=12)
        self.label_saldo_total_billetest3 = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_billetest3.grid(row=10,column=12)
        self.label_saldo_total_billetest4 = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_billetest4.grid(row=11,column=12)
        self.label_saldo_total_billetest5 = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_billetest5.grid(row=12,column=12)
        self.label_saldo_total_total_billetes = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_total_billetes.grid(row=13,column=12)
        self.label_saldo_total_espacio2 = Label(self.canvas_cargar, text='')
        self.label_saldo_total_espacio2.grid(row=14,column=12)
        self.label_saldo_total_total_cajero = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_total_cajero.grid(row=15,column=12)



        # Botones cargar cajero

        def guardar_cajero():

            moneda1 = self.label_carga_cantidad_monedast1.get()
            if int(moneda1) <0:
                return messagebox.showerror('Error', "La cantidad de monedas de " + conf[5]+ " debe de ser mayor o igual a 1")
            moneda2 = self.label_carga_cantidad_monedast2.get()
            if float(moneda2) <0:
                return messagebox.showerror('Error', "La cantidad de monedas de " + conf[6]+ " debe de ser mayor o igual a 1")
            moneda3 = self.label_carga_cantidad_monedast3.get()
            if float(moneda3) <0:
                return messagebox.showerror('Error', "La cantidad de monedas de " + conf[7]+ " debe de ser mayor o igual a 1")
            billete1 = self.label_carga_cantidad_billetest1.get()
            if int(billete1) <0:
                return messagebox.showerror('Error', "La cantidad de billetes de " + conf[8]+ " debe de ser mayor o igual a 1")
            billete2 = self.label_carga_cantidad_billetest2.get()
            if int(billete2) <0:
                return messagebox.showerror('Error',"La cantidad de billetes de " + conf[9]+ " debe de ser mayor o igual a 1")
            billete3 = self.label_carga_cantidad_billetest3.get()
            if int(billete3) <0:
                return messagebox.showerror('Error', "La cantidad de billetes de " + conf[10]+ " debe de ser mayor o igual a 1")
            billete4 = self.label_carga_cantidad_billetest4.get()
            if int(billete4) <0:
                return messagebox.showerror('Error', "La cantidad de billetes de " + conf[11]+ " debe de ser mayor o igual a 1")
            billete5 = self.label_carga_cantidad_billetest5.get()
            if int(billete5) <0:
                return messagebox.showerror('Error', "La cantidad de billetes de " + conf[12]+ " debe de ser mayor o igual a 1")

            cajero[conf[5]] += int(self.label_carga_cantidad_monedast1.get())
            cajero[conf[6]] += int(self.label_carga_cantidad_monedast2.get())
            cajero[conf[7]] += int(self.label_carga_cantidad_monedast3.get())
            cajero[conf[8]] += int(self.label_carga_cantidad_billetest1.get())
            cajero[conf[9]] += int(self.label_carga_cantidad_billetest2.get())
            cajero[conf[10]] += int(self.label_carga_cantidad_billetest3.get())
            cajero[conf[11]] += int(self.label_carga_cantidad_billetest4.get())
            cajero[conf[12]] += int(self.label_carga_cantidad_billetest5.get())

            self.label_carga_cantidad_total_monedas.config(text=int(self.label_carga_cantidad_monedast1.get())+int(self.label_carga_cantidad_monedast2.get())+int(self.label_carga_cantidad_monedast3.get()))
            self.label_carga_cantidad_total_billetes.config(text=int(self.label_carga_cantidad_billetest1.get())+int(self.label_carga_cantidad_billetest2.get())+int(self.label_carga_cantidad_billetest3.get())+int(self.label_carga_cantidad_billetest4.get())+int(self.label_carga_cantidad_billetest5.get()))

            self.label_carga_total_monedast1.config(text=int(self.label_carga_cantidad_monedast1.get())*int(conf[5]))
            self.label_carga_total_monedast2.config(text=int(self.label_carga_cantidad_monedast2.get())*int(conf[6]))
            self.label_carga_total_monedast3.config(text=int(self.label_carga_cantidad_monedast3.get())*int(conf[7]))
            self.label_carga_total_total_monedas.config(text=int(self.label_carga_cantidad_monedast1.get())*int(conf[5])+int(self.label_carga_cantidad_monedast2.get())*int(conf[6])+int(self.label_carga_cantidad_monedast3.get())*int(conf[7]))

            self.label_carga_total_billetest1.config(text=int(self.label_carga_cantidad_billetest1.get())*int(conf[8]))
            self.label_carga_total_billetest2.config(text=int(self.label_carga_cantidad_billetest2.get())*int(conf[9]))
            self.label_carga_total_billetest3.config(text=int(self.label_carga_cantidad_billetest3.get())*int(conf[10]))
            self.label_carga_total_billetest4.config(text=int(self.label_carga_cantidad_billetest4.get())*int(conf[11]))
            self.label_carga_total_billetest5.config(text=int(self.label_carga_cantidad_billetest5.get())*int(conf[12]))
            self.label_carga_total_total_billetes.config(text=int(self.label_carga_cantidad_billetest1.get())*int(conf[8])+int(self.label_carga_cantidad_billetest2.get())*int(conf[9])+int(self.label_carga_cantidad_billetest3.get())*int(conf[10])+int(self.label_carga_cantidad_billetest4.get())*int(conf[11])+int(self.label_carga_cantidad_billetest5.get())*int(conf[12]))
            
            self.label_saldo_cantidad_monedast1.config(text=cajero[conf[5]])
            self.label_saldo_cantidad_monedast2.config(text=cajero[conf[6]])
            self.label_saldo_cantidad_monedast3.config(text=cajero[conf[7]])
            self.label_saldo_cantidad_total_monedas.config(text=cajero[conf[5]]+cajero[conf[6]]+cajero[conf[7]])
            self.label_saldo_cantidad_billetest1.config(text=cajero[conf[8]])
            self.label_saldo_cantidad_billetest2.config(text=cajero[conf[9]])
            self.label_saldo_cantidad_billetest3.config(text=cajero[conf[10]])
            self.label_saldo_cantidad_billetest4.config(text=cajero[conf[11]])
            self.label_saldo_cantidad_billetest5.config(text=cajero[conf[12]])
            self.label_saldo_cantidad_total_billetes.config(text=cajero[conf[8]]+cajero[conf[9]]+cajero[conf[10]]+cajero[conf[11]]+cajero[conf[12]])
            
            self.label_saldo_total_monedast1.config(text=cajero[conf[5]]*int(conf[5]))
            self.label_saldo_total_monedast2.config(text=cajero[conf[6]]*int(conf[6]))
            self.label_saldo_total_monedast3.config(text=cajero[conf[7]]*int(conf[7]))
            self.label_saldo_total_total_monedas.config(text=cajero[conf[5]]*int(conf[5])+cajero[conf[6]]*int(conf[6])+cajero[conf[7]]*int(conf[7]))
            self.label_saldo_total_billetest1.config(text=cajero[conf[8]]*int(conf[8]))
            self.label_saldo_total_billetest2.config(text=cajero[conf[9]]*int(conf[9]))
            self.label_saldo_total_billetest3.config(text=cajero[conf[10]]*int(conf[10]))
            self.label_saldo_total_billetest4.config(text=cajero[conf[11]]*int(conf[11]))
            self.label_saldo_total_billetest5.config(text=cajero[conf[12]]*int(conf[12]))
            self.label_saldo_total_total_billetes.config(text=cajero[conf[8]]*int(conf[8])+cajero[conf[9]]*int(conf[9])+cajero[conf[10]]*int(conf[10])+cajero[conf[11]]*int(conf[11])+cajero[conf[12]]*int(conf[12]))
            self.label_saldo_total_total_cajero.config(text=cajero[conf[5]]*int(conf[5])+cajero[conf[6]]*int(conf[6])+cajero[conf[7]]*int(conf[7])+cajero[conf[8]]*int(conf[8])+cajero[conf[9]]*int(conf[9])+cajero[conf[10]]*int(conf[10])+cajero[conf[11]]*int(conf[11])+cajero[conf[12]]*int(conf[12]))
            
            f = open('cajero.dat','w')
            f.write(str(cajero))
            f.close()
            
        def vaciar():

            f = open('configuración.dat','r')

            conf = []    
            for line in f:
                conf.append(line[:-1])
            f.close()

            f = open('cajero.dat','r')
            cajero = eval(f.read())

            cajero[conf[5]] = int("0")
            cajero[conf[6]] = int("0")
            cajero[conf[7]] = int("0")
            cajero[conf[8]] = int("0")
            cajero[conf[9]] = int("0")
            cajero[conf[10]] = int("0")
            cajero[conf[11]] = int("0")
            cajero[conf[12]] = int("0")

                       
            self.label_antescargar_cantidad_monedast1.config(text="0")
            self.label_antescargar_cantidad_monedast2.config(text="0")
            self.label_antescargar_cantidad_monedast3.config(text="0")
            self.label_antescargar_cantidad_total_monedas.config(text="0")
            self.label_antescargar_cantidad_billetest1.config(text="0")
            self.label_antescargar_cantidad_billetest2.config(text="0")
            self.label_antescargar_cantidad_billetest3.config(text="0")
            self.label_antescargar_cantidad_billetest4.config(text="0")
            self.label_antescargar_cantidad_billetest5.config(text="0")
            self.label_antescargar_cantidad_total_billetes.config(text="0")


            self.label_carga_cantidad_total_monedas.config(text="0")
            self.label_carga_cantidad_total_billetes.config(text="0")


            self.label_antescargar_total_monedast1.config(text="0")
            self.label_antescargar_total_monedast2.config(text="0")
            self.label_antescargar_total_monedast3.config(text="0")
            self.label_antescargar_total_total_monedas.config(text="0")
            self.label_antescargar_total_billetest1.config(text="0")
            self.label_antescargar_total_billetest2.config(text="0")
            self.label_antescargar_total_billetest3.config(text="0")
            self.label_antescargar_total_billetest4.config(text="0")
            self.label_antescargar_total_billetest5.config(text="0")
            self.label_antescargar_total_total_billetes.config(text="0")

            self.label_carga_total_monedast1.config(text="0")
            self.label_carga_total_monedast2.config(text="0")
            self.label_carga_total_monedast3.config(text="0")
            self.label_carga_total_total_monedas.config(text="0")
            self.label_carga_total_billetest1.config(text="0")
            self.label_carga_total_billetest2.config(text="0")
            self.label_carga_total_billetest3.config(text="0")
            self.label_carga_total_billetest4.config(text="0")
            self.label_carga_total_billetest5.config(text="0")
            self.label_carga_total_total_billetes.config(text="0")

            self.label_saldo_cantidad_monedast1.config(text="0")
            self.label_saldo_cantidad_monedast2.config(text="0")
            self.label_saldo_cantidad_monedast3.config(text="0")
            self.label_saldo_cantidad_total_monedas.config(text="0")
            self.label_saldo_cantidad_billetest1.config(text="0")
            self.label_saldo_cantidad_billetest2.config(text="0")
            self.label_saldo_cantidad_billetest3.config(text="0")
            self.label_saldo_cantidad_billetest4.config(text="0")
            self.label_saldo_cantidad_billetest5.config(text="0")
            self.label_saldo_cantidad_total_billetes.config(text="0")
            
            self.label_saldo_total_monedast1.config(text="0")
            self.label_saldo_total_monedast2.config(text="0")
            self.label_saldo_total_monedast3.config(text="0")
            self.label_saldo_total_total_monedas.config(text="0")
            self.label_saldo_total_billetest1.config(text="0")
            self.label_saldo_total_billetest2.config(text="0")
            self.label_saldo_total_billetest3.config(text="0")
            self.label_saldo_total_billetest4.config(text="0")
            self.label_saldo_total_billetest5.config(text="0")
            self.label_saldo_total_total_billetes.config(text="0")
            self.label_saldo_total_total_cajero.config(text="0")

            f = open('cajero.dat','w')
            f.write(str(cajero))
            f.close()

   
        boton_Ok = tk.Button(self.canvas_cargar, text="Ok",command=guardar_cajero)
        boton_Ok.grid(row=22, column=3)

        boton_cancelar = tk.Button(self.canvas_cargar, text="Cancelar",command=self.ventana_cambiar_menu)
        boton_cancelar.grid(row=22, column=4)

        boton_vaciar_cajero = tk.Button(self.canvas_cargar, text="Vaciar cajero",command=vaciar)
        boton_vaciar_cajero.grid(row=22, column=5)
        self.canvas_cargar.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_cargar.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

class SaldoCajero:
    def __init__(self, master):


        f = open('configuración.dat','r')

        conf = []    
        for line in f:
            conf.append(line[:-1])
        f.close()

        f = open('cajero.dat','r')
        cajero = eval(f.read())
    
        self.master = master
        self.master.geometry('700x350')
        self.canvas_saldo = Canvas(self.master, width=500,height=500, highlightthickness=0)
        self.canvas_saldo.place(x=0,y=0)
        self.label_saldo = Label(self.canvas_saldo, text='PARQUEO - SALDO DEL CAJERO')
        self.label_saldo.grid(row=0,column=0)

        self.label_saldo = Label(self.canvas_saldo, text='ENTRADAS')
        self.label_saldo.grid(row=1,column=1,columnspan=3)
        self.label_saldo = Label(self.canvas_saldo, text='              SALIDAS')
        self.label_saldo.grid(row=1,column=5,columnspan=3)
        self.label_saldo = Label(self.canvas_saldo, text='                                       SALDO')
        self.label_saldo.grid(row=1,column=9,columnspan=3)
        
        self.label_saldo = Label(self.canvas_saldo, text='DENOMINACIÓN')
        self.label_saldo.grid(row=2,column=0)
        self.label_denominacion_monedast1 = Label(self.canvas_saldo, text='Monedas de '+conf[5])
        self.label_denominacion_monedast1.grid(row=3,column=0)
        self.label_denominacion_monedast2 = Label(self.canvas_saldo, text='Monedas de '+conf[6])
        self.label_denominacion_monedast2.grid(row=4,column=0)
        self.label_denominacion_monedast3 = Label(self.canvas_saldo, text='Monedas de '+conf[7])
        self.label_denominacion_monedast3.grid(row=5,column=0)
        self.label_denominacion_total_monedas = Label(self.canvas_saldo, text='TOTAL DE MONEDAS')
        self.label_denominacion_total_monedas.grid(row=6,column=0)
        self.label_denominacion_espacio1 = Label(self.canvas_saldo, text='')
        self.label_denominacion_espacio1.grid(row=7,column=0)
        self.label_denominacion_billetest1 = Label(self.canvas_saldo, text='Billetes de '+conf[8])
        self.label_denominacion_billetest1.grid(row=8,column=0)
        self.label_denominacion_billetest2 = Label(self.canvas_saldo, text='Billetes de '+conf[9])
        self.label_denominacion_billetest2.grid(row=9,column=0)
        self.label_denominacion_billetest3 = Label(self.canvas_saldo, text='Billetes de '+conf[10])
        self.label_denominacion_billetest3.grid(row=10,column=0)
        self.label_denominacion_billetest4 = Label(self.canvas_saldo, text='Billetes de '+conf[11])
        self.label_denominacion_billetest4.grid(row=11,column=0)
        self.label_denominacion_billetest5 = Label(self.canvas_saldo, text='Billetes de '+conf[12])
        self.label_denominacion_billetest5.grid(row=12,column=0)
        self.label_denominacion_total_billetes = Label(self.canvas_saldo, text='TOTAL DE BILLETES')
        self.label_denominacion_total_billetes.grid(row=13,column=0)
 

        self.label_saldo = Label(self.canvas_saldo, text='CANTIDAD')
        self.label_saldo.grid(row=2,column=1)
        self.label_entradas_cantidad_monedast1 = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_monedast1.grid(row=3,column=1)
        self.label_entradas_cantidad_monedast2 = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_monedast2.grid(row=4,column=1)
        self.label_entradas_cantidad_monedast3 = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_monedast3.grid(row=5,column=1)
        self.label_entradas_cantidad_total_monedas = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_total_monedas.grid(row=6,column=1)
        self.label_entradas_cantidad_espacio1 = Label(self.canvas_saldo, text='')
        self.label_entradas_cantidad_espacio1.grid(row=7,column=1)
        self.label_entradas_cantidad_billetest1 = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_billetest1.grid(row=8,column=1)
        self.label_entradas_cantidad_billetest2 = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_billetest2.grid(row=9,column=1)
        self.label_entradas_cantidad_billetest3 = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_billetest3.grid(row=10,column=1)
        self.label_entradas_cantidad_billetest4 = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_billetest4.grid(row=11,column=1)
        self.label_entradas_cantidad_billetest5 = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_billetest5.grid(row=12,column=1)
        self.label_entradas_cantidad_total_billetes = Label(self.canvas_saldo, text='0')
        self.label_entradas_cantidad_total_billetes.grid(row=13,column=1)
        
        self.label_saldo = Label(self.canvas_saldo, text='TOTAL')
        self.label_saldo.grid(row=2,column=2)
        self.label_entradas_total_monedast1 = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_monedast1.grid(row=3,column=2)
        self.label_entradas_total_monedast2 = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_monedast2.grid(row=4,column=2)
        self.label_entradas_total_monedast3 = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_monedast3.grid(row=5,column=2)
        self.label_entradas_total_total_monedas = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_total_monedas.grid(row=6,column=2)
        self.label_entradas_total_espacio1 = Label(self.canvas_saldo, text='')
        self.label_entradas_total_espacio1.grid(row=7,column=2)
        self.label_entradas_total_billetest1 = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_billetest1.grid(row=8,column=2)
        self.label_entradas_total_billetest2 = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_billetest2.grid(row=9,column=2)
        self.label_entradas_total_billetest3 = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_billetest3.grid(row=10,column=2)
        self.label_entradas_total_billetest4 = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_billetest4.grid(row=11,column=2)
        self.label_entradas_total_billetest5 = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_billetest5.grid(row=12,column=2)
        self.label_entradas_total_total_billetes = Label(self.canvas_saldo, text='0')
        self.label_entradas_total_total_billetes.grid(row=13,column=2)

        self.label_saldo = Label(self.canvas_saldo, text='  CANTIDAD')
        self.label_saldo.grid(row=2,column=6)
        self.label_salidas_cantidad_monedast1 = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_monedast1.grid(row=3,column=6)
        self.label_salidas_cantidad_monedast2 = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_monedast2.grid(row=4,column=6)
        self.label_salidas_cantidad_monedast3 = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_monedast3.grid(row=5,column=6)
        self.label_salidas_cantidad_total_monedas = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_total_monedas.grid(row=6,column=6)
        self.label_salidas_cantidad_espacio1 = Label(self.canvas_saldo, text='')
        self.label_salidas_cantidad_espacio1.grid(row=7,column=6)
        self.label_salidas_cantidad_billetest1 = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_billetest1.grid(row=8,column=6)
        self.label_salidas_cantidad_billetest2 = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_billetest2.grid(row=9,column=6)
        self.label_salidas_cantidad_billetest3 = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_billetest3.grid(row=10,column=6)
        self.label_salidas_cantidad_billetest4 = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_billetest4.grid(row=11,column=6)
        self.label_salidas_cantidad_billetest5 = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_billetest5.grid(row=12,column=6)
        self.label_salidas_cantidad_total_billetes = Label(self.canvas_saldo, text='0')
        self.label_salidas_cantidad_total_billetes.grid(row=13,column=6)

        self.label_saldo = Label(self.canvas_saldo, text='     ')
        self.label_saldo.grid(row=2,column=5)

        self.label_saldo = Label(self.canvas_saldo, text='  TOTAL')
        self.label_saldo.grid(row=2,column=7)
        self.label_salidas_total_monedast1 = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_monedast1.grid(row=3,column=7)
        self.label_salidas_total_monedast2 = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_monedast2.grid(row=4,column=7)
        self.label_salidas_total_monedast3 = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_monedast3.grid(row=5,column=7)
        self.label_salidas_total_total_monedas = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_total_monedas.grid(row=6,column=7)
        self.label_salidas_total_espacio1 = Label(self.canvas_saldo, text='')
        self.label_salidas_total_espacio1.grid(row=7,column=7)
        self.label_salidas_total_billetest1 = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_billetest1.grid(row=8,column=7)
        self.label_salidas_total_billetest2 = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_billetest2.grid(row=9,column=7)
        self.label_salidas_total_billetest3 = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_billetest3.grid(row=10,column=7)
        self.label_salidas_total_billetest4 = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_billetest4.grid(row=11,column=7)
        self.label_salidas_total_billetest5 = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_billetest5.grid(row=12,column=7)
        self.label_salidas_total_total_billetes = Label(self.canvas_saldo, text='0')
        self.label_salidas_total_total_billetes.grid(row=13,column=7)

        self.label_saldo = Label(self.canvas_saldo, text='    CANTIDAD')
        self.label_saldo.grid(row=2,column=10)
        self.label_saldo_cantidad_monedast1 = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_monedast1.grid(row=3,column=10)
        self.label_saldo_cantidad_monedast2 = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_monedast2.grid(row=4,column=10)
        self.label_saldo_cantidad_monedast3 = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_monedast3.grid(row=5,column=10)
        self.label_saldo_cantidad_total_monedas = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_total_monedas.grid(row=6,column=10)
        self.label_saldo_cantidad_espacio1 = Label(self.canvas_saldo, text='')
        self.label_saldo_cantidad_espacio1.grid(row=7,column=10)
        self.label_saldo_cantidad_billetest1 = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_billetest1.grid(row=8,column=10)
        self.label_saldo_cantidad_billetest2 = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_billetest2.grid(row=9,column=10)
        self.label_saldo_cantidad_billetest3 = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_billetest3.grid(row=10,column=10)
        self.label_saldo_cantidad_billetest4 = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_billetest4.grid(row=11,column=10)
        self.label_saldo_cantidad_billetest5 = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_billetest5.grid(row=12,column=10)
        self.label_saldo_cantidad_total_billetes = Label(self.canvas_saldo, text='0')
        self.label_saldo_cantidad_total_billetes.grid(row=13,column=10)

        self.label_saldo = Label(self.canvas_saldo, text='TOTAL')
        self.label_saldo.grid(row=2,column=12)
        self.label_saldo_total_monedast1 = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_monedast1.grid(row=3,column=12)
        self.label_saldo_total_monedast2 = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_monedast2.grid(row=4,column=12)
        self.label_saldo_total_monedast3 = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_monedast3.grid(row=5,column=12)
        self.label_saldo_total_total_monedas = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_total_monedas.grid(row=6,column=12)
        self.label_saldo_total_espacio1 = Label(self.canvas_saldo, text='')
        self.label_saldo_total_espacio1.grid(row=7,column=12)
        self.label_saldo_total_billetest1 = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_billetest1.grid(row=8,column=12)
        self.label_saldo_total_billetest2 = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_billetest2.grid(row=9,column=12)
        self.label_saldo_total_billetest3 = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_billetest3.grid(row=10,column=12)
        self.label_saldo_total_billetest4 = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_billetest4.grid(row=11,column=12)
        self.label_saldo_total_billetest5 = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_billetest5.grid(row=12,column=12)
        self.label_saldo_total_total_billetes = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_total_billetes.grid(row=13,column=12)

        self.label_saldo_cantidad_monedast1.config(text=cajero[conf[5]])
        self.label_saldo_cantidad_monedast2.config(text=cajero[conf[6]])
        self.label_saldo_cantidad_monedast3.config(text=cajero[conf[7]])
        self.label_saldo_cantidad_total_monedas.config(text=cajero[conf[5]]+cajero[conf[6]]+cajero[conf[7]])
        self.label_saldo_cantidad_billetest1.config(text=cajero[conf[8]])
        self.label_saldo_cantidad_billetest2.config(text=cajero[conf[9]])
        self.label_saldo_cantidad_billetest3.config(text=cajero[conf[10]])
        self.label_saldo_cantidad_billetest4.config(text=cajero[conf[11]])
        self.label_saldo_cantidad_billetest5.config(text=cajero[conf[12]])
        self.label_saldo_cantidad_total_billetes.config(text=cajero[conf[8]]+cajero[conf[9]]+cajero[conf[10]]+cajero[conf[11]]+cajero[conf[12]])
        
        self.label_saldo_total_monedast1.config(text=cajero[conf[5]]*int(conf[5]))
        self.label_saldo_total_monedast2.config(text=cajero[conf[6]]*int(conf[6]))
        self.label_saldo_total_monedast3.config(text=cajero[conf[7]]*int(conf[7]))
        self.label_saldo_total_total_monedas.config(text=cajero[conf[5]]*int(conf[5])+cajero[conf[6]]*int(conf[6])+cajero[conf[7]]*int(conf[7]))
        self.label_saldo_total_billetest1.config(text=cajero[conf[8]]*int(conf[8]))
        self.label_saldo_total_billetest2.config(text=cajero[conf[9]]*int(conf[9]))
        self.label_saldo_total_billetest3.config(text=cajero[conf[10]]*int(conf[10]))
        self.label_saldo_total_billetest4.config(text=cajero[conf[11]]*int(conf[11]))
        self.label_saldo_total_billetest5.config(text=cajero[conf[12]]*int(conf[12]))
        self.label_saldo_total_total_billetes.config(text=cajero[conf[8]]*int(conf[8])+cajero[conf[9]]*int(conf[9])+cajero[conf[10]]*int(conf[10])+cajero[conf[11]]*int(conf[11])+cajero[conf[12]]*int(conf[12]))
       

        f = open('cajero.dat','w')
        f.write(str(cajero))
        f.close()

        boton_Ok = tk.Button(self.canvas_saldo, text="Ok")
        boton_Ok.grid(row=24, column=6)

        boton_cancelar = tk.Button(self.canvas_saldo, text="Cancelar",command=self.ventana_cambiar_menu)
        boton_cancelar.grid(row=24, column=7)

     
        self.canvas_saldo.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_saldo.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

class IngresosDinero:
    def __init__(self, master):
    
        self.master = master
        self.master.geometry('600x250')
        self.canvas_ingresos = Canvas(self.master, width=500,height=500, highlightthickness=0)
        self.canvas_ingresos.place(x=0,y=0)
        self.label_ingresos = Label(self.canvas_ingresos, text='PARQUEO - INGRESOS DE DINERO')
        self.label_ingresos.grid(row=0,column=0)

        self.label_ingresos_inicio = Label(self.canvas_ingresos, text="Del dia")
        self.label_ingresos_inicio.grid(row=1,column=0)

        self.label_ingresos_inicio_1 = tk.Entry(self.canvas_ingresos)
        self.label_ingresos_inicio_1.grid(row=1,column=1)
        

        self.label_ingresos_fin = Label(self.canvas_ingresos, text="Al dia")
        self.label_ingresos_fin.grid(row=2,column=0)

        self.label_ingresos_fin_1 = tk.Entry(self.canvas_ingresos)
        self.label_ingresos_fin_1.grid(row=2,column=1)
        

        self.label_ingresos_espacio1 = Label(self.canvas_ingresos, text='')
        self.label_ingresos_espacio1.grid(row=3,column=0)
        self.label_ingresos_efectivo = Label(self.canvas_ingresos, text='TOTAL DE INGRESOS EN EFECTIVO')
        self.label_ingresos_efectivo.grid(row=4,column=0)
        self.label_ingresos_efectivo_1 = Label(self.canvas_ingresos, text='XXX.XXX.XXX')
        self.label_ingresos_efectivo_1.grid(row=4,column=6)
        self.label_ingresos_tarjeta = Label(self.canvas_ingresos, text='TOTAL DE INGRESOS POR TARJETA DE CRÉDITO')
        self.label_ingresos_tarjeta.grid(row=5,column=0)
        self.label_ingresos_tarjeta1 = Label(self.canvas_ingresos, text='XXX.XXX.XXX')
        self.label_ingresos_tarjeta1 .grid(row=5,column=6)
        self.label_ingresos_total_ingresos = Label(self.canvas_ingresos, text='TOTAL DE INGRESOS')
        self.label_ingresos_total_ingresos.grid(row=6,column=0)
        self.label_ingresos_total_ingresos1 = Label(self.canvas_ingresos, text='XXX.XXX.XXX')
        self.label_ingresos_total_ingresos1.grid(row=6,column=6)
        self.label_ingresos_espacio2 = Label(self.canvas_ingresos, text='')
        self.label_ingresos_espacio2.grid(row=7,column=0)
        self.label_ingresos_recibir = Label(self.canvas_ingresos, text='ESTIMADO DE INGRESOS POR RECIBIR')
        self.label_ingresos_recibir.grid(row=8,column=0)
        self.label_ingresos_recibir1 = Label(self.canvas_ingresos, text='XXX.XXX.XXX')
        self.label_ingresos_recibir1 .grid(row=8,column=6)

        boton_Ok = tk.Button(self.canvas_ingresos, text="Ok")
        boton_Ok.grid(row=22, column=6)

        boton_cancelar = tk.Button(self.canvas_ingresos, text="Cancelar",command=self.ventana_cambiar_menu)
        boton_cancelar.grid(row=22, column=7)

     
        self.canvas_ingresos.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_ingresos.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

class EntradaVehiculo:
    def __init__(self, master):
    
        self.master = master
        self.master.geometry('500x300')
        self.canvas_entrada = Canvas(self.master, width=500,height=500, highlightthickness=0)
        self.canvas_entrada.place(x=0,y=0)
        self.label_entrada = Label(self.canvas_entrada, text='PARQUEO - ENTRADA DE VEHÍCULO')
        self.label_entrada.grid(row=0,column=0)

        self.label_entrada_espacios_disponibles = Label(self.canvas_entrada, text="Espacios disponibles")
        self.label_entrada_espacios_disponibles.grid(row=1,column=0)
        self.label_entrada_espacios_disponibles_1 = Label(self.canvas_entrada, text="XXXXXXXXXX")
        self.label_entrada_espacios_disponibles_1.grid(row=1,column=3)
        self.label_entrada_espacios_1 = Label(self.canvas_entrada, text="")
        self.label_entrada_espacios_1.grid(row=2,column=3)

        self.label_entrada_placa = Label(self.canvas_entrada, text="SU PLACA")
        self.label_entrada_placa.grid(row=3,column=0)

        self.label_entrada_placa_1 = tk.Entry(self.canvas_entrada)
        self.label_entrada_placa_1.grid(row=3,column=3)
        
        self.label_entrada_espacios_2 = Label(self.canvas_entrada, text="")
        self.label_entrada_espacios_2.grid(row=4,column=3)

        self.label_entrada_campo = Label(self.canvas_entrada, text="Campo asigando")
        self.label_entrada_campo.grid(row=5,column=0)
        self.label_entrada_campo_1 = Label(self.canvas_entrada, text="XXXXXXXXXX")
        self.label_entrada_campo_1.grid(row=5,column=3)
        self.label_entrada_espacios_3 = Label(self.canvas_entrada, text="")
        self.label_entrada_espacios_3.grid(row=6,column=3)

        self.label_entrada_hora_entrada = Label(self.canvas_entrada, text="Hora de entrada")
        self.label_entrada_hora_entrada.grid(row=7,column=0)
        self.label_entrada_hora_entrada_1 = Label(self.canvas_entrada, text="hh:mm dd/mm/aaaa")
        self.label_entrada_hora_entrada_1.grid(row=7,column=3)
        self.label_entrada_espacios_4 = Label(self.canvas_entrada, text="")
        self.label_entrada_espacios_4.grid(row=8,column=3)

        self.label_entrada_precio = Label(self.canvas_entrada, text="Precio por hora")
        self.label_entrada_precio.grid(row=9,column=0)
        self.label_entrada_precio_1 = Label(self.canvas_entrada, text="XXXXXXXXXX")
        self.label_entrada_precio_1.grid(row=9,column=3)


        boton_Ok = tk.Button(self.canvas_entrada, text="Ok")
        boton_Ok.grid(row=22, column=6)

        boton_cancelar = tk.Button(self.canvas_entrada, text="Cancelar",command=self.ventana_cambiar_menu)
        boton_cancelar.grid(row=22, column=7)

     
        self.canvas_entrada.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_entrada.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

class CajeroParqueo:
    def __init__(self, master):
    
        self.master = master
        self.master.geometry('600x500')
        self.canvas_cajero = Canvas(self.master, width=500,height=500, highlightthickness=0)
        self.canvas_cajero.place(x=0,y=0)
        self.label_cajero = Label(self.canvas_cajero, text='CAJERO DEL PARQUEO')
        self.label_cajero.grid(row=0,column=0)

        self.label_cajero_espacio1 = Label(self.canvas_cajero, text='                    ')
        self.label_cajero_espacio1.grid(row=0,column=2)
        self.label_cajero_por_hora = Label(self.canvas_cajero, text='XXXXX POR HORA')
        self.label_cajero_por_hora.grid(row=0,column=3)

        self.label_cajero_espacio2 = Label(self.canvas_cajero, text='')
        self.label_cajero_espacio2.grid(row=1,column=0)
        self.label_cajero_paso1 = Label(self.canvas_cajero, text='Paso 1: SU PLACA')
        self.label_cajero_paso1.grid(row=2,column=0)
        self.label_cajero_espacio3 = Label(self.canvas_cajero, text='    ')
        self.label_cajero_espacio3.grid(row=2,column=1)

        self.label_cajero_paso1_1 = tk.Entry(self.canvas_cajero)
        self.label_cajero_paso1_1.grid(row=2, column=2)  
    
        self.label_cajero_espacio4 = Label(self.canvas_cajero, text=' ')
        self.label_cajero_espacio4.grid(row=3,column=0)

        self.label_cajero_hora_entrada = Label(self.canvas_cajero, text='HORA DE ENTRADA')
        self.label_cajero_hora_entrada.grid(row=4,column=0)
        self.label_cajero_hora_entrada_1 = Label(self.canvas_cajero, text='HH:MM')
        self.label_cajero_hora_entrada_1.grid(row=4,column=1)
        self.label_cajero_hora_entrada_2 = Label(self.canvas_cajero, text='dd/mm/aaaa')
        self.label_cajero_hora_entrada_2.grid(row=4,column=2)

        self.label_cajero_a_pagar = Label(self.canvas_cajero, text='A PAGAR')
        self.label_cajero_a_pagar.grid(row=4,column=6)
        self.label_cajero_a_pagar_1 = Label(self.canvas_cajero, text='XXXXXX', bg="#ff6961")
        self.label_cajero_a_pagar_1.grid(row=5,column=6)

        self.label_cajero_hora_salida = Label(self.canvas_cajero, text='HORA DE SALIDA')
        self.label_cajero_hora_salida.grid(row=5,column=0)
        self.label_cajero_hora_salida_1 = Label(self.canvas_cajero, text='HH:MM')
        self.label_cajero_hora_salida_1.grid(row=5,column=1)
        self.label_cajero_hora_salida_2 = Label(self.canvas_cajero, text='dd/mm/aaaa')
        self.label_cajero_hora_salida_2.grid(row=5,column=2)

        self.label_cajero_tiempo_cobrado = Label(self.canvas_cajero, text='TIEMPO COBRADO')
        self.label_cajero_tiempo_cobrado.grid(row=6,column=0)
        self.label_cajero_tiempo_cobrado_1 = Label(self.canvas_cajero, text='XXh')
        self.label_cajero_tiempo_cobrado_1.grid(row=6,column=1)
        self.label_cajero_tiempo_cobrado_2 = Label(self.canvas_cajero, text='YYm')
        self.label_cajero_tiempo_cobrado_2.grid(row=6,column=2)
        self.label_cajero_tiempo_cobrado_3 = Label(self.canvas_cajero, text='zzzd')
        self.label_cajero_tiempo_cobrado_3.grid(row=6,column=3)

        self.label_cajero_espacio5 = Label(self.canvas_cajero, text='')
        self.label_cajero_espacio5.grid(row=7,column=0)
        self.label_cajero_paso2 = Label(self.canvas_cajero, text='Paso 2: SU PAGO EN:')
        self.label_cajero_paso2.grid(row=8,column=0)
        
        self.label_cajero_paso2_monedas = Label(self.canvas_cajero, text='MONEDAS')
        self.label_cajero_paso2_monedas.grid(row=8,column=1)
        boton_1_monedas = tk.Button(self.canvas_cajero, text="50")
        boton_1_monedas.grid(row=9, column=1)
        boton_2_monedas = tk.Button(self.canvas_cajero, text="100")
        boton_2_monedas.grid(row=10, column=1)
        boton_3_monedas = tk.Button(self.canvas_cajero, text="500")
        boton_3_monedas.grid(row=11, column=1)

        self.label_cajero_paso2_billetes = Label(self.canvas_cajero, text='BILLETES')
        self.label_cajero_paso2_billetes.grid(row=8,column=2)
        boton_1_billetes = tk.Button(self.canvas_cajero, text="1000")
        boton_1_billetes.grid(row=9, column=2)
        boton_2_billetes = tk.Button(self.canvas_cajero, text="2000")
        boton_2_billetes.grid(row=10, column=2)
        boton_3_billetes = tk.Button(self.canvas_cajero, text="5000")
        boton_3_billetes.grid(row=11, column=2)
        boton_4_billetes = tk.Button(self.canvas_cajero, text="10000")
        boton_4_billetes.grid(row=12, column=2)
        boton_5_billetes = tk.Button(self.canvas_cajero, text="20000")
        boton_5_billetes.grid(row=13, column=2)

        self.label_cajero_paso2_tarjeta = Label(self.canvas_cajero, text='TARJETA DE CRÉDITO')
        self.label_cajero_paso2_tarjeta.grid(row=8,column=3)

        self.label_cajero_paso2_tarjeta1 = tk.Entry(self.canvas_cajero)
        self.label_cajero_paso2_tarjeta1.grid(row=9, column=3)

        self.label_cajero_pagado = Label(self.canvas_cajero, text='Pagado')
        self.label_cajero_pagado.grid(row=9,column=6)
        self.label_cajero_pagado1 = Label(self.canvas_cajero, text='XXXXXX', bg="#77dd77")
        self.label_cajero_pagado1.grid(row=10,column=6)

        self.label_cajero_cambio = Label(self.canvas_cajero, text='Cambio')
        self.label_cajero_cambio.grid(row=11,column=6)
        self.label_cajero_cambio1 = Label(self.canvas_cajero, text='XXXXXX',bg="#77dd77")
        self.label_cajero_cambio1.grid(row=12,column=6)

        self.label_cajero_espacio6 = Label(self.canvas_cajero, text='')
        self.label_cajero_espacio6.grid(row=14,column=0)
        self.label_cajero_paso3 = Label(self.canvas_cajero, text='Paso 3: SU CAMBIO EN:')
        self.label_cajero_paso3.grid(row=15,column=0)

        self.label_cajero_paso3_monedas = Label(self.canvas_cajero, text='MONEDAS')
        self.label_cajero_paso3_monedas.grid(row=15,column=1)
        self.label_cajero_paso3_monedas1 = Label(self.canvas_cajero, text='XX DE 50')
        self.label_cajero_paso3_monedas1.grid(row=16,column=1)
        self.label_cajero_paso3_monedas2 = Label(self.canvas_cajero, text='XX DE 100')
        self.label_cajero_paso3_monedas2.grid(row=17,column=1)
        self.label_cajero_paso3_monedas3 = Label(self.canvas_cajero, text='XX DE 500')
        self.label_cajero_paso3_monedas3.grid(row=18,column=1)

        self.label_cajero_paso3_billetes = Label(self.canvas_cajero, text='BILLETES')
        self.label_cajero_paso3_billetes.grid(row=15,column=2)
        self.label_cajero_paso3_billetes1 = Label(self.canvas_cajero, text='XX DE 1000')
        self.label_cajero_paso3_billetes1.grid(row=16,column=2)
        self.label_cajero_paso3_billetes2 = Label(self.canvas_cajero, text='XX DE 2000')
        self.label_cajero_paso3_billetes2.grid(row=17,column=2)
        self.label_cajero_paso3_billetes3 = Label(self.canvas_cajero, text='XX DE 5000')
        self.label_cajero_paso3_billetes3.grid(row=18,column=2)
        self.label_cajero_paso3_billetes4 = Label(self.canvas_cajero, text='XX DE 10000')
        self.label_cajero_paso3_billetes4.grid(row=19,column=2)
        self.label_cajero_paso3_billetes5 = Label(self.canvas_cajero, text='XX DE 20000')
        self.label_cajero_paso3_billetes5.grid(row=20,column=2)

        boton_anular = tk.Button(self.canvas_cajero, text="Anular el pago")
        boton_anular.grid(row=21, column=6)
        
        boton_cancelar = tk.Button(self.canvas_cajero, text="Cancelar",command=self.ventana_cambiar_menu)
        boton_cancelar.grid(row=21, column=7)

     
        self.canvas_cajero.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_cajero.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

class SalidaVehiculo:
    def __init__(self, master):
    
        self.master = master
        self.master.geometry('450x100')
        self.canvas_salida = Canvas(self.master, width=500,height=500, highlightthickness=0)
        self.canvas_salida.place(x=0,y=0)
        self.label_salida = Label(self.canvas_salida, text='PARQUEO - SALIDA DE VEHÍCULO')
        self.label_salida.grid(row=0,column=0)

        self.label_salida_placa = Label(self.canvas_salida, text="SU PLACA")
        self.label_salida_placa.grid(row=1,column=0)

        self.label_salida_placa_1 = tk.Entry(self.canvas_salida)
        self.label_salida_placa_1.grid(row=1,column=3)

        boton_Ok = tk.Button(self.canvas_salida, text="Ok")
        boton_Ok.grid(row=22, column=6)

        boton_cancelar = tk.Button(self.canvas_salida, text="Cancelar",command=self.ventana_cambiar_menu)
        boton_cancelar.grid(row=22, column=7)

     
        self.canvas_salida.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_salida.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)


class AcercaDe:

    def __init__(self, master):
    
        self.master = master
        self.master.geometry('500x300')
        self.canvas_acerca_de = Canvas(self.master,width=500,height=500, highlightthickness=0)
        self.canvas_acerca_de.place(x=0,y=0)
        self.label_acerca_de = Label(self.canvas_acerca_de, text='ACERCA DE')
        self.label_acerca_de.place(x=175,y=20,width=150)

        self.label_acerca_de_nombre = Label(self.canvas_acerca_de, text='PROYECTO PARQUEO')
        self.label_acerca_de_nombre.place(x=175,y=60,width=150)

        self.label_acerca_de_version = Label(self.canvas_acerca_de, text='Version 1.0')
        self.label_acerca_de_version.place(x=175,y=100,width=150)

        self.label_acerca_de_fecha = Label(self.canvas_acerca_de, text='21 de junio 2022')
        self.label_acerca_de_fecha.place(x=175,y=140,width=150)

        self.label_acerca_de_autor = Label(self.canvas_acerca_de, text='Dina Monge Sandoval')
        self.label_acerca_de_autor.place(x=175,y=180,width=150)

        boton_cancelar = tk.Button(self.canvas_acerca_de, text="Volver al menu principal",command=self.ventana_cambiar_menu)
        boton_cancelar.place(x=175,y=220,width=150)

     
        self.canvas_acerca_de.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_acerca_de.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

window = Tk()
MenuPrincipal(window)
window.title('Proyecto')
window.geometry('500x500')
window.mainloop()
