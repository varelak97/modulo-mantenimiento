from ._anvil_designer import A_mainTemplate
from anvil import *
from ..PRODUCCCION_LOTES import PRODUCCCION_LOTES
from ..PRODUCCION_LOTES_EXISTENTES import PRODUCCION_LOTES_EXISTENTES
from ..PRODUCCION_LOTES_HISTORICO import PRODUCCION_LOTES_HISTORICO

class A_main(A_mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    form_activo = None
    datos = {
      'id_usuario_erp': 18,
      'clave_form':"PRODUCCION_LOTES_EXISTENTES",
      'test':True
    }

    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.content_panel.visible = True

  def actualizar_form_activo(self, datos, **event_args):
    if datos['clave_form'] == 'PRODUCCION_LOTES_EXISTENTES':
      self.abrir_form(PRODUCCION_LOTES_EXISTENTES(datos))
    elif datos['clave_form'] == 'PRODUCCION_LOTES':
      self.abrir_form(PRODUCCION_LOTES(datos))
    elif datos['clave_form'] == 'PRODUCCION_LOTES_HISTORICO':
      self.abrir_form(PRODUCCION_LOTES_HISTORICO()(datos))