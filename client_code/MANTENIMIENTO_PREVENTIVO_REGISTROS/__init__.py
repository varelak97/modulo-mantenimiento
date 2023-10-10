from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate
from anvil import *

class MANTENIMIENTO_PREVENTIVO_REGISTROS(MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate):
  def __init__(self,datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
