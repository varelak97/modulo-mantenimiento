from ._anvil_designer import MANTENIMIENTO_NUMEROS_PARTETemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class MANTENIMIENTO_NUMEROS_PARTE(MANTENIMIENTO_NUMEROS_PARTETemplate):
  datos = None
  ws_herramentales = None
  ss_vista_numeros_parte = None
  vista_numeros_parte = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.button_actualizar_click()

  ################################################# FUNCIONES PERSONALIZADAS #################################################
  def set_ini_config(self, datos):
    self.datos = datos

  def get_data(self):
    

  ########################################################## EVENTOS #########################################################

  def button_actualizar_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
