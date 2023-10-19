from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROSTemplate):
  datos = {}
  libro_solicitudes_mtto = None
  ws_consulta_solicitudes_mtto = None
  registros_consulta_mtto = None
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.datos = datos
    self.libro_solicitudes_mtto = app_files.mantenimiento_solicitudes
    self.ws_consulta_solicitudes_mtto = self.libro_solicitudes_mtto['Consulta']
    self.registros_consulta_mtto = self.ws_consulta_solicitudes_mtto.rows
    print(f"los registros:{self.registros_consulta_mtto}")
    self.repeating_panel_registros.items = self.registros_consulta_mtto
