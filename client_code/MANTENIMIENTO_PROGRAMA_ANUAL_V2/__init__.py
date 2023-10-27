from ._anvil_designer import MANTENIMIENTO_PROGRAMA_ANUAL_V2Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class MANTENIMIENTO_PROGRAMA_ANUAL_V2(MANTENIMIENTO_PROGRAMA_ANUAL_V2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
