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
      self.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo',datos=datos)
      
      #################regresar###################
      """ datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CHECKLIST'
      datos['id_mtto_preventivo'] = self.button_editar.tag
      datos['actividades'] = self.tag
      datos['equipo'] = self.label_equipo.text
      resp = alert(content = MANTENIMIENTO_PREVENTIVO_CHECKLIST(datos), buttons = [("REGRESAR","REGRESAR")], large=True, dismissible=False)
      if resp:
        print("lo hizo")"""
    elif respuesta == "reprogramar":
      self.parent.parent.parent.parent.parent.raise_event('x-editar_registro',orden_compra=po)
    elif respuesta == "ver_checklist":
      pass

