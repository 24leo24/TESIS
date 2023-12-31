import tkinter as tk
from primaria import Vista1
from secundaria import Vista2


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mi Aplicación")
        self.configure(bg="#CCE6FF")  # Fondo celeste claro
        self.resizable(False, False)  # Ventana no redimensionable

        # Dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Dimensiones de la ventana
        window_width = int(screen_width * 0.6)  # 60% del ancho de la pantalla
        window_height = int(screen_height * 0.6)  # 60% de la altura de la pantalla

        # Posición para centrar la ventana en la pantalla
        window_x = (screen_width - window_width) // 2
        window_y = (screen_height - window_height) // 2

        # Configuración de la ventana
        self.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

        


        self.vista_actual = None
        self.switch_vista(Vista1)

    def switch_vista(self, vista_class):
        if self.vista_actual is not None:
            self.vista_actual.pack_forget()

        if vista_class == Vista1:
            self.vista_actual = Vista1(self, mostrar_vista2=self.mostrar_vista2)
        if vista_class == Vista2:
            self.vista_actual = Vista2(self, mostrar_vista1=self.mostrar_vista1)

        self.vista_actual.pack()

    def mostrar_vista2(self):
        self.switch_vista(Vista2)

    def mostrar_vista1(self):
        self.switch_vista(Vista1)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
