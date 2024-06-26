from ._anvil_designer import Registros_HerramentalesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..Form_Edicion_Herramental import Form_Edicion_Herramental
from datetime import datetime, date


class Registros_Herramentales(Registros_HerramentalesTemplate):
  datos = None
  ws_herramentales = None
  ss_vista_registros = None
  vista_registros = None
  ss_vista_numeros_parte = None
  vista_numeros_parte = None
  ss_registros = None
  registros = None
  ss_herramentales = None
  herramentales = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_event_handler('x-abrir_form', self.abrir_popup_form)
    self.set_event_handler('x-actualizar_status', self.actualizar_status)
    
    self.datos = datos
    self.ws_herramentales = app_files.control_herramentales
    self.ss_vista_registros = self.ws_herramentales['VISTA_REGISTROS']
    self.ss_vista_numeros_parte = self.ws_herramentales["VISTA_NUMEROS_PARTE"]
    self.ss_registros = self.ws_herramentales['REGISTROS']
    self.ss_herramentales = self.ws_herramentales['HERRAMENTALES']
    
    self.label_title.text = f"HERRAMENTAL {self.datos['codigo_herramental']}"
    self.button_actualizar_click()

  #################################################### FUNCIONES PERSONALIZADAS #####################################################
  def actualizar_status(self, datos, **event_args):
    with Notification("Actualizando status del registro...", title="ACTUALIZANDO", style="notification"):
      registro_anterior = None
      for registro in self.registros:
        if registro['id_registro'] == datos['id_registro'] and registro['registro_principal'] == "1":
          registro_anterior = registro
          break
      nuevo_registro = dict(registro_anterior).copy()
      registro_anterior['registro_principal'] = 0
      nuevo_registro['status'] = 1
      nuevo_registro['marca_temporal'] = datetime.now()
      nuevo_registro['comentarios'] = "Cierre"
      nuevo_registro['id_usuario_registrador'] = self.datos['id_usuario_erp']
      self.ss_registros.add_row(**nuevo_registro)

      self.herramentales = self.ss_herramentales.rows
      herramental = None
      for registro in self.herramentales:
        if self.datos['id_herramental'] == registro['id_herramental'] and registro['registro_principal'] == "1":
          herramental = registro
          alert(f"encontrado:{herramental}")
          break
      herramental['contador'] = int(herramental['contador']) + int(nuevo_registro['suajes_programados'])    
    Notification("El registro ha sido actualizado correctamente!", "HECHO!", style="success").show(3)
    self.button_actualizar_click()
    
  def abrir_popup_form(self, datos, **event_args):
    #datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == "FORMULARIO_REGISTRO_HERRAMENTAL":
      datos['id_usuario_erp'] = self.datos['id_usuario_erp']
      self.abrir_form(Form_Edicion_Herramental(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", True)], role="wide-modal-content")
    if respuesta == "registro_guardado":
      self.button_actualizar_click()

  def get_data(self):
    self.registros = self.ss_registros.rows
    self.vista_registros = self.ss_vista_registros.rows
    self.vista_numeros_parte = self.ss_vista_numeros_parte.rows
    lista_registros = list(self.vista_registros)
    self.vista_registros = []
    for registro in lista_registros:
      for numero_parte in self.vista_numeros_parte:
        if registro['id_numero_parte'] == numero_parte['id_numero_parte']:
          dicc_registro = dict(registro)
          dicc_registro['numero_parte'] = numero_parte['numero_parte']
          self.vista_registros.append(dicc_registro)
    self.repeating_panel_registros.items = self.vista_registros


  
  ############################################################# EVENTOS #############################################################
  def button_registrar_click(self, **event_args):
    datos = {}
    datos['clave_form'] = "FORMULARIO_REGISTRO_HERRAMENTAL"
    datos['modo'] = "nuevo"
    datos['id_herramental'] = self.datos['id_herramental']
    datos['tipo_suaje'] = self.datos['tipo_suaje']
    self.abrir_popup_form(datos)

  def button_actualizar_click(self, **event_args):
    if len(event_args) > 0:
      with Notification("Actualizando la tabla...", title="ACTUALIZANDO.", style="notification"):
          self.get_data()
    else:
      self.get_data()
