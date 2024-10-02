from ._anvil_designer import MANTENIMIENTO_SISTEMASTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class MANTENIMIENTO_SISTEMAS(MANTENIMIENTO_SISTEMASTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
