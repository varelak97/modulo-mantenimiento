from ._anvil_designer import opciones_inspeccionesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class opciones_inspecciones(opciones_inspeccionesTemplate):
  id_inspeccion = None
  modo = None
  def __init__(self, id_inspeccion, modo, **properties):
    self.init_components(**properties)
    self.id_inspeccion = id_inspeccion
    self.modo = modo

  ################################################# FUNCIONES PERSONALIZADAS #################################################
  def abrir_form(self, modo, clave_form):
    datos  = {
      'id_inspeccion': self.id_inspeccion,
      'modo': modo,
      'clave_form': 'FORM_INSPECCION_SUAJE'
    }
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_form', datos=datos)

  ########################################################## EVENTOS #########################################################
  def button_editar_click(self, **event_args):
    self.abrir_form('edicion')

  def button_ver_click(self, **event_args):
    self.abrir_form('visor')

  def button_visual_click(self, **event_args):
    self.abrir_form('edicion')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
