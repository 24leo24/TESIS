import tkinter as tk
from usuario.gui_app import Frame, barra_menu
from usuario.crear_contenedor import Frame2 
#from usuario.crear_contenedor import Frame as Frame2



def switch_vista(self, vista_class):
    if self.vista_actual is not None:
        self.vista_actual.pack_forget()

    if vista_class == Frame:
        self.vista_actual = Frame(self, mostrar_vista2=self.mostrar_vista2)
    if vista_class == Frame2:
        self.vista_actual = Frame2(self, mostrar_vista1=self.mostrar_vista1)

    self.vista_actual.pack()

def mostrar_vista2(self):
    self.switch_vista(Frame2)

def mostrar_vista1(self):
    self.switch_vista(Frame)



def main():

    root = tk.Tk()
    root.title('HERRAMIENTA DE APOYO')
    root.iconbitmap('img/UVALPO_ESC.ico')
    root.resizable(0,0) 
    root.vista_actual = None
    root.switch_vista(Frame)
    barra_menu(root)
    #crear_contenedor=crear_contenedor.ventana_secundaria(root, mostrar_principal)


    #app = Frame(root=root) 
    #app2 = Frame2(root=root) 

    #app2.mainloop()
    root.mainloop()



    
    

if __name__ == '__main__':
    main()
    