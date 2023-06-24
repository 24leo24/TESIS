import tkinter as tk
#from usuario.crear_contenedor import Frame2

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_principal = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_principal)

    menu_principal.add_command(label='Crear Contenedor')
    menu_principal.add_command(label='Lista de contenedores')
    menu_principal.add_command(label='Editar Contenedor')
    menu_principal.add_command(label='Salir', command=root.destroy)

#def abrir_nueva_vista():
    # Crear una nueva ventana
    #nueva_vista = tk.Toplevel()
    
    # Configurar propiedades de la nueva ventana
    #nueva_vista.title("Nueva Vista")
    #nueva_vista.geometry("400x300")
    
    # Agregar contenido a la nueva ventana
    #label = tk.Label(nueva_vista, text="¡Has abierto una nueva vista!")
    #label.pack()
#def mostrar_secundaria(self):
#    Frame.pack_forget()
#    crear_contenedor.pack()

#def mostrar_principal():
#    crear_contenedor.pack_forget()
#    Frame.pack()


class Frame(tk.Frame):
    def __init__(self, root = None, mostrar_vista2=None):
        super().__init__(root,width=880, height=500)
        self.root = root
        self.pack()
        
        self.mostrar_vista2 = mostrar_vista2
        
        self.campos_contenedor()
       
        

    #def mostrar_secundaria(self):
     #   self.pack_forget()
      #  Frame2().pack()

    def campos_contenedor(self):
        #Labels de cada campo 
        #self.label_nombre = tk.Label(self, text='Nombre del contenedor ')
        #self.label_nombre.config(font= ('Arial', 12, 'bold'))
        #self.label_nombre.grid(row=0, column=0, padx= 10, pady= 10)

        #self.label_contenido = tk.Label(self, text='Contenido del contenedor ')
        #self.label_contenido.config(font= ('Arial', 12, 'bold'))
        #self.label_contenido.grid(row=1, column=0, padx= 10, pady= 10)

        #campos de entrada 
        #self.entry_nombre = tk.Entry(self)
        #self.entry_nombre.config(width=50, font=('Arial',12))
        #self.entry_nombre.grid(row= 0, column=1, padx=10, pady= 10)

        #self.entry_contenido = tk.Entry(self)
        #self.entry_contenido.config(width=50, font=('Arial',12))
        #self.entry_contenido.grid(row= 1, column=1, padx=10, pady= 10)

        #boton crear contenedor 
        self.boton_nuevo = tk.Button(self, text="CREAR CONTENEDOR")
        self.boton_nuevo.config(width=28, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#3371FF', cursor='hand2', activebackground='#33ACFF', command=self.mostrar_vista2)
        self.boton_nuevo.grid(row= 2, column=2, padx=50, pady= 45)

        #boton bibloteca de contenedores
        self.boton_bibloteca = tk.Button(self, text="BIBLOTECA DE CONTENEDORES")
        self.boton_bibloteca.config(width=28, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#3371FF', cursor='hand2', activebackground='#33ACFF')
        self.boton_bibloteca.grid(row= 3, column=2, padx=50, pady= 45)

        #boton editar contenedor
        self.boton_editar = tk.Button(self, text="EDITAR CONTENEDORES")
        self.boton_editar.config(width=28, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#3371FF', cursor='hand2', activebackground='#33ACFF')
        self.boton_editar.grid(row= 4, column=2, padx=50, pady= 45)
 

