from ._anvil_designer import MANTENIMIENTO_CORRECTIVO_REGISTROSTemplate
from anvil import *
import anvil.server

class MANTENIMIENTO_CORRECTIVO_REGISTROS(MANTENIMIENTO_CORRECTIVO_REGISTROSTemplate):
  datos = {}
  def __init__(self, datos, **properties):
    self.datos = datos
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
