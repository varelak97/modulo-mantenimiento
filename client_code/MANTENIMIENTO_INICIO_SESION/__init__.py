from ._anvil_designer import MANTENIMIENTO_INICIO_SESIONTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..RegistroUsuarios import RegistroUsuarios

class MANTENIMIENTO_INICIO_SESION(MANTENIMIENTO_INICIO_SESIONTemplate):
  libro_usuarios = None
  ws_usuarios = None
  usuarios = None
  def __init__(self, **properties):
    self.init_components(**properties)
    self.libro_usuarios = app_files.usuarios_erp
    self.ws_usuarios = self.libro_usuarios['Vista']

  def button_iniciar_sesion_click(self, **event_args):
    with Notification("Buscando usuario...", title="Iniciando sesión."):
      datos = {}
      self.usuarios = self.ws_usuarios.rows
      for usuario in self.usuarios:
        if usuario['numero_empleado'] == self.text_box_usuario.text:
          if usuario['password'] == "" and self.text_box_password.text == "":
            datos['usuario'] = self.text_box_usuario.text
            alert(RegistroUsuarios(datos))
