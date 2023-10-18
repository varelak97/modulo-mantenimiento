from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROSTemplate):
  datos = {}
  def __init__(self, datos, **properties):
    self.datos = datos
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
