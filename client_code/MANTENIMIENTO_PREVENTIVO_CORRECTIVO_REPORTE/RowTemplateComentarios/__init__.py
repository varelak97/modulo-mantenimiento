from ._anvil_designer import RowTemplateComentariosTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class RowTemplateComentarios(RowTemplateComentariosTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
 
  #################################################### EVENTOS ####################################################
  def button_editar_click(self, **event_args):
    self.column_panel_comentario.visible = True
    self.label_comentario.visible = False
    self.parent.parent.parent.parent.parent.parent.parent.raise_event('x-editar_comentario')

  def button_guardar_click(self, **event_args):
    datos = {}
    datos['indice'] = int(self.label_index.text) - 1
    datos['comentario'] = self.text_area_comentario.text
    self.parent.parent.parent.parent.parent.parent.parent.raise_event('x-guardar_comentario', datos = datos)
    self.button_borrar.enabled = True
    self.button_editar.enabled = True

  def button_borrar_click(self, **event_args):
    indice = int(self.label_index.text) - 1
    self.parent.parent.parent.parent.parent.parent.parent.raise_event('x-eliminar_comentario', indice = indice)
