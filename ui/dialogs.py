###
# Archivo "Dialogs".
# Archivo "Manager" de "Dialogs".
###

# Importar librerías necesarias:
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from __feature__ import snake_case, true_property
from styles.styles import estilos_generales
from styles.styles import estilos_dialog

# Crear clase de "QDialog":
class dialog(QDialog):
    def __init__(self, mensaje): #TODO: Función que se ejecuta al iniciar la clase.
        super().__init__() #TODO: Función que carga todas las propiedades del "QDialog" antes de aplicar cambios.
        #* Establecer tamaño del "QDialog":
        self.set_fixed_size(400, 100)
        #* Crear "QFrame":
        self.frame = QFrame(self)
        self.frame.geometry = QRect(0, 0, 400, 100)
        self.frame.style_sheet = estilos_generales
        #* Crear y configurar "QLabel"
        self.titulo = QLabel(self.frame)
        self.titulo.object_name = "mensaje"
        self.titulo.geometry = QRect(0, 0, 400, 100)
        self.titulo.text = mensaje
        self.titulo.alignment = Qt.AlignCenter
        self.titulo.style_sheet = estilos_generales