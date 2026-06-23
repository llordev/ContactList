###
# Archivo "Checker".
# Archivo que verifica las búquedas.
###

# Importar archivos y librerías respectivas:
import sqlite3 as sql

# Crear variable de ruta:
ruta_db = "database/contacts.db"

# Crear función de búsqueda:
def encontrar_contacto(informacion): #TODO: Función para validar el contacto buscado:
    #* Conectar con la base de datos:
    print("Conctándose a la base de datos para comprobar información...")
    conexion = sql.connect(ruta_db)
    print("Conectado a la base de datos.")
    #* Crear lista de los campos:
    campos = ["nombre", "numero", "correo"]
    #* Crear "cursor()":
    cursor = conexion.cursor()
    #* Crear datos:
    datos = []
    for campo in campos: #?  Bucle para obtener información:
        instruccion = f"SELECT * FROM contactos WHERE {campo}='{informacion}'"
        cursor.execute(instruccion)
        datos.append(cursor.fetchall())
    #* Guardar cambios en la base de datos:
    conexion.commit()
    #* Desconectarse de la base de datos:
    conexion.close()
    #* Devolver la variable datos:
    return datos