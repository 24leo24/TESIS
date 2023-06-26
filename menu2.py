import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import filedialog


class AbstractFactory(ABC):
    @abstractmethod
    def create_header(self):
        pass
    
    @abstractmethod
    def create_section(self):
        pass
    
    @abstractmethod
    def create_line(self):
        pass

class ConcreteFactory(AbstractFactory):
    def create_header(self):
        return Header()
    
    def create_section(self):
        return Section()
    
    def create_line(self):
        return Line()

class AbstractProduct(ABC):
    @abstractmethod
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

def add_content(factory):
    header = factory.create_header()
    section = factory.create_section()
    line = factory.create_line()

    # Agregar el contenido a la estructura predefinida del archivo TXT
    txt_content = [header.get_content(), section.get_content(), line.get_content()]
    # Agregar el contenido ingresado por el usuario
    user_content = "Contenido ingresado por el usuario"
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

    btn_export = tk.Button(root, text="Exportar", command=lambda: add_content(factory))
    btn_export.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
