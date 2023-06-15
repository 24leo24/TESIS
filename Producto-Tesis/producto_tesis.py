import tkinter as tk
from usuario.gui_app import Frame

def main():
    root = tk.Tk()
    root.title('HERRAMIENTA DE APOYO')
    root.iconbitmap('img/UVALPO_ESC.ico')
    root.resizable(0,0) 

    app = Frame(root=root)

    app.mainloop()

if __name__ == '__main__':
    main()