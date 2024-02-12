from ._anvil_designer import MANTENIMIENTO_LISTA_EQUIPOSTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil_extras import augment
from anvil_extras import popover
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS
from ..MANTENIMIENTO_PREVENTIVO_REGISTROS import MANTENIMIENTO_PREVENTIVO_REGISTROS
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS
from ..MANTENIMIENTO_PROGRAMA_ANUAL import MANTENIMIENTO_PROGRAMA_ANUAL
from ..MANTENIMIENTO_AUTONOMO import MANTENIMIENTO_AUTONOMO

class MANTENIMIENTO_LISTA_EQUIPOS(MANTENIMIENTO_LISTA_EQUIPOSTemplate):
  ################################### DEFINICION DE VARIABLES ####################################
  form_activo = None
  datos = {}
  boton = None
  url_imagenes_equipos ={
    "ATMA 70":"_/theme/equipos/ATMA70.jpg",
    "LÁSER M-300":"_/theme/equipos/M300.jpg",
    "LÁSER VLS-360":"_/theme/equipos/VLS360.jpg",
    "PICK&PLACE 2":"_/theme/equipos/pnp2.jpg",
    "SPS":"_/theme/equipos/sps.jpg",
    "IMPRESORA MIMAKI":"_/theme/equipos/mimaki.jpg",
    "default":"_/theme/equipos/default.png"
  }
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
  libro_equipos = None
  ws_equipos = None
  registros_vista_equipos = None
  registros_vista_actividades = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ########################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos
    self.drop_down_area.items = self.lista_areas
    self.drop_down_equipo.items = self.lista_equipos  
    #popovers
    """self.boton = Button(text="prueba")
    self.outlined_card_calendario_mttos.popover(content=MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS(self.datos), title="TITULO DE PRUEBA", trigger="manual")"""

    #set color when mouseevent(leave,enter) occurs
    augment.set_event_handler(self.outlined_card_calendario_mttos,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_calendario_mttos,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_mtto_preventivo_correctivo,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_mtto_preventivo_correctivo,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_solicitudes_mtto,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_solicitudes_mtto,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_mtto_autonomo,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_mtto_autonomo,'mouseleave',self.set_color)

    if self.datos['id_usuario_erp'] == 58 or self.datos['id_usuario_erp'] == 884 or self.datos['id_usuario_erp'] == 0:
      self.content_panel_general.visible = False
      self.content_panel.visible = True
    else:
      self.content_panel.visible = False
      self.content_panel_general.visible = True
  ##################################### FUNCIONES PERSONALIZADS #####################################
  def set_color(self,**event_args):
    card = event_args['sender']
    if 'enter' in event_args['event_type']:
      card.background = app.theme_colors['LightBlue']
    else:
      card.background = app.theme_colors['White']
    
  ############################################# EVENTOS #############################################
  def drop_down_area_change(self, **event_args):
    area_seleccionada = self.drop_down_area.selected_value
    if area_seleccionada != None:
      equipos_area = []
      self.drop_down_equipo.enabled = True
      
      for item in self.lista_equipos:
        if item[1]["AREA"] == area_seleccionada:
          equipos_area.append(item)
      
      self.drop_down_equipo.items = equipos_area
    else:
      self.drop_down_equipo.enabled = False
      self.drop_down_equipo.selected_value = None

  def drop_down_tipo_mtto_change(self, **event_args):
    if self.drop_down_tipo_mtto.selected_value != None:
      tipo_mtto = self.drop_down_tipo_mtto.selected_value
      try: #Se utiliza un try porque la primera vez que se abre el form RECUERSOS_HUMANOS no tiene ningún form hijo cargado, entonces levantará un error.
        self.form_activo.remove_from_parent()
      except: #no se necesita para manejar el error, pero el 'except' es obligado a estar cuando se usa un try. ¡NO BORRAR!
        pass

      if tipo_mtto == "PREVENTIVO":
        self.datos['modo'] = "todos"
        self.form_activo = MANTENIMIENTO_PREVENTIVO_REGISTROS(self.datos)
      elif tipo_mtto == "PREVENTIVO/CORRECTIVO PROGRAMADO":
        self.form_activo = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS(self.datos)
      self.add_component(self.form_activo)

  def link_calendario_mttos_click(self, **event_args):
    datos = self.datos
    respuesta = alert(content = MANTENIMIENTO_PROGRAMA_ANUAL(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_nueva_solicitud_click(self, **event_args):
    datos = self.datos
    datos['modo'] = "nuevo"
    respuesta = alert(content = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_mtto_preventivo_correctivo_click(self, **event_args):
    datos = self.datos
    datos['equipo'] = self.drop_down_equipo.selected_value['EQUIPO'] if self.drop_down_equipo.selected_value != None else "todos"
    respuesta = alert(content = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_solicitudes_mtto_click(self, **event_args):
    datos = self.datos
    datos['equipo'] = self.drop_down_equipo.selected_value['EQUIPO'] if self.drop_down_equipo.selected_value != None else "todos"
    respuesta = alert(content = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_mtto_autonomo_click(self, **event_args):
    datos = self.datos
    respuesta = alert(content = MANTENIMIENTO_AUTONOMO(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def actualizar_form_activo(self, datos, **event_args):
    datos['mes'] = self.drop_down_mes.selected_value
    datos['anio'] = self.drop_down_anio.selected_value
    datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    datos['modo'] = "dia"
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content")
    if respuesta:
      self.llenar_calendario()

  def drop_down_equipo_change(self, **event_args):
    equipo_seleccionado = self.drop_down_equipo.selected_value['EQUIPO'] if self.drop_down_equipo.selected_value != None else "default"
    if equipo_seleccionado in self.url_imagenes_equipos:
      self.image_equipo.source = self.url_imagenes_equipos[equipo_seleccionado]
    else:
      self.image_equipo.source = self.url_imagenes_equipos["default"]
      
