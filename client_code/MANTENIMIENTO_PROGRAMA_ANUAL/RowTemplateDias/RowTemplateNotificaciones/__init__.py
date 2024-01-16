from ._anvil_designer import RowTemplateNotificacionesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class RowTemplateNotificaciones(RowTemplateNotificacionesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
