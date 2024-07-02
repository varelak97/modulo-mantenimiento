from ._anvil_designer import Form_Edicion_HerramentalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ... import Funciones_Globales
from datetime import datetime


class Form_Edicion_Herramental(Form_Edicion_HerramentalTemplate):
  datos = None
  ws_herramentales = None
  ss_heramentales = None
  herramentales = None
  lista_componentes = None
  registro_actual = None
  campos_no_obligatorios = []
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)

    if self.datos['modo'] == "edicion" or self.datos['modo'] == "visor":
      self.registro_actual = Funciones_Globales.get_registro(self.datos['id_herramental'], 'id_herramental', self.herramentales)
      Funciones_Globales.fill_formulario(self.lista_componentes, self.registro_actual)
      if self.datos['modo'] == "visor":
        self.deshabilitar_form()

  #################################################### FUNCIONES PERSONALIZADAS ####################################################
        
  def set_ini_config(self, datos):
    self.ws_herramentales = app_files.control_herramentales
    self.ss_heramentales = self.ws_herramentales['HERRAMENTALES']
    self.herramentales = self.ss_heramentales.rows
    self.datos = datos

    self.lista_componentes = [
      self.text_box_codigo_herramental,
      self.date_picker_fecha_registro,
      self.text_area_descripcion,
      self.text_box_tipo_material,
      self.text_box_tipo_suaje,
      self.text_box_ubicacion,
      self.text_box_vida_util,
      self.text_box_alerta
    ]

  def save_data(self, modo):
    mensaje = "Actualizando registro en la base de datos..." if modo == "edicion" else "Guardando registro en la base de datos..."
    title = "ACTUALIZANDO." if modo == "edicion" else "GUARDANDO."
    with Notification(mensaje, title=title, style="notification"):
      dicc_datos = Funciones_Globales.genera_diccionario(self.lista_componentes)
      if modo == "edicion":
        self.registro_actual['registro_principal'] = 0
        dicc_datos['id_herramental'] = self.registro_actual['id_herramental']
      else:
        dicc_datos['id_herramental'] = (max([int(item['id_herramental']) for item in self.herramentales]) + 1) if len(self.herramentales) > 0 else 0
      dicc_datos['contador'] = 0 if modo == "nuevo" else self.registro_actual['contador']  
      dicc_datos['activo'] = 1  
      dicc_datos['registro_principal'] = 1
      dicc_datos['id_usuario_registrador'] = self.datos['id_usuario_erp']
      dicc_datos['nombre_usuario'] = self.datos['nombre_usuario']
      dicc_datos['comentarios'] = "Alta" if modo == "nuevo" else "Edición"
      dicc_datos['marca_temporal'] = datetime.now()
        
      
      status = "registro_actualizado" if  modo == "edicion" else "registro_guardado"
      self.ss_heramentales.add_row(**dicc_datos)
      self.raise_event("x-close-alert",value=status)

  def deshabilitar_form(self):
    for componente in self.lista_componentes:
      componente.enabled = False
    self.button_guardar.enabled = False

  
  ############################################################ EVENTOS ############################################################
  def button_guardar_click(self, **event_args):
    status = Funciones_Globales.validar_campos( self.lista_componentes, self.registro_actual, self.campos_no_obligatorios, self.datos['modo'])
    if status == 1:
      self.save_data(self.datos['modo'])
    elif status == 2:
      alert("No hay cambios que guardar.", title="ERROR!")
    elif status == 3:
      alert("faltan campos por llenar!", title="ERROR!")

  def text_box_codigo_herramental_change(self, **event_args):
    self.text_box_codigo_herramental.role = "outlined"

  def text_area_descripcion_change(self, **event_args):
    self.text_area_descripcion.role = "outlined"

  def text_box_tipo_suaje_change(self, **event_args):
    self.text_box_tipo_suaje.role = "outlined"

  def text_box_vida_util_change(self, **event_args):
    self.text_box_vida_util.role = "outlined"

  def text_box_ubicacion_change(self, **event_args):
    self.text_box_ubicacion.role = "outlined"

  def text_box_tipo_material_change(self, **event_args):
    self.text_box_tipo_material.role = "outlined"


    
