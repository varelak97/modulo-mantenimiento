from ._anvil_designer import RowTemplateCheckTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class RowTemplateCheck(RowTemplateCheckTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def radio_button_si_clicked(self, **event_args):
    #print(self.parent.parent.parent.parent.parent.parent.parent.repeating_panel_registros.items)
    fila = {}
    fila['id'] = self.tag
    fila['tipo'] = "si"
    fila['check'] = self.radio_button_si.selected
    self.parent.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_checklist',fila=fila)

