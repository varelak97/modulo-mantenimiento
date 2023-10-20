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
      botones = [("VER REPORTE","ver_reporte")]
    else:
      botones = [("GENERAR REPORTE","generar_reporte"),("PROGRAMAR MTTO","programar")]
    respuesta = alert(title=self.label_equipo.text,buttons=botones)
    if respuesta == "generar_reporte":
      datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE'
      datos['id_solicitud_mtto'] = self.tag
      datos['modo'] = "nuevo"
      self.parent.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo',datos=datos)
    elif respuesta == "programar":
      botones = [("PROGRAMAR", True)]
      dp = DatePicker(format='%Y-%m-%d')
      status = alert(title="SELECCIONE FECHA:",content=dp, buttons=botones)
      if status:
        datos['fecha_programada'] = dp.date
        datos['id_solicitud_mtto'] = self.tag
        self.parent.parent.parent.parent.parent.parent.raise_event('x-programar_mantenimiento',datos=datos)
    elif respuesta == "ver_reporte":
      alert("Aqui va el reporte...",title="FORMULARIO REPORTE")

