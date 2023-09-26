from ._anvil_designer import PRODUCCION_LOTES_EXISTENTESTemplate
from anvil import *

class PRODUCCION_LOTES_EXISTENTES(PRODUCCION_LOTES_EXISTENTESTemplate):
  datos = {}
  
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.datos = datos
