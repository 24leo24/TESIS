
"""
Dentro de este módulo se encuntran la conexion entre la GUI y la base de datos, 
ademas de todas las consultas sql.
"""

import sqlite3
import os

class Comunicacion():
    def __init__(self):

         # Obtén la ruta del directorio actual donde se encuentra este archivo (conexion_sqlite.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Retrocede un nivel para acceder a la carpeta principal
        main_dir = os.path.dirname(current_dir)
        
        # Crea la ruta absoluta para la base de datos
        db_path = os.path.join(main_dir, 'database', 'contenedores.db')

        # Abre la base de datos con la ruta absoluta
        self.conexion = sqlite3.connect(db_path)
        #self.conexion = sqlite3.connect('database/contenedores.db')

    def insertar_datos(self, nombre, asignatura, recomendacion, contenido):
        cursor = self.conexion.cursor()
        bd = ''' INSERT INTO contenedor (NOMBRE, ASIGNATURA, RECOMENDACION, CONTENIDO)
        VALUES ('{}','{}','{}','{}')'''.format(nombre, asignatura, recomendacion, contenido)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def mostrar_datos(self):
        cursor=self.conexion.cursor()
        bd="SELECT * FROM contenedor  "
        cursor.execute(bd)
        contenedor = cursor.fetchall()
        return contenedor
    
    def eliminar_datos(self, id):
        cursor = self.conexion.cursor()
        bd = "DELETE FROM contenedor WHERE ID = ?"
        cursor.execute(bd, (id,))
        self.conexion.commit()
        cursor.close()
        

    def actulizar_datos(self, ID, nombre, asignatura, recomendacion, contenido):
        cursor = self.conexion.cursor()
        bd = '''UPDATE contenedor SET NOMBRE = '{}', ASIGNATURA = '{}', RECOMENDACION = '{}', CONTENIDO = '{}'
        WHERE ID = '{}' '''.format(nombre, asignatura, recomendacion, contenido, ID)
        cursor.execute(bd)
        contenedor = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return contenedor
    
    def mostrar_registro_por_id(self, id):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM contenedor WHERE ID = ?"
        cursor.execute(bd, (id,))
        registro = cursor.fetchone()
        cursor.close()
        
        # Comprueba si se encontró un registro
        if registro is not None:
            nombre = registro[1]
            asignatura = registro[2]
            recomendacion = registro[3]
            contenido = registro[4]
            
            # Devuelve los valores como resultado
            return nombre, asignatura, recomendacion, contenido
        else:
            # Si no se encuentra ningún registro, devuelve None
            return None

