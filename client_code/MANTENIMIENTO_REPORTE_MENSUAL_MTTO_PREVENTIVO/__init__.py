from ._anvil_designer import MANTENIMIENTO_REPORTE_MENSUAL_MTTO_PREVENTIVOTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class MANTENIMIENTO_REPORTE_MENSUAL_MTTO_PREVENTIVO(MANTENIMIENTO_REPORTE_MENSUAL_MTTO_PREVENTIVOTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
