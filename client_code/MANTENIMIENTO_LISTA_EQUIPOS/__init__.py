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
from ..MANTENIMIENTO_FORMS_REPORTES import MANTENIMIENTO_FORMS_REPORTES

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

  #libro_equipos = None
  ws_areas = None
  ws_equipos = None
  ws_actividades = None
  registros_vista_areas = None
  registros_vista_equipos = None
  registros_vista_actividades = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ########################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos
    self.libro_equipos = app_files.mantenimiento_lista_equipos
    self.ws_areas = self.libro_equipos['VISTA_AREAS']
    self.registros_vista_areas = self.ws_areas.rows
    self.ws_equipos = self.libro_equipos['VISTA_EQUIPOS']
    self.registros_vista_equipos = self.ws_equipos.rows

    self.drop_down_area.items = [item['area'] for item in self.registros_vista_areas if item['nivel'] == '1']
    self.drop_down_equipo.items = [item['equipo'] for item in self.registros_vista_equipos]
    
    #self.drop_down_area.items = self.lista_areas #antes
    #self.drop_down_equipo.items = self.lista_equipos #antes
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
    augment.set_event_handler(self.outlined_card_nueva_solicitud,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_nueva_solicitud,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_solicitudes_mtto_copy,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_solicitudes_mtto_copy,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_mtto_autonomo_copy,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_mtto_autonomo_copy,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_req_consumibles,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_req_consumibles,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_req_consumibles_copy,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_req_consumibles_copy,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_inventario,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_inventario,'mouseleave',self.set_color)

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
      card.background = app.theme_colors['Background']
    
  ############################################# EVENTOS #############################################
  def drop_down_area_change(self, **event_args):
    self.column_panel_luz_resistencia.visible = False
    area_seleccionada = self.drop_down_area.selected_value
    if area_seleccionada != None:
      equipos_area = []
      self.drop_down_equipo.enabled = True
      
      #antes
      """for item in self.lista_equipos:
        if item[1]["AREA"] == area_seleccionada:
          equipos_area.append(item)"""
      for item in self.registros_vista_equipos:
        if item['area'] == area_seleccionada:
          equipos_area.append(item['equipo'])
      self.drop_down_equipo.items = equipos_area
    else:
      #self.drop_down_equipo.enabled = False #antes
      self.drop_down_equipo.selected_value = None
      self.drop_down_equipo.items = [item['equipo'] for item in self.registros_vista_equipos]

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
    #antes
    #datos['equipo'] = self.drop_down_equipo.selected_value['EQUIPO'] if self.drop_down_equipo.selected_value != None else "todos"
    datos['equipo'] = self.drop_down_equipo.selected_value if self.drop_down_equipo.selected_value != None else "todos"
    datos['area'] = self.drop_down_area.selected_value if self.drop_down_area.selected_value != None else "todas"
    respuesta = alert(content = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_solicitudes_mtto_click(self, **event_args):
    datos = self.datos
    #antes
    #datos['equipo'] = self.drop_down_equipo.selected_value['EQUIPO'] if self.drop_down_equipo.selected_value != None else "todos"
    datos['equipo'] = self.drop_down_equipo.selected_value if self.drop_down_equipo.selected_value != None else "todos"
    datos['area'] = self.drop_down_area.selected_value if self.drop_down_area.selected_value != None else "todas"
    respuesta = alert(content = MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_mtto_autonomo_click(self, **event_args):
    datos = self.datos
    datos['tipo'] = "mtto_autonomo"
    respuesta = alert(content = MANTENIMIENTO_FORMS_REPORTES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_req_consumibles_click(self, **event_args):
    datos = self.datos
    datos['tipo'] = "requerimiento_consumibles"
    respuesta = alert(content = MANTENIMIENTO_FORMS_REPORTES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def actualizar_form_activo(self, datos, **event_args):
    datos['mes'] = self.drop_down_mes.selected_value
    datos['anio'] = self.drop_down_anio.selected_value
    datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    datos['modo'] = "dia"
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")
    if respuesta:
      self.llenar_calendario()

  def drop_down_equipo_change(self, **event_args):
    lista_hornos_calor = ["HORNO 1", "HORNO 4"]
    lista_hornos_luz = ["HORNO 1", "HORNO 2", "HORNO 3", "HORNO 4", "HORNO 5"]
    equipo_seleccionado = self.drop_down_equipo.selected_value if self.drop_down_equipo.selected_value != None else "default"
    
    self.drop_down_luz_resistencia.selected_value = None
    
    if equipo_seleccionado in lista_hornos_calor or equipo_seleccionado in lista_hornos_luz:
      items_luz_calor = []
      
      if equipo_seleccionado in lista_hornos_luz:
        items_luz_calor.append(("FOR-MAN-028 REPORTE DE MEDICIÓN DE INTENSIDAD DE LUZ UV","medicion_luz"))
      if equipo_seleccionado in lista_hornos_calor:
        items_luz_calor.append(("FOR-MAN-029 REPORTE DE MEDICIÓN DE RESISTENCIAS","medicion_resistencia"))

      items_luz_calor.append(("FOR-MAN-028 Y 029 MEDICIÓN DE LUZ UV Y RESISTENCIA (RESPUESTAS)","reporte_luz_resistencia"))        
      self.drop_down_luz_resistencia.items = items_luz_calor
      self.column_panel_luz_resistencia.visible = True
    else:
      self.column_panel_luz_resistencia.visible = False
      
    if equipo_seleccionado in self.url_imagenes_equipos:
      self.image_equipo.source = self.url_imagenes_equipos[equipo_seleccionado]
    else:
      self.image_equipo.source = self.url_imagenes_equipos["default"]

  def drop_down_luz_resistencia_change(self, **event_args):
    datos = self.datos
    datos['tipo'] = self.drop_down_luz_resistencia.selected_value
    datos['formularios'] = self.drop_down_luz_resistencia.items
    respuesta = alert(content = MANTENIMIENTO_FORMS_REPORTES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_inventario_click(self, **event_args):
    datos = self.datos
    datos['tipo'] = "inventario"
    respuesta = alert(content = MANTENIMIENTO_FORMS_REPORTES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")
      
