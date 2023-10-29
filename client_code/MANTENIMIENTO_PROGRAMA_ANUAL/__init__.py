from ._anvil_designer import MANTENIMIENTO_PROGRAMA_ANUALTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class MANTENIMIENTO_PROGRAMA_ANUAL(MANTENIMIENTO_PROGRAMA_ANUALTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  def __init__(self, datos, **properties):
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.init_components(**properties)
    self.datos = datos
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
