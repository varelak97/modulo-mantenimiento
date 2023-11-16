from ._anvil_designer import RowTemplateComentariosTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class RowTemplateComentarios(RowTemplateComentariosTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  #################################################### EVENTOS ####################################################
  def button_editar_click(self, **event_args):
    indice = int(self.label_index.text)
    self.parent.parent.parent.parent.parent.parent.raise_event('x-editar_comentario', indice = indice)