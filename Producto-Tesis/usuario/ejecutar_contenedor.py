
import tkinter as tk
import os
#from tkinter import filedialog
#from tkinter import Scrollbar
#from tkinter import PhotoImage
#from tkinter import ttk
from tkinter import Menu , END

class Frame6(tk.Frame):
    def __init__(self, master=None, mostrar_vista1=None):
        super().__init__(master)

        # Obtiene la ruta del directorio actual del script
        script_dir = os.path.dirname(__file__)

         # Retrocede un nivel para acceder a la carpeta principal
        main_dir1 = os.path.dirname(script_dir)

        # Construye la ruta a la imagen usando el directorio actual
        imagen_path1 = os.path.join(main_dir1, 'img', 'img1.gif')
        imagen_path2 = os.path.join(main_dir1, 'img', 'imagen 2.gif')
        imagen_path3 = os.path.join(main_dir1, 'img', 'imagen 3.gif')
        imagen_path4 = os.path.join(main_dir1, 'img', 'img4.gif')
        imagen_path5 = os.path.join(main_dir1, 'img', 'img5.gif')
        imagen_path6 = os.path.join(main_dir1, 'img', 'imagen 6.gif')
        imagen_path7 = os.path.join(main_dir1, 'img', 'img7.gif')
        imagen_path8 = os.path.join(main_dir1, 'img', 'img8.gif')
        imagen_path9 = os.path.join(main_dir1, 'img', 'img9.gif')
        imagen_path10 = os.path.join(main_dir1, 'img', 'img10.gif')
        imagen_path11 = os.path.join(main_dir1, 'img', 'img11.gif')
        imagen_path12 = os.path.join(main_dir1, 'img', 'img12.gif')

        #imagen = tk.PhotoImage(file=imagen_path3)
        #imagen = tk.PhotoImage(file=imagen_path4)
        #imagen = tk.PhotoImage(file=imagen_path5)
        #imagen = tk.PhotoImage(file=imagen_path6)
        #imagen = tk.PhotoImage(file=imagen_path7)
        #imagen = tk.PhotoImage(file=imagen_path8)
        #imagen = tk.PhotoImage(file=imagen_path9)
        #imagen = tk.PhotoImage(file=imagen_path10)
        #imagen = tk.PhotoImage(file=imagen_path11)
        #imagen = tk.PhotoImage(file=imagen_path12)






        self.mostrar_vista1 = mostrar_vista1

        #BOTONES DE LA VISTA CREAR CONTENEDOR imagen = tk.PhotoImage(file="img/pan1.gif")
        self.boton_nuevo = tk.Button(self, text="VOLVER")
        self.boton_nuevo.config(width=12, font=('Arial', 12, 'bold'),fg = '#DAD5D6', bg='#FF3333', cursor='hand2', activebackground='#FF6B33', command=self.mostrar_vista1)
        self.boton_nuevo.grid(row=2, column=0, padx=0, pady=50)
        
        # Crea un scrollbar para la ventana
        scrollbar = tk.Scrollbar(self, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Crea un lienzo para contener los elementos
        lienzo = tk.Canvas(self, yscrollcommand=scrollbar.set, width=800, height=440 ) #height=600#  # Aumenta el ancho del lienzo
        lienzo.grid(row=0, column=0, sticky="nsew")

        # Configura el scrollbar para desplazarse en el lienzo
        scrollbar.config(command=lienzo.yview)

        # Crea un marco para contener los elementos
        marco = tk.Frame(lienzo)
        lienzo.create_window((0, 0), window=marco, anchor="nw")

        # Inserta labels con instrucciones e imágenes
        etiqueta_instruccion1 = tk.Label(marco, text="Instrucciones")
        etiqueta_instruccion1.config(width=12, font=('Arial', 12, 'bold'))
        etiqueta_instruccion1.grid(row=0, column=0,padx=300, pady=0,sticky="w")

        etiqueta_instruccion3 = tk.Label(marco, text="PASO 1: Antes de exportar un Dockerfile, cree una carpeta, con un nombre de su preferencia, donde posteriormente deberá alojar el \n Dockerfile a exportar. (Trate de generar la carpeta en una ruta fácil de acceder) ")
        etiqueta_instruccion3.grid(row=1, column=0, sticky="w")

        etiqueta_instruccion2 = tk.Label(marco, text="A continuación, se entrega un ejemplo donde en una primera instancia se crea nueva carpeta con el nombre “Carpeta_Prueba”  \n la cual estará ubicada en el escritorio. ")
        etiqueta_instruccion2.grid(row=2, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path1)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=3, column=0, pady=10)
        
        #text_instruccion2 = tk.Text(marco, wrap=tk.WORD, height=4, width=100, )
        #text_instruccion2.grid(row=2, column=0, sticky="w")
        #text_instruccion2.insert(tk.END, "PASO 1: Antes de exportar un Dockerfile, cree una carpeta, con un nombre de su preferencia, donde posteriormente deberá alojar el Dockerfile a exportar. (Trate de generar la carpeta en una ruta fácil de acceder) ")
        #text_instruccion2.bind("<Button-3>", self.mostrar_menu_copiar)

        

        etiqueta_instruccion4 = tk.Label(marco, text="PASO 2: Al momento de exportar un Dockerfile con la herramienta de apoyo, guarde el archivo en la carpeta antes generada. Este archivo Dockerfile \n vendrá  con un nombre ya definido (“Dockerfile”), pero puede manejar el nombre a su gusto. ")
        etiqueta_instruccion4.grid(row=4, column=0, sticky="w")
        ############################
        etiqueta_instruccion5 = tk.Label(marco, text="Dentro de la “Biblioteca de contenedores”  seleccionamos el Dockerfile a exportar, en este caso de ejemplo, se seleccionó un Dockerfile el cual \n contiene una imagen con “Apache2”, donde posteriormente será usada para crear un contenedor")
        etiqueta_instruccion5.grid(row=5, column=0,sticky="w")

        imagen = tk.PhotoImage(file=imagen_path2)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=6, column=0, pady=10)

        etiqueta_instruccion6 = tk.Label(marco, text="Ya al momento de exportar el Dockerfile, se selecciona la carpeta creada, dejando el archivo Dockerfile guardado dentro de Carpeta_Prueba")
        etiqueta_instruccion6.grid(row=7, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path3)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=8, column=0, pady=10)

        etiqueta_instruccion7 = tk.Label(marco, text="PASO 3: Ya con el archivo Dockerfile dentro de la carpeta a preferencia, ya podemos comenzar con el proceso de generar y ejecutar un contenedor. \n Para esto nos dirigiremos a la barra de busqueda y se buscara Windows PowerShell y lo ejecutaremos.")
        etiqueta_instruccion7.grid(row=9, column=0, sticky="w")

        etiqueta_instruccion8 = tk.Label(marco, text="Se guarda el Dockerfile dentro de la Carpeta_Prueba y procedemos a buscar Windows PowerShell")
        etiqueta_instruccion8.grid(row=10, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path4)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=11, column=0, pady=10)

        etiqueta_instruccion4 = tk.Label(marco, text="Dentro de la barra de búsqueda de Windows ingresamos Windows PowerShell")
        etiqueta_instruccion4.grid(row=12, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path5)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=13, column=0, pady=10)

        etiqueta_instruccion4 = tk.Label(marco, text="Donde luego la ejecutamos y ya esta lista para realizar los comandos necesarios ")
        etiqueta_instruccion4.grid(row=14, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path6)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=15, column=0, pady=10)

        etiqueta_instruccion4 = tk.Label(marco, text="PASO 4: Dentro de Windows PowerShell dirijase a la carpeta generada que contiene el archivo Dockerfile, para esto se puede utilizar los \n comandos “ls” el cual permite visualizar los contenidos actuales del directorio donde se esta ubicado y el comando “cd”  que permite \n ingresar a un directorio.  Por ejemplo, podemos realizar “cd + nombre del directorio” y se ingresa al directorio \n perteneciente al nombre ingresado, donde luego realizando un “ls” se puede verificar el contenido del directorio. ")
        etiqueta_instruccion4.grid(row=16, column=0, sticky="w")

        etiqueta_instruccion4 = tk.Label(marco, text="Para llegar a la Carpeta Prueba primero se debe llegar al escritorio, es por esto, que en una primera instancia, se realiza un “ls” \n para visualizar todos los contenidos del directorio actual y encontrar el escritorio")
        etiqueta_instruccion4.grid(row=17, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path7)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=18, column=0, pady=10)

        etiqueta_instruccion9 = tk.Label(marco, text="Ya con el directorio “escritorio” encontrado, debemos ingresar a él, para realizar esto, se utiliza el comando “cd + nombre del directorio”,  por lo que \n en este  caso se utiliza: “cd Desktop”. Ya están dentro de este directorio, se vuelve a realizar un “ls” para comprobar que la carpeta que \n  buscamos se encuentra aquí.")
        etiqueta_instruccion9.grid(row=19, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path8)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=20, column=0, pady=10)

        etiqueta_instruccion10 = tk.Label(marco, text="Ya con la carpeta detectada, se ingresa a esta, con el comando ya utilizado “cd” y para visualizar si en su interior se encuentra \n el archivo Dockerfile se utiliza el comando “ls” ")
        etiqueta_instruccion10.grid(row=21, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path9)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=22, column=0, pady=10)

        etiqueta_instruccion10 = tk.Label(marco, text="PASO 5: En el momento que ya se esta ubicado dentro de la carpeta que contiene el Dockerfile, se procede a crear la imagen de docker, \n utilizando el siguiente comando en Windows PowerShell: ")
        etiqueta_instruccion10.grid(row=23, column=0, sticky="w")

        text_instruccion2 = tk.Text(marco, wrap=tk.WORD, height=4, width=100)
        text_instruccion2.grid(row=24, column=0, sticky="w")
        text_instruccion2.insert(tk.END, "docker build -t nombre .  ((se incluye el punto) Puedes copiar y modificar esta liena de comando)")

        etiqueta_instruccion10 = tk.Label(marco, text="La variable “nombre” puede tomar cualquier nombre a elección y  será el nombre de la imagen a crear.")
        etiqueta_instruccion10.grid(row=25, column=0, sticky="w")

        etiqueta_instruccion10 = tk.Label(marco, text="Se copia la línea de comando anteriormente mencionada y se pega dentro de Windows PowerShell, ejecutandola, generando así la imagen de Docker ")
        etiqueta_instruccion10.grid(row=26, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path10)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=27, column=0, pady=10)

        etiqueta_instruccion10 = tk.Label(marco, text="PASO 6: Ya con el comando anterior ejecutado, se procederá a crear y ejecutar el contenedor de Docker. Realizando la siguiente línea de comando: ")
        etiqueta_instruccion10.grid(row=28, column=0, sticky="w")

        text_instruccion3 = tk.Text(marco, wrap=tk.WORD, height=4, width=100)
        text_instruccion3.grid(row=29, column=0, sticky="w")
        text_instruccion3.insert(tk.END, "docker run -d -p 8085:80 --name nombre_container nombre  ( Puedes copiar y modificar esta liena de comando)")

        etiqueta_instruccion10 = tk.Label(marco, text="La variable “nombre_container” puede tomar cualquier nombre a elección y será el nombre del contenedor a crear. La variavle “nombre” \n debe ser del mismo nombre que la imagen creada anteriormente y los puertos utilizados en este caso “8085:80”,  pueden variar según necesidad.  ")
        etiqueta_instruccion10.grid(row=30, column=0, sticky="w")

        etiqueta_instruccion10 = tk.Label(marco, text="Se copiar la línea de comando anteriormente mencionada y se pega dentro de  Windows PowerShell y se ejecuta, generando y ejecutando el \n contenedor de Docker con “Apache2” ")
        etiqueta_instruccion10.grid(row=31, column=0, sticky="w")

        imagen = tk.PhotoImage(file=imagen_path11)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=32, column=0, pady=10)

        etiqueta_instruccion10 = tk.Label(marco, text="PASO 7: Con la última línea de comando ya ejecutada, en la consola de Windows PowerShell aparece una línea en hexadecimal, esto indicara \n que el contenedor ya está creado y encendido, por lo que se podrá comenzar a utilizar.  ")
        etiqueta_instruccion10.grid(row=33, column=0, sticky="w")

        etiqueta_instruccion10 = tk.Label(marco, text="PASO 8: Ya para finalizar, se puede observar que el contenedor con “Apache2” que esta activo, abriendo un navegador e ingresar a “localhost + puerto” \n  que en este caso corresponde a  “localhost:8085”  ")
        etiqueta_instruccion10.grid(row=34, column=0, sticky="w")\
        
        imagen = tk.PhotoImage(file=imagen_path12)
        etiqueta_imagen = tk.Label(marco, image=imagen)
        etiqueta_imagen.photo = imagen  # Importante para evitar que la imagen se elimine
        etiqueta_imagen.grid(row=35, column=0, pady=10)


        # Carga y muestra una imagen
       
        ##############
        

        marco.update_idletasks()
        lienzo.config(scrollregion=lienzo.bbox("all"))

        
    def mostrar_menu_copiar(self, event):
        menu = Menu(self, tearoff=0)
        menu.add_command(label="Copiar", command=lambda: self.copiar_texto(event))
        menu.tk_popup(event.x_root, event.y_root)

    def copiar_texto(self, event):
        widget = self.winfo_containing(event.x_root, event.y_root)
        if widget and isinstance(widget, tk.Text):
            selected_text = widget.get(tk.SEL_FIRST, tk.SEL_LAST)
            if selected_text:
                self.clipboard_clear()
                self.clipboard_append(selected_text)
                self.update()
       
        

    

        #etiqueta_titulo = tk.Label(self, text="EJECUTAR CONTENEDORES", font=("Arial", 16, "bold"))
        #etiqueta_titulo.grid(row=2, column=2, padx=0, pady=50)