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
    self.datos = datos

    self.set_event_handler('x-abrir_form', self.abrir_popup_form)
    
    self.ws_herramentales = app_files.control_herramentales
    self.ss_herramentales = self.ws_herramentales['VISTA_HERRAMENTALES']

    self.button_actualizar_click()

  ############################################# FUNCIONES PERSONALIZADAS ##############################################
  def abrir_popup_form(self, datos, **event_args):
    #datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == 'REGISTROS_HERRAMENTAL':
      datos.update(self.datos)
      self.abrir_form(MANTENIMIENTO_REGISTRO_SUAJES(datos))
    elif datos['clave_form'] == 'FORM_HERRAMENTAL':
      datos.update(self.datos)
      self.abrir_form(Form_Edicion_Herramental(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", True)], role="wide-modal-content-bigger")
    if respuesta == "registro_guardado":
        self.button_actualizar_click()
  
  ###################################################### EVENTOS ######################################################
  def button_actualizar_click(self, **event_args):
    self.herramentales = self.ss_herramentales.rows
    self.repeating_panel_herramentales.items = self.herramentales

  def button_nuevo_click(self, **event_args):
    datos = {}
    datos['clave_form'] = 'FORM_HERRAMENTAL'
    datos['modo'] = "nuevo"
    self.abrir_popup_form(datos)
