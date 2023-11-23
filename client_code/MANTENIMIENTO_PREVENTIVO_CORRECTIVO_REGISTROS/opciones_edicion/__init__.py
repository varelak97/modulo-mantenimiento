from ._anvil_designer import opciones_edicionTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class opciones_edicion(opciones_edicionTemplate):
  id_mtto = None
  def __init__(self, id_mtto, **properties):
    self.init_components(**properties)
    self.id_mtto = id_mtto

  def button_ver_reporte_click(self, **event_args):
    datos = {}
    datos['id_mtto_preventivo_correctivo'] = self.id_mtto
    self.popper.parent.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_reporte', datos=datos)

  def button_editar_reporte_click(self, **event_args):
    alert(f"id:{self.id_mtto}")
    

