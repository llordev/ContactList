###
# Archivo "Main_Window".
# Manager de la ventana principal.
###

# Importar archivos y librerías necesarias:
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from __feature__ import snake_case, true_property
from ui import dialogs
from styles.styles import estilos_generales
from styles.styles import estilos_menu
from styles.styles import estilos_encontrado
from database import controller, checker

# Crear clase para iniciar el programa:
class ventana(QMainWindow):
    def crear(self):
        #* Configurar tamaño:
        self.set_fixed_size(500, 500)
        #* Configurar estilos:
        self.style_sheet = estilos_generales
        #* Crear "QWidget":
        self.widget = QWidget()
        #* Establecer "QWidget" como "Widget" central:
        self.set_central_widget(self.widget)
        #* Crear "QHBoxLyout":
        self.layout_inicial = QHBoxLayout()
        #* Añadir "Layout" al "Widget" central:
        self.widget.set_layout(self.layout_inicial)
        #* Crear el primer "QFrame":
        self.frame1 = QFrame()
        self.frame1.style_sheet = estilos_generales
        #* Crear "QStackedWidget":
        self.stacked = QStackedWidget()
        #* Añadir "Widgets" al "Layout":
        self.layout_inicial.add_widget(self.stacked, 60)
        self.layout_inicial.add_widget(self.frame1, 40)
        #* Crear "QFrame" de navegación:
        self.frame_navegacion = QFrame()
        self.frame_navegacion.style_sheet = estilos_generales
        #* Añadir "QFrame" de navegación al "QStackedWidget":
        self.stacked.add_widget(self.frame_navegacion)
        self.stacked.set_current_widget(self.frame_navegacion)
        #* Crear y configurar "QVBoxLayout" para el "QFrame" de navegación:
        self.layout_navegacion = QVBoxLayout()
        self.frame_navegacion.set_layout(self.layout_navegacion)
        #* Añadir espacio al "QHBoxLayout" de navegación:
        self.layout_navegacion.add_spacing(20)
        #* Crear y configurar "QLabel" para el "QVBoxLayout" de navegación:
        self.titulo = QLabel()
        self.titulo.text = "Bienvenido a tu aplicación de contactos:"
        self.titulo.object_name = "titulo"
        self.titulo.word_wrap = True
        self.titulo.style_sheet = estilos_generales
        #* Añadir "QLabel" al "QVBoxLayout" de navegación:
        self.layout_navegacion.add_widget(self.titulo)
        #* Crear y configurar "QPushButtons" de navegación:
        self.boton_anadir = QPushButton()
        self.boton_anadir.text = "Añadir un contacto."
        self.boton_anadir.clicked.connect(self.pestana_anadir)
        self.boton_anadir.style_sheet = estilos_generales
        self.boton_buscar = QPushButton()
        self.boton_buscar.text = "Buscar un contacto."
        self.boton_buscar.clicked.connect(self.pestana_buscar)
        self.boton_buscar.style_sheet = estilos_generales
        self.boton_eliminar = QPushButton()
        self.boton_eliminar.text = "Eliminar un contacto."
        self.boton_eliminar.clicked.connect(self.pestana_eliminar)
        self.boton_eliminar.style_sheet = estilos_generales
        #* Añadir "QPushButtons" al "Layout":
        self.layout_navegacion.add_widget(self.boton_anadir)
        self.layout_navegacion.add_widget(self.boton_buscar)
        self.layout_navegacion.add_widget(self.boton_eliminar)
        #* Añadir "stretch()" al "Layout" de navegación:
        self.layout_navegacion.add_stretch()
        #* Crear y configurar "QFrame" para la ventana "Añadir contacto":
        self.frame_anadir = QFrame()
        self.frame_anadir.style_sheet = estilos_generales
        #* Añadir "QFrame" de la ventana "Añadir contacto" al "QStackedWidget":
        self.stacked.add_widget(self.frame_anadir)
        #* Crear y configurar "QVBoxLayout" para la ventana "Añadir contacto":
        self.layout_anadir = QVBoxLayout()
        #* Añadir "Layout" al "QFrame":
        self.frame_anadir.set_layout(self.layout_anadir)
        #* Crear y configuarar "QLabel" para la ventana de "Añadir contacto":
        self.titulo_anadir = QLabel()
        self.titulo_anadir.text = "Añade un contacto nuevo:"
        self.titulo_anadir.object_name = "titulo"
        self.titulo_anadir.word_wrap = True
        self.titulo_anadir.style_sheet = estilos_generales
        #* Añadir "QLabel" al "Layout" para la ventana "Añadir contacto":
        self.layout_anadir.add_widget(self.titulo_anadir)
        #* Crear "QLabel" y "QLineEdit" del campo "nombre":
        self.label_nombre = QLabel()
        self.label_nombre.text = "Escribe el nombre del contacto que quieres añadir:"
        self.label_nombre.word_wrap = True
        self.label_nombre.style_sheet = estilos_generales
        self.input_nombre = QLineEdit()
        self.input_nombre.placeholder_text = "Nombre."
        #* Crear "QLabel" y "QLineEdit" del campo "numero":
        self.label_numero = QLabel()
        self.label_numero.text = "Escribe el número de teléfono del contacto que quieres añadir:"
        self.label_numero.word_wrap = True
        self.label_numero.style_sheet = estilos_generales
        self.input_numero = QLineEdit()
        self.input_numero.placeholder_text = "Número de teléfono."
        #* Crear "QLabel" y "QLineEdit" del campo "correo":
        self.label_correo = QLabel()
        self.label_correo.text = "Escribe el correo electrónico del contacto que quieres añadir:"
        self.label_correo.word_wrap = True
        self.label_correo.style_sheet = estilos_generales
        self.input_correo = QLineEdit()
        self.input_correo.placeholder_text = "Correo electrónico."
        #* Añadir formulario al "QVBoxLayout":
        self.layout_anadir.add_widget(self.label_nombre)
        self.layout_anadir.add_widget(self.input_nombre)
        self.layout_anadir.add_widget(self.label_numero)
        self.layout_anadir.add_widget(self.input_numero)
        self.layout_anadir.add_widget(self.label_correo)
        self.layout_anadir.add_widget(self.input_correo)
        #* Crear "QPushButton" enviar para la ventana "Añadir contacto":
        self.boton_enviar = QPushButton()
        self.boton_enviar.text = "Añadir Contacto."
        self.boton_enviar.clicked.connect(self.anadir_contacto)
        self.boton_enviar.style_sheet = estilos_generales
        #* Añadir "QPushButton" enviar al "QVBoxLayout":
        self.layout_anadir.add_widget(self.boton_enviar)
        #* Crear "QPushButton" cancelar para la ventana "Añadir contacto":
        self.boton_cancelar_anadir = QPushButton()
        self.boton_cancelar_anadir.text = "Cancelar."
        self.boton_cancelar_anadir.clicked.connect(self.cancelar)
        self.boton_cancelar_anadir.style_sheet = estilos_generales
        #* Añadir "QPushButton" cancelar al "QVBoxLayout":
        self.layout_anadir.add_widget(self.boton_cancelar_anadir)
        #* Añadir "stretch()" al "Layout" de "Añadir contacto":
        self.layout_anadir.add_stretch()
        #* Crear "QFrame" de la ventana "Buscar contacto":
        self.frame_buscar = QFrame()
        self.frame_buscar.style_sheet = estilos_generales
        #* Añadir "QFrame" de la ventana "Buscar contactos" al "QStackedWidget":
        self.stacked.add_widget(self.frame_buscar)
        #* Crear "QVBoxLayout" de la ventana "Buscar contactos":
        self.layout_buscar = QVBoxLayout()
        #* Añadir "QVBoxLayout" al "QFrame" de la ventana "Buscar contacto":
        self.frame_buscar.set_layout(self.layout_buscar)
        #* Crear "QLabel" de la ventana "Buscar contacto":
        self.titulo_buscar = QLabel(self.frame_buscar)
        self.titulo_buscar.text = "Busca un contacto:"
        self.titulo_buscar.object_name = "titulo"
        self.titulo_buscar.style_sheet = estilos_generales
        self.layout_buscar.add_widget(self.titulo_buscar)
        #* Crear "QLineEdit" de la ventana "Buscar contacto":
        self.input_buscar = QLineEdit()
        self.input_buscar.placeholder_text = "Busca un contacto."
        self.input_buscar.style_sheet = estilos_generales
        #* Crear y configurar "QPushButton" buscar de la ventana "Buscar contacto":
        self.boton_buscar_contacto = QPushButton()
        self.boton_buscar_contacto.text = "Buscar contacto."
        self.boton_buscar_contacto.style_sheet = estilos_generales
        self.boton_buscar_contacto.clicked.connect(self.buscar_contacto)
        #* Crear "QPushButton" cancelar para la ventana "Añadir contacto":
        self.boton_cancelar_buscar = QPushButton()
        self.boton_cancelar_buscar.text = "Cancelar."
        self.boton_cancelar_buscar.style_sheet = estilos_generales
        self.boton_cancelar_buscar.clicked.connect(self.cancelar)
        #* Añadir "Widgets" al "QVBoxLayout" de la ventana "Buscar contacto":
        self.layout_buscar.add_widget(self.input_buscar)
        self.layout_buscar.add_widget(self.boton_buscar_contacto)
        self.layout_buscar.add_widget(self.boton_cancelar_buscar)
        #* Añadir "stretch()" al "Layout" de "Buscar contacto":
        self.layout_buscar.add_stretch()
        #* Crear y configurar "QFrame" de la ventana "Contacto encontrado":
        self.frame_mostrar = QFrame()
        #* Añadir "QFrame" al "QStackedWidget" de la ventana "Contacto encontrado":
        self.stacked.add_widget(self.frame_mostrar)
        #* Crear "QVBoxLayout" para el "QFrame" de la ventana "Contacto encontrado":
        self.layout_contacto_encontrado = QVBoxLayout()
        #* Establecer "QVBoxLayout" del "QFrame" de la ventana "Contacto encontrado":
        self.frame_mostrar.set_layout(self.layout_contacto_encontrado)
        #* Crear y configurar "QLabels" de la información del contacto encontrado de la ventana "Contacto encontrado":
        self.label_nombre_info = QLabel()
        self.label_nombre_info.text = "El nombre del contacto encontrado es:"
        self.label_nombre_info.word_wrap = True
        self.label_nombre_info.style_sheet = estilos_generales
        self.label_numero_info = QLabel()
        self.label_numero_info.text = "El número de teléfono del contacto encontrado es:"
        self.label_numero_info.word_wrap = True
        self.label_numero_info.style_sheet = estilos_generales
        self.label_correo_info = QLabel()
        self.label_correo_info.text = "El correo electrónico del contacto encontrado es:"
        self.label_correo_info.word_wrap = True
        self.label_correo_info.style_sheet = estilos_generales
        #* Crear y configurar "QLabel" principal del contacto de la ventana "Contacto encontrado":
        self.titulo_encontrado = QLabel()
        self.titulo_encontrado.text = "Información del contacto encontrado:"
        self.titulo_encontrado.word_wrap = True
        self.titulo_encontrado.object_name = "titulo"
        self.titulo_encontrado.style_sheet = estilos_generales
        #* Añadir "QLabel" principal al "QVBoxLayout" de la ventana "Contacto encontrado":
        self.layout_contacto_encontrado.add_widget(self.titulo_encontrado)
        #* Crear y configurar "QLabels" del contacto encontrado de la ventana "Contacto encontrado":
        self.label_nombre_encontrado = QLabel()
        self.label_nombre_encontrado.object_name = "encontrado"
        self.label_nombre_encontrado.style_sheet = estilos_encontrado
        self.label_numero_encontrado = QLabel()
        self.label_numero_encontrado.object_name = "encontrado"
        self.label_numero_encontrado.style_sheet = estilos_encontrado
        self.label_correo_encontrado = QLabel()
        self.label_correo_encontrado.object_name = "encontrado"
        self.label_correo_encontrado.style_sheet = estilos_encontrado
        #* Crear "QPushButton" para volver a la ventana anterior de la ventana "Contacto encontrado":
        self.boton_volver = QPushButton()
        self.boton_volver.text = "Volver."
        self.boton_volver.style_sheet = estilos_generales
        self.boton_volver.clicked.connect(self.volver)
        #* Añadir "Widgets" al "QVBoxLayout" del "QFrame" de la ventana "Contacto encontrado":
        self.layout_contacto_encontrado.add_widget(self.label_nombre_info)
        self.layout_contacto_encontrado.add_widget(self.label_nombre_encontrado)
        self.layout_contacto_encontrado.add_widget(self.label_numero_info)
        self.layout_contacto_encontrado.add_widget(self.label_numero_encontrado)
        self.layout_contacto_encontrado.add_widget(self.label_correo_info)
        self.layout_contacto_encontrado.add_widget(self.label_correo_encontrado)
        self.layout_contacto_encontrado.add_widget(self.boton_volver)
        #* Añadir "stretch()" al "Layout" de "Contacto encontrado":
        self.layout_contacto_encontrado.add_stretch()
        #* Crear "QFrame" de la ventana "Eliminar contacto":
        self.frame_eliminar = QFrame()
        self.frame_eliminar.style_sheet = estilos_generales
        #* Añadir "QFrame" al "QStackedWidget" de la ventana "Eliminar contacto":
        self.stacked.add_widget(self.frame_eliminar)
        #* Crear "QVBoxLayout" para el "QFrame" de la ventana "Eliminar contacto":
        self.layout_eliminar = QVBoxLayout()
        #* Establecer "Layout" del "QFrame" de la ventana
        self.frame_eliminar.set_layout(self.layout_eliminar)
        #* Crear y configurar "QLabel" principal de la ventana "Eliminar contacto":
        self.titulo_eliminar = QLabel()
        self.titulo_eliminar.text = "Elimina un contacto:"
        self.titulo_eliminar.object_name = "titulo"
        self.titulo_eliminar.style_sheet = estilos_generales
        #* Añadir "QLabel" al "QVBoxLayout" de la ventana "Eliminar contacto":
        self.layout_eliminar.add_widget(self.titulo_eliminar)
        #* Crear y configurar "QLineEdit" de la ventana "Eliminar contacto":
        self.input_eliminar = QLineEdit()
        self.input_eliminar.placeholder_text = "Elimina un contacto."
        self.input_eliminar.style_sheet = estilos_generales
        #* Crear y configurar "QPushButton" eliminar de la ventana "Eliminar contacto":
        self.boton_eliminar_contacto = QPushButton()
        self.boton_eliminar_contacto.text = "Eliminar contacto."
        self.boton_eliminar_contacto.style_sheet = estilos_generales
        self.boton_eliminar_contacto.clicked.connect(self.eliminar_contacto)
        #* Crear y configurar "QPushButton" para volver a la ventana inicial:
        self.boton_cancelar_eliminar = QPushButton()
        self.boton_cancelar_eliminar.text = "Canclear."
        self.boton_cancelar_eliminar.style_sheet = estilos_generales
        self.boton_cancelar_eliminar.clicked.connect(self.cancelar)
        #* Añadir "Widgets" al "QVBoxLayout" del "QFrame" de la ventana "Eliminar contacto":
        self.layout_eliminar.add_widget(self.input_eliminar)
        self.layout_eliminar.add_widget(self.boton_eliminar_contacto)
        self.layout_eliminar.add_widget(self.boton_cancelar_eliminar)
        #* Añadir "stretch()" al "Layout" de la ventana "Eliminar contacto":
        self.layout_eliminar.add_stretch()

    def pestana_anadir(self): #TODO: Función para acceder a la ventana "Añadir contacto":
        print("Accediendo a la interfaz para añadir un contacto nuevo...")
        #* Cambiar "Widget" actual:
        self.stacked.set_current_widget(self.frame_anadir)
    def anadir_contacto(self): #TODO: Función para enviar información a la base de datos local:
        #* Guardar variables del texto introducido en los "QLineEdit":
        nombre = self.input_nombre.text
        numero = self.input_numero.text
        correo = self.input_correo.text
        #* Limpiar "QLineEdits":
        self.input_nombre.clear()
        self.input_numero.clear()
        self.input_correo.clear()
        #* Cambiar "Widget" actual:
        self.stacked.set_current_widget(self.frame_navegacion)
        self.mensaje = "Contacto añadido exitosamente."
        controller.anadir_contacto(nombre, numero, correo)
        dialog = dialogs.dialog(self.mensaje)
        dialog.exec()
    def pestana_buscar(self): #TODO: Función para acceder a la ventana "Buscar contacto":
        print("Accediendo a la interfaz para buscar un contacto...")
        #* Cambiar "Widget" actual:
        self.stacked.set_current_widget(self.frame_buscar)
    def buscar_contacto(self): #TODO: Función para buscar información en la base de datos:
        print("Buscando contacto...")
        #* Crear variable para obtener el texto introducido en el "QLineEdit" de la ventana "Buscar contacto":
        self.informacion = self.input_buscar.text
        #* Limpiar el texto introducido en el "QLineEdit" de la ventana "Buscar contacto".
        self.input_buscar.clear()
        #* Llamar función para encontrar el contacto en la base de datos:
        self.datos = checker.encontrar_contacto(self.informacion)
        for dato in self.datos:
            if not dato:
                continue
            else:
                print("Contacto encontrado.")
                self.datos = dato
                self.crear_contacto_buscado(self.datos)
                break
        else:
            mensaje = "Introduce un contacto existente."
            dialog = dialogs.dialog(mensaje)
            dialog.exec()
        
    def pestana_eliminar(self): #TODO: Función para acceder a la ventana "Eliminar contacto":
        print("Accediendo a la interfaz para eliminar un contacto...")
        #* Cambiar "Widget" actual:
        self.stacked.set_current_widget(self.frame_eliminar)
    def eliminar_contacto(self): #TODO: Función para eliminar un contacto:
        #* Llamar función para eliminar contacto:
        informacion = self.input_eliminar.text
        self.eliminado = controller.eliminar_contacto(informacion)
        #* Crear condicionales para mostrar el "QDialog" con el mensaje correspondiente:
        if self.eliminado == True:
            #? True
            mensaje = "Contacto eliminado exitosamente."
            dialog = dialogs.dialog(mensaje)
            self.input_eliminar.clear()
            self.stacked.set_current_widget(self.frame_navegacion)
            dialog.exec()
        else:
            #? False:
            mensaje = "Introduce un contacto existente."
            self.input_eliminar.clear()
            dialog = dialogs.dialog(mensaje)
            dialog.exec()

    def crear_contacto_buscado(self, datos): #TODO: Función para crear la ventana "Contacto encontrado":
        #* Cambiar texto de los "QLabels":
        self.label_nombre_encontrado.text = datos[0][0]
        self.label_numero_encontrado.text = datos[0][1]
        self.label_correo_encontrado.text = datos[0][2]
        #* Cambiar "Widget" actual:
        self.stacked.set_current_widget(self.frame_mostrar)

    def cancelar(self): #TODO: Función reusable para volver a la ventana inicial:
        #* Cambiar "Widget" actual:
        print("Accediendo a la interfaz inicial...")
        self.stacked.set_current_widget(self.frame_navegacion)
        #* Limpiar todos los "QLineEdits":
        self.input_nombre.clear()
        self.input_numero.clear()
        self.input_correo.clear()
        self.input_buscar.clear()
        self.input_eliminar.clear()

    def volver(self): #TODO: Función para volver a la pestaña anterior(no resusable):
        #* Cambiar "Widget" actual:
        self.stacked.set_current_widget(self.frame_buscar)