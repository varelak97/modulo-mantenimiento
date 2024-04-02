from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROSTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES
from anvil_extras import popover
from anvil.js import get_dom_node
from anvil.js.window import jQuery
from datetime import datetime, date

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROSTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  libro_solicitudes_mtto = None
  ws_consulta_solicitudes_mtto = None
  registros_consulta_mtto = None
  #ws_solicitudes_mtto = None
  #registros_mtto = None
  items_drop_down_status = [("PENDIENTE", 0),("REALIZADO", 1),("APROBADO", 2)]
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.set_event_handler('x-programar_mantenimiento', self.programar_mantenimiento)
    self.set_event_handler('x-abrir_solicitud', self.abrir_solicitud)
    self.set_event_handler('x-abrir_reporte', self.abrir_reporte)
    
    self.datos = datos
    self.libro_solicitudes_mtto = app_files.mantenimiento_solicitudes
    self.ws_solicitudes_mtto = self.libro_solicitudes_mtto['Registros']
    #self.registros_mtto = self.ws_solicitudes_mtto.rows
    self.ws_consulta_solicitudes_mtto = self.libro_solicitudes_mtto['Consulta']

    self.drop_down_status.items = self.items_drop_down_status
    
    self.repeating_panel_aux.items = ["ramdom_data"]
    aux_grid = get_dom_node(self.data_grid_aux)
    main_grid = get_dom_node(self.data_grid_registros)
    anvil.js.call("add_scroll_event", main_grid.childNodes[0], aux_grid.childNodes[0])

    self.button_actualizar_click()
    
    #self.registros_consulta_mtto = self.ws_consulta_solicitudes_mtto.rows

    #self.registros_consulta_mtto = []

    """if self.datos['id_usuario_erp'] != 58 and self.datos['id_usuario_erp'] != 884:
      for row in self.ws_consulta_solicitudes_mtto.rows:
        if row['persona_reporta'] == self.datos['nombre_usuario']:
          self.registros_consulta_mtto.append(row)
    else:
      if self.datos['equipo'] == "todos":
        self.registros_consulta_mtto = self.ws_consulta_solicitudes_mtto.rows
      else:
        for row in self.ws_consulta_solicitudes_mtto.rows:
          if row['equipo'] == self.datos['equipo']:
            self.registros_consulta_mtto.append(row)
    
    if len(self.registros_consulta_mtto) > 0:
      self.column_panel_empty_db.visible = False
      self.data_grid_registros.visible = True
      dict_registros_consulta_mtto = []
      for fila in self.registros_consulta_mtto:
        dic_fila = dict(fila).copy()
        dic_fila['id_usuario_erp'] = self.datos['id_usuario_erp']
        dict_registros_consulta_mtto.append(dic_fila)
      self.repeating_panel_registros.items = dict_registros_consulta_mtto#self.registros_consulta_mtto
      self.drop_down_status.items = self.items_drop_down_status
    else:
      self.column_panel_empty_db.visible = True
      self.data_grid_registros.visible = False"""
    
  ############################### FUNCIONES PERSONALIZADAS ########################################
  def test(self):
    print("scrolling...")
    
  def abrir_reporte(self, datos, **event_args):
    datos.update(self.datos)
    if datos['modo'] == "validacion":
      if datos['id_usuario_erp'] == 58:
        datos['modo'] = 'visor_by_folio'
    respuesta = alert(content = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")
    if respuesta == "registro_guardado":
      with Notification("Actualizando tabla...", title="ACTUALIZANDO", style="success"):
        self.button_actualizar_click()
    
  def abrir_solicitud(self, datos, **event_args):
    datos.update(self.datos)
    respuesta = alert(content = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")
    if respuesta == "registro_guardado":
      with Notification("Actualizando tabla...", title="ACTUALIZANDO", style="success"):
        self.button_actualizar_click()
        
  def actualizar_form_activo(self, datos, **event_args):
    #datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE':
      datos.update(self.datos)
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", True)])
    if respuesta == "registro_guardado":
        self.button_actualizar_click()
    
  def programar_mantenimiento(self, datos, **event_args):
    with Notification("Registrando fecha en la base de datos...",title="GUARDANDO.", style="info"):
      registro_actual = None
      for item in self.registros_mtto:
        if item['id_solicitud_mtto'] == datos['id_solicitud_mtto'] and item['registro_principal'] == '1':
          registro_actual = item
          break
      nuevo_registro = dict(registro_actual).copy()
      nuevo_registro['fecha_programada'] = datos['fecha_programada']
      nuevo_registro['id_usuario_registrador'] = self.datos['id_usuario_erp']
      nuevo_registro['usuario_registrador'] = self.datos['nombre_usuario']
      nuevo_registro['operacion'] = "edicion"
      nuevo_registro['marca_temporal'] = datetime.now()
      registro_actual['registro_principal'] = 0
      self.ws_solicitudes_mtto.add_row(**nuevo_registro)
    Notification("Fecha registrada correctamente!", title="ÉXITO!.", style="success").show()
    self.button_actualizar_click()

  def filtros(self):
    items = self.registros_consulta_mtto.copy()
    if len(self.text_box_filtro_folio.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_folio.text).upper() in str(item['folio'])]
    if self.date_picker_filtro_fecha_programada.date != None:
      items = [item for item in items if (self.date_picker_filtro_fecha_programada.date).strftime("%d/%m/%Y") in str(item['fecha_programada'])]
    if len(self.text_box_filtro_area.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_area.text).upper() in str(item['area'])]
    if len(self.text_box_filtro_equipo.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_equipo.text).upper() in str(item['equipo'])]
    if self.drop_down_status.selected_value != None:
      items = [item for item in items if (int(item['mtto_realizado']) + int(item['vobo_solicitante'])) == self.drop_down_status.selected_value]
      #items = [item for item in items if bool(int(item['mtto_realizado'])) == self.drop_down_status.selected_value]
    if len(self.text_box_filtro_descripcion_anomalia.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_descripcion_anomalia.text).upper() in str(item['descripcion_anomalia']).upper()]
    if len(self.text_box_filtro_persona_reporta.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_persona_reporta.text).upper() in str(item['persona_reporta']).upper()]
    
    self.repeating_panel_registros.items = items
    
  ############################################ EVENTOS ############################################
  def button_actualizar_click(self, **event_args):
    if len(event_args) > 0:
      with Notification("Actualizando tabla",title="ACTUALIZANDO", style="info"):
        self.leer_registros()
    else:
      self.leer_registros()

  def leer_registros(self):
    self.registros_consulta_mtto = []
    dict_registros_consulta_mtto = []
    
    if self.datos['id_usuario_erp'] != 58 and self.datos['id_usuario_erp'] != 884:
      for row in self.ws_consulta_solicitudes_mtto.rows:
        if row['persona_reporta'] == self.datos['nombre_usuario'] or row['nombre_testigo'] == self.datos['nombre_usuario']:
          self.registros_consulta_mtto.append(row)
    else:
      self.registros_mtto = self.ws_solicitudes_mtto.rows #lee todos los registros
      if self.datos['area'] == "todas":     
        if self.datos['equipo'] == "todos":
          self.registros_consulta_mtto = self.ws_consulta_solicitudes_mtto.rows
        else:
          for row in self.ws_consulta_solicitudes_mtto.rows:
            if self.datos['equipo'] == row['equipo']:
              self.registros_consulta_mtto.append(row)
      else:
        if self.datos['equipo'] == "todos":
          for row in self.ws_consulta_solicitudes_mtto.rows:
            if row['area'] == self.datos['area']:
              self.registros_consulta_mtto.append(row)
        else:
          for row in self.ws_consulta_solicitudes_mtto.rows:
            if row['equipo'] == self.datos['equipo'] and row['area'] == self.datos['area']:
              self.registros_consulta_mtto.append(row)
          
    if len(self.registros_consulta_mtto) > 0:
      for fila in self.registros_consulta_mtto:
        dic_fila = dict(fila).copy()
        dic_fila['id_usuario_erp'] = self.datos['id_usuario_erp']
        dict_registros_consulta_mtto.append(dic_fila)
      self.repeating_panel_registros.items = dict_registros_consulta_mtto#self.registros_consulta_mtto
      self.column_panel_empty_db.visible = False
      self.data_grid_registros.visible = True
      self.data_grid_aux.visible = True
    else:
      self.column_panel_empty_db.visible = True
      self.data_grid_registros.visible = False
      self.data_grid_aux.visible = False

  def button_erase_filtros_click(self, **event_args):
    self.text_box_filtro_folio.text = ""
    self.date_picker_filtro_fecha_programada.date = None
    self.text_box_filtro_area.text = None
    self.text_box_filtro_equipo.text = None
    self.drop_down_status.selected_value = None
    self.date_picker_fecha_reporte_anomalia.date = None
    self.text_box_filtro_descripcion_anomalia.text = ""
    self.text_box_filtro_persona_reporta.text = ""
    self.filtros()

  def text_box_filtro_folio_change(self, **event_args):
    self.filtros()

  def date_picker_filtro_fecha_programada_change(self, **event_args):
    self.filtros()

  def text_box_filtro_area_change(self, **event_args):
    self.filtros()

  def text_box_filtro_equipo_change(self, **event_args):
    self.filtros()

  def drop_down_status_change(self, **event_args):
    self.filtros()

  def date_picker_fecha_reporte_anomalia_change(self, **event_args):
    self.filtros()

  def text_box_filtro_descripcion_anomalia_change(self, **event_args):
    self.filtros()

  def text_box_filtro_persona_reporta_change(self, **event_args):
    self.filtros()

  def button_nueva_solicitud_click(self, **event_args):
    datos = self.datos
    datos['modo'] = "nuevo"
    respuesta = alert(content = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")
    if respuesta == "registro_guardado":
      self.button_actualizar_click()

    










  