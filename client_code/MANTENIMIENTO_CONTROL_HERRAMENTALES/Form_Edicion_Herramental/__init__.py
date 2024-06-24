from ._anvil_designer import Form_Edicion_HerramentalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class Form_Edicion_Herramental(Form_Edicion_HerramentalTemplate):
  lista_componentes = None
  datos = None
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  ################################################### FUNCIONES PERSONALIZADAS ###################################################

  ############################################################ EVENTOS ###########################################################
