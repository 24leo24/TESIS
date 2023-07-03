import tkinter as tk
from tkinter import filedialog
import io

class Frame3(tk.Frame):
    def __init__(self, master=None, mostrar_vista1=None):
        super().__init__(master)
        

        self.mostrar_vista1 = mostrar_vista1
       

        #BOTONES DE LA VISTAA
        self.boton_nuevo = tk.Button(self, text="VOLVER")
        self.boton_nuevo.config(width=12, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#FF3333', cursor='hand2', activebackground='#FF6B33', command=self.mostrar_vista1)
        self.boton_nuevo.grid(row=3, column=2, padx=0, pady= 100)

        self.marco_archivos = tk.LabelFrame(self, text="BIBLOTECA DE CONTENEDORES")
        self.marco_archivos.grid(row=2, column=2, padx=0, pady=0)

        self.crear_archivos()

    def crear_archivos(self):
        # Archivo 1
        nombre_archivo1 = "Contenedor con Apache2"
        contenido_archivo1 = """FROM ubuntu:latest
MAINTAINER EUGENIO eucm2g@gmail.com
RUN apt-get update
RUN apt-get -y install apache2
expose 80
CMD /usr/sbin/apache2ctl -D FOREGROUND"""

        marco_archivo1 = tk.Frame(self.marco_archivos)
        marco_archivo1.pack(padx=100, pady=20)

        etiqueta_nombre_archivo1 = tk.Label(marco_archivo1, text=nombre_archivo1)
        etiqueta_nombre_archivo1.config(font=('Arial', 12, 'bold'))
        etiqueta_nombre_archivo1.pack(side="left")

        boton_crear_archivo1 = tk.Button(marco_archivo1, text="CREAR", command=lambda: self.exportar_archivo(contenido_archivo1, nombre_archivo1))
        boton_crear_archivo1.config(width=9, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#229805', cursor='hand2', activebackground='#34CD0E')
        boton_crear_archivo1.pack(side="right")

        # Archivo 2
        nombre_archivo2 = "Contenedor con MYSQL"
        contenido_archivo2 = """FROM ubuntu:14.04 
MAINTAINER José Domingo Muñoz "josedom24@gmail.com"

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y mysql-server

ADD my.cnf /etc/mysql/conf.d/my.cnf 
ADD script.sh /usr/local/bin/script.sh
RUN chmod +x /usr/local/bin/script.sh

EXPOSE 3306

CMD ["/usr/local/bin/script.sh"]"""

        marco_archivo2 = tk.Frame(self.marco_archivos)
        marco_archivo2.pack(padx=100, pady=20)

        etiqueta_nombre_archivo2 = tk.Label(marco_archivo2, text=nombre_archivo2)
        etiqueta_nombre_archivo2.config(font=('Arial', 12, 'bold'))
        etiqueta_nombre_archivo2.pack(side="left")

        boton_crear_archivo2 = tk.Button(marco_archivo2, text="CREAR", command=lambda: self.exportar_archivo(contenido_archivo2, nombre_archivo2))
        boton_crear_archivo2.config(width=9, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#229805', cursor='hand2', activebackground='#34CD0E')
        boton_crear_archivo2.pack(side="right")

        # Archivo 3
        nombre_archivo3 = "Contenedor con Node.js"
        contenido_archivo3 = """FROM node:8

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 3000
CMD [ "npm", "start" ]"""

        marco_archivo3 = tk.Frame(self.marco_archivos)
        marco_archivo3.pack(padx=100, pady=20)

        etiqueta_nombre_archivo3 = tk.Label(marco_archivo3, text=nombre_archivo3)
        etiqueta_nombre_archivo3.config(font=('Arial', 12, 'bold'))
        etiqueta_nombre_archivo3.pack(side="left")

        boton_crear_archivo3 = tk.Button(marco_archivo3, text="CREAR", command=lambda: self.exportar_archivo(contenido_archivo3, nombre_archivo3))
        boton_crear_archivo3.config(width=9, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#229805', cursor='hand2', activebackground='#34CD0E')
        boton_crear_archivo3.pack(side="right")

    def exportar_archivo(self, contenido, nombre):
        archivo = filedialog.asksaveasfile(mode='w', defaultextension=".txt", initialfile="Dockerfile", filetypes=[("", "*.")])
        if archivo is not None:
            archivo.write(contenido)
            archivo.close()