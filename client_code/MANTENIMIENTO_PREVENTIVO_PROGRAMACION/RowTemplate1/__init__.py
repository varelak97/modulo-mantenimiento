from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_editar_click(self, **event_args):
    if self.button_editar.icon == "fa:edit":
      self.label_fecha_inicial.visible = False
      self.label_fecha_final.visible = False
      self.date_picker_fecha_inicial.visible = True
      self.date_picker_fecha_final.visible = True
      self.parent.parent.parent.parent.parent.raise_event('x-editar_fecha_excluida')
      self.button_editar.enabled = True
      self.button_editar.icon = "fa:check"
    else:
      self.label_fecha_inicial.visible = True
      self.label_fecha_final.visible = True
      self.date_picker_fecha_inicial.visible = False
      self.date_picker_fecha_final.visible = False
      self.button_editar.icon = "fa:edit"
      self.parent.parent.parent.parent.parent.raise_event('x-guardar_fecha_excluida')

  def button_borrar_click(self, **event_args):
    indice = int(self.label_index.text) - 1
    self.parent.parent.parent.parent.parent.raise_event('x-eliminar_fecha_excluida', indice = indice)