from ._anvil_designer import RowTemplateCheckTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
from ...MANTENIMIENTO_FORMS_REPORTES import MANTENIMIENTO_FORMS_REPORTES

class RowTemplateCheck(RowTemplateCheckTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  """def radio_button_si_clicked(self, **event_args):
    #print(self.parent.parent.parent.parent.parent.parent.parent.repeating_panel_registros.items)
    fila = {}
    fila['id'] = self.tag
    fila['tipo'] = "si"
    fila['check'] = self.radio_button_si.selected
    self.parent.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_checklist',fila=fila)"""

  def radio_button_si_clicked(self, **event_args):
    if self.label_actividad.text == "MEDICIÓN DE INTENSIDAD DE LUZ":
      datos = {}
      datos['tipo'] = "medicion_luz"
      datos['formularios'] = [("FOR-MAN-028 REPORTE DE MEDICIÓN DE INTENSIDAD DE LUZ UV","medicion_luz")]
      respuesta = alert(content = MANTENIMIENTO_FORMS_REPORTES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")
    elif self.label_actividad.text == "MEDICIÓN DE RESISTENCIA":
      datos = {}
      datos['tipo'] = "medicion_resistencia"
      datos['formularios'] = [("FOR-MAN-029 REPORTE DE MEDICIÓN DE RESISTENCIAS","medicion_resistencia")]
      respuesta = alert(content = MANTENIMIENTO_FORMS_REPORTES(datos), large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content-bigger")

