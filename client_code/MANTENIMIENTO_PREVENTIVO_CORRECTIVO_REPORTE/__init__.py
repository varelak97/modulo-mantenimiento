from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
from datetime import datetime, date

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate):
  ################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  libro_solicitudes_mtto = None
  ws_solicitudes_mtto = None
  solicitudes_mtto = None
  solicitud_registro_actual = None
  
  libro_mtto_corr_prev = None
  ws_mtto_corr_prev = None
  mtto_corr_prev_todos = None
  mtto_corr_prev_reporte = None

  lista_areas = [
    "IMPRESIÓN",
    "SUAJE",
    "MANUALES",
    "LÁSER",
    "CALIDAD",
    "REVELADO",
    "ENSAMBLE",
    "ALMACÉN MP",
    "SERVICIOS GENERALES"
  ]
  lista_equipos = [
    ("ATMA 57",{"EQUIPO":"ATMA 57","AREA":"IMPRESIÓN"}),
    ("ATMA 71",{"EQUIPO":"ATMA 71","AREA":"IMPRESIÓN"}),
    ("ATMA 70",{"EQUIPO":"ATMA 70","AREA":"IMPRESIÓN"}),
    ("ATMA 45",{"EQUIPO":"ATMA 45","AREA":"IMPRESIÓN"}),
    ("ATMA 710",{"EQUIPO":"ATMA 710","AREA":"IMPRESIÓN"}),
    ("ATMA 80",{"EQUIPO":"ATMA 80","AREA":"IMPRESIÓN"}),
    ("HORNO 1",{"EQUIPO":"HORNO 1","AREA":"IMPRESIÓN"}),
    ("HORNO 2",{"EQUIPO":"HORNO 2","AREA":"IMPRESIÓN"}),
    ("HORNO 3",{"EQUIPO":"HORNO 3","AREA":"IMPRESIÓN"}),
    ("HORNO 4",{"EQUIPO":"HORNO 4","AREA":"IMPRESIÓN"}),
    ("HORNO 5",{"EQUIPO":"HORNO 5","AREA":"IMPRESIÓN"}),
    ("IMPRESORA MIMAKI",{"EQUIPO":"IMPRESORA MIMAKI","AREA":"IMPRESIÓN"}),
    ("IMPRESORA OFFSET",{"EQUIPO":"IMPRESORA OFFSET","AREA":"IMPRESIÓN"}),
    ("SPS",{"EQUIPO":"SPS","AREA":"IMPRESIÓN"}),
    ("SUAJADORA 1",{"EQUIPO":"SUAJADORA 1","AREA":"SUAJE"}),
    ("SUAJADORA 2",{"EQUIPO":"SUAJADORA 2","AREA":"SUAJE"}),
    ("SUAJADORA 3",{"EQUIPO":"SUAJADORA 3","AREA":"SUAJE"}),
    ("SUAJADORA 4",{"EQUIPO":"SUAJADORA 4","AREA":"SUAJE"}),
    ("EMBOSADORA",{"EQUIPO":"EMBOSADORA","AREA":"SUAJE"}),
    ("LÁSER V-460",{"EQUIPO":"LÁSER V-460","AREA":"LÁSER"}),
    ("LÁSER M-300",{"EQUIPO":"LÁSER M-300","AREA":"LÁSER"}),
    ("LÁSER VLS-360",{"EQUIPO":"LÁSER VLS-360","AREA":"LÁSER"}),
    ("MESA DE COORDENADAS X-Y",{"EQUIPO":"MESA DE COORDENADAS X-Y","AREA":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 2 (CC015)",{"EQUIPO":"PROBADOR ELÉCTRICO 2 (CC015)","AREA":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 3 (C0025)",{"EQUIPO":"PROBADOR ELÉCTRICO 3 (C0025)","AREA":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 4 (C0028)",{"EQUIPO":"PROBADOR ELÉCTRICO 4 (C0028)","AREA":"CALIDAD"}),
    ("INSOLADORA",{"EQUIPO":"INSOLADORA","AREA":"REVELADO"}),
    ("AFILADOR DE RASEROS",{"EQUIPO":"AFILADOR DE RASEROS","AREA":"REVELADO"}),
    ("LAMINADORA 1",{"EQUIPO":"LAMINADORA 1","AREA":"ENSAMBLE"}),
    ("LAMINADORA 2",{"EQUIPO":"LAMINADORA 2","AREA":"ENSAMBLE"}),
    ("LAMINADORA 3",{"EQUIPO":"LAMINADORA 3","AREA":"ENSAMBLE"}),
    ("PICK&PLACE 2",{"EQUIPO":"PICK&PLACE 2","AREA":"ENSAMBLE"}),
    ("TROQUELADORA MANUAL",{"EQUIPO":"TROQUELADORA MANUAL","AREA":"ENSAMBLE"}),
    ("DISPENSADORES",{"EQUIPO":"DISPENSADORES","AREA":"ENSAMBLE"}),
    ("PICK&PLACE 3",{"EQUIPO":"PICK&PLACE 3","AREA":"ENSAMBLE"}),
    ("GUILLOTINA 1",{"EQUIPO":"GUILLOTINA 1","AREA":"ALMACÉN MP"}),
    ("GUILLOTINA 2",{"EQUIPO":"GUILLOTINA 2","AREA":"ALMACÉN MP"}),
    ("GUILLOTINA 3",{"EQUIPO":"GUILLOTINA 3","AREA":"ALMACÉN MP"}),
    ("HOJEADORA",{"EQUIPO":"HOJEADORA","AREA":"ALMACÉN MP"}),
    ("EMBOLSADORA",{"EQUIPO":"EMBOLSADORA","AREA":"MANUALES"})
  ]

  lista_text_components = None
  lista_drop_downs = None
  lista_date_pickers = None

  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.lista_drop_downs = [
      self.drop_down_area,
      self.drop_down_equipo,
      self.drop_down_refaccion,
      self.drop_down_servicio,
      self.drop_down_tipo_mantenimiento
    ]
    self.lista_text_components = [
      self.text_box_folio,
      self.text_box_persona_ejecuta_mtto,
      self.text_box_persona_recibe_conformidad,
      self.text_area_descripcion_falla,
      self.text_area_actividades
    ]
    self.lista_date_pickers = [
      self.date_picker_fecha_hora_solicitud,
      self.date_picker_fecha_hora_inicial,
      self.date_picker_fecha_hora_final
    ]
    
    self.datos = datos
    self.drop_down_area.items = self.lista_areas
    self.drop_down_equipo.items = self.lista_equipos

    self.libro_mtto_corr_prev = app_files.mantenimiento_correctivo_preventivo_programado
    self.ws_mtto_corr_prev = self.libro_mtto_corr_prev['Registros']
    self.mtto_corr_prev_todos = self.ws_mtto_corr_prev.rows

    if self.datos['modo'] == "nuevo":
      self.libro_solicitudes_mtto = app_files.mantenimiento_solicitudes
      self.ws_solicitudes_mtto = self.libro_solicitudes_mtto['Registros']
      self.solicitudes_mtto = self.ws_solicitudes_mtto.rows
      #self.solicitud_registro_actual = self.solicitudes_mtto[int(datos['id_renglon'])]
      for item in self.solicitudes_mtto:
        if item['id_solicitud_mtto'] == self.datos['id_solicitud_mtto'] and item['registro_principal'] == '1':
          self.solicitud_registro_actual = item
          break
      
      self.date_picker_fecha_hora_solicitud.date = self.solicitud_registro_actual['fecha_reporte']
      self.text_box_folio.text = self.solicitud_registro_actual['folio']
      self.drop_down_area.selected_value = self.solicitud_registro_actual['area']
      self.drop_down_area_change()
      for item in self.drop_down_equipo.items:
        if item[1]['EQUIPO'] == self.solicitud_registro_actual['equipo']:
          self.drop_down_equipo.selected_value = item[1]
          break
    elif self.datos['modo'] == "editor":
      self.outlined_card_mtto_preventivo_correctivo.visible = True
    elif self.datos['modo'] == "visor":
      alert("entro en modo visor")
    
    
    
  ################################ FUNCIONES PERSONALIZADS ########################################
  def valida_campos(self):
    status = True
    respuesta = {}
    for item in self.lista_text_components:
      if item.text == "":
        status = False
      else:
        respuesta[item.tag] = item.text
    for index,item in enumerate(self.lista_drop_downs):
      if item.selected_value == None:
        status = False
      else:
        if index == 1:
          respuesta[item.tag] = item.selected_value['EQUIPO']
        else:
          respuesta[item.tag] = item.selected_value
    for item in self.lista_date_pickers:
      if item.date == None:
        status = False
      else:
        respuesta[item.tag] = item.date
    if self.radio_button_mal_uso.get_group_value() == None:
      status = False
    else:
      respuesta['clasificacion_mtto'] = self.radio_button_mal_uso.get_group_value()

    if not status:
      return status
    return respuesta

  ############################################ EVENTOS ############################################

  def drop_down_tipo_mantenimiento_change(self, **event_args):
    if self.drop_down_tipo_mantenimiento.selected_value == "CORRECTIVO":
      self.column_panel_tipo_mtto.visible = True
      self.column_panel_clasificacion.visible = True
      self.label_titulo_mtto_preventivo_correctivo.text = "MANTENIMIENTO PREVENTIVO CORRECTIVO"
    elif self.drop_down_tipo_mantenimiento.selected_value == "PREVENTIVO PROGRAMADO":
      self.column_panel_tipo_mtto.visible = True
      self.column_panel_clasificacion.visible = False
      self.label_titulo_mtto_preventivo_correctivo.text = "MANTENIMIENTO PREVENTIVO PROGRAMADO"
    else:
      self.column_panel_tipo_mtto.visible = False
      self.column_panel_clasificacion.visible = False
      self.label_titulo_mtto_preventivo_correctivo.text = "TIPO DE MANTENIMIENTO"

  def drop_down_area_change(self, **event_args):
    area_seleccionada = self.drop_down_area.selected_value
    if area_seleccionada != None:
      equipos_area = []
      for item in self.lista_equipos:
        if item[1]["AREA"] == area_seleccionada:
          equipos_area.append(item)
      self.drop_down_equipo.items = equipos_area
      #self.label_titulo_area.text = area_seleccionada
    else:
      self.drop_down_equipo.enabled = False
      self.drop_down_equipo.selected_value = None
      #self.label_titulo_area.text = "AREA"
      #self.button_enviar.enabled = False
      #self.text_area_anomalia.enabled = False

  def button_guardar_click(self, **event_args):
    respuesta = self.valida_campos()
    if respuesta == False:
      alert("Por favor, llene todos los campos!",title="ERROR!")
    else:
      with Notification("Guardando reporte...", title="GUARDANDO.", style="info"):
        respuesta['id_mtto_preventivo_correctivo'] = (max([int(item['id_mtto_preventivo_correctivo']) for item in self.mtto_corr_prev_todos]) + 1) if len(self.mtto_corr_prev_todos) > 0 else 1
        respuesta['descripcion_problema'] = self.solicitud_registro_actual['descripcion_anomalia']
        respuesta['id_usuario_registrador'] = self.datos['id_usuario_erp']
        respuesta['usuario_registrador'] = "falta"
        respuesta['operacion'] = "creacion"
        respuesta['marca_temporal'] = datetime.now()
        respuesta['comentarios'] = ""
        respuesta['registro_principal'] = 1
        self.ws_mtto_corr_prev.add_row(**respuesta)
        
        registro_solicitud_editado = dict(self.solicitud_registro_actual).copy() #self.solicitud_registro_actual['mtto_realizado'] = 1 
        self.solicitud_registro_actual['registro_principal'] = 0
        registro_solicitud_editado['operacion'] = "edicion"
        registro_solicitud_editado['marca_temporal'] = datetime.now()
        registro_solicitud_editado['mtto_realizado'] = 1
        self.ws_solicitudes_mtto.add_row(**registro_solicitud_editado)

        ##################### seguir aqui!!!!!!!!!!!!!!!!! ##############################
        
      Notification("Reporte guardado correctamente!", title="ÉXITO!", style="success").show()
      self.raise_event("x-close-alert",value="registro_guardado")
      



