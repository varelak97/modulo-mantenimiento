from ._anvil_designer import MANTENIMIENTO_AUTONOMO_copyTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil.js.window import jQuery
from anvil.js import get_dom_node

class MANTENIMIENTO_AUTONOMO_copy(MANTENIMIENTO_AUTONOMO_copyTemplate):
  datos = None
  id_respuestas = "1Z5ARoekL1Ion2yieVu4InueSgfIEUNvME99TtrB3I-4" # FOR-MAN-006 (REQUERIMIENTO DE CONSUMIBLES) Y FOR-MAN-008(VERIFICACIÓN DE MANTENIMIENTO AUTONOMO)
  id_verificacion_mtto_autonomo = "1QvSQLXGmQO363Vy9YwhmimKXSMNaH0z1I7PauPuCvIs" #FORM-MAN-006 VERIFICACIONES DE MANTENIMIENTO AUTÓNOMO
  id_requerimiento_comsumibles = "1pv78MjKT9njCWzzyH8t4c2prlR9voh0hXA_k7Vb4txI" #FOR-MAN-008 REQUERIMIENTO DE CONSUMIBLES
  iframe_size = "<iframe width='100%' height='800px'>"


  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos
    iframe = jQuery(self.iframe_size).attr("src",f"https://docs.google.com/spreadsheets/d/{self.id_respuestas}/edit?usp=sharing&embedded=true")
    iframe.appendTo(get_dom_node(self.outlined_card_visor_google))

  #################################################### EVENTOS ####################################################
  def drop_down_tipo_change(self, **event_args):
    if self.drop_down_tipo.selected_value == "FOR-MAN-006 REQUERIMIENTO DE CONSUMIBLES":
      self.outlined_card_visor_google.clear()
      iframe = jQuery(self.iframe_size).attr("src",f"https://docs.google.com/forms/d/{self.id_requerimiento_comsumibles}/viewform?embedded=true")
      iframe.appendTo(get_dom_node(self.outlined_card_visor_google))
    elif self.drop_down_tipo.selected_value == "FOR-MAN-008 VERIFICACIONES DE MANTENIMIENTO AUTÓNOMO":
      self.outlined_card_visor_google.clear()
      iframe = jQuery(self.iframe_size).attr("src",f"https://docs.google.com/forms/d/{self.id_verificacion_mtto_autonomo}/viewform?embedded=true")
      iframe.appendTo(get_dom_node(self.outlined_card_visor_google))
    elif self.drop_down_tipo.selected_value == "RESPUESTAS FORM-MAN-006 Y FORM-MAN-008":
      self.outlined_card_visor_google.clear()
      iframe = jQuery(self.iframe_size).attr("src",f"https://docs.google.com/spreadsheets/d/{self.id_respuestas}/edit?usp=sharing&embedded=true")
      iframe.appendTo(get_dom_node(self.outlined_card_visor_google))
