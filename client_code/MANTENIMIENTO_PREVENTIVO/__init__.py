from ._anvil_designer import MANTENIMIENTO_PREVENTIVOTemplate
from anvil import *

class MANTENIMIENTO_PREVENTIVO(MANTENIMIENTO_PREVENTIVOTemplate):
  datos = {}
  lista_areas = {
    
  }
  def __init__(self,datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.datos = datos

  def button_volver_click(self, **event_args):
    self.datos['clave_form'] = 'MANTENIMIENTO_PROGRAMA_ANUAL'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)

