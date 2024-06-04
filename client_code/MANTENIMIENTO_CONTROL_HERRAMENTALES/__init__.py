from ._anvil_designer import MANTENIMIENTO_CONTROL_HERRAMENTALESTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil_extras import popover


class MANTENIMIENTO_CONTROL_HERRAMENTALES(MANTENIMIENTO_CONTROL_HERRAMENTALESTemplate):
  datos = None
  ws_herramentales = None
  ss_herramentales = None
  herramentales = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    datos = self.datos
    
    self.ws_herramentales = app_files.control_herramentales
    self.ss_herramentales = self.ws_herramentales['VISTA_HERRAMENTALES']

    
    
    self.button_actualizar_click()

  def button_actualizar_click(self, **event_args):
    self.herramentales = self.ss_herramentales.rows
    self.repeating_panel_herramentales.items = self.herramentales
