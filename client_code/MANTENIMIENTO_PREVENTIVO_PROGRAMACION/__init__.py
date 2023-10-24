from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_PROGRAMACIONTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class MANTENIMIENTO_PREVENTIVO_PROGRAMACION(MANTENIMIENTO_PREVENTIVO_PROGRAMACIONTemplate):
  ################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  lista_areas = [
    "IMPRESIÓN",
    "SUAJE",
    "MANUALES",
    "LÁSER",
    "CALIDAD",
    "REVELADO",
    "ENSAMBLE",
    "ALMACÉN MP"
  ]
  lista_equipos = [
    ("ATMA 57",{"EQUIPO":"ATMA 57","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 71",{"EQUIPO":"ATMA 71","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 70",{"EQUIPO":"ATMA 70","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 45",{"EQUIPO":"ATMA 45","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 710",{"EQUIPO":"ATMA 710","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 80",{"EQUIPO":"ATMA 80","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("HORNO 1",{"EQUIPO":"HORNO 1","AREA":"IMPRESIÓN","FRECUENCIA":["SEMANAL","MENSUAL","SEMESTRAL"]}),
    ("HORNO 2",{"EQUIPO":"HORNO 2","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 3",{"EQUIPO":"HORNO 3","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 4",{"EQUIPO":"HORNO 4","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 5",{"EQUIPO":"HORNO 5","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("IMPRESORA MIMAKI",{"EQUIPO":"IMPRESORA MIMAKI","AREA":"IMPRESIÓN","FRECUENCIA":["MENSUAL"]}),
    ("IMPRESORA OFFSET",{"EQUIPO":"IMPRESORA OFFSET","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("SPS",{"EQUIPO":"SPS","AREA":"IMPRESIÓN","FRECUENCIA":["MENSUAL"]}),
    ("SUAJADORA 1",{"EQUIPO":"SUAJADORA 1","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 2",{"EQUIPO":"SUAJADORA 2","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 3",{"EQUIPO":"SUAJADORA 3","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 4",{"EQUIPO":"SUAJADORA 4","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("EMBOSADORA",{"EQUIPO":"EMBOSADORA","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("LÁSER V-460",{"EQUIPO":"LÁSER V-460","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("LÁSER M-300",{"EQUIPO":"LÁSER M-300","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("LÁSER VLS-360",{"EQUIPO":"LÁSER VLS-360","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("MESA DE COORDENADAS X-Y",{"EQUIPO":"MESA DE COORDENADAS X-Y","AREA":"CALIDAD","FRECUENCIA":["TRIMESTRAL"]}),
    ("PROBADOR ELÉCTRICO 2 (CC015)",{"EQUIPO":"PROBADOR ELÉCTRICO 2 (CC015)","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("PROBADOR ELÉCTRICO 3 (C0025)",{"EQUIPO":"PROBADOR ELÉCTRICO 3 (C0025)","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("PROBADOR ELÉCTRICO 4 (C0028)",{"EQUIPO":"PROBADOR ELÉCTRICO 4 (C0028)","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("INSOLADORA",{"EQUIPO":"INSOLADORA","AREA":"REVELADO","FRECUENCIA":["TRIMESTRAL"]}),
    ("AFILADOR DE RASEROS",{"EQUIPO":"AFILADOR DE RASEROS","AREA":"REVELADO","FRECUENCIA":["TRIMESTRAL"]}),
    ("LAMINADORA 1",{"EQUIPO":"LAMINADORA 1","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("LAMINADORA 2",{"EQUIPO":"LAMINADORA 2","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("LAMINADORA 3",{"EQUIPO":"LAMINADOR 3","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("PICK&PLACE 2",{"EQUIPO":"PICK&PLACE 2","AREA":"ENSAMBLE","FRECUENCIA":["TRIMESTRAL"]}),
    ("TROQUELADORA MANUAL",{"EQUIPO":"TROQUELADORA MANUAL","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("DISPENSADORES",{"EQUIPO":"DISPENSADORES","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("PICK&PLACE 3",{"EQUIPO":"PICK&PLACE 3","AREA":"ENSAMBLE","FRECUENCIA":["TRIMESTRAL"]}),
    ("GUILLOTINA 1",{"EQUIPO":"GUILLOTINA 1","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("GUILLOTINA 2",{"EQUIPO":"GUILLOTINA 2","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("GUILLOTINA 3",{"EQUIPO":"GUILLOTINA 3","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("HOJEADORA",{"EQUIPO":"HOJEADORA","AREA":"ALMACÉN MP","FRECUENCIA":["TRIMESTRAL"]}),
    ("EMBOLSADORA",{"EQUIPO":"EMBOLSADORA","AREA":"MANUALES","FRECUENCIA":["TRIMESTRAL"]}),
  ]
  
  def __init__(self, **properties):
    self.init_components(**properties)
  ########################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    datos = None
    self.datos = datos
    self.drop_down_area.items = self.lista_areas
    self.drop_down_equipo.items = self.lista_equipos
    if datos['modo'] == 'reprogramar':
      self.rellenar_campos()

  ################################ FUNCIONES PERSONALIZADS ########################################
  def rellenar_campos(self):
    if self.datos['modo'] == "reprogramar":
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
    pass
    
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

  def date_picker_reprogramar_change(self, **event_args):
    if self.date_picker_reprogramar.date != None:
      self.button_guardar.enabled = True
    else:
      self.button_guardar.enabled = False

  def button_cancelar_click(self, **event_args):
    alert("cerrar ventana")
    
