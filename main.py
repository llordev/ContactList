###
# Archivo "Main".
# Manager de la aplicación.
###

# Importar archivos y librerías necesarias:
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
from __feature__ import snake_case, true_property
from ui.main_window import ventana

# Crear clase para iniciar el programa:
class iniciar_aplicacion:
    def __init__(self):
        #* Acceder a la ventana:
        self.ventana_principal = ventana()
        #* Configurar ventana:
        self.ventana_principal.crear()

# Ejecutar aplicación:
try:
    print("Abriendo aplicación...")
    app = QApplication(sys.argv)
    print("Aplicación creada exitosamente.")
    iniciar = iniciar_aplicacion()
    ventana = iniciar.ventana_principal
    print("Ventana creada exitosamente.")
    ventana.show()
    print("Ventana mostrada.")
    sys.exit(app.exec())
except:
    print("Aplicación cerrada.")