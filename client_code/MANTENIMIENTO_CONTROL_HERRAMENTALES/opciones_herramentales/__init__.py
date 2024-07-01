from ._anvil_designer import opciones_herramentalesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class opciones_herramentales(opciones_herramentalesTemplate):
  id_herramental = None
  def __init__(self, id_herramental, **properties):
    self.init_components(**properties)
    self.id_herramental = id_herramental

  def button_editar_click(self, **event_args):
    datos  = {
      'id_herramental': self.id_herramental,
      'modo': 'edicion',
      'clave_form': 'FORM_HERRAMENTAL'
    }
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_form', datos=datos)
    
