from ._anvil_designer import Form_Edicion_HerramentalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ... import Funciones_Globales


class Form_Edicion_Herramental(Form_Edicion_HerramentalTemplate):
  datos = None
  ws_herramentales = None
  ss_heramentales = None
  herramentales = None
  lista_componentes = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config()

    if self.datos['modo'] == "edicion":
      registro = Funciones_Globales.get_registro(self.datos['id_herramental'], 'id_herramental', self.herramentales)
      Funciones_Globales.fill_formulario(self.lista_componentes, registro)

  #################################################### FUNCIONES PERSONALIZADAS ####################################################
        
  def set_ini_config(self, datos):
    self.ws_herramentales = app_files.control_herramentales
    self.ss_heramentales = self.ws_herramentales['HERRAMENTALES']
    self.datos = datos

    self.lista_componentes = [
      self.text_box_codigo_herramental,
      self.text_area_descripcion,
      self.text_box_tipo_material,
      self.text_box_tipo_suaje,
      self.text_box_ubicacion,
      self.text_box_vida_util
    ]

    
