from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate
from anvil import *

class MANTENIMIENTO_PREVENTIVO_REGISTROS(MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate):
  datos = {}
  def __init__(self,datos, **properties):
    self.datos = datos
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
