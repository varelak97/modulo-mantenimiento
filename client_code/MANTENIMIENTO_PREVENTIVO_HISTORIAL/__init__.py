from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_HISTORIALTemplate
from anvil import *

class MANTENIMIENTO_PREVENTIVO_HISTORIAL(MANTENIMIENTO_PREVENTIVO_HISTORIALTemplate):
  def __init__(self,datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
