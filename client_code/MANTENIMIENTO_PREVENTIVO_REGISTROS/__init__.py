from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate
from anvil import *
import anvil.server

class MANTENIMIENTO_PREVENTIVO_REGISTROS(MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate):
  datos = {}
  def __init__(self,datos, **properties):
    self.datos = datos
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_nuevo_click(self, **event_args):
    self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO'
    self.datos['modo'] = 'nuevo'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)

