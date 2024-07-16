from ._anvil_designer import MANTENIMIENTO_INSPECCION_SUAJESTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class MANTENIMIENTO_INSPECCION_SUAJES(MANTENIMIENTO_INSPECCION_SUAJESTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
