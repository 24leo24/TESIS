
"""
Dentro de este módulo se genera toda la logica de la bibloteca de contenedores.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
#from tkinter import messagebox
from tkinter import Scrollbar
from usuario.ventana_modal import VentanaModal
from usuario.ventana_modal import VentanaModal2
#import io
from usuario.conexion_sqlite import Comunicacion

class Frame5(tk.Frame):
    def __init__(self, master=None, mostrar_vista1=None):
        super().__init__(master)
        self.mostrar_vista1 = mostrar_vista1
        self.tabla = None
        self.seleccion_actual = None
        self.comunicacion = Comunicacion()  # Crea una instancia de la clase Comunicacion
        self.marco_archivos = tk.LabelFrame(self, text="Lista de contenedores")
        self.marco_archivos.grid(row=1, column=2,padx=0, pady=0)
        self.crear_archivos()

    def crear_archivos(self):
        datos_contenedores = self.comunicacion.mostrar_datos()#Obtiene de la base de datos

        self.marco_scroll = tk.Frame(self.marco_archivos)
        self.marco_scroll.grid(row=3, column=3,padx=0, pady=0,sticky="ns")

        self.tabla = ttk.Treeview(self.marco_scroll, height=14,
        columns=("ID", "Nombre", "Asignatura", "Recomendación"), show="headings")

        # Ajusta el ancho de las columnas
        self.tabla.column("ID", width=70)
        self.tabla.column("Nombre", width=230)
        self.tabla.column("Asignatura", width=230)
        self.tabla.column("Recomendación", width=300)

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Asignatura", text="Asignatura")
        self.tabla.heading("Recomendación", text="Recomendación")

        self.scroll_y = Scrollbar(self.marco_scroll,orient="vertical", command=self.tabla.yview)
        self.scroll_y.pack(fill="y", side="right")

        self.tabla.configure(yscrollcommand=self.scroll_y.set)

        for dato in datos_contenedores:
            self.tabla.insert("", "end", values=dato)

            self.tabla.pack(fill="both", expand=True)



        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)

        #BOTONES DE LA VISTA
        self.boton_exportar = tk.Button(self, text="Exportar", command=self.exportar_archivo)
        self.boton_exportar.config(width=12, font=('Arial', 12, 'bold'),
        fg = '#DAD5D6', bg='#229805', cursor='hand2', activebackground='#34CD0E')
        self.boton_exportar.grid(row=2, column=2, padx=0, pady=0)

        self.boton_borrar = tk.Button(self, text="Borrar", command=self.borrar_fila)
        self.boton_borrar.config(width=12, font=('Arial', 12, 'bold'),
        fg = '#DAD5D6', bg='#3371FF', cursor='hand2', activebackground='#33ACFF')
        self.boton_borrar.grid(row=3, column=2, padx=0, pady=50)

        self.boton_nuevo = tk.Button(self, text="VOLVER")
        self.boton_nuevo.config(width=12, font=('Arial', 12, 'bold'),
        fg = '#DAD5D6', bg='#FF3333', cursor='hand2',
        activebackground='#FF6B33', command=self.mostrar_vista1)
        self.boton_nuevo.grid(row=4, column=2, padx=0, pady= 10)


    #def borrar_fila2(self):
        #selected_item = self.tabla.selection()
        #if selected_item:
            #item_data = self.tabla.item(selected_item)['values']
            #contenido = item_data[0]
            #print(contenido)
            #fila_id = selected_item[0]
            #self.tabla.delete(fila_id)
            #self.comunicacion.eliminar_datos(contenido)
            #self.seleccion_actual = None

        #else:
            #VentanaModal(self, "FILA NO SELECCIONADA", "Por favor, seleccione una fila.")

    def borrar_fila(self):
        selected_item = self.tabla.selection()
        if selected_item:
            # Obtén el ID de la fila seleccionada
            item_data = self.tabla.item(selected_item)['values']
            contenido = item_data[0]
            #print(contenido)
            fila_id = selected_item[0]
            #Muestra la ventana modal de confirmación
            confirmacion = VentanaModal2(self, "Confirmación",
            "¿Está seguro de que desea eliminar este registro?", botones=("Sí", "No"))
            #Espera hasta que se cierre la ventana modal
            self.wait_window(confirmacion)
            # Verifica la respuesta de la ventana modal
            if confirmacion.respuesta == "Sí":
                # Elimina la fila de la tabla
                self.tabla.delete(fila_id)
                # Elimina el registro correspondiente de la base de datos
                self.comunicacion.eliminar_datos(contenido)

            # Limpia la selección actual
            self.seleccion_actual = None
        else:
            VentanaModal(self, "FILA NO SELECCIONADA", "Por favor, seleccione una fila.")


    def seleccionar_fila(self, event):
        selected_item = self.tabla.selection()
        if selected_item:
            self.seleccion_actual = selected_item[0]

    def exportar_archivo(self):
        selected_item = self.tabla.selection()
        if selected_item:
            item_data = self.tabla.item(selected_item)['values']
            contenido = item_data[4]
            archivo = filedialog.asksaveasfile(mode='w', defaultextension=".txt",
            initialfile="Dockerfile",filetypes=[("", "*.")])
            if archivo is not None:
                archivo.write(contenido)
                archivo.close()

            VentanaModal(self, "EXITO", "EL ARCHIVO SE HA EXPORTADO CORRECTAMENTE.")

        else:
            VentanaModal(self, "FILA NO SELECCIONADA", "Por favor, seleccione una fila.")
