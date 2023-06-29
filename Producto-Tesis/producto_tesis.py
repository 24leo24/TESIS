import tkinter as tk
from usuario.gui_app import Frame
from usuario.crear_contenedor import Frame2
from usuario.bibloteca import Frame3
from usuario.editar import Frame4


class mainapp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("HERRAMIENTA DE APOYO")
        self.iconbitmap('img/UVALPO_ESC.ico')
        #self.resizable(False, False)  # Ventana no redimensionable

        # Dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Dimensiones de la ventana
        window_width = int(screen_width * 0.4)  # 60% del ancho de la pantalla
        window_height = int(screen_height * 0.38)  # 60% de la altura de la pantalla

        # Posición para centrar la ventana en la pantalla
        window_x = (screen_width - window_width) // 2
        window_y = (screen_height - window_height) // 2

        # Configuración de la ventana
        self.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

        self.vista_actual = None
        self.switch_vista(Frame)

    def switch_vista(self, vista_class):
        if self.vista_actual is not None:
            self.vista_actual.pack_forget()

        if vista_class == Frame:
            self.vista_actual = Frame(self, mostrar_vista2=self.mostrar_vista2, mostrar_vista3=self.mostrar_vista3, mostrar_vista4=self.mostrar_vista4)
        
        if vista_class == Frame2:
            self.vista_actual = Frame2(self, mostrar_vista1=self.mostrar_vista1)

        if vista_class == Frame3:
            self.vista_actual = Frame3(self, mostrar_vista1=self.mostrar_vista1)

        if vista_class == Frame4:
            self.vista_actual = Frame4(self, mostrar_vista1=self.mostrar_vista1)

        self.vista_actual.pack()

    def mostrar_vista1(self):
        self.switch_vista(Frame)

    def mostrar_vista2(self):
        self.switch_vista(Frame2)

    def mostrar_vista3(self):
        self.switch_vista(Frame3)

    def mostrar_vista4(self):
        self.switch_vista(Frame4)


if __name__ == '__main__':
    app = mainapp()
    app.mainloop()
