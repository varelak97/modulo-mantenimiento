from ._anvil_designer import Registros_HerramentalesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..Form_Edicion_Herramental import Form_Edicion_Herramental


class Registros_Herramentales(Registros_HerramentalesTemplate):
  datos = None
  ws_herramentales = None
  ss_vista_registros = None
  vista_registros = None
  ss_vista_numeros_parte = None
  vista_numeros_parte = None
  ss_registros = None
  registros = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_event_handler('x-abrir_form', self.abrir_popup_form)
    self.set_event_handler('x-actualizar_status', self.actualizar_status)
    
    self.datos = datos
    self.ws_herramentales = app_files.control_herramentales
    self.ss_vista_registros = self.ws_herramentales['VISTA_REGISTROS']
    self.ss_vista_numeros_parte = self.ws_herramentales["VISTA_NUMEROS_PARTE"]
    self.ss_registros = self.ws_herramentales['REGISTROS']
    
    self.label_title.text = f"HERRAMENTAL {self.datos['codigo_herramental']}"
    self.button_actualizar_click()

  #################################################### FUNCIONES PERSONALIZADAS #####################################################
  def actualizar_status(self, datos):
    pass
    
  def abrir_popup_form(self, datos, **event_args):
    #datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == "FORMULARIO_REGISTRO_HERRAMENTAL":
      datos['id_usuario_erp'] = self.datos['id_usuario_erp']
      self.abrir_form(Form_Edicion_Herramental(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", True)], role="wide-modal-content")
    if respuesta == "registro_guardado":
      with Notification("Actualizando tabla...", title="ACTUALIZANDO", style="success"):
        self.button_actualizar_click()


  
  ############################################################# EVENTOS #############################################################
  def button_registrar_click(self, **event_args):
    datos = {}
    datos['clave_form'] = "FORMULARIO_REGISTRO_HERRAMENTAL"
    datos['modo'] = "nuevo"
    datos['id_herramental'] = self.datos['id_herramental']
    datos['tipo_suaje'] = self.datos['tipo_suaje']
    self.abrir_popup_form(datos)

  def button_actualizar_click(self, **event_args):
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
