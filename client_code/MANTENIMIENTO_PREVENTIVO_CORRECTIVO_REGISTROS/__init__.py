from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROSTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  libro_reportes = None
  ws_reportes = None
  registros_reportes = None
  def __init__(self, datos, **properties):
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos
    self.init_components(**properties)

    self.libro_reportes = app_files.mantenimiento_correctivo_preventivo_programado
    self.ws_reportes = self.libro_reportes['Registros']
    self.registros_reportes = self.ws_reportes.rows
    self.repeating_panel_registros.items = self.registros_reportes

    ############################### FUNCIONES PERSONALIZADS #######################################

    ########################################### EVENTOS ###########################################
