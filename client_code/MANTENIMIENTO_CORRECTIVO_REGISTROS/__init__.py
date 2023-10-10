from ._anvil_designer import MANTENIMIENTO_CORRECTIVO_REGISTROSTemplate
from anvil import *

class MANTENIMIENTO_CORRECTIVO_REGISTROS(MANTENIMIENTO_CORRECTIVO_REGISTROSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
