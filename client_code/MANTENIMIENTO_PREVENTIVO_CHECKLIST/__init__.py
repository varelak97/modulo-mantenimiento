from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CHECKLISTTemplate
from anvil import *

class MANTENIMIENTO_PREVENTIVO_CHECKLIST(MANTENIMIENTO_PREVENTIVO_CHECKLISTTemplate):
  datos = {}
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.datos = datos
    self.repeating_panel_registros.items = datos['actividades']

  def button_regresar_click(self, **event_args):
    self.datos['clave_form'] = 'MANTENIMIENTO_PROGRAMA_ANUAL'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)

