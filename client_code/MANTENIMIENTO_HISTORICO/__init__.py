from ._anvil_designer import MANTENIMIENTO_HISTORICOTemplate
from anvil import *

class MANTENIMIENTO_HISTORICO(MANTENIMIENTO_HISTORICOTemplate):
  datos = {}
  
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.datos = datos
