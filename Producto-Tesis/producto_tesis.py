
"""
Dentro de este módulo se encuntra la clase pricipal del programa
donde se generan la estructura base de la GUI y toda su navegacion.
"""

import tkinter as tk
import os
from usuario.gui_app import Frame
from usuario.crear_contenedor import Frame2
from usuario.ejecutar_contenedor import Frame6
from usuario.editar import Frame4
from usuario.bibloteca2 import Frame5

class MainApp(tk.Tk):
    """
    Clase en donde se genera toda la estructura de la GUI
    """
    def __init__(self):
        super().__init__()

        # Obtiene la ruta del directorio actual del script
        script_di0 = os.path.dirname(__file__)

         # Retrocede un nivel para acceder a la carpeta principal
        #main_dir0 = os.path.dirname(script_di0)

        # Construye la ruta a la imagen usando el directorio actual
        imagen_path0 = os.path.join(script_di0, 'img', 'UVALPO_ESC.ico')

        

        self.title("HERRAMIENTA DE APOYO")
        self.iconbitmap(imagen_path0)
        self.resizable(False, False)  # Ventana no redimensionable

        # Dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Dimensiones de la ventana
        window_width = int(screen_width * 0.48)  # 60% del ancho de la pantalla
        window_height = int(screen_height * 0.53)  # 60% de la altura de la pantalla

        # Posición para centrar la ventana en la pantalla
        window_x = (screen_width - window_width) // 2
        window_y = (screen_height - window_height) // 2

        # Configuración de la ventana
        self.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

        self.vista_actual = None
        self.switch_vista(Frame)
    def switch_vista(self, vista_class):
        """
        Dentro de esta funcion se genera toda la nevegacion dentro de la GUI
        """
        if self.vista_actual is not None:
            self.vista_actual.pack_forget()

        if vista_class == Frame:
            self.vista_actual = Frame(self,mostrar_vista2=self.mostrar_vista2,mostrar_vista4=self.mostrar_vista4,mostrar_vista5=self.mostrar_vista5,mostrar_vista3=self.mostrar_vista3)

        if vista_class == Frame2:
            self.vista_actual = Frame2(self, mostrar_vista1=self.mostrar_vista1)

        if vista_class == Frame5:
            self.vista_actual = Frame5(self, mostrar_vista1=self.mostrar_vista1)

        if vista_class == Frame4:
            self.vista_actual = Frame4(self, mostrar_vista1=self.mostrar_vista1)

        if vista_class == Frame6:
            self.vista_actual = Frame6(self, mostrar_vista1=self.mostrar_vista1)

        self.vista_actual.pack()

    def mostrar_vista1(self):
        self.switch_vista(Frame)

    def mostrar_vista2(self):
        self.switch_vista(Frame2)

    def mostrar_vista3(self):
        self.switch_vista(Frame5)

    def mostrar_vista4(self):
        self.switch_vista(Frame4)

    def mostrar_vista5(self):
        self.switch_vista(Frame6)


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
