from ._anvil_designer import REGISTRO_USUARIOSTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class REGISTRO_USUARIOS(REGISTRO_USUARIOSTemplate):
  ##################################### VARIABLES #####################################
  datos = {}
  libro_usuarios = None
  ws_usuarios = None
  usuarios = None
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    ########################## INICIALIZACION DE VARIABLES ############################
    self.datos = datos
    self.label_nuevo_usuario.text = f"BIENVENIDO/A:\n{self.datos['nombre_usuario']}"
    self.libro_usuarios = app_files.usuarios_erp
    self.ws_usuarios = self.libro_usuarios['Registros']
  ###################################### EVENTOS ######################################
  def button_registrar_click(self, **event_args):
    if self.text_box_password.text != self.text_box_confirm_password.text:
      alert("Las contraseñas no coinciden.", title="ERROR AL REGISTRAR")
    else:
      with Notification("Registrando contraseña en la base de datos..", title="Registrando.", style="info"):
        self.usuarios = self.ws_usuarios.rows
        for usuario in self.usuarios:
          if str(self.datos['id_usuario_erp']) == str(usuario['numero_empleado']):
            usuario['password'] = self.text_box_password.text
            break
      self.raise_event("x-close-alert",value=True)
      Notification("La contraseña se ha registrada correctamente!", title="ÉXITO.", style="success").show()
      
