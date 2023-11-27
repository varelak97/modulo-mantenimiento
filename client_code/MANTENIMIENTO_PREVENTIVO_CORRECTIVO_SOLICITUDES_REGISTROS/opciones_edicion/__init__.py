from ._anvil_designer import opciones_edicionTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class opciones_edicion(opciones_edicionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_ver_reporte_click(self, **event_args):
    alert("click en ver reporte")
    """datos = {}
    datos['id_mtto_preventivo_correctivo'] = self.id_mtto
    datos['modo'] = "visor"
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_reporte', datos=datos)"""

  def button_editar_reporte_click(self, **event_args):
    alert("click en editar reporte")
    """datos = {}
    datos['id_mtto_preventivo_correctivo'] = self.id_mtto
    datos['modo'] = "editor"
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_reporte', datos=datos)"""
