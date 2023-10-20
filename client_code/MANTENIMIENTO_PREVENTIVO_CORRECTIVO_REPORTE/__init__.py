from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate):
  ################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos

  ################################ FUNCIONES PERSONALIZADS ########################################

  ############################################ EVENTOS ############################################

  def drop_down_tipo_mantenimiento_change(self, **event_args):
    if self.drop_down_clasificacion.selected_value == "PREVENT"

