from ._anvil_designer import MANTENIMIENTO_AUTONOMOTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil.js.window import jQuery
from anvil.js import get_dom_node

class MANTENIMIENTO_AUTONOMO(MANTENIMIENTO_AUTONOMOTemplate):
  datos = None
  iframe_size = "<iframe width='100%' height='800px'>"
  libro_lista_formularios = None
  ws_lista_formluarios = None
  lista_formularios = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos
    self.libro_lista_formularios = app_files.lista_mantenimiento_autonomo
    self.ws_lista_formluarios = self.libro_lista_formularios['LISTA']
    self.lista_formularios = self.ws_lista_formluarios.rows
    items_drop_dowm = []
    for formulario in self.lista_formularios:
      items_drop_dowm.append((formulario['nombre_formulario'],formulario['id_formulario']))
    self.drop_down_tipo.items = items_drop_dowm
    self.drop_down_tipo_change()
    #iframe = jQuery(self.iframe_size)#.attr("src",f"https://docs.google.com/spreadsheets/d/{self.id_respuestas}/edit?usp=sharing&embedded=true")
    #iframe.appendTo(get_dom_node(self.outlined_card_visor_google))
  #################################################### EVENTOS ####################################################
  def drop_down_tipo_change(self, **event_args):
    self.outlined_card_visor_google.clear()
    iframe = jQuery(self.iframe_size).attr("src",f"https://docs.google.com/forms/d/{self.drop_down_tipo.selected_value}/viewform?embedded=true")
    iframe.appendTo(get_dom_node(self.outlined_card_visor_google))
