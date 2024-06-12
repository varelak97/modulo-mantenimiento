from ._anvil_designer import MANTENIMIENTO_CONTROL_HERRAMENTALESTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil_extras import popover
from .Registros_Herramentales import Registros_Herramentales


class MANTENIMIENTO_CONTROL_HERRAMENTALES(MANTENIMIENTO_CONTROL_HERRAMENTALESTemplate):
  datos = None
  ws_herramentales = None
  ss_herramentales = None
  herramentales = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos

    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    
    self.ws_herramentales = app_files.control_herramentales
    self.ss_herramentales = self.ws_herramentales['VISTA_HERRAMENTALES']

    self.button_actualizar_click()

  ############################################# FUNCIONES PERSONALIZADAS ##############################################
  def actualizar_form_activo(self, datos, **event_args):
    #datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == 'REGISTROS_HERRAMENTALES':
      datos.update(self.datos)
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", True)])
    if respuesta == "registro_guardado":
        self.button_actualizar_click()
  
  ###################################################### EVENTOS ######################################################
  def button_actualizar_click(self, **event_args):
    self.herramentales = self.ss_herramentales.rows
    self.repeating_panel_herramentales.items = self.herramentales
