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

  ################################ FUNCIONES PERSONALIZADS #######################################
  def filtros(self):
    items = self.registros_reportes.copy()
    if len(self.text_box_filtro_folio.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_folio.text).upper() in str(item['folio'])]
    if len(self.text_box_filtro_area.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_area.text).upper() in str(item['area'])]
    if len(self.text_box_filtro_equipo.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_equipo.text).upper() in str(item['equipo'])]
    if self.drop_down_filtro_refaccion.selected_value != None:
      items = [item for item in items if item['requiere_refaccion'] == self.drop_down_filtro_refaccion.selected_value]
    if self.drop_down_filtro_servicio.selected_value != None:
      items = [item for item in items if item['requiere_servicio'] == self.drop_down_filtro_servicio.selected_value]
    if self.drop_down_filtro_mantenimiento.selected_value != None:
      items = [item for item in items if item['tipo_mantenimiento'] == self.drop_down_filtro_mantenimiento.selected_value]
    if len(self.text_box_filtro_falla.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_falla.text).upper() in str(item['descripcion_falla']).upper()]
    if len(self.text_box_filtro_problema.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_problema.text).upper() in str(item['descripcion_problema']).upper()]
    if len(self.text_box_filtro_actividades_mtto.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_actividades_mtto.text).upper() in str(item['actividades_mtto']).upper()]
    
    self.repeating_panel_registros.items = items

    ########################################### EVENTOS ###########################################

  def text_box_filtro_folio_change(self, **event_args):
    self.filtros()

  def text_box_filtro_area_change(self, **event_args):
    self.filtros()

  def text_box_filtro_equipo_change(self, **event_args):
    self.filtros()

  def drop_down_filtro_refaccion_change(self, **event_args):
    self.filtros()

  def drop_down_filtro_servicio_change(self, **event_args):
    self.filtros()

  def drop_down_filtro_mantenimiento_change(self, **event_args):
    self.filtros()

  def text_box_filtro_falla_change(self, **event_args):
    self.filtros()

  def text_box_filtro_problema_change(self, **event_args):
    self.filtros()

  def text_box_filtro_actividades_mtto_change(self, **event_args):
    self.filtros()









