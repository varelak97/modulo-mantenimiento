from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
from datetime import date,datetime
from ..MANTENIMIENTO_PREVENTIVO_CHECKLIST import MANTENIMIENTO_PREVENTIVO_CHECKLIST

class MANTENIMIENTO_PREVENTIVO_REGISTROS(MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  libro_mttos = None
  ws_consulta_mttos = None
  registros_consulta_mttos = None
  ws_registros_totales = None
  registros_totales = None
  registro_seleccionado = None
  
  def __init__(self,datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.set_event_handler('x-editar_registro', self.editar_registro)
    
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

  def actualizar_form_activo(self, datos, **event_args):
    self.datos.update(datos)
    if self.datos['modo'] == "reprogramar":
      self.outlined_card_tabla.visible = False
    else:
      if self.datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CHECKLIST':
        self.abrir_form(MANTENIMIENTO_PREVENTIVO_CHECKLIST(datos))
  
  def editar_registro(self, datos, **event_args):
    self.datos.update(datos)
    if self.datos['modo'] == "reprogramar":
      self.outlined_card_tabla.visible = False
      self.button_programar_click()
      self.column_panel_reprogramar.visible = True
      for item in self.registros_totales:
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
      self.button_guardar.enabled = False
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", True)])
    if respuesta == "registro_guardado":
      with Notification("Actualizando tabla...",title="ACTUALIZANDO."):
        self.button_actualizar_click()
  
  def get_actividades(self, equipo_seleccionado, frecuencia_mtto):
    actividades = None
    if equipo_seleccionado['AREA'] == "IMPRESIÓN":
      if equipo_seleccionado['EQUIPO'] == "IMPRESORA MIMAKI":
        actividades = self.actividades_equipo_mimaki_mensual
      elif equipo_seleccionado['EQUIPO'] == "SPS":
        actividades = self.actividades_equipo_sps_mensual
      elif equipo_seleccionado['EQUIPO'] == "IMPRESORA OFFSET":
        actividades = self.actividades_equipo_offset_trimestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 1":
        if frecuencia_mtto == "SEMANAL":
          actividades = self.actividades_equipo_horno_1_semanal
        elif frecuencia_mtto == "MENSUAL":
          actividades = self.actividades_equipo_horno_1_mensual
        elif frecuencia_mtto == "SEMESTRAL":
          actividades = self.actividades_equipo_horno_1_semestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 2":
        actividades = self.actividades_equipo_horno_2_semestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 3":
        actividades = self.actividades_equipo_horno_3_semestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 4":
        actividades = self.actividades_equipo_horno_4_semestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 5":
        actividades = elf.actividades_equipo_horno_5_semestral
      elif equipo_seleccionado['EQUIPO'] == "ATMA 80" or equipo_seleccionado['EQUIPO'] == "ATMA 710":
        self.actividades_equipos_atma_trimestral += self.actividades_equipos_atma80_710_trimestral
        self.actividades_equipos_atma_trimestral = sorted(self.actividades_equipos_atma_trimestral, key=lambda d: d['id']) 
        actividades = self.actividades_equipos_atma_trimestral
      else:
        for index,actividad in enumerate(self.actividades_equipos_atma_trimestral):
          actividad['id'] = index + 1
        actividades = self.actividades_equipos_atma_trimestral
    ################################################# SUAJE ########################################################
    elif equipo_seleccionado['AREA'] == "SUAJE":
      if equipo_seleccionado['EQUIPO'] == "EMBOSADORA":
        actividades = self.actividades_equipo_embosadora_trimestral
      else:
        actividades = self.actividades_equipos_suaje_trimestral
    ################################################# MANUALES ########################################################
    elif equipo_seleccionado['AREA'] == "MANUALES":
      actividades = self.actividades_equipo_embolsadora_trimestral
    ################################################# LASER ########################################################
    elif equipo_seleccionado['AREA'] == "LÁSER":
      if frecuencia_mtto == "SEMANAL":
        actividades = self.actividades_equipos_laser_semanal
      elif frecuencia_mtto == "MENSUAL":
        actividades = self.actividades_equipos_laser_mensual
    ################################################# CALIDAD ########################################################
    elif equipo_seleccionado['AREA'] == "CALIDAD":
      if equipo_seleccionado['EQUIPO'] == "MESA DE COORDENADAS X-Y":
        actividades = self.actividades_equipo_mesa_coordenadas_trimestral
      elif equipo_seleccionado['EQUIPO'] != "PROBADOR ELÉCTRICO 2 (CC015)":
        self.actividades_equipos_probadores_electricos_mensual += self.actividades_equipo_probador_electrico_2_mensual
        actividades = self.actividades_equipos_probadores_electricos_mensual
      else:
        actividades = self.actividades_equipos_probadores_electricos_mensual
    ################################################# REVELADO ########################################################
    elif equipo_seleccionado['AREA'] == "REVELADO":
      if equipo_seleccionado['EQUIPO'] == "INSOLADORA":
        actividades = self.actividades_equipo_insoladora_semestral
      elif equipo_seleccionado['EQUIPO'] == "AFILADOR DE RASEROS":
        actividades = self.actividades_equipo_afilador_raseros_trimestral
    ################################################# ENSAMBLE ########################################################
    elif equipo_seleccionado['AREA'] == "ENSAMBLE":
      if equipo_seleccionado['EQUIPO'] == "PICK&PLACE 2":
        actividades = self.actividades_equipo_pickAndPlace_2_trimestral
      elif equipo_seleccionado['EQUIPO'] == "PICK&PLACE 3":
        actividades = self.actividades_equipo_pickAndPlace_3_trimestral
      elif equipo_seleccionado['EQUIPO'] == "TROQUELADORA MANUAL":
        actividades = self.actividades_equipo_troqueladora_manual_semestral
      elif equipo_seleccionado['EQUIPO'] == "DISPENSADORES":
        actividades = self.actividades_equipos_dispensadores_semestral
      else:
        actividades = self.actividades_equipos_laminadoras_semestral
    ################################################# ALMACEN MP ########################################################
    elif equipo_seleccionado['AREA'] == "ALMACÉN MP":
      if equipo_seleccionado['EQUIPO'] == "HOJEADORA":
        actividades = self.actividades_equipo_hojeadora_trimestral
      else:
        actividades = self.actividades_equipos_guillotinas_semestral
    return actividades
  
  
  ############################################ EVENTOS ############################################
  def button_programar_click(self, **event_args):
    self.outlined_card_equipo.visible = True
    self.button_programar.visible = False
    self.column_panel_reprogramar.visible = False
    self.datos['modo'] = 'nuevo'


  def button_cancelar_click(self, **event_args):
    self.outlined_card_equipo.visible = False
    self.outlined_card_tabla.visible = True
    self.button_programar.visible = True
    self.button_guardar.enabled = False
    self.drop_down_area.selected_value = None
    self.drop_down_equipo.selected_value = None
    self.drop_down_frecuencia.selected_value = None

  def drop_down_area_change(self, **event_args):
    area_seleccionada = self.drop_down_area.selected_value
    if area_seleccionada != None:
      equipos_area = []
      frecuencias = []
      self.drop_down_equipo.enabled = True
      
      for item in self.lista_equipos:
        if item[1]["AREA"] == area_seleccionada:
          equipos_area.append(item)
      
      self.drop_down_equipo.items = equipos_area
      self.button_guardar.enabled = False
      self.drop_down_frecuencia.selected_value = None
      self.drop_down_frecuencia.enabled = False
    else:
      self.drop_down_equipo.enabled = False
      self.drop_down_equipo.selected_value = None
      self.drop_down_frecuencia.enabled = False
      self.drop_down_frecuencia.selected_value = None
      self.button_guardar.enabled = False

  def drop_down_equipo_change(self, **event_args):
    equipo_seleccionado = self.drop_down_equipo.selected_value
    if equipo_seleccionado != None:
      lista_frecuencia_mtto = equipo_seleccionado["FRECUENCIA"]
      if len(lista_frecuencia_mtto) == 1:
        self.drop_down_frecuencia.items = lista_frecuencia_mtto
        self.drop_down_frecuencia.selected_value = lista_frecuencia_mtto[0]
        self.drop_down_frecuencia.enabled = False
        self.button_guardar.enabled = True
      else:
        self.drop_down_frecuencia.items = lista_frecuencia_mtto
        self.drop_down_frecuencia.enabled = True
    else:
      self.drop_down_frecuencia.selected_value = None
      self.drop_down_frecuencia.enabled = None
      self.button_guardar.enabled = False

  def drop_down_frecuencia_change(self, **event_args):
    if self.drop_down_frecuencia.selected_value != None:
      self.button_guardar.enabled = True
    else:
      self.button_guardar.enabled = False

  def button_guardar_click(self, **event_args):
    if self.datos['modo'] == "reprogramar":
      with Notification("Actualizando registro...",title="GUARDANDO."):
        registro_nuevo = dict(self.registro_seleccionado).copy()
        self.registro_seleccionado['registro_principal'] = 0
        registro_nuevo['fecha_programada'] = self.date_picker_reprogramar.date
        registro_nuevo['status_mantenimiento'] = "REPROGRAMADO"
        registro_nuevo['operacion'] = "edicion"
        registro_nuevo['marca_temporal'] = datetime.now()
        self.ws_registros_totales.add_row(**registro_nuevo)
    else:
      with Notification("Registrando en la base de datos...",title="GUARDANDO."):
        dict_mtto = {
          "id_mtto_preventivo":(max([int(item['id_mtto_preventivo']) for item in self.registros_consulta_mttos]) + 1) if len(self.registros_consulta_mttos) > 0 else 1,
          "fecha_programada":f"{self.datos['anio']}-{self.datos['mes']}-{self.datos['dia']}",
          "area":self.drop_down_area.selected_value,
          "equipo":self.drop_down_equipo.selected_value['EQUIPO'],
          "frecuencia":self.drop_down_frecuencia.selected_value,
          "status_mantenimiento":"PROGRAMADO",
          "actividades":self.get_actividades(self.drop_down_equipo.selected_value, self.drop_down_frecuencia.selected_value),
          "id_usuario_registrador":self.datos['id_usuario_erp'],
          "usuario_registrador":"pendiente",
          "operacion":"creacion",
          "marca_temporal":datetime.now(),
          "comentarios":"",
          "registro_principal": 1
        }
        self.ws_registros_totales.add_row(**dict_mtto)
    Notification("Registro guardado correctamente.", title="GUARDADO.", style="success").show()
    with Notification("Actualizando tabla", title="ACTUALIZANDO."):
      self.repeating_panel_registros.items = self.get_datos_actuales()
    self.button_cancelar_click()

  def button_actualizar_click(self, **event_args):
    self.repeating_panel_registros.items = self.get_datos_actuales()

  def date_picker_reprogramar_change(self, **event_args):
    if self.date_picker_reprogramar.date != None:
      self.button_guardar.enabled = True
    else:
      self.button_guardar.enabled = False
      




