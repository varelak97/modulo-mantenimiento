from ._anvil_designer import lista_equiposTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class lista_equipos(lista_equiposTemplate):
  datos = {}
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.datos = datos

    print("entra a lista de equipos...")

    # Any code you write here will run before the form opens.
