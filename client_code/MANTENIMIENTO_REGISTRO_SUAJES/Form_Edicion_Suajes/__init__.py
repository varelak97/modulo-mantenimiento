from ._anvil_designer import Form_Edicion_SuajesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ... import Funciones_Globales
from datetime import datetime, date


class Form_Edicion_Suajes(Form_Edicion_SuajesTemplate):
  lista_input_components = None
  datos = None
  ws_control_herramentales = None
  ss_vista_numeros_parte = None
  numeros_parte = None
  ss_registros = None
  registros = None
  campos_no_obligatorios = []
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)

    self.lista_input_components = [
      self.date_picker_fecha_programada,
      self.drop_down_numeros_parte,
      self.text_box_tipo_suaje,
      self.text_box_suajes_programados
    ]

    self.datos = datos
    self.get_data()

  ################################################### FUNCIONES PERSONALIZADAS ###################################################
  def get_data(self):
    self.ws_control_herramentales = app_files.control_herramentales
    self.ss_vista_numeros_parte = self.ws_control_herramentales['VISTA_NUMEROS_PARTE']
    self.numeros_parte = self.ss_vista_numeros_parte.rows
    self.ss_registros = self.ws_control_herramentales['REGISTROS']
    self.registros = self.ss_registros.rows

    lista_numeros_parte = []
    for numero_parte in self.numeros_parte:
      if int(self.datos['id_herramental']) in eval(numero_parte['id_herramentales']):
        lista_numeros_parte.append((numero_parte['numero_parte'], numero_parte['id_numero_parte']))
    self.drop_down_numeros_parte.items = lista_numeros_parte
    self.text_box_tipo_suaje.text = self.datos['tipo_suaje']
    
  ############################################################ EVENTOS ###########################################################
  def button_guardar_click(self, **event_args):
    status = Funciones_Globales.validar_campos(self.lista_input_components, None, self.campos_no_obligatorios, self.datos['modo'])
    if status == 1:
      dicc_datos = Funciones_Globales.genera_diccionario(self.lista_input_components)
      dicc_datos['id_numero_parte'] = dicc_datos['id_numero_parte'][0]
      dicc_datos['id_registro'] = (max([int(item['id_registro']) for item in self.registros]) + 1) if len(self.registros) > 0 else 0
      dicc_datos['status'] = 0
      dicc_datos['id_herramental'] = self.datos['id_herramental']
      dicc_datos['registro_principal'] = 1
      dicc_datos['id_usuario_registrador'] = self.datos['id_usuario_erp']
      dicc_datos['comentarios'] = "Alta"
      dicc_datos['marca_temporal'] = datetime.now()
      status = ""
      if self.datos['modo'] == "edicion":
        
        status = "registro_actualizado"
      elif self.datos['modo'] == "nuevo":
        self.ss_registros.add_row(**dicc_datos)
        status = "registro_guardado"
      self.raise_event("x-close-alert",value=status)
    elif status == 2:
      alert("No hay cambios que guardar.", title="ERROR!")
    elif status == 3:
      alert("faltan campos por llenar!", title="ERROR!")

    
