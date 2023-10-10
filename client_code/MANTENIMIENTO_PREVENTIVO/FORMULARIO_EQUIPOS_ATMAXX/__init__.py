from ._anvil_designer import FORMULARIO_EQUIPOS_ATMAXXTemplate
from anvil import *

class FORMULARIO_EQUIPOS_ATMAXX(FORMULARIO_EQUIPOS_ATMAXXTemplate):
  datos = {}
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.datos = datos

    # Any code you write here will run before the form opens.
