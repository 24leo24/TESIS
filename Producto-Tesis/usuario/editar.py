
"""
Dentro de este módulo se genera toda la logica para poder editar los contenedores.
"""

import tkinter as tk
#from tkinter import messagebox
from usuario.conexion_sqlite import Comunicacion
from usuario.ventana_modal import VentanaModal

class Frame4(tk.Frame):
    def __init__(self, master=None, mostrar_vista1=None):
        super().__init__(master)

        self.mostrar_vista1 = mostrar_vista1

        etiqueta_id = tk.Label(self, text="ID:")
        etiqueta_id.grid(row=3, column=1, padx=10, pady=10)

        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=3, column=2, padx=10, pady=10)

        boton_buscar = tk.Button(self, text="Buscar", command=self.buscar_registro)
        boton_buscar.config(width=12, font=('Arial', 12, 'bold'),
        fg = '#DAD5D6', bg='#3371FF', cursor='hand2', activebackground='#33ACFF')
        boton_buscar.grid(row=3, column=3, padx=10, pady=10)

        etiqueta_nombre = tk.Label(self, text="Nombre:")
        etiqueta_nombre.grid(row=4, column=1, padx=10, pady=10)

        self.entry_nombre = tk.Entry(self, width=50)
        self.entry_nombre.grid(row=4, column=2, padx=10, pady=10)

        etiqueta_asignatura = tk.Label(self, text="Asignatura:")
        etiqueta_asignatura.grid(row=5, column=1, padx=10, pady=10)

        self.entry_asignatura = tk.Entry(self, width=50)
        self.entry_asignatura.grid(row=5, column=2, padx=10, pady=10)

        etiqueta_recomendacion = tk.Label(self, text="Recomendación:")
        etiqueta_recomendacion.grid(row=6, column=1, padx=10, pady=10)

        self.entry_recomendacion = tk.Entry(self, width=50)
        self.entry_recomendacion.grid(row=6, column=2, padx=10, pady=10)

        etiqueta_contenido = tk.Label(self, text="Contenido:")
        etiqueta_contenido.grid(row=7, column=1, padx=10, pady=10)

        self.entry_contenido = tk.Text(self, height=15, width=55)
        self.entry_contenido.grid(row=7, column=2, padx=10, pady=10)

        boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_registro)
        boton_guardar.config(width=12, font=('Arial', 12, 'bold'),fg = '#DAD5D6',
        bg='#229805', cursor='hand2', activebackground='#34CD0E')
        boton_guardar.grid(row=8, column=2, padx=10, pady=10)

        boton_nuevo = tk.Button(self, text="VOLVER")
        boton_nuevo.config(width=12, font=('Arial', 12, 'bold'),
        fg='#DAD5D6',bg='#FF3333',cursor='hand2',
        activebackground='#FF6B33',command=self.mostrar_vista1)
        boton_nuevo.grid(row=9, column=2, padx=0, pady=30)

    def buscar_registro(self):
        id = self.entry_id.get()
        if id:
            try:
                id = int(id)
                comunicacion = Comunicacion()
                registro = comunicacion.mostrar_registro_por_id(id)
                if registro:
                    self.entry_nombre.delete(0, tk.END)
                    self.entry_asignatura.delete(0, tk.END)
                    self.entry_recomendacion.delete(0, tk.END)
                    self.entry_contenido.delete("1.0", tk.END)
                    self.entry_nombre.insert(0, registro[0])
                    self.entry_asignatura.insert(0, registro[1])
                    self.entry_recomendacion.insert(0, registro[2])
                    self.entry_contenido.insert("1.0", registro[3])
                else:
                    VentanaModal(self,"ERROR", f"No se encontró un registro con el ID {id}")
            except ValueError:
                VentanaModal(self,"ERROR", "Por favor, ingrese un ID válido.")
        else:
            VentanaModal(self,"ERROR", "Por favor, ingrese un ID válido.")

    def guardar_registro(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        asignatura = self.entry_asignatura.get()
        recomendacion = self.entry_recomendacion.get()
        contenido = self.entry_contenido.get("1.0", tk.END)

        if id and nombre and asignatura and recomendacion and contenido:
            try:
                id = int(id)
                comunicacion = Comunicacion()
                comunicacion.actulizar_datos(id, nombre, asignatura, recomendacion, contenido)
                VentanaModal(self,"EXITO", "Registro actualizado exitosamente.")
            except ValueError:
                VentanaModal(self,"ERROR", "Por favor, ingrese un ID válido.")
        else:
            VentanaModal(self,"ERROR", "Por favor, ingrese un ID.")
