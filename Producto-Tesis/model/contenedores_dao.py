from .conexion_db import ConexionDB

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE contenedores(
        id_contenedor INTEGER,
        asignatura VARCHAR(100),
        uso_recomendado VARCHAR(100),
        contenido VARCHAR(800),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )'''

    conexion.cursor.execute(sql)
    conexion.cerrar()


def borrar_tabla():
    conexion = ConexionDB

    sql = 'DROP TABLE contenedores'

    conexion.cursor.execute(sql)
    conexion.cerrar()