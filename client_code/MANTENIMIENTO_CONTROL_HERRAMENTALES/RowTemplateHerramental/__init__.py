from ._anvil_designer import RowTemplateHerramentalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..opciones_herramentales import opciones_herramentales


class RowTemplateHerramental(RowTemplateHerramentalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.button_editar.popover(content=opciones_herramentales(self.button_editar.tag),title=self.label_codigo_herramental.text, trigger="click",max_width="450px")

  def button_ver_click(self, **event_args):
    datos = {
      "id_herramental": self.button_editar.tag,
      "codigo_herramental": self.label_codigo_herramental.text,
      "clave_form": "REGISTROS_HERRAMENTAL"
    }
    print(self.button_editar.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_form', datos=datos))
    #abrir herramental

