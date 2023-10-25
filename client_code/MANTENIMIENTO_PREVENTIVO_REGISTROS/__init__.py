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
    
    self.repeating_panel_registros.items = self.get_datos_actuales()
    #self.ws_registros_totales = self.libro_mttos['Registros'] #revisar si es necesario   

  ################################ FUNCIONES PERSONALIZADS ########################################
  def get_datos_actuales(self):
    self.registros_consulta_mttos = self.ws_consulta_mttos.rows
    registros_dia_seleccionado = []
    for item in self.registros_consulta_mttos:
      fecha_seleccionada = item['fecha_programada'].split('-')
      if int(fecha_seleccionada[0]) == int(self.datos['anio']) and int(fecha_seleccionada[1]) == int(self.datos['mes']) and int(fecha_seleccionada[2]) == int(self.datos['dia']):
        registros_dia_seleccionado.append(item)
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
      nuevo_registro['marca_temporal'] = datetime.now()
      registro_actual['registro_principal'] = 0
      self.ws_registros_totales.add_row(**nuevo_registro)

  def actualizar_form_activo(self, datos, **event_args):
    self.datos.update(datos)
    if self.datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CHECKLIST':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CHECKLIST(datos))
    elif self.datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_PROGRAMACION':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_PROGRAMACION(datos))
  
  def editar_registro(self, datos, **event_args):
    self.datos.update(datos)
    if self.datos['modo'] == "reprogramar":
      #self.outlined_card_tabla.visible = False regresar
      #self.button_programar_click() #regresar
      #self.column_panel_reprogramar.visible = True

      
      """for item in self.registros_totales:
        if item['id_mtto_preventivo'] == self.datos['id_mtto_preventivo'] and item['registro_principal'] == '1':
          self.registro_seleccionado = item
          break
      self.drop_down_area.selected_value = self.registro_seleccionado['area']
      self.drop_down_area_change()
      item_equipo = None
      for item in self.lista_equipos:
        if item[0] == self.registro_seleccionado['equipo']:
          item_equipo = item[1]
          break
      self.drop_down_equipo.selected_value = item_equipo
      self.drop_down_equipo_change()
      self.drop_down_frecuencia.selected_value = self.registro_seleccionado['frecuencia']
      
      self.drop_down_area.enabled = False
      self.drop_down_equipo.enabled = False
      self.drop_down_frecuencia.enabled = False
      self.button_guardar.enabled = False"""
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", True)])
    if respuesta == "registro_guardado":
      with Notification("Actualizando tabla...",title="ACTUALIZANDO."):
        self.button_actualizar_click()
  
  ############################################ EVENTOS ############################################
  def button_programar_click(self, **event_args):
    #regresar
    """self.outlined_card_equipo.visible = True
    self.button_programar.visible = False
    self.column_panel_reprogramar.visible = False"""
    self.datos['modo'] = 'nuevo'
    self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_PROGRAMACION'
    self.actualizar_form_activo(self.datos)


    #regresar
    """def button_cancelar_click(self, **event_args):
    self.outlined_card_equipo.visible = False
    self.outlined_card_tabla.visible = True
    self.button_programar.visible = True
    self.button_guardar.enabled = False
    self.drop_down_area.selected_value = None
    self.drop_down_equipo.selected_value = None
    self.drop_down_frecuencia.selected_value = None"""


  def button_actualizar_click(self, **event_args):
    self.repeating_panel_registros.items = self.get_datos_actuales()

      




