from ._anvil_designer import opciones_inspeccionesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class opciones_inspecciones(opciones_inspeccionesTemplate):
  id_herramental = None
  status_reportes = None
  def __init__(self, id_herramental, status_reportes, **properties):
    self.init_components(**properties)
    self.id_herramental = id_herramental
    self.status_reportes = status_reportes
    self.set_config(status_reportes)

  ################################################# FUNCIONES PERSONALIZADAS #################################################
  def set_config(self, status_reportes):
    if status_reportes[0] == '1':
      self.button_visual_ver.foreground = app.theme_colors['Primary']
    else:
      self.button_visual_ver.foreground = app.theme_colors['LightGray']
    if status_reportes[1] == '1':
      self.button_dimensional_ver.foreground = app.theme_colors['Primary']
    else:
      self.button_dimensional_ver.foreground = app.theme_colors['LightGray']
    
  def abrir_form(self, modo):
    datos  = {
      'id_inspeccion': self.id_herramental,
      'modo': modo,
      'clave_form': 'FORM_INSPECCION_SUAJE'
    }
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_form', datos=datos)

  ########################################################## EVENTOS #########################################################

  def button_visual_editar_click(self, **event_args):
    if self.status_reportes[0] == '1' or self.status_reportes[1] == '1':
      self.abrir_form('edicion')
    else:
      self.abrir_form('nuevo')

  def button_visual_ver_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_dimensional_editar_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_dimensional_ver_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

