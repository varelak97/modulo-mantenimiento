from ._anvil_designer import MANTENIMIENTO_LISTA_EQUIPOSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class MANTENIMIENTO_LISTA_EQUIPOS(MANTENIMIENTO_LISTA_EQUIPOSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
