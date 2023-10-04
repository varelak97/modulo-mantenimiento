from ._anvil_designer import MANTENIMIENTO_REPORTE_MTTO_PREVENTIVOTemplate
from anvil import *

class MANTENIMIENTO_REPORTE_MTTO_PREVENTIVO(MANTENIMIENTO_REPORTE_MTTO_PREVENTIVOTemplate):
  datos = {}
  def __init__(self,datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.datos = datos
