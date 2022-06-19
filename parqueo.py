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
        self.master.geometry('800x500')
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
        self.label_denominacion_monedast1 = Label(self.canvas_cargar, text='Monedas de '+conf[6])
        self.label_denominacion_monedast1.grid(row=3,column=0)
        self.label_denominacion_monedast2 = Label(self.canvas_cargar, text='Monedas de '+conf[7])
        self.label_denominacion_monedast2.grid(row=4,column=0)
        self.label_denominacion_monedast3 = Label(self.canvas_cargar, text='Monedas de '+conf[8])
        self.label_denominacion_monedast3.grid(row=5,column=0)
        self.label_denominacion_total_monedas = Label(self.canvas_cargar, text='TOTAL DE MONEDAS')
        self.label_denominacion_total_monedas.grid(row=6,column=0)
        self.label_denominacion_espacio1 = Label(self.canvas_cargar, text='')
        self.label_denominacion_espacio1.grid(row=7,column=0)
        self.label_denominacion_billetest1 = Label(self.canvas_cargar, text='Billetes de '+conf[10])
        self.label_denominacion_billetest1.grid(row=8,column=0)
        self.label_denominacion_billetest2 = Label(self.canvas_cargar, text='Billetes de '+conf[11])
        self.label_denominacion_billetest2.grid(row=9,column=0)
        self.label_denominacion_billetest3 = Label(self.canvas_cargar, text='Billetes de '+conf[12])
        self.label_denominacion_billetest3.grid(row=10,column=0)
        self.label_denominacion_billetest4 = Label(self.canvas_cargar, text='Billetes de '+conf[13])
        self.label_denominacion_billetest4.grid(row=11,column=0)
        self.label_denominacion_billetest5 = Label(self.canvas_cargar, text='Billetes de '+conf[14])
        self.label_denominacion_billetest5.grid(row=12,column=0)
        self.label_denominacion_total_billetes = Label(self.canvas_cargar, text='TOTAL DE BILLETES')
        self.label_denominacion_total_billetes.grid(row=13,column=0)
        self.label_denominacion_espacio2 = Label(self.canvas_cargar, text='')
        self.label_denominacion_espacio2.grid(row=14,column=0)
        self.label_denominacion_total_cajero = Label(self.canvas_cargar, text='TOTAL DEL CAJERO')
        self.label_denominacion_total_cajero.grid(row=15,column=0)

        self.label_cargar = Label(self.canvas_cargar, text='CANTIDAD')
        self.label_cargar.grid(row=2,column=1)
        self.label_antescargar_cantidad_monedast1 = Label(self.canvas_cargar, text=cajero[conf[6]])
        self.label_antescargar_cantidad_monedast1.grid(row=3,column=1)
        self.label_antescargar_cantidad_monedast2 = Label(self.canvas_cargar, text=cajero[conf[7]])
        self.label_antescargar_cantidad_monedast2.grid(row=4,column=1)
        self.label_antescargar_cantidad_monedast3 = Label(self.canvas_cargar, text=cajero[conf[8]])
        self.label_antescargar_cantidad_monedast3.grid(row=5,column=1)
        self.label_antescargar_cantidad_total_monedas = Label(self.canvas_cargar, text=cajero[conf[6]]+cajero[conf[7]]+cajero[conf[8]])
        self.label_antescargar_cantidad_total_monedas.grid(row=6,column=1)
        self.label_antescargar_cantidad_espacio1 = Label(self.canvas_cargar, text='')
        self.label_antescargar_cantidad_espacio1.grid(row=7,column=1)
        self.label_antescargar_cantidad_billetest1 = Label(self.canvas_cargar, text=cajero[conf[10]])
        self.label_antescargar_cantidad_billetest1.grid(row=8,column=1)
        self.label_antescargar_cantidad_billetest2 = Label(self.canvas_cargar, text=cajero[conf[11]])
        self.label_antescargar_cantidad_billetest2.grid(row=9,column=1)
        self.label_antescargar_cantidad_billetest3 = Label(self.canvas_cargar, text=cajero[conf[12]])
        self.label_antescargar_cantidad_billetest3.grid(row=10,column=1)
        self.label_antescargar_cantidad_billetest4 = Label(self.canvas_cargar, text=cajero[conf[13]])
        self.label_antescargar_cantidad_billetest4.grid(row=11,column=1)
        self.label_antescargar_cantidad_billetest5 = Label(self.canvas_cargar, text=cajero[conf[14]])
        self.label_antescargar_cantidad_billetest5.grid(row=12,column=1)
        self.label_antescargar_cantidad_total_billetes = Label(self.canvas_cargar, text=cajero[conf[10]]+cajero[conf[11]]+cajero[conf[12]]+cajero[conf[13]]+cajero[conf[14]])
        self.label_antescargar_cantidad_total_billetes.grid(row=13,column=1)
        
        self.label_cargar = Label(self.canvas_cargar, text='TOTAL')
        self.label_cargar.grid(row=2,column=2)
        self.label_antescargar_total_monedast1 = Label(self.canvas_cargar, text=cajero[conf[6]]*int(conf[6]))
        self.label_antescargar_total_monedast1.grid(row=3,column=2)
        self.label_antescargar_total_monedast2 = Label(self.canvas_cargar, text=cajero[conf[7]]*int(conf[7]))
        self.label_antescargar_total_monedast2.grid(row=4,column=2)
        self.label_antescargar_total_monedast3 = Label(self.canvas_cargar, text=cajero[conf[8]]*int(conf[8]))
        self.label_antescargar_total_monedast3.grid(row=5,column=2)
        self.label_antescargar_total_total_monedas = Label(self.canvas_cargar, text=cajero[conf[6]]*int(conf[6])+cajero[conf[7]]*int(conf[7])+cajero[conf[8]]*int(conf[8]))
        self.label_antescargar_total_total_monedas.grid(row=6,column=2)
        self.label_antescargar_total_espacio1 = Label(self.canvas_cargar, text='')
        self.label_antescargar_total_espacio1.grid(row=7,column=2)
        self.label_antescargar_total_billetest1 = Label(self.canvas_cargar, text=cajero[conf[10]]*int(conf[10]))
        self.label_antescargar_total_billetest1.grid(row=8,column=2)
        self.label_antescargar_total_billetest2 = Label(self.canvas_cargar, text=cajero[conf[11]]*int(conf[11]))
        self.label_antescargar_total_billetest2.grid(row=9,column=2)
        self.label_antescargar_total_billetest3 = Label(self.canvas_cargar, text=cajero[conf[12]]*int(conf[12]))
        self.label_antescargar_total_billetest3.grid(row=10,column=2)
        self.label_antescargar_total_billetest4 = Label(self.canvas_cargar, text=cajero[conf[13]]*int(conf[13]))
        self.label_antescargar_total_billetest4.grid(row=11,column=2)
        self.label_antescargar_total_billetest5 = Label(self.canvas_cargar, text=cajero[conf[14]]*int(conf[14]))
        self.label_antescargar_total_billetest5.grid(row=12,column=2)
        self.label_antescargar_total_total_billetes = Label(self.canvas_cargar, text=cajero[conf[10]]*int(conf[10])+cajero[conf[11]]*int(conf[11])+cajero[conf[12]]*int(conf[12])+cajero[conf[13]]*int(conf[13])+cajero[conf[14]]*int(conf[14]))
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
        self.label_saldo_total_total__cajero = Label(self.canvas_cargar, text='0')
        self.label_saldo_total_total__cajero.grid(row=15,column=12)

        # Botones cargar cajero

        def guardar_cajero():
            cajero[conf[6]] += int(self.label_carga_cantidad_monedast1.get())
            cajero[conf[7]] += int(self.label_carga_cantidad_monedast2.get())
            cajero[conf[8]] += int(self.label_carga_cantidad_monedast3.get())
            
            cajero[conf[10]] += int(self.label_carga_cantidad_billetest1.get())
            cajero[conf[11]] += int(self.label_carga_cantidad_billetest2.get())
            cajero[conf[12]] += int(self.label_carga_cantidad_billetest3.get())
            cajero[conf[13]] += int(self.label_carga_cantidad_billetest4.get())
            cajero[conf[14]] += int(self.label_carga_cantidad_billetest5.get())
            print(cajero)

            self.label_saldo_cantidad_monedast1.config(text=cajero[conf[6]])
            self.label_saldo_cantidad_monedast2.config(text=cajero[conf[7]])
            self.label_saldo_cantidad_monedast3.config(text=cajero[conf[8]])
            self.label_saldo_cantidad_total_monedas.config(text=cajero[conf[6]]+cajero[conf[7]]+cajero[conf[8]])
            self.label_saldo_cantidad_billetest1.config(text=cajero[conf[10]])
            self.label_saldo_cantidad_billetest2.config(text=cajero[conf[11]])
            self.label_saldo_cantidad_billetest3.config(text=cajero[conf[12]])
            self.label_saldo_cantidad_billetest4.config(text=cajero[conf[13]])
            self.label_saldo_cantidad_billetest5.config(text=cajero[conf[14]])
            self.label_saldo_cantidad_total_billetes.config(text=cajero[conf[10]]+cajero[conf[11]]+cajero[conf[12]]+cajero[conf[13]]+cajero[conf[14]])
            
            self.label_saldo_total_monedast1.config(text=cajero[conf[6]]*int(conf[6]))
            self.label_saldo_total_monedast2.config(text=cajero[conf[7]]*int(conf[7]))
            self.label_saldo_total_monedast3.config(text=cajero[conf[8]]*int(conf[8]))
            self.label_saldo_total_total_monedas.config(text=cajero[conf[6]]*int(conf[6])+cajero[conf[7]]*int(conf[7])+cajero[conf[8]]*int(conf[8]))
            self.label_saldo_total_billetest1.config(text=cajero[conf[10]]*int(conf[10]))
            self.label_saldo_total_billetest2.config(text=cajero[conf[11]]*int(conf[11]))
            self.label_saldo_total_billetest3.config(text=cajero[conf[12]]*int(conf[12]))
            self.label_saldo_total_billetest4.config(text=cajero[conf[13]]*int(conf[13]))
            self.label_saldo_total_billetest5.config(text=cajero[conf[14]]*int(conf[14]))
            self.label_saldo_total_total_billetes.config(text=cajero[conf[10]]*int(conf[10])+cajero[conf[11]]*int(conf[11])+cajero[conf[12]]*int(conf[12])+cajero[conf[13]]*int(conf[13])+cajero[conf[14]]*int(conf[14]))
            self.label_saldo_total_total__cajero.config(text=cajero[conf[6]]*int(conf[6])+cajero[conf[7]]*int(conf[7])+cajero[conf[8]]*int(conf[8])+cajero[conf[10]]*int(conf[10])+cajero[conf[11]]*int(conf[11])+cajero[conf[12]]*int(conf[12])+cajero[conf[13]]*int(conf[13])+cajero[conf[14]]*int(conf[14]))
            
            f = open('cajero.dat','w')
            f.write(str(cajero))
            f.close()

    
            
        boton_Ok = tk.Button(self.canvas_cargar, text="Ok",command=guardar_cajero)
        boton_Ok.grid(row=22, column=2)

        boton_cancelar = tk.Button(self.canvas_cargar, text="Cancelar",command=self.ventana_cambiar_menu)
        boton_cancelar.grid(row=22, column=3)

        boton_vaciar_cajero = tk.Button(self.canvas_cargar, text="Vaciar cajero")
        boton_vaciar_cajero.grid(row=22, column=4)

     
        self.canvas_cargar.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_cargar.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

