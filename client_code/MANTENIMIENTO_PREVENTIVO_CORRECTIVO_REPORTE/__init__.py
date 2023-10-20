from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate):
  ################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  libro_solicitudes_mtto = None
  ws_solicitudes_mtto = None
  solicitudes_mtto = None
  registro_solicitud = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos
    self.libro_solicitudes_mtto = app_files.mantenimiento_solicitudes
    self.ws_solicitudes_mtto = self.libro_solicitudes_mtto['Registros']
    self.solicitudes_mtto = self.ws_solicitudes_mtto.rows
    self.registro_solicitud = self.get_registro(datos['id_solicitud_mtto'])
  ################################ FUNCIONES PERSONALIZADS ########################################
  def get_registro(self, id_solicitud_mtto):
    

  ############################################ EVENTOS ############################################

  def drop_down_tipo_mantenimiento_change(self, **event_args):
    if self.drop_down_tipo_mantenimiento.selected_value == "CORRECTIVO":
      self.column_panel_clasificacion.visible = True
    else:
      self.column_panel_clasificacion.visible = False

