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
    id_herramental = self.button_borrar.tag
    self.button_borrar.parent.parent.parent.parent.parent.parent.raise_event('x-borrar_item', id_herramental=id_herramental)
    #.raise_event('x-abrir_form', datos=datos)
    pass
