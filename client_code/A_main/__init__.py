from ._anvil_designer import A_mainTemplate
from anvil import *
from ..MANTENIMIENTO_HISTORICO import MANTENIMIENTO_HISTORICO
from ..MANTENIMIENTO_PROGRAMA_ANUAL import MANTENIMIENTO_PROGRAMA_ANUAL
from ..MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO import MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO

class A_main(A_mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    form_activo = None
    datos = {
      'id_usuario_erp': 18,
      'clave_form':"MANTENIMIENTO_PROGRAMA_ANUAL",
      'test':True
    }

    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.content_panel.visible = True

  def actualizar_form_activo(self, datos, **event_args):
    if datos['clave_form'] == 'MANTENIMIENTO_PROGRAMA_ANUAL':
      self.abrir_form(MANTENIMIENTO_PROGRAMA_ANUAL(datos))