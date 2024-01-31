from ._anvil_designer import REGISTRO_USUARIOSTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class REGISTRO_USUARIOS(REGISTRO_USUARIOSTemplate):
  ##################################### VARIABLES #####################################
  datos = {}
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    ########################## INICIALIZACION DE VARIABLES ############################
    self.datos = datos
    self.label_nuevo_usuario.text = f"BIENVENIDO/A:\n{self.datos['nombre_usuario']}"

  ###################################### EVENTOS ######################################
  def button_iniciar_sesion_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
