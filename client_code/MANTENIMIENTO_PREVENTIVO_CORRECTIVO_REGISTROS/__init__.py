from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
from anvil_extras import popover
from anvil.js import get_dom_node
from anvil.js.window import jQuery
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE

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

    self.set_event_handler('x-abrir_reporte', self.abrir_reporte)

    self.repeating_panel_aux.items = ["random data"]
    aux_grid = get_dom_node(self.data_grid_aux)
    main_grid = get_dom_node(self.data_grid_reportes)
    anvil.js.call("add_scroll_event", main_grid.childNodes[0], aux_grid.childNodes[0])

    self.libro_reportes = app_files.mantenimiento_correctivo_preventivo_programado
    self.ws_reportes = self.libro_reportes['Consulta']
    self.registros_reportes = []

    self.button_actualizar_click()

  ################################ FUNCIONES PERSONALIZADS #######################################    
  def abrir_reporte(self, datos, **event_args):
    datos.update(self.datos)
    respuesta = alert(content = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")
    if respuesta == "registro_guardado":
      with Notification("Actualizando tabla...", title="ACTUALIZANDO", style="success"):
        self.button_actualizar_click()
    
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
  def button_actualizar_click(self, **event_args):
    if self.datos['area'] == "todas":
      if self.datos['equipo'] == "todos":
        self.registros_reportes = self.ws_reportes.rows
      else:
        for row in self.ws_reportes.rows:
          if row['equipo'] == self.datos['equipo']:
            self.registros_reportes.append(row)
    else:
      if self.datos['equipo'] == "todos":
        for row in self.ws_reportes.rows:
          if row['area'] == self.datos['area']:
            self.registros_reportes.append(row)
      else:
        for row in self.ws_reportes.rows:
          if row['equipo'] == self.datos['equipo'] and row['area'] == self.datos['area']:
            self.registros_reportes.append(row)
    if len(self.registros_reportes) > 0:
      self.repeating_panel_registros.items = self.registros_reportes
      self.data_grid_reportes.visible = True
      self.data_grid_aux.visible = True
      self.column_panel_empty_db.visible = False
    else:
      self.data_grid_reportes.visible = False
      self.data_grid_aux.visible = False
      self.column_panel_empty_db.visible = True
      
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

  def button_test_click(self, **event_args):
    elemento = get_dom_node(self.data_grid_reportes)
    print(jQuery(elemento).children().scrollLeft())
    div = jQuery("<div style='overflow-y:visible; background-color:red'></div>")
    div.appendTo(get_dom_node(self.data_grid_reportes))
    

  def slider_1_change(self, handle, **event_args):
    """This method is called when the slider has finished sliding"""
    pass










