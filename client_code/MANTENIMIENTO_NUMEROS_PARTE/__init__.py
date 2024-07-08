from ._anvil_designer import MANTENIMIENTO_NUMEROS_PARTETemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class MANTENIMIENTO_NUMEROS_PARTE(MANTENIMIENTO_NUMEROS_PARTETemplate):
  datos = None
  ws_suajes = None
  ss_herramentales = None
  vista_herramentales = None
  ss_vista_numeros_parte = None
  vista_numeros_parte = None
  dicc_vista_numeros_parte = None
  ss_vista_clientes = None
  vista_clientes = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.button_actualizar_click()

  ################################################# FUNCIONES PERSONALIZADAS #################################################
  def set_ini_config(self, datos):
    self.datos = datos
    self.ws_suajes = app_files.control_herramentales
    self.ss_vista_numeros_parte = self.ws_suajes['VISTA_NUMEROS_PARTE']
    self.ss_herramentales = self.ws_suajes['VISTA_HERRAMENTALES']
    self.ss_vista_clientes = self.ws_suajes['VISTA_CLIENTES']

  def get_data(self):
    self.vista_numeros_parte = self.ss_vista_numeros_parte.rows
    self.vista_herramentales = self.ss_herramentales.rows
    self.vista_clientes = self.ss_vista_clientes.rows

    self.dicc_vista_numeros_parte = []
    
    for numero_parte in self.vista_numeros_parte:
      for cliente in self.vista_clientes:
        if numero_parte['id_cliente'] == cliente['id_cliente']:
          dicc_numero_parte = dict(numero_parte)
          dicc_numero_parte['cliente'] = cliente['nombre_cliente']
          self.dicc_vista_numeros_parte.append(dicc_numero_parte)
          break
    for numero_parte in self.dicc_vista_numeros_parte:
      lista_herramentales = ""
      for id_herramental in eval(numero_parte['id_herramentales']):
        if lista_herramentales != "":
          lista_herramentales += "\n"
        for herramentales in self.vista_herramentales:
          if id_herramental == int(herramentales['id_herramental']):
            lista_herramentales += f"{herramentales['codigo_herramental']}"
            break
      numero_parte['herramentales'] = lista_herramentales

    self.repeating_panel_numeros_parte.items = self.dicc_vista_numeros_parte
      
    

  ########################################################## EVENTOS #########################################################
  def button_actualizar_click(self, **event_args):
    if len(event_args) > 0:
      with Notification("Actualizando tabla...", title="ACTUALIZANDO." , style="notification"):
        self.get_data()
    else:
      self.get_data()
