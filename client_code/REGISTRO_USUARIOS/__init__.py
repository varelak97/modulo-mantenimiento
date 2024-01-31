from ._anvil_designer import REGISTRO_USUARIOSTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class REGISTRO_USUARIOS(REGISTRO_USUARIOSTemplate):
  ##################################### VARIABLES #####################################
  datos = {}
  libro_usuarios = app_files.usuarios_erp
  ws_usuarios = libro_usuarios['Vista']
  usuarios = None
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    ########################## INICIALIZACION DE VARIABLES ############################
    self.datos = datos
    self.label_nuevo_usuario.text = f"BIENVENIDO/A:\n{self.datos['nombre_usuario']}"
  ###################################### EVENTOS ######################################
  def button_registrar_click(self, **event_args):
    if self.text_box_password.text != self.text_box_confirm_password.text:
      alert("Las contraseñas no coinciden.", title="ERROR AL REGISTRAR")
    else:
      self.usuarios = self.ws_usuarios.rows
      for usuario in self.usuarios:
        if usuario[]
      
