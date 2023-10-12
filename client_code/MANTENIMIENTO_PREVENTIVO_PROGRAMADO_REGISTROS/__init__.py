from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_PROGRAMADO_REGISTROSTemplate
from anvil import *
import anvil.server

class MANTENIMIENTO_PREVENTIVO_PROGRAMADO_REGISTROS(MANTENIMIENTO_PREVENTIVO_PROGRAMADO_REGISTROSTemplate):
  datos = {}
  def __init__(self, datos, **properties):
    self.datos = datos
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
