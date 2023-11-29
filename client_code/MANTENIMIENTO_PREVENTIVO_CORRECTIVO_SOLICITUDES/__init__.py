from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDESTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from datetime import datetime, date

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDESTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
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
    ("LAMINADORA 3",{"EQUIPO":"LAMINADOR 3","AREA":"ENSAMBLE"}),
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
  libro_solicitudes = None
  ws_solicitudes = None
  registros_solicitudes = None
  registro_actual = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos
    self.drop_down_area.items = self.lista_areas
    self.libro_solicitudes = app_files.mantenimiento_solicitudes
    self.ws_solicitudes = self.libro_solicitudes['Registros']
    self.registros_solicitudes = self.ws_solicitudes.rows

    if self.datos['modo'] == "editor":
      self.text_box_nombre.enabled = False
      self.date_picker_fecha_solicitud.enabled = False
      self.text_area_anomalia.enabled = False
      self.button_enviar.text = "GUARDAR"
      self.button_enviar.icon = "fa:save"
      self.button_enviar.enabled = True
      self.llenar_campos()

  #################################### FUNCIONES PERSONALIZADS ####################################
  def llenar_campos(self):
    for registro in self.registros_solicitudes:
      if registro['id_solicitud_mtto'] == self.datos['id_solicitud_mtto'] and registro['registro_principal'] == '1':
        self.registro_actual = registro
        break
    self.text_box_nombre.text = self.registro_actual['persona_reporta']
    self.date_picker_fecha_solicitud.date = self.registro_actual['fecha_reporte']
    self.drop_down_area.selected_value = self.registro_actual['area']
    self.drop_down_area_change()
    self.text_area_anomalia.text = self.registro_actual['descripcion_anomalia']
    self.drop_down_equipo.selected_value = [equipo[1] for equipo in self.lista_equipos if self.registro_actual['equipo'] in equipo][0]

  def validar_campos(self):
    dict_solicitud = {}
    status_validacion = True
    if self.text_box_nombre.text == "": 
      status_validacion = False 
    else: 
      dict_solicitud['persona_reporta'] = self.text_box_nombre.text 
    if self.date_picker_fecha_solicitud.date == None: 
      status_validacion = False 
    else: 
      dict_solicitud['fecha_reporte'] = self.date_picker_fecha_solicitud.date 
    if self.drop_down_area.selected_value == None:
      status_validacion = False 
    else: 
      dict_solicitud['area'] = self.drop_down_area.selected_value 
    if self.drop_down_equipo.selected_value == None:
      status_validacion = False 
    else: 
      dict_solicitud['equipo'] = self.drop_down_equipo.selected_value['EQUIPO']
    if self.text_area_anomalia.text == "":
      status_validacion = False 
    else: 
      dict_solicitud['descripcion_anomalia'] = self.text_area_anomalia.text

    if not status_validacion:
      return status_validacion
    return dict_solicitud

  def get_folio(self, fecha, equipo, consecutivo):
    temp = datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!
    delta = fecha - temp
    fecha_numero = round(float(delta.days) + (float(delta.seconds) / 86400))
    str_consecutivo = str(consecutivo)
    str_consecutivo = "0"*(3 - len(str_consecutivo)) + str_consecutivo
    return f"{fecha_numero}-{equipo}-{str_consecutivo}"

  def limpiar_campos(self):
    self.text_box_nombre.text = ""
    self.date_picker_fecha_solicitud.date = None
    self.drop_down_area.selected_value = None
    self.drop_down_equipo.selected_value = None
    self.text_area_anomalia.text = None
    self.label_titulo_area.text = "AREA"
  ############################################ EVENTOS ############################################

  def drop_down_area_change(self, **event_args):
    area_seleccionada = self.drop_down_area.selected_value
    if area_seleccionada != None:
      equipos_area = []
      for item in self.lista_equipos:
        if item[1]["AREA"] == area_seleccionada:
          equipos_area.append(item)
      self.drop_down_equipo.items = equipos_area
      self.drop_down_equipo.enabled = True
      self.label_titulo_area.text = area_seleccionada
    else:
      self.drop_down_equipo.enabled = False
      self.drop_down_equipo.selected_value = None
      self.label_titulo_area.text = "AREA"
      self.button_enviar.enabled = False
      self.text_area_anomalia.enabled = False
      

  def button_enviar_click(self, **event_args):
    respuesta = self.validar_campos()
    if respuesta == False:
      alert(title="ERROR!", content="Faltan campos por llenar!")
    else:
      if self.datos['modo'] == "nuevo":
        with Notification("Guardando registro en la base de datos...", title="GUARDANDO.", style="info"):
          id_nuevo_solicitud_mtto = (max([int(item['id_solicitud_mtto']) for item in self.registros_solicitudes]) + 1) if len(self.registros_solicitudes) > 0 else 1
          dict_datos = {
            "id_solicitud_mtto":id_nuevo_solicitud_mtto,
            "mtto_realizado": 0,
            "folio":self.get_folio(datetime.now(),self.drop_down_equipo.selected_value['EQUIPO'],id_nuevo_solicitud_mtto) if len(self.registros_solicitudes) > 0 else self.get_folio(datetime.now(),self.drop_down_equipo.selected_value['EQUIPO'],1),
            "id_usuario_registrador":"4",
            "usuario_registrador":"test",
            "operacion":"creacion",
            "marca_temporal":datetime.now(),
            "registro_principal":1
          }
          respuesta.update(dict_datos)
          self.ws_solicitudes.add_row(**respuesta)
          self.limpiar_campos()
          self.drop_down_area_change()
      else:
        #self.get_folio(datetime.now(),self.drop_down_equipo.selected_value['EQUIPO'],id_nuevo_solicitud_mtto)
        nuevo_registro = dict(self.registro_actual).copy()
        self.registro_actual['registro_principal'] = '0'
        print("nuevo registro:{}")
      
      with Notification("Actualizando base de datos",title="ACTUALIZANDO.", style="info"):
        self.registros_solicitudes = self.ws_solicitudes.rows
      Notification("Registro de solicitud guardada correctamente.",title="GUARDADO.", style="success").show()
      

  def drop_down_equipo_change(self, **event_args):
    if self.drop_down_equipo.selected_value != None:
      self.text_area_anomalia.enabled = True
    else:
      self.text_area_anomalia.enabled = False

  def text_area_anomalia_change(self, **event_args):
    if self.text_area_anomalia.text == None or self.text_area_anomalia.text == "":
      self.button_enviar.enabled = False
    else:
      self.button_enviar.enabled = True




