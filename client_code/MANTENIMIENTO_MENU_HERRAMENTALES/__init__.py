from ._anvil_designer import MANTENIMIENTO_MENU_HERRAMENTALESTemplate
from anvil import *
import anvil.server
from anvil_extras import augment
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..MANTENIMIENTO_CONTROL_SUAJES import MANTENIMIENTO_CONTROL_SUAJES
from ..MANTENIMIENTO_REGISTRO_SUAJES import MANTENIMIENTO_REGISTRO_SUAJES
from ..MANTENIMIENTO_NUMEROS_PARTE import MANTENIMIENTO_NUMEROS_PARTE


class MANTENIMIENTO_MENU_HERRAMENTALES(MANTENIMIENTO_MENU_HERRAMENTALESTemplate):
  datos = None
  usuarios_autorizados = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos

    self.usuarios_autorizados = [58, 884]

    augment.set_event_handler(self.outlined_card_registros_suaje,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_registros_suaje,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_numeros_parte,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_numeros_parte,'mouseleave',self.set_color)
    if self.datos['id_usuario_erp'] in self.usuarios_autorizados:
      augment.set_event_handler(self.outlined_card_control_suajes,'mouseenter',self.set_color)
      augment.set_event_handler(self.outlined_card_control_suajes,'mouseleave',self.set_color)

  ############################################# FUNCIONES PERSONALIZADAS #############################################
  def set_color(self,**event_args):
    card = event_args['sender']
    if 'enter' in event_args['event_type']:
      card.background = app.theme_colors['LightBlue']
    else:
      card.background = app.theme_colors['Background']

  ##################################################### EVENTOS #####################################################
  def link_numeros_parte_click(self, **event_args):
    datos = self.datos
    datos['modo'] = "todos"
    respuesta = alert(content = MANTENIMIENTO_NUMEROS_PARTE(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_registros_suaje_click(self, **event_args):
    datos = self.datos
    datos['modo'] = "todos"
    respuesta = alert(content = MANTENIMIENTO_REGISTRO_SUAJES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

  def link_control_suajes_click(self, **event_args):
    if self.datos['id_usuario_erp'] in self.usuarios_autorizados:
      datos = self.datos
      datos['modo'] = "todos"
      respuesta = alert(content = MANTENIMIENTO_CONTROL_SUAJES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")