class SaldoCajero:
    def __init__(self, master):
    
        self.master = master
        self.master.geometry('800x500')
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
        self.label_denominacion_monedast1 = Label(self.canvas_saldo, text='Moneda de 50')
        self.label_denominacion_monedast1.grid(row=3,column=0)
        self.label_denominacion_monedast2 = Label(self.canvas_saldo, text='Moneda de 100')
        self.label_denominacion_monedast2.grid(row=4,column=0)
        self.label_denominacion_monedast3 = Label(self.canvas_saldo, text='Moneda de 500')
        self.label_denominacion_monedast3.grid(row=5,column=0)
        self.label_denominacion_total_monedas = Label(self.canvas_saldo, text='TOTAL DE MONEDAS')
        self.label_denominacion_total_monedas.grid(row=6,column=0)
        self.label_denominacion_espacio1 = Label(self.canvas_saldo, text='')
        self.label_denominacion_espacio1.grid(row=7,column=0)
        self.label_denominacion_billetest1 = Label(self.canvas_saldo, text='Billetes de 1000')
        self.label_denominacion_billetest1.grid(row=8,column=0)
        self.label_denominacion_billetest2 = Label(self.canvas_saldo, text='Billetes de 2000')
        self.label_denominacion_billetest2.grid(row=9,column=0)
        self.label_denominacion_billetest3 = Label(self.canvas_saldo, text='Billetes de 5000')
        self.label_denominacion_billetest3.grid(row=10,column=0)
        self.label_denominacion_billetest4 = Label(self.canvas_saldo, text='Billetes de 10000')
        self.label_denominacion_billetest4.grid(row=11,column=0)
        self.label_denominacion_billetest5 = Label(self.canvas_saldo, text='Billetes de 20000')
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
        self.label_saldo_total_total__monedas = Label(self.canvas_saldo, text='0')
        self.label_saldo_total_total__monedas.grid(row=6,column=12)
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

        boton_Ok = tk.Button(self.canvas_saldo, text="Ok")
        boton_Ok.grid(row=22, column=2)

        boton_cancelar = tk.Button(self.canvas_saldo, text="Cancelar",command=self.ventana_cambiar_menu)
        boton_cancelar.grid(row=22, column=3)

     
        self.canvas_saldo.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_saldo.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

class IngresosDinero:
    def __init__(self, master):
    
        self.master = master
        self.master.geometry('500x500')
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
        boton_Ok.grid(row=22, column=2)

        boton_cancelar = tk.Button(self.canvas_ingresos, text="Cancelar",command=self.ventana_cambiar_menu)
        boton_cancelar.grid(row=22, column=3)

     
        self.canvas_ingresos.mainloop()

    def ventana_cambiar_menu(self):
        self.canvas_ingresos.destroy()
        self.master.geometry('500x500')
        MenuPrincipal(self.master)

window = Tk()
MenuPrincipal(window)
window.title('Proyecto')
window.geometry('500x500')
window.mainloop()