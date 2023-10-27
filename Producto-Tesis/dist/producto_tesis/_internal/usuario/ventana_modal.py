"""
Dentro de este módulo se genera toda la logica para genrar 
ventanas modales dentro de la herramienta.
"""

import tkinter as tk
#from tkinter import messagebox

class VentanaModal(tk.Toplevel):
    def __init__(self, parent, titulo, mensaje):
        super().__init__(parent)

        self.title(titulo)
        self.geometry("300x150")
        self.resizable(False, False)

        self.label_mensaje = tk.Label(self, text=mensaje, padx=20, pady=20)
        self.label_mensaje.pack()

        self.boton_aceptar = tk.Button(self, text="Aceptar", command=self.cerrar)
        self.boton_aceptar.pack()

        #  Obtenemos el largo y  ancho de la pantalla
        wtotal = self.winfo_screenwidth()
        htotal = self.winfo_screenheight()
        #  Guardamos el largo y alto de la ventana
        wventana = 300
        hventana = 150

        #  Aplicamos la siguiente formula para calcular donde debería posicionarse
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        #  Se lo aplicamos a la geometría de la ventana
        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def cerrar(self):
        self.destroy()
class VentanaModal2(tk.Toplevel):
    def __init__(self, parent, titulo, mensaje, botones=("Sí", "No")):
        super().__init__(parent)

        self.title(titulo)
        self.geometry("300x150")
        self.resizable(False, False)

        self.label_mensaje = tk.Label(self, text=mensaje, padx=20, pady=20)
        self.label_mensaje.pack()

        self.boton_aceptar = tk.Button(self, text=botones[0],
        command=self.aceptar , width=10)
        self.boton_aceptar.pack(side="left", padx=10)

        self.boton_cancelar = tk.Button(self, text=botones[1],
        command=self.cancelar , width=10)
        self.boton_cancelar.pack(side="right", padx=10)

        # Obtenemos el largo y ancho de la pantalla
        wtotal = self.winfo_screenwidth()
        htotal = self.winfo_screenheight()
        # Guardamos el largo y alto de la ventana
        wventana = 300
        hventana = 150

        # Aplicamos la siguiente formula para calcular donde debería posicionarse
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        # Se lo aplicamos a la geometría de la ventana
        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

        # Variable para almacenar la respuesta del usuario
        self.respuesta = None

    def aceptar(self):
        self.respuesta = "Sí"
        self.destroy()

    def cancelar(self):
        self.respuesta = "No"
        self.destroy()
