import tkinter as tk
from tkinter import filedialog

class AbstractFactory:
    def create_header(self):
        pass
    
    def create_section(self):
        pass
    
    def create_line(self):
        pass

class ConcreteFactory(AbstractFactory):
    def create_header(self):
        return Header()
    
    def create_section(self):
        return Section()
    
    def create_line(self):
        return Line()

class AbstractProduct:
    def get_content(self):
        pass

class Header(AbstractProduct):
    def get_content(self):
        return "Contenido del encabezado"

class Section(AbstractProduct):
    def get_content(self):
        return "Contenido de la sección"

class Line(AbstractProduct):
    def get_content(self):
        return "Contenido de la línea"

def add_content(factory, text_widget):
    header = factory.create_header()
    section = factory.create_section()
    line = factory.create_line()

    # Agregar el contenido a la estructura predefinida del archivo TXT
    txt_content = [header.get_content(), section.get_content(), line.get_content()]
    # Agregar el contenido ingresado por el usuario
    user_content = text_widget.get("1.0", "end-1c")
    txt_content.append(user_content)

    # Obtener la ruta de archivo de salida mediante un cuadro de diálogo
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

    # Exportar el contenido del archivo TXT
    if file_path:
        with open(file_path, "w") as file:
            file.write("\n".join(txt_content))

def main():
    root = tk.Tk()
    root.title("Exportador de Archivo TXT")

    factory = ConcreteFactory()

    # Crear una sección de entrada de texto
    section_text = tk.Text(root, height=5, width=30)
    section_text.pack()

    btn_export = tk.Button(root, text="Exportar", command=lambda: add_content(factory, section_text))
    btn_export.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
