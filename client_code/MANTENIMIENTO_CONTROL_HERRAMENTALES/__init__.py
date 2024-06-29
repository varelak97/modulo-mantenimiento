from ._anvil_designer import MANTENIMIENTO_CONTROL_HERRAMENTALESTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil_extras import popover
from ..MANTENIMIENTO_REGISTRO_SUAJES import MANTENIMIENTO_REGISTRO_SUAJES
from .Form_Edicion_Herramental import Form_Edicion_Herramental


class MANTENIMIENTO_CONTROL_HERRAMENTALES(MANTENIMIENTO_CONTROL_HERRAMENTALESTemplate):
  datos = None
  ws_herramentales = None
  ss_herramentales = None
  herramentales = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.set_event_handler('x-abrir_form', self.abrir_popup_form)
    
    self.button_actualizar_click()

  ############################################# FUNCIONES PERSONALIZADAS ##############################################
  def set_ini_config(self, datos):
    self.datos = datos
    self.ws_herramentales = app_files.control_herramentales
    self.ss_herramentales = self.ws_herramentales['VISTA_HERRAMENTALES']

  def get_datos(self):
    self.herramentales = self.ss_herramentales.rows
    self.repeating_panel_herramentales.items = self.herramentales
    
  def abrir_popup_form(self, datos, **event_args):
    #datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == 'REGISTROS_HERRAMENTAL':
      datos['id_usuario_erp'] = self.datos['id_usuario_erp']
      self.abrir_form(MANTENIMIENTO_REGISTRO_SUAJES(datos))
    elif datos['clave_form'] == 'FORM_HERRAMENTAL':
      datos['id_usuario_erp'] = self.datos['id_usuario_erp']
      self.abrir_form(Form_Edicion_Herramental(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", False)], role="wide-modal-content-bigger")
    if respuesta is not False and  respuesta is not None:
      mensaje = "El registro ha sido guardado correctamente" if respuesta == "registro_guardado" else "El registro ha sido actualizado correctamente."
      Notification(mensaje, title="ÉXITO!", style="success").show(3)
      self.button_actualizar_click()
  
  ###################################################### EVENTOS ######################################################
  def button_actualizar_click(self, **event_args):
    if len(event_args) > 0:
      with Notification("Actualizando tabla...", title="ACTUALIZANDO.", style="notification"):
        self.get_datos()
    else:
      self.get_datos()
    

  def button_nuevo_click(self, **event_args):
    datos = {}
    datos['clave_form'] = 'FORM_HERRAMENTAL'
    datos['modo'] = "nuevo"
    self.abrir_popup_form(datos)
