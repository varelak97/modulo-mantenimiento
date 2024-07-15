from ._anvil_designer import RowTemplate13Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class RowTemplate13(RowTemplate13Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  ####################################################### EVENTOS #######################################################
  def button_borrar_click(self, **event_args):
    datos = {}
    datos['id_herramental'] = self.button_borrar.tag
    datos['llave'] = 'id_herramental'
    datos['repeating_panel'] = self.parent
    self.button_borrar.parent.parent.parent.parent.parent.parent.raise_event('x-borrar_item', datos=datos)
