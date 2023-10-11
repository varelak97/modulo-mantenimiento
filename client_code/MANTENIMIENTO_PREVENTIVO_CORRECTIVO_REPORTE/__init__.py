from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate
from anvil import *

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
