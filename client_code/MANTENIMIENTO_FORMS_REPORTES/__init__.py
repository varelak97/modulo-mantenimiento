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
  ws_lista_formularios = None
  registros_lista_formularios = None
  lista_formularios = None
  #target = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos
    self.lista_formularios = []
    self.libro_lista_formularios = app_files.lista_mantenimiento_autonomo
    self.ws_lista_formularios = self.libro_lista_formularios['LISTA']
    self.registros_lista_formularios = self.ws_lista_formularios.rows
    selected_item = None
    #self.target = ColumnPanel(role="elevated-card")
    
    if self.datos['tipo'] == "mtto_autonomo":
      for item in self.registros_lista_formularios:
        if item['tipo'] == "mtto_autonomo":
          self.lista_formularios.append(item)
    elif self.datos['tipo'] == "requerimiento_consumibles":
      for item in self.registros_lista_formularios:
        if item['tipo'] == "requerimiento_consumibles":
          self.lista_formularios.append(item)
    else:
      self.label_titulo.text = "REPORTE DE MEDICIÓN DE INTENSIDAD DE LUZ UV Y RESISTENCIAS"
      for nombre_form in self.datos['formularios']:
        for formulario in self.registros_lista_formularios:
          if nombre_form[1] == formulario['tipo']:
            print(f"agrega:{formulario}")
            self.lista_formularios.append(formulario)
    items_drop_dowm = []
    for formulario in self.lista_formularios:
      url = None
      if formulario['formato'] == "form":
        url = f"https://docs.google.com/forms/d/{formulario['id_formulario']}/viewform?embedded=true"
      elif formulario['formato'] == "sheet":
        url = f"https://docs.google.com/spreadsheets/d/{formulario['id_formulario']}/edit?usp=sharing&embedded=true"
      items_drop_dowm.append((formulario['nombre_formulario'],url))
      if self.datos['tipo'] == formulario['tipo']:#datos['tipo'] != "mtto_autonomo" and datos['tipo'] == formulario['tipo']:
        selected_item = url
        """if formulario['formato'] == "form":
          self.content_panel.add_component(self.target, full_width_row=False)
        elif formulario['formato'] == "sheet":
          self.content_panel.add_component(self.target, full_width_row=True)"""
        
    self.drop_down_tipo.items = items_drop_dowm
    if selected_item != None:
      self.drop_down_tipo.selected_value = selected_item
    self.drop_down_tipo_change()
    #iframe = jQuery(self.iframe_size)#.attr("src",f"https://docs.google.com/spreadsheets/d/{self.id_respuestas}/edit?usp=sharing&embedded=true")
    #iframe.appendTo(get_dom_node(self.outlined_card_visor_google))
  #################################################### EVENTOS ####################################################
  def drop_down_tipo_change(self, **event_args):
    self.outlined_card_visor_google.clear()
    iframe = jQuery(self.iframe_size).attr("src",self.drop_down_tipo.selected_value)
    iframe.appendTo(get_dom_node(self.outlined_card_visor_google))
    #iframe.appendTo(get_dom_node(self.target))
