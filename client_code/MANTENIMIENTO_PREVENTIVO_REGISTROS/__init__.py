from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
from datetime import date,datetime
from ..MANTENIMIENTO_PREVENTIVO_CHECKLIST import MANTENIMIENTO_PREVENTIVO_CHECKLIST
from ..MANTENIMIENTO_PREVENTIVO_PROGRAMACION import MANTENIMIENTO_PREVENTIVO_PROGRAMACION

class MANTENIMIENTO_PREVENTIVO_REGISTROS(MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  
  libro_mttos = None
  ws_consulta_mttos = None
  registros_consulta_mttos = None
  ws_registros_totales = None
  registros_totales = None
  #registro_seleccionado = None
  
  def __init__(self,datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.set_event_handler('x-programar_mantenimiento', self.programar_mantenimiento)
    
    self.datos = datos
    
    self.libro_mttos = app_files.mantenimiento_preventivo
    self.ws_consulta_mttos = self.libro_mttos['Consulta']
    self.ws_registros_totales = self.libro_mttos['Registros']
    self.registros_totales = self.ws_registros_totales.rows
    if self.datos['modo'] == "dia":
      self.data_row_panel_filtros.visible = False
      self.repeating_panel_registros.items = self.get_datos_actuales()
    elif self.datos['modo'] == "todos":
      self.button_programar.visible = False
      self.registros_consulta_mttos = self.ws_consulta_mttos.rows
      self.repeating_panel_registros.items = self.registros_consulta_mttos
    #self.ws_registros_totales = self.libro_mttos['Registros'] #revisar si es necesario   

  ################################ FUNCIONES PERSONALIZADS ########################################
  def filtros(self):
    items = self.registros_consulta_mttos.copy()
    if self.date_picker_filtro_fecha_programada.date != None:
      items = [item for item in items if (self.date_picker_filtro_fecha_programada.date).strftime("%Y-%m-%d") in str(item['fecha_programada'])]
    if len(self.text_box_filtro_area.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_area.text).upper() in str(item['area'])]
    if len(self.text_box_filtro_equipo.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_equipo.text).upper() in str(item['equipo'])]
    if len(self.text_box_filtro_status.text) > 0:
      items = [item for item in items if str(self.text_box_filtro_status.text).upper() in str(item['status_mantenimiento']).upper()]
    
    if self.drop_down_filtro_frecuencia.selected_value != None:
      items = [item for item in items if item['frecuencia'] == self.drop_down_filtro_frecuencia.selected_value]
    
    self.repeating_panel_registros.items = items
    
  def get_datos_actuales(self):
    self.registros_consulta_mttos = self.ws_consulta_mttos.rows
    registros_dia_seleccionado = []
    for item in self.registros_consulta_mttos:
      fecha_seleccionada = item['fecha_programada'].split('-')
      if int(fecha_seleccionada[0]) == int(self.datos['anio']) and int(fecha_seleccionada[1]) == int(self.datos['mes']) and int(fecha_seleccionada[2]) == int(self.datos['dia']):
        registros_dia_seleccionado.append(item)
    if len(registros_dia_seleccionado) > 0:
      self.data_grid_registros.visible = True
      self.column_panel_empty_db.visible = False
    else:
      self.data_grid_registros.visible = False
      self.column_panel_empty_db.visible = True
    return registros_dia_seleccionado

  def programar_mantenimiento(self, datos, **events_args):
    with Notification("Registrando fecha en la base de datos...",title="GUARDANDO.", style="info"):
      registro_actual = None
      for item in self.registros_totales:
        if item['id_mtto_preventivo'] == datos['id_mtto_preventivo'] and item['registro_principal'] == '1':
          registro_actual = item
          break
      nuevo_registro = dict(registro_actual).copy()
      nuevo_registro['fecha_programada'] = datos['fecha_programada']
      nuevo_registro['operacion'] = "edicion"
      nuevo_registro['status_mantenimiento'] = "REPROGRAMADO"
      nuevo_registro['marca_temporal'] = datetime.now()
      registro_actual['registro_principal'] = 0
      self.ws_registros_totales.add_row(**nuevo_registro)
    with Notification("Actualizando tabla...",title="ACTUALIZANDO."):
      self.button_actualizar_click()

  def actualizar_form_activo(self, datos, **event_args):
    self.datos.update(datos)
    if self.datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CHECKLIST':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CHECKLIST(datos), True)
    elif self.datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_PROGRAMACION':
      respuesta = self.abrir_form(MANTENIMIENTO_PREVENTIVO_PROGRAMACION(datos), False)
      
  def abrir_form(self, form_de_interes, windows_size):
    respuesta = None
    if windows_size:
      respuesta = alert(content = form_de_interes, large=windows_size, dismissible=False, buttons=[("REGRESAR", True)], role='wide-modal-content')
    else:
      respuesta = alert(content = form_de_interes, large=windows_size, dismissible=False, buttons=[("REGRESAR", True)], role='wide-modal-content_small')
    if respuesta == "registro_guardado":
      with Notification("Actualizando tabla...",title="ACTUALIZANDO."):
        self.button_actualizar_click()
      #with Notification("Actualizando calendario...",title="ACTUALIZANDO."):
        
        
  ############################################ EVENTOS ############################################
  def button_programar_click(self, **event_args):
    self.datos['modo'] = 'nuevo'
    self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_PROGRAMACION'
    self.actualizar_form_activo(self.datos)

  def button_actualizar_click(self, **event_args):
    self.repeating_panel_registros.items = self.get_datos_actuales()

  def button_borrar_filtros_click(self, **event_args):
    self.text_box_filtro_area.text = ""
    self.text_box_filtro_equipo.text =""
    self.text_box_fitro_status.text = ""
    self.drop_down_filtro_frecuencia.selected_value = None
    self.date_picker_filtro_fecha_programada.date = None
    self.filtros()

  def date_picker_filtro_fecha_programada_change(self, **event_args):
    self.filtros()

  def text_box_filtro_area_change(self, **event_args):
    self.filtros()

  def text_box_filtro_equipo_change(self, **event_args):
    self.filtros()

  def drop_down_filtro_frecuencia_change(self, **event_args):
    self.filtros()

  def text_box_fitro_status_change(self, **event_args):
    self.filtros()







  

      




