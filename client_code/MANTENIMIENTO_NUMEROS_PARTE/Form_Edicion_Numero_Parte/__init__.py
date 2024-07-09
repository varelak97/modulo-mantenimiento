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
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.get_datos()

  ################################################# FUNCIONES PERSONALIZADAS #################################################
  def set_ini_config(self, datos):
    self.datos = datos
    self.ws_libro_suajes = app_files.control_herramentales
    self.ss_numeros_parte = self.ws_libro_suajes['NUMEROS_PARTE']
    self.ss_vista_herramentales = self.ws_libro_suajes['VISTA_HERRAMENTALES']
    self.ss_vista_clientes = self.ws_libro_suajes['VISTA_CLIENTES']
    self.lista_componentes = [
      self.text_area_descripcion,
      self.date_picker_fecha_registro,
      self.drop_down_cliente,
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
                            
    if self.datos['modo'] == "edicion":
      for numero_parte in self.numeros_parte:
        if numero_parte['id_numero_parte'] == self.datos['id_numero_parte'] and numero_parte['registro_activo'] == '1':
          self.registro_actual = numero_parte
          break
      modos = [{"tag":"cliente","modo":"modo1","llave:":"id_cliente"}]
      Funciones_Globales.fill_formulario(self.lista_componentes, self.registro_actual, modos)
    
  ########################################################## EVENTOS #########################################################
  def button_agregar_click(self, **event_args):
    dropdown_suajes = DropDown(role='outlined', background='On Primary', placeholder='-- SELECCIONE --', items=-"")
    respuesta = alert(dropdown_suajes, title="SELECCIONE SUAJE:", buttons=[("ACEPTAR", dropdown_suajes.selected_value),("CANCELAR", False)])
    print(f"la respuesta seleccionada es:{respuesta}")