import tkinter as tk


class Frame4(tk.Frame):
    def __init__(self, master=None, mostrar_vista1=None):
        super().__init__(master)
        

        self.mostrar_vista1 = mostrar_vista1
       

       #esto
        #self.boton_nuevo = tk.Button(self, text="BOTON DE EDITAR")
        #self.boton_nuevo.config(width=28, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#3371FF', cursor='hand2', activebackground='#33ACFF', command=self.mostrar_vista1)
        #self.boton_nuevo.grid(row= 2, column=2, padx=50, pady= 45)

        self.boton_nuevo = tk.Button(self, text="VOLVER")
        self.boton_nuevo.config(width=12, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#FF3333', cursor='hand2', activebackground='#FF6B33', command=self.mostrar_vista1)
        self.boton_nuevo.grid(row=4, column=3, padx=600, pady= 370)