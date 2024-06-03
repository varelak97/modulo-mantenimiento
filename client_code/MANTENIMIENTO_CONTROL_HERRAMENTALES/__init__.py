from ._anvil_designer import MANTENIMIENTO_CONTROL_HERRAMENTALESTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class MANTENIMIENTO_CONTROL_HERRAMENTALES(MANTENIMIENTO_CONTROL_HERRAMENTALESTemplate):
  datos = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    datos = self.datos
