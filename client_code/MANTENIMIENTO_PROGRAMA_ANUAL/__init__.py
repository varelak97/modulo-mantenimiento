from ._anvil_designer import MANTENIMIENTO_PROGRAMA_ANUALTemplate
from anvil import *

class MANTENIMIENTO_PROGRAMA_ANUAL(MANTENIMIENTO_PROGRAMA_ANUALTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  def __init__(self, datos, **properties):
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos

    self.init_components(**properties)
