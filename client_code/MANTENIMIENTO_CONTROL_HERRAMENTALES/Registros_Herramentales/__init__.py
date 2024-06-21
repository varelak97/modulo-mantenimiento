from ._anvil_designer import Registros_HerramentalesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..Form_Edicion_Herramental import Form_Edicion_Herramental


class Registros_Herramentales(Registros_HerramentalesTemplate):
  datos = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos
    self.label_title.text = f"HERRAMENTAL {self.datos['codigo_herramental']}"


  
  ################################################ EVENTOS ################################################
  def button_registrar_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
