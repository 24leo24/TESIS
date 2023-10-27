
"""
Dentro de este módulo la logica para crear un nuevo contenedor.
"""

import tkinter as tk
#from tkinter import messagebox
from usuario.conexion_sqlite import Comunicacion
from usuario.ventana_modal import VentanaModal


class Frame2(tk.Frame):
    def __init__(self, master=None, mostrar_vista1=None):
        super().__init__(master)
        self.mostrar_vista1 = mostrar_vista1
        self.comunicacion = Comunicacion()

        # Etiqueta de título
        etiqueta_titulo = tk.Label(self, text="CREAR CONTENEDORES", font=("Arial", 16, "bold"))
        etiqueta_titulo.grid(row=1, column=1, columnspan=2, padx=10, pady=20)

        # Etiquetas y campos de entrada
        tk.Label(self, text="Nombre:", pady=15).grid(row=2, column=1, sticky="e", padx=10)
        self.entry_nombre = tk.Entry(self, width=70, font=("Arial", 12), justify="left", )
        self.entry_nombre.grid(row=2, column=2, padx=10)

        tk.Label(self, text="Asignatura:", pady=15).grid(row=3, column=1, sticky="e", padx=10)
        self.entry_asignatura = tk.Entry(self, width=70, font=("Arial", 12), justify="left")
        self.entry_asignatura.grid(row=3, column=2, padx=10)

        tk.Label(self, text="Recomendación:").grid(row=4, column=1, sticky="e", padx=10, pady=5)
        self.entry_recomendacion = tk.Entry(self, width=70, font=("Arial", 12), justify="left")
        self.entry_recomendacion.grid(row=4, column=2, padx=10, pady=5)

        tk.Label(self, text="Contenido:").grid(row=5, column=1, sticky="e", padx=10, pady=5)
        self.text_contenido = tk.Text(self, height=8, wrap="word")
        self.text_contenido.grid(row=5, column=2, padx=10, pady=5)

        # Botónes
        boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        boton_guardar.config(width=12, font=('Arial', 12, 'bold'),
        fg = '#DAD5D6', bg='#229805', cursor='hand2',
        activebackground='#34CD0E')
        boton_guardar.grid(row=6, column=2, padx=10, pady=20)

        boton_volver = tk.Button(self, text="Volver", command=self.mostrar_vista1)
        boton_volver.config(width=12, font=('Arial', 12, 'bold'),
        fg = '#DAD5D6', bg='#FF3333', cursor='hand2',
        activebackground='#FF6B33')
        boton_volver.grid(row=7, column=2, padx=330, pady=50, sticky="w")


    def guardar_datos(self):
        nombre = self.entry_nombre.get()
        asignatura = self.entry_asignatura.get()
        recomendacion = self.entry_recomendacion.get()
        contenido = self.text_contenido.get("1.0", "end-1c")  # Obtener el contenido del Text widget

        # Verificar si todos los campos están completos
        if not nombre or not asignatura or not recomendacion or not contenido:
            VentanaModal(self, "CAMPOS VACIOS", "Por favor, rellene todos los campos.")
            return

        # Si todos los campos están completos, insertar los datos en la base de datos
        self.comunicacion.insertar_datos(nombre, asignatura, recomendacion, contenido)

        # Limpiar los campos después de guardar
        self.entry_nombre.delete(0, "end")
        self.entry_asignatura.delete(0, "end")
        self.entry_recomendacion.delete(0, "end")
        self.text_contenido.delete("1.0", "end")

        # Mostrar mensaje de éxito
        VentanaModal(self, "EXITO", "Los datos se han guardado correctamente.")

        #BOTONES DE LA VISTA CREAR CONTENEDOR
        #self.boton_nuevo = tk.Button(self, text="VOLVER")
        #self.boton_nuevo.config(width=12, font=('Arial', 12, 'bold'),
        #fg = '#DAD5D6', bg='#FF3333', cursor='hand2',
        #activebackground='#FF6B33', command=self.mostrar_vista1)
        #self.boton_nuevo.grid(row=6, column=2, padx=10, pady= 20)

        #etiqueta_titulo = tk.Label(self, text="CREAR CONTENEDORES", font=("Arial", 16, "bold"))
        #etiqueta_titulo.grid(row=2, column=2, padx=0, pady=50)
 