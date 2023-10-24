from ._anvil_designer import RowTemplateEditarTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ...MANTENIMIENTO_PREVENTIVO_CHECKLIST import MANTENIMIENTO_PREVENTIVO_CHECKLIST

class RowTemplateEditar(RowTemplateEditarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_editar_click(self, **event_args):
    datos = {}
    botones = None
    if self.label_status.text == "REALIZADO":
      botones = [("VER CHECKLIST","ver_checklist")]
    else:
      botones = [("REALIZAR CHECKLIST","checklist"),("REPROGRAMAR","reprogramar")]
    respuesta = alert(title=self.label_equipo.text,buttons=botones)
    if respuesta == "checklist":
      datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CHECKLIST'
      datos['id_mtto_preventivo'] = self.button_editar.tag
      datos['modo'] = "checklist"
      self.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo',datos=datos)
    elif respuesta == "ver_checklist":
      datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CHECKLIST'
      datos['id_mtto_preventivo'] = self.button_editar.tag
      datos['modo'] = "ver_checklist"
      self.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo',datos=datos)
    elif respuesta == "reprogramar":
      datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_PROGRAMACION'
      datos['modo'] = "reprogramar"
      
    datos['id_mtto_preventivo'] = self.button_editar.tag
    self.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo',datos=datos)

