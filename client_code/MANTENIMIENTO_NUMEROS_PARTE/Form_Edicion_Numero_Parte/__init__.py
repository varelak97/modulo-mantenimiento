from ._anvil_designer import Form_Edicion_Numero_ParteTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ... import Funciones_Globales
from datetime import datetime


class Form_Edicion_Numero_Parte(Form_Edicion_Numero_ParteTemplate):
  datos = None
  ws_libro_suajes = None
  ss_numeros_parte = None
  numeros_parte = None
  ss_vista_herramentales = None
  vista_herramentales = None
  ss_vista_clientes = None
  vista_clientes = None
  registro_actual = None
  lista_componentes = None
  lista_suajes = None
  campos_no_obligatorios = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.get_datos()

  ################################################# FUNCIONES PERSONALIZADAS #################################################
  def set_ini_config(self, datos):
    self.set_event_handler('x-borrar_item', Funciones_Globales.borrar_item)
    self.datos = datos
    self.ws_libro_suajes = app_files.control_herramentales
    self.ss_numeros_parte = self.ws_libro_suajes['NUMEROS_PARTE']
    self.ss_vista_herramentales = self.ws_libro_suajes['VISTA_HERRAMENTALES']
    self.ss_vista_clientes = self.ws_libro_suajes['VISTA_CLIENTES']
    
    self.lista_componentes = [
      self.text_box_numero_parte,
      self.text_area_descripcion,
      self.date_picker_fecha_registro,
      self.drop_down_cliente,
      self.text_area_descripcion,
      self.repeating_panel_suajes_asociados
    ]
    self.campos_no_obligatorios = [
      self.text_area_descripcion
    ]

  def get_datos(self):
    self.numeros_parte = self.ss_numeros_parte.rows
    self.vista_herramentales = self.ss_vista_herramentales.rows
    self.vista_clientes = self.ss_vista_clientes.rows
    lista_clientes = []
    for cliente in self.vista_clientes:
      lista_clientes.append((cliente['cliente'], (cliente['id_cliente'], cliente['cliente'])))
    self.drop_down_cliente.items = lista_clientes
    self.lista_suajes = []
    for suaje in self.vista_herramentales:
      self.lista_suajes.append((suaje['codigo_herramental'], suaje['id_herramental']))
                            
    if self.datos['modo'] == "edicion":
      self.llenar_formulario()

  def llenar_formulario(self):
    for numero_parte in self.numeros_parte:
        if numero_parte['id_numero_parte'] == self.datos['id_numero_parte'] and numero_parte['registro_principal'] == '1':
          self.registro_actual = numero_parte
          break
    datos_suaje = []
    for suaje_registro in eval(self.registro_actual['id_herramentales']):
      for herramental in self.vista_herramentales:
        if suaje_registro == int(herramental['id_herramental']):
          datos_suaje.append(herramental)
          break
    dicc_registro_actual = dict(self.registro_actual)
    dicc_registro_actual['tabla'] = datos_suaje
    for cliente in self.vista_clientes:
      if cliente['id_cliente'] == dicc_registro_actual['id_cliente']:
        dicc_registro_actual['cliente'] = cliente['cliente']
        break
      
    modos = [{"modo":"modo1", "tag":"id_cliente", "llave":"cliente"}]
    Funciones_Globales.fill_formulario(self.lista_componentes, dicc_registro_actual, modos)

  def guardar_datos(self, modo):
    nuevo_registro = dict(self.registro_actual).copy()
    #self.registro_actual['registro_principal'] = 0
    datos_formulario = Funciones_Globales.genera_diccionario(self.lista_componentes, 'id_herramental')
    nuevo_registro.update(datos_formulario)
    nuevo_registro['id_usuario_registrador'] = self.datos['id_usuario_erp']
    nuevo_registro['nombre_usuario'] = self.datos['nombre_usuario']
    nuevo_registro['marca_temporal'] = datetime.now()
    nuevo_registro['operacion'] = 'Alta' if self.datos['modo'] == 'nuevo' else 'Edicion'
    nuevo_registro['id_cliente'] = nuevo_registro['id_cliente'][0]
    if self.datos['modo'] == 'nuevo':
      nuevo_registro['id_numero_parte'] = max([int(item['id_numero_parte']) for item in self.numeros_parte]) + 1
    #self.ss_numeros_parte.add_row(**nuevo_registro)
    print(f"registro anterior:{self.registro_actual}")
    alert(f"se guardaron los datos:{nuevo_registro}")
    
    
  ########################################################## EVENTOS #########################################################
  def button_agregar_click(self, **event_args):
    dropdown_suajes = DropDown(role='outlined', background='On Primary', placeholder='-- SELECCIONE --', items=self.lista_suajes)
    respuesta = alert(dropdown_suajes, title="SELECCIONE SUAJE:", buttons=[("ACEPTAR", True),("CANCELAR", False)])
    if respuesta:
      items_actuales = self.repeating_panel_suajes_asociados.items
      if items_actuales is None:
        items_actuales = []
      for herramental in self.vista_herramentales:
        if int(herramental['id_herramental']) == int(dropdown_suajes.selected_value):
          items_actuales.append(dict(herramental))
      self.repeating_panel_suajes_asociados.items = items_actuales

  def button_guardar_click(self, **event_args):
    
    status = Funciones_Globales.validar_campos( self.lista_componentes, self.registro_actual, self.campos_no_obligatorios, self.datos['modo'], None, 'id_herramental')
    if status == 1:
      mensaje = "Guardando registro en la base de datos" if self.datos['modo'] == 'nuevo' else 'Actualizando registro en la base de datos'
      titulo = "GUARDANDO" if self.datos['modo'] == 'nuevo' else "ACTUALIZANDO."
      with Notification(mensaje, title=titulo, style='notification'):
        self.guardar_datos(self.datos['modo'])
      status = 'registro_guardado' if self.datos['modo'] == 'nuevo' else 'registro_actualizado'
      self.raise_event("x-close-alert", value=status)
    elif status == 2:
      alert("No hay cambios que guardar.", title="ERROR!")
    elif status == 3:
      alert("faltan campos por llenar!", title="ERROR!")
