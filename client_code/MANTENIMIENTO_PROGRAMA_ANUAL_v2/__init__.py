from ._anvil_designer import MANTENIMIENTO_PROGRAMA_ANUAL_v2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class MANTENIMIENTO_PROGRAMA_ANUAL_v2(MANTENIMIENTO_PROGRAMA_ANUAL_v2Template):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  def __init__(self, datos, **properties):
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.init_components(**properties)
    self.datos = datos
    self.test()
    # Any code you write here will run before the form opens.
  ################################ FUNCIONES PERSONALIZADS ########################################
  def test(self):
    """columnas = self.data_grid_1.columns
    print(columnas[0])
    columnas.pop(0)
    self.data_grid_1.columns = columnas"""
    self.repeating_panel_mes.items = [1,2,3,4]
    pass

  ############################################ EVENTOS ############################################
