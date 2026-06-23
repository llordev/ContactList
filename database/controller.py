###
# Base de datos local.
# "Contacts DataBase".
###

# Importar archivos y librerías necesarias:
import sqlite3 as sql
from database.checker import encontrar_contacto

# Crear ruta absoluta de la base de datos:
ruta_db = "database/contacts.db"
#* Crear base de datos:
def acceder_base_de_datos():
    print("Conectando a la base de datos...")
    conexion = sql.connect(ruta_db)
    print("Se ha establecido conexión con la base de datos.")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            nombre text,
            numero text,
            correo text
        )
    """)
    conexion.commit()
    conexion.close()
    print("Desconectado de la base de datos.")
acceder_base_de_datos()

#* Crear función para añadir contactos:
def anadir_contacto(nombre, numero, correo):
    print("Conectando a la base de datos...")
    conexion = sql.connect(ruta_db)
    print("Se ha establecido conexión con la base de datos.")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO contactos VALUES ('{nombre}', {numero},'{correo}')"
    cursor.execute(instruccion)
    conexion.commit()
    print("Contacto guardado correctamente.")
    conexion.close()
    print("Desconectado de la base de datos.")

# Crear función para eliminar contacto:
def eliminar_contacto(informacion):
    #* Conectar con la base de datos:
    conexion = sql.connect(ruta_db)
    cursor = conexion.cursor()
    #* Comprobar existencia del contacto:
    datos = encontrar_contacto(informacion)
    #* Eliminar contacto de la base de datos:
    for dato in datos:
        if not dato:
            continue
        else:
            print("Contacto encontrado.")
            datos = dato
            campos = ["nombre", "numero", "correo"]
            for campo in campos:
                instruccion = f"DELETE FROM contactos WHERE {campo}='{informacion}'"
                cursor.execute(instruccion)
            print("Contacto eliminado.")
            break
    else:
        #? Devolver estado del contacto que se ha intentado eliminar, False:
        #* Guardar cambios en la base de datos:
        conexion.commit()
        #* Cerrar conexión con la base de datos:
        conexion.close()
        #*
        eliminado = False
        return eliminado
    #? Devolver estado del contacto que se ha intentado eliminar, True:
    #* Guardar cambios en la base de datos:
    conexion.commit()
    #* Cerrar conexión con la base de datos:
    conexion.close()
    #*
    eliminado = True
    return eliminado