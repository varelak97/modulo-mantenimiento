from ._anvil_designer import RowTemplate12Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class RowTemplate12(RowTemplate12Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    #self.button_editar.popover(content=opciones_edicion(self.button_editar.tag, self.label_status.tag, id_usuario_erp),title=self.label_equipo.text, trigger="click",max_width="450px")
