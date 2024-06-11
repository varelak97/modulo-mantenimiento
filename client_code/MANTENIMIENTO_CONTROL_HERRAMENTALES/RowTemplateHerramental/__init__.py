from ._anvil_designer import RowTemplateHerramentalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class RowTemplateHerramental(RowTemplateHerramentalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    #self.button_editar.popover(content=opciones_edicion(self.button_editar.tag, self.label_status.tag, id_usuario_erp),title=self.label_equipo.text, trigger="click",max_width="450px")
