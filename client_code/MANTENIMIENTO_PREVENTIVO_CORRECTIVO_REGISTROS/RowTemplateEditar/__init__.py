from ._anvil_designer import RowTemplateEditarTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..opciones_edicion import opciones_edicion

class RowTemplateEditar(RowTemplateEditarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.button_editar.popover(content=opciones_edicion(self.button_editar.tag),title=self.label_equipo.text, trigger="click",max_width="450px")

  def llena_comentarios(self, comentarios):
    texto = ""
    if comentarios != "":
      for comentario in eval(comentarios):
        texto += comentario['comentario']
        texto += '\n'
    return texto

  def link_fotos_click(self, **event_args):
    if self.label_fotos.text != "NA":
      js.call('openURL', self.link_fotos.tag)
