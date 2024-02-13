from ._anvil_designer import MANTENIMIENTO_FORMS_REPORTESTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil.js.window import jQuery
from anvil.js import get_dom_node

class MANTENIMIENTO_FORMS_REPORTES(MANTENIMIENTO_FORMS_REPORTESTemplate):
  datos = None
  iframe_size = "<iframe width='100%' height='800px'>"
  libro_lista_formularios = None
  ws_lista_formluarios = None
  lista_formularios = []
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos
    print(f"datos recibidos:{self.datos['tipo']}")
    self.libro_lista_formularios = app_files.lista_mantenimiento_autonomo
    self.ws_lista_formluarios = self.libro_lista_formularios['LISTA']
    selected_item = None
    
    if self.datos['tipo'] == "mtto_autonomo":
      for item in self.ws_lista_formluarios.rows:
        if item['tipo'] == "mtto_autonomo":
          self.lista_formularios.append(item)
    else:
      registros_formularios = self.ws_lista_formluarios.rows
      for nombre_form in self.datos['formularios']:
        for formulario in registros_formularios:
          if nombre_form[1] == formulario['tipo']:
            self.lista_formularios.append(formulario)
          if datos['tipo'] == formulario['tipo']:
            selected_item = formulario['nombre_formulario']
    items_drop_dowm = []
    for formulario in self.lista_formularios:
      url = None
      if formulario['formato'] == "form":
        url = f"https://docs.google.com/forms/d/{formulario['id_formulario']}/viewform?embedded=true"
      elif formulario['formato'] == "sheet":
        url = ""
      items_drop_dowm.append((formulario['nombre_formulario'],url))
    self.drop_down_tipo.items = items_drop_dowm
    if selected_item != None:
      print(f"item seleccionado:{selected_item}")
      self.drop_down_tipo.selected_value = selected_item
    self.drop_down_tipo_change()
    #iframe = jQuery(self.iframe_size)#.attr("src",f"https://docs.google.com/spreadsheets/d/{self.id_respuestas}/edit?usp=sharing&embedded=true")
    #iframe.appendTo(get_dom_node(self.outlined_card_visor_google))
  #################################################### EVENTOS ####################################################
  def drop_down_tipo_change(self, **event_args):
    self.outlined_card_visor_google.clear()
    iframe = jQuery(self.iframe_size).attr("src",self.drop_down_tipo.selected_value)
    iframe.appendTo(get_dom_node(self.outlined_card_visor_google))
