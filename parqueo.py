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

window = Tk()
MenuPrincipal(window)
window.title('Proyecto')
window.geometry('500x500')
window.mainloop()