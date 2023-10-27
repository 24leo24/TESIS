"""
Dentro de este módulo se encuntran los botones principales que contiene la GUI y su navegacion.
"""

import tkinter as tk

class Frame(tk.Frame):
    def __init__(self,master = None, mostrar_vista2=None, mostrar_vista3=None, mostrar_vista4=None, mostrar_vista5=None):
        super().__init__(master)
        self.mostrar_vista2 = mostrar_vista2
        self.mostrar_vista3 = mostrar_vista3
        self.mostrar_vista4 = mostrar_vista4
        self.mostrar_vista5 = mostrar_vista5

        # boton de crear contenedor
        self.boton_nuevo = tk.Button(self, text="CREAR CONTENEDOR")
        self.boton_nuevo.config(width=28, font=('Arial', 12, 'bold'))
        self.boton_nuevo.config(fg = '#DAD5D6', bg='#3371FF', cursor='hand2'
        , activebackground='#33ACFF', command=self.mostrar_vista2)
        self.boton_nuevo.grid(row= 2, column=2, padx=50, pady= 45)

        # boton de bibloteca de contenedores
        self.boton_nuevo = tk.Button(self, text="BIBLOTECA DE CONTENEDORES")
        self.boton_nuevo.config(width=28, font=('Arial', 12, 'bold'),
        fg = '#DAD5D6', bg='#3371FF', cursor='hand2',
        activebackground='#33ACFF', command=self.mostrar_vista3)
        self.boton_nuevo.grid(row= 3, column=2, padx=50, pady= 45)

        # boton de editar contenodes
        self.boton_nuevo = tk.Button(self, text="EDITAR CONTENEDOR")
        self.boton_nuevo.config(width=28, font=('Arial', 12, 'bold'),
        fg = '#DAD5D6', bg='#3371FF', cursor='hand2',
        activebackground='#33ACFF', command=self.mostrar_vista4)
        self.boton_nuevo.grid(row= 4, column=2, padx=50, pady= 45)

        # boton de editar contenodes
        self.boton_nuevo = tk.Button(self, text="¿COMO EJECUTAR UN CONTENEDOR?")
        self.boton_nuevo.config(width=32, font=('Arial', 12, 'bold'),
        fg = '#DAD5D6', bg='#3371FF', cursor='hand2',
        activebackground='#33ACFF', command=self.mostrar_vista5)
        self.boton_nuevo.grid(row= 5, column=2, padx=50, pady= 45)
