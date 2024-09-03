from ._anvil_designer import opciones_inspeccionesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class opciones_inspecciones(opciones_inspeccionesTemplate):
  datos = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos
    self.set_config()

  ################################################# FUNCIONES PERSONALIZADAS #################################################
  def set_config(self):
    if self.datos['id_inspeccion'] is None:
      self.button_visual_ver.foreground = app.theme_colors['LightGray']
    else:
    
      pass
    
    if self.datos['status_visual'] == '1':
      self.button_visual_ver.foreground = app.theme_colors['Primary']
    else:
      self.button_visual_ver.foreground = app.theme_colors['LightGray']
    if self.datos['status_dimensional'] == '1':
      self.button_dimensional_ver.foreground = app.theme_colors['Primary']
    else:
      self.button_dimensional_ver.foreground = app.theme_colors['LightGray']
    
  def abrir_form(self, modo, clave_form):
    datos  = {
      'id_inspeccion': self.id_herramental,
      'modo': modo,
      'clave_form': clave_form
    }
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_form', datos=datos)

  ########################################################## EVENTOS #########################################################

  def button_visual_editar_click(self, **event_args):
    if self.datos['id_inspeccion'] is None:
      self.abrir_form('nuevo_reg_insp', 'FORM_INSPECCION_VISUAL')
    else:
      if self.datos['status_visual'] == '0':
        self.abrir_form('nuevo_insp', 'FORM_INSPECCION_VISUAL')
      else:
        self.abrir_form('edicion', 'FORM_INSPECCION_VISUAL')

  def button_visual_ver_click(self, **event_args):
    if self.datos['inspeccion_visual'] == '1':
      self.abrir_form('visor', 'FORM_INSPECCION_VISUAL')

  def button_dimensional_editar_click(self, **event_args):
    if self.datos['id_inspeccion'] is None:
      self.abrir_form('nuevo_reg_inps', 'FORM_INSPECCION_DIMENSIONAL')
    else:
      if self.datos['status_visual'] == '0':
        self.abrir_form('nuevo_insp', 'FORM_INSPECCION_DIMENSIONAL')
      else:
        self.abrir_form('edicion', 'FORM_INSPECCION_DIMENSIONAL')

  def button_dimensional_ver_click(self, **event_args):
    if self.datos['inspeccion_dimensional'] == '1':
      self.abrir_form('visor', 'FORM_INSPECCION_DIMENSIONAL')

