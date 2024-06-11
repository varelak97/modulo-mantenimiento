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

    self.button_editar.popover(content=opciones_herramentales(self.button_editar.tag),title=self.label_equipo.text, trigger="click",max_width="450px")
