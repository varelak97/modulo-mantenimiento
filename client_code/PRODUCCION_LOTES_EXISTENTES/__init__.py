from ._anvil_designer import PRODUCCION_LOTES_EXISTENTESTemplate
from anvil import *

class PRODUCCION_LOTES_EXISTENTES(PRODUCCION_LOTES_EXISTENTESTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
