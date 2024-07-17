from ._anvil_designer import Form_Inspeccion_visualTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ... import Funciones_Globales

class Form_Inspeccion_visual(Form_Inspeccion_visualTemplate):
  ws_herramentales = None
  ss_reporte_suajes = None
  reporte_suajes = None
  registro_actual = {}
  datos = None
  lista_componentes = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.get_datos()
    
  ############################################# FUNCIONES PERSONALIZADAS #############################################
  def set_ini_config(self, datos):
    self.datos = datos
    self.ws_herramentales = app_files.control_herramentales
    self.ss_reporte_suajes = self.ws_herramentales['REVISION_SUAJE']
    self.lista_componentes = [
      self.label_cliente,
      self.label_codigo_suaje,
      self.label_tipo_suaje,
      self.text_box_revisor,
      self.text_area_filo,
      self.text_area_union,
      self.text_area_estado,
      self.button_filo_bien,
      self.button_filo_mal,
      self.button_union_bien,
      self.button_union_mal,
      self.button_estado_bien,
      self.button_estado_mal
    ]

  def get_datos(self):
    if self.datos['modo'] == 'edicion':
      self.reporte_suajes = self.ss_reporte_suajes.rows
      for row in self.reporte_suajes:
        if self.datos['id_inspeccion'] == row['id_inspeccion']:
          self.registro_actual = row
          break
      Funciones_Globales.fill_formulario(datos,self.registro_actual, None)
    else:
      self.label_cliente.text = self.datos['cliente']
      self.label_codigo_suaje.text = self.datos['codigo_suaje']
      self.label_tipo_suaje.text = self.datos['tipo_suaje']

  def fill_form(self, registro):
    pass
    
    
  ###################################################### EVENTOS #####################################################

  def button_filo_bien_click(self, **event_args):
    self.button_filo_bien.background = app.theme_colors['Primary']
    self.button_filo_bien.foreground = app.theme_colors['On Primary']
    
    self.button_filo_mal.background = app.theme_colors['LightGray']
    self.button_filo_mal.foreground = app.theme_colors['Secondary']

  def button_filo_mal_click(self, **event_args):
    self.button_filo_bien.background = app.theme_colors['LightGray']
    self.button_filo_bien.foreground = app.theme_colors['Secondary']
    
    self.button_filo_mal.background = app.theme_colors['Red']
    self.button_filo_mal.foreground = app.theme_colors['On Primary']

  def button_union_bien_click(self, **event_args):
    self.button_union_bien.background = app.theme_colors['Primary']
    self.button_union_bien.foreground = app.theme_colors['On Primary']
    
    self.button_union_mal.background = app.theme_colors['LightGray']
    self.button_union_mal.foreground = app.theme_colors['Secondary']

  def button_union_mal_click(self, **event_args):
    self.button_union_bien.background = app.theme_colors['LightGray']
    self.button_union_bien.foreground = app.theme_colors['Secondary']
    
    self.button_union_mal.background = app.theme_colors['Red']
    self.button_union_mal.foreground = app.theme_colors['On Primary']

  def button_estado_bien_click(self, **event_args):
    self.button_estado_bien.background = app.theme_colors['Primary']
    self.button_estado_bien.foreground = app.theme_colors['On Primary']
    
    self.button_estado_mal.background = app.theme_colors['LightGray']
    self.button_estado_mal.foreground = app.theme_colors['Secondary']

  def button_estado_mal_click(self, **event_args):
    self.button_estado_bien.background = app.theme_colors['LightGray']
    self.button_estado_bien.foreground = app.theme_colors['Secondary']
    
    self.button_estado_mal.background = app.theme_colors['Red']
    self.button_estado_mal.foreground = app.theme_colors['On Primary']
