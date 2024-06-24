from ._anvil_designer import Form_Edicion_HerramentalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class Form_Edicion_Herramental(Form_Edicion_HerramentalTemplate):
  lista_componentes = None
  datos = None
  ws_control_herramentales = None
  ss_vista_numeros_parte = None
  numeros_parte = None
  ss_registros = None
  registros = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)

    self.datos = datos
    self.get_data()
    

  ################################################### FUNCIONES PERSONALIZADAS ###################################################
  def get_data(self):
    self.ws_control_herramentales = app_files.control_herramentales
    self.ss_vista_numeros_parte = self.ws_control_herramentales['VISTA_NUMEROS_PARTE']
    self.registros = self.ss_vista_numeros_parte.rows
    self.ss_registros = self.ws_control_herramentales['VISTA_REGISTROS']
    self.registros = self.ss_registros.rows

    lista_numeros_parte = []
    for numero_parte in self.ss_vista_numeros_parte:
      lista_numeros_parte.append((numero_parte['numero_parte'], numero_parte['tipo_corte']))
    print(lista_numeros_parte)
  ############################################################ EVENTOS ###########################################################
