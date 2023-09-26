from ._anvil_designer import PRODUCCION_LOTES_HISTORICOTemplate
from anvil import *

class PRODUCCION_LOTES_HISTORICO(PRODUCCION_LOTES_HISTORICOTemplate):
  datos = {}
  def __init__(self,datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.datos = datos
