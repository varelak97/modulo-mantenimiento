from ._anvil_designer import MANTENIMIENTO_MENUTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil_extras import augment

class MANTENIMIENTO_MENU(MANTENIMIENTO_MENUTemplate):
  datos = None
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.datos = datos

    augment.set_event_handler(self.outlined_card_mantenimiento,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_mantenimiento,'mouseleave',self.set_color)
    #augment.set_event_handler(self.outlined_card_sistemas,'mouseenter',self.set_color)
    #augment.set_event_handler(self.outlined_card_sistemas,'mouseleave',self.set_color)
    augment.set_event_handler(self.outlined_card_herramentales,'mouseenter',self.set_color)
    augment.set_event_handler(self.outlined_card_herramentales,'mouseleave',self.set_color)

  ############################################################# FUNCIONES PERSONALIZADAS #############################################################
  def set_color(self,**event_args):
    card = event_args['sender']
    if 'enter' in event_args['event_type']:
      card.background = app.theme_colors['LightBlue']
    else:
      card.background = app.theme_colors['Background']

  def link_mantenimiento_click(self, **event_args):
    self.datos['clave_form'] = "MANTENIMIENTO_LISTA_EQUIPOS"
    self.link_herramentales.parent.parent.parent.parent.raise_event("x-actualizar_form_activo", datos = self.datos)

  def link_herramentales_click(self, **event_args):
    self.datos['clave_form'] = "MANTENIMIENTO_MENU_HERRAMENTALES"
    self.link_herramentales.parent.parent.parent.parent.raise_event("x-actualizar_form_activo", datos = self.datos)

  def link_sistemas_click(self, **event_args):
    self.datos['clave_form'] = "MANTENIMIENTO_SISTEMAS_MENU"
    self.link_herramentales.parent.parent.parent.parent.raise_event("x-actualizar_form_activo", datos = self.datos)
