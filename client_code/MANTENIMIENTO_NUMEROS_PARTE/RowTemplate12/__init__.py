from ._anvil_designer import RowTemplate12Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class RowTemplate12(RowTemplate12Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_editar_click(self, **event_args):
    datos = {}
    datos['id_numero_parte'] = self.button_editar.tag
    datos['modo'] = "edicion"
    datos['clave_form'] = 'FORM_NUMERO_PARTE'
    self.button_editar.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_form', datos=datos)
