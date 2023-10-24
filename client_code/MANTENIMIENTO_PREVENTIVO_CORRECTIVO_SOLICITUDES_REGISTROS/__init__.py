from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE
from datetime import datetime, date

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROSTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  libro_solicitudes_mtto = None
  ws_consulta_solicitudes_mtto = None
  registros_consulta_mtto = None
  ws_solicitudes_mtto = None
  registros_mtto = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.set_event_handler('x-programar_mantenimiento', self.programar_mantenimiento)
    self.datos = datos
    self.libro_solicitudes_mtto = app_files.mantenimiento_solicitudes
    self.ws_solicitudes_mtto = self.libro_solicitudes_mtto['Registros']
    self.registros_mtto = self.ws_solicitudes_mtto.rows
    self.ws_consulta_solicitudes_mtto = self.libro_solicitudes_mtto['Consulta']
    self.registros_consulta_mtto = self.ws_consulta_solicitudes_mtto.rows
    if len(self.registros_mtto) > 0:
      self.column_panel_empty_db.visible = False
      self.data_grid_registros.visible = True
    else:
      self.column_panel_empty_db.visible = True
      self.data_grid_registros.visible = False
    self.repeating_panel_registros.items = self.registros_consulta_mtto
    
  ############################### FUNCIONES PERSONALIZADAS ########################################
  def actualizar_form_activo(self, datos, **event_args):
    datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", True)])
    if respuesta == "registro_guardado":
        self.button_actualizar_click()
    
  def programar_mantenimiento(self, datos, **event_args):
    with Notification("Registrando fecha en la base de datos...",title="GUARDANDO.", style="info"):
      registro_actual = None
      for item in self.registros_mtto:
        if item['id_solicitud_mtto'] == datos['id_solicitud_mtto'] and item['registro_principal'] == '1':
          registro_actual = item
          break
      nuevo_registro = dict(registro_actual).copy()
      nuevo_registro['fecha_programada'] = datos['fecha_programada']
      nuevo_registro['operacion'] = "edicion"
      nuevo_registro['marca_temporal'] = datetime.now()
      registro_actual['registro_principal'] = 0
      self.ws_solicitudes_mtto.add_row(**nuevo_registro)
    Notification("Fecha registrada correctamente!", title="ÉXITO!.", style="success").show()
    self.button_actualizar_click()
    
  ############################################ EVENTOS ############################################
  def button_actualizar_click(self, **event_args):
    with Notification("Actualizando tabla",title="ACTUALIZANDO", style="info"):
      self.registros_consulta_mtto = self.ws_consulta_solicitudes_mtto.rows
      self.registros_mtto = self.ws_solicitudes_mtto.rows
      if len(self.registros_mtto) > 0:
        self.column_panel_empty_db.visible = False
        self.data_grid_registros.visible = True
      else:
        self.column_panel_empty_db.visible = True
        self.data_grid_registros.visible = False
        
      self.repeating_panel_registros.items = self.registros_consulta_mtto
