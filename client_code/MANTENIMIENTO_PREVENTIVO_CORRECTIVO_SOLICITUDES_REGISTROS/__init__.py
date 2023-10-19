from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
