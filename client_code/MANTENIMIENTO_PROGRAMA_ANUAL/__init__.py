from ._anvil_designer import MANTENIMIENTO_PROGRAMA_ANUALTemplate
from anvil import *

class MANTENIMIENTO_PROGRAMA_ANUAL(MANTENIMIENTO_PROGRAMA_ANUALTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  def __init__(self, datos, **properties):
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos

    self.init_components(**properties)

  def button_nuevo_click(self, **event_args):
    self.datos['clave_form'] = 'MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO'
    self.datos['modo'] = 'nuevo'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)

