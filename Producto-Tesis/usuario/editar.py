import tkinter as tk


class Frame4(tk.Frame):
    def __init__(self, master=None, mostrar_vista1=None):
        super().__init__(master)
        

        self.mostrar_vista1 = mostrar_vista1
       

       #BOTONES DE LA VISTA
        self.boton_nuevo = tk.Button(self, text="VOLVER")
        self.boton_nuevo.config(width=12, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#FF3333', cursor='hand2', activebackground='#FF6B33', command=self.mostrar_vista1)
        self.boton_nuevo.grid(row=3, column=2, padx=0, pady= 230)

        etiqueta_titulo = tk.Label(self, text="EDITAR CONTENEDORES", font=("Arial", 16, "bold"))
        etiqueta_titulo.grid(row=2, column=2, padx=0, pady=50)