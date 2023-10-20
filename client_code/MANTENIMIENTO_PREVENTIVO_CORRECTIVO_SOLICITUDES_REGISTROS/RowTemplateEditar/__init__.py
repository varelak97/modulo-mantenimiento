from ._anvil_designer import RowTemplateEditarTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class RowTemplateEditar(RowTemplateEditarTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  def __init__(self, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################

  ############################### FUNCIONES PERSONALIZADAS ########################################

  ############################################ EVENTOS ############################################
  def button_editar_click(self, **event_args):
    datos = {}
    if self.check_box_status.checked:
      botones = [("PRUEBA","prueba")]
    else:
      botones = [("GENERAR REPORTE","reporte"),("PROGRAMAR MTTO","programar")]
    respuesta = alert(title=self.label_equipo.text,buttons=botones)
    if respuesta == "reporte":
      datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE'
      datos['id_solicitud_mtto'] = self.tag
      datos['modo'] = "nuevo"
      self.parent.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo',datos=datos)
    elif respuesta == "programar":
      botones = [("PROGRAMAR", "PROGRAMAR")]
      fecha = alert(title="SELECCIONE FECHA:",content=DatePicker(format='%Y-%m-%d %H:%M:%S'), buttons=botones)
      """datos['id_solicitud_mtto'] = self.button_editar.tag
      self.parent.parent.parent.parent.parent.parent.parent.raise_event('x-programar_mantenimiento',datos=datos)"""

