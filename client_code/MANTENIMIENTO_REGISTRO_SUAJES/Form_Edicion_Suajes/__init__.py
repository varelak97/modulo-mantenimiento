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
  ss_vista_clientes = None
  vista_clientes = None
  ss_vista_numeros_parte = None
  vista_numeros_parte = None
  ss_vista_herramentales = None
  vista_herramentales = None
  ss_registros = None
  registros = None
  registro_actual = None
  campos_no_obligatorios = []
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.get_data()

  ################################################### FUNCIONES PERSONALIZADAS ###################################################
  def set_ini_config(self, datos):
    self.datos = datos
    
    self.lista_input_components = [
      self.date_picker_fecha_programada,
      self.drop_down_cliente,
      self.drop_down_numeros_parte,
      self.drop_down_tipo_suaje,
      self.text_box_suajes_programados
    ]
    
    self.ws_control_herramentales = app_files.control_herramentales
    self.ss_vista_clientes = self.ws_control_herramentales['VISTA_CLIENTES']
    self.ss_vista_numeros_parte = self.ws_control_herramentales['VISTA_NUMEROS_PARTE']
    self.ss_vista_herramentales = self.ws_control_herramentales['VISTA_HERRAMENTALES']
    self.ss_registros = self.ws_control_herramentales['REGISTROS']
    
  def get_data(self):
    self.vista_clientes = self.ss_vista_clientes.rows
    self.vista_numeros_parte = self.ss_vista_numeros_parte.rows
    self.vista_herramentales = self.ss_vista_herramentales.rows
    self.registros = self.ss_registros.rows

    lista_clientes = []
    for cliente in self.vista_clientes:
      lista_clientes.append((cliente['cliente'], (cliente['id_cliente'], cliente['cliente'])))
    self.drop_down_cliente.items = lista_clientes

    lista_numeros_parte = []
    for numero_parte in self.vista_numeros_parte:
      #if int(self.datos['id_herramental']) in eval(numero_parte['id_herramentales']):
      lista_numeros_parte.append((numero_parte['numero_parte'], (numero_parte['id_numero_parte'], numero_parte['id_herramentales'])))
    self.drop_down_numeros_parte.items = lista_numeros_parte
    
    if self.datos['modo'] == "edicion":
      for registro in self.registros:
        if registro['id_registro'] == self.datos['id_registro'] and registro['registro_principal'] == "1":
          self.registro_actual = registro
          break
      dicc_registro_actual = dict(self.registro_actual)
      for numero_parte in self.vista_numeros_parte:
        if numero_parte['id_numero_parte'] == dicc_registro_actual['id_numero_parte']:
          dicc_registro_actual['id_herramentales'] = numero_parte['id_herramentales']
          break
      """for cliente in self.vista_clientes:
        if cliente['id_cliente'] == dicc_registro_actual['id_cliente']:
          dicc_registro_actual['cliente'] = cliente['cliente']
          break"""
      dicc_registro_actual['id_herramental'] = self.datos['id_herramental']
      modos = [
        {'tag':'id_numero_parte', 'modo':'modo1', 'llave':'id_herramentales'}, 
        {'tag':'tipo_suaje', 'modo':'modo1', 'llave': 'id_herramental'}
      ]
      Funciones_Globales.fill_formulario(self.lista_input_components, dicc_registro_actual, modos)
      self.drop_down_numeros_parte_change()
  ############################################################ EVENTOS ###########################################################
  def button_guardar_click(self, **event_args):
    dicc_modos = [{'tag':'id_numero_parte', 'index': 0}, {'tag':'tipo_suaje', 'index': 0}, {'tag':'id_cliente', 'index': 0}]
    status = Funciones_Globales.validar_campos(self.lista_input_components, self.registro_actual, self.campos_no_obligatorios, self.datos['modo'], dicc_modos, None)
    if status == 1:
      mensaje = "Actualizando registro en la base de datos..." if self.datos['modo'] == "edicion" else "Guardando registro en la base de datos..."
      title = "ACTUALIZANDO." if self.datos['modo'] == "edicion" else "GUARDANDO."
      with Notification(mensaje, title=title):
        dicc_datos = Funciones_Globales.genera_diccionario(self.lista_input_components, None)

        consecutivo = None
        if self.datos['modo'] == 'nuevo':
          consecutivo = (max([int(item['id_registro']) for item in self.registros]) + 1) if len(self.registros) > 0 else 0
        else:
          consecutivo = self.registro_actual['id_registro']
          self.registro_actual['registro_principal'] = 0
        dicc_datos['id_cliente'] = dicc_datos['id_cliente'][0]
        dicc_datos['id_numero_parte'] = dicc_datos['id_numero_parte'][0]
        dicc_datos['id_herramental'] = dicc_datos['tipo_suaje'][1]
        dicc_datos['tipo_suaje'] = dicc_datos['tipo_suaje'][0]
        dicc_datos['id_registro'] = consecutivo
        dicc_datos['status'] = 0
        dicc_datos['registro_principal'] = 1
        dicc_datos['id_usuario_registrador'] = self.datos['id_usuario_erp']
        dicc_datos['nombre_usuario'] = self.datos['nombre_usuario']
        dicc_datos['comentarios'] = "Alta" if self.datos['modo'] == 'nuevo' else "Edición" 
        dicc_datos['marca_temporal'] = datetime.now()
        status = "registro_guardado" if self.datos['modo'] == 'nuevo' else "registro_actualizado"
        self.ss_registros.add_row(**dicc_datos)
      self.raise_event("x-close-alert",value=status)
    elif status == 2:
      alert("No hay cambios que guardar.", title="ERROR!")
    elif status == 3:
      alert("faltan campos por llenar!", title="ERROR!")

  def drop_down_numeros_parte_change(self, **event_args):
    self.drop_down_numeros_parte.role = "outlined"
    if self.drop_down_numeros_parte.selected_value is not None:
      lista_suajes = []
      for herramental in self.vista_herramentales:
        if int(herramental['id_herramental']) in eval(self.drop_down_numeros_parte.selected_value[1]):
          lista_suajes.append((herramental['tipo_suaje'], (herramental['tipo_suaje'], herramental['id_herramental'])))
      self.drop_down_tipo_suaje.items = lista_suajes

      numero_parte_seleccionado = None
      for numero_parte in self.vista_numeros_parte:
        if self.drop_down_numeros_parte.selected_value[0] == numero_parte['id_numero_parte']:
          numero_parte_seleccionado = numero_parte
          break
      cliente_seleccionado = None
      for cliente in self.vista_clientes:
        if numero_parte_seleccionado['id_cliente'] == cliente['id_cliente']:
          cliente_seleccionado = cliente
          break
      self.drop_down_cliente.selected_value = (cliente_seleccionado['id_cliente'], cliente_seleccionado['cliente'])
    
      self.drop_down_tipo_suaje.enabled = True
    else:
      self.drop_down_tipo_suaje.selected_value = None
      self.drop_down_tipo_suaje.enabled = False

  def drop_down_cliente_change(self, **event_args):
    self.drop_down_cliente.role = "outlined"
    if self.drop_down_cliente.selected_value is not None:
      lista_numeros_parte = []
      for numero_parte in self.vista_numeros_parte:
        if self.drop_down_cliente.selected_value[0] == numero_parte['id_cliente']:
          lista_numeros_parte.append((numero_parte['numero_parte'], (numero_parte['id_numero_parte'], numero_parte['id_herramentales'])))
      self.drop_down_numeros_parte.items = lista_numeros_parte
      self.drop_down_numeros_parte_change()
    else:
      lista_numeros_parte = []
      for numero_parte in self.vista_numeros_parte:
        lista_numeros_parte.append((numero_parte['numero_parte'], (numero_parte['id_numero_parte'], numero_parte['id_herramentales'])))
      self.drop_down_numeros_parte.items = lista_numeros_parte
      self.drop_down_numeros_parte.selected_value = None
      self.drop_down_numeros_parte_change()

  def date_picker_fecha_programada_change(self, **event_args):
    self.date_picker_fecha_programada.role = "outlined"

  def drop_down_tipo_suaje_change(self, **event_args):
    self.drop_down_tipo_suaje.role = "outlined"

  def text_box_suajes_programados_change(self, **event_args):
    self.text_box_suajes_programados.role = "outlined"
    
