from ._anvil_designer import Form_Inspeccion_visualTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class Form_Inspeccion_visual(Form_Inspeccion_visualTemplate):
  ws_herramentales = None
  ss_reporte_suajes = None
  reporte_suajes = None
  ss_vista_suaje = None
  vista_suaje = None
  datos = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.get_datos()
    
  ############################################# FUNCIONES PERSONALIZADAS #############################################
  def set_ini_config(self, datos):
    self.datos = datos
    self.ws_herramentales = app_files.control_herramentales
    self.ss_reporte_suajes = self.ws_herramentales['REVISION_SUAJE']
    self.ss_vista_suaje = self.ws_herramentales['VISTA_HERRAMENTALES']

  def get_datos(self):
    if self.datos['modo'] == 'edicion':
      self.reporte_suajes = self.ss_reporte_suajes.rows
    self.vista_suaje = self.ss_vista_suaje.rows
    for suaje in self.vista_suaje:
      if suaje['id_herramental'] == self.datos['id_herramental']:
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
