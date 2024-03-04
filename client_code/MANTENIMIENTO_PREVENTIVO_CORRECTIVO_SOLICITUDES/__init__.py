from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDESTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from datetime import datetime, date

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDESTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  
  lista_equipos = None
  
  libro_solicitudes = None
  ws_solicitudes = None
  registros_solicitudes = None
  registro_actual = None

  libro_equipos = None
  ws_equipos_vista = None
  registros_equipos_vista = None
  ws_areas_vista = None
  registros_areas_vista = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos
    self.text_box_nombre.text = self.datos['nombre_usuario']
    self.libro_solicitudes = app_files.mantenimiento_solicitudes
    self.ws_solicitudes = self.libro_solicitudes['Registros']
    self.registros_solicitudes = self.ws_solicitudes.rows

    self.libro_equipos = app_files.mantenimiento_lista_equipos
    self.ws_equipos_vista = self.libro_equipos['VISTA_EQUIPOS']
    self.registros_equipos_vista = self.ws_equipos_vista.rows
    self.ws_areas_vista = self.libro_equipos['VISTA_AREAS']
    self.registros_areas_vista = self.ws_areas_vista.rows

    self.lista_equipos = self.get_lista_equipos()
    self.drop_down_area.items = self.get_lista_areas()

    if self.datos['modo'] == "editor":
      self.text_box_nombre.enabled = False
      self.date_picker_fecha_solicitud.enabled = False
      self.text_area_anomalia.enabled = False
      self.button_enviar.text = "GUARDAR"
      self.button_enviar.icon = "fa:save"
      self.button_enviar.enabled = True
      self.llenar_campos()
    elif self.datos['modo'] == "visor":
      self.llenar_campos()
      self.text_box_nombre.enabled = False
      self.date_picker_fecha_solicitud.enabled = False
      self.text_area_anomalia.enabled = False
      self.drop_down_area.enabled = False
      self.drop_down_equipo.enabled = False
      self.text_area_anomalia.enabled = False
      self.button_enviar.enabled = False

  #################################### FUNCIONES PERSONALIZADS ####################################
  def get_lista_areas(self):
    equipos_tuplas = []
    for fila in self.registros_areas_vista:
      if(fila['nivel'] == '1'):
        equipos_tuplas.append(fila['area'])
    return equipos_tuplas
  def get_lista_equipos(self):
    equipos_tuplas = []
    for fila in self.registros_equipos_vista:
      equipos_tuplas.append((fila['equipo'],{"EQUIPO":fila['equipo'],"AREA":fila['area']}))
    return equipos_tuplas
    
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
      print(self.drop_down_equipo.selected_value)
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
          id_nuevo_solicitud_mtto = (max([int(item['id_solicitud_mtto']) for item in self.registros_solicitudes]) + 1) if len(self.registros_solicitudes) > 0 else 293
          dict_datos = {
            "id_solicitud_mtto":id_nuevo_solicitud_mtto,
            "mtto_realizado": 0,
            "folio":self.get_folio(datetime.now(),self.drop_down_area.selected_value,id_nuevo_solicitud_mtto) if len(self.registros_solicitudes) > 0 else self.get_folio(datetime.now(),self.drop_down_area.selected_value,1),
            #"folio":self.get_folio(datetime.now(),self.drop_down_equipo.selected_value['EQUIPO'],id_nuevo_solicitud_mtto) if len(self.registros_solicitudes) > 0 else self.get_folio(datetime.now(),self.drop_down_equipo.selected_value['EQUIPO'],1),
            "vobo_solicitante": 0,
            "id_usuario_registrador":self.datos['id_usuario_erp'],
            "usuario_registrador":self.datos['nombre_usuario'],
            "operacion":"creacion",
            "marca_temporal":datetime.now(),
            "registro_principal":1
          }
          respuesta.update(dict_datos)
          self.ws_solicitudes.add_row(**respuesta)
          with Notification("Enviando correo de notificación a jefe de mantenimiento...", title=" GENERANDO CORREO.", style="info"):
            titulo = "SOLICITUD DE MANTENIMIENTO"
            texto = f"Tienes una nueva solicitud de mantenimiento con folio:{dict_datos['folio']}"
            anvil.server.call('enviar_mail','mtto@ensel.org', titulo, texto)
          self.limpiar_campos()
          self.drop_down_area_change()
      else:
        nuevo_registro = dict(self.registro_actual).copy()
        dict_datos = {
          "folio": self.get_folio(datetime.now(),self.drop_down_area.selected_value,self.registro_actual['id_solicitud_mtto']),
          "id_usuario_registrador": "6",
          "usuario_registrador": "otro usuario",
          "operacion": "edicion",
          "marca_temporal": datetime.now()
        }
        nuevo_registro.update(dict_datos)
        nuevo_registro.update(respuesta)
        print(f"viejo registro:{self.registro_actual}")
        print(f"nuevo registro:{nuevo_registro}")
        #self.registro_actual['registro_principal'] = '0'

      self.raise_event("x-close-alert",value="registro_guardado")
      """with Notification("Actualizando base de datos",title="ACTUALIZANDO.", style="info"):
        self.registros_solicitudes = self.ws_solicitudes.rows
      Notification("Registro de solicitud guardada correctamente.",title="GUARDADO.", style="success").show()"""
      

  def drop_down_equipo_change(self, **event_args):
    if self.datos['modo'] != "editor":
      if self.drop_down_equipo.selected_value != None:
        self.text_area_anomalia.enabled = True
      else:
        self.text_area_anomalia.enabled = False

  def text_area_anomalia_change(self, **event_args):
    if self.text_area_anomalia.text == None or self.text_area_anomalia.text == "":
      self.button_enviar.enabled = False
    else:
      self.button_enviar.enabled = True




