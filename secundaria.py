import tkinter as tk


class Vista2(tk.Frame):
    def __init__(self, master=None, mostrar_vista1=None):
        super().__init__(master)

        self.mostrar_vista1 = mostrar_vista1

        self.button = tk.Button(self, text="Mostrar Vista 1", command=self.mostrar_vista1)
        self.button.pack()
