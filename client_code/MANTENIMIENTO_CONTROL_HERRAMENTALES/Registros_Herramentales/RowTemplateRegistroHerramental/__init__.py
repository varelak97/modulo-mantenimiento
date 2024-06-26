from ._anvil_designer import RowTemplateRegistroHerramentalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class RowTemplateRegistroHerramental(RowTemplateRegistroHerramentalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_status_click(self, **event_args):
    if int(self.item['status']) == 0:
      respuesta = alert("¿Confirma que desea marcar como terminado?", title="CONFIRMACIÓN", buttons=(("ACEPTAR", True),("CANCELAR", False)))
      if respuesta:
        datos = {}
        datos['id_registro'] = self.button_editar.tag
        #alert(f"el parent:{self.parent.parent.parent.parent.parent} ---- id_registro:{self.button_editar.tag}")
        self.parent.parent.parent.parent.parent.raise_event("x-actualizar_status",datos = datos)
        
