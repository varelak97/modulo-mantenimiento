from ._anvil_designer import Form_Edicion_Numero_ParteTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ... import Funciones_Globales


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
    self.set_event_handler('x-borrar_item', self.borrar_item)
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
      lista_clientes.append((cliente['cliente'], (cliente['cliente'], cliente['id_cliente'])))
    self.drop_down_cliente.items = lista_clientes
    self.lista_suajes = []
    for suaje in self.vista_herramentales:
      self.lista_suajes.append((suaje['codigo_herramental'], suaje['id_herramental']))
                            
    if self.datos['modo'] == "edicion":
      self.llenar_formulario()

  def llenar_formulario(self):
    for numero_parte in self.numeros_parte:
        if numero_parte['id_numero_parte'] == self.datos['id_numero_parte'] and numero_parte['registro_principal'] == '1':
          self.registro_actual = dict(numero_parte)
          break
    datos_suaje = []
    for suaje_registro in eval(self.registro_actual['id_herramentales']):
      for herramental in self.vista_herramentales:
        if suaje_registro == int(herramental['id_herramental']):
          datos_suaje.append(herramental)
          break
    self.registro_actual['tabla'] = datos_suaje
    for cliente in self.vista_clientes:
      if cliente['id_cliente'] == self.registro_actual['id_cliente']:
        self.registro_actual['cliente'] = cliente['cliente']
        break
      
    modos = [{"tag":"cliente","modo":"modo1","llave":"id_cliente"}]
    Funciones_Globales.fill_formulario(self.lista_componentes, self.registro_actual, modos)

  def borrar_item(self, id_herramental, **event_args):
    lista_suajes = self.repeating_panel_suajes_asociados.items
    id_borrar = None
    for index, suaje in enumerate(lista_suajes):
      if int(suaje['id_herramental']) == int(id_herramental):
        id_borrar = index
        break
    del(lista_suajes[id_borrar])
    self.repeating_panel_suajes_asociados.items = lista_suajes
    
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
            #items_actuales.append({'id_herramental':herramental['id_herramental'],'codigo_herramental':herramental['codigo_herramental'],'tipo_suaje':herramental['tipo_suaje']})

  def button_guardar_click(self, **event_args):
    status = Funciones_Globales.validar_campos( self.lista_componentes, self.registro_actual, self.campos_no_obligatorios, self.datos['modo'], None)
    if status == 1:
      self.save_data(self.datos['modo'])
    elif status == 2:
      alert("No hay cambios que guardar.", title="ERROR!")
    elif status == 3:
      alert("faltan campos por llenar!", title="ERROR!")
