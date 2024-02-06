from ._anvil_designer import RowTemplateEditarTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..opciones_edicion import opciones_edicion

class RowTemplateEditar(RowTemplateEditarTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  def __init__(self, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    if self.label_status.tag:
      self.button_editar.icon = "fa:eye"
    else:
      self.button_editar.popover(content=opciones_edicion(self.button_editar.tag, self.label_status.tag),title=self.label_equipo.text, trigger="click",max_width="450px")

    if self.label_status.icon == "fa:clock-o":
      self.label_status.background = app.theme_colors['Yellow']
    else:
      self.label_status.background = app.theme_colors['SecondaryGreen'] if bool(int(self.item['mtto_realizado'])) and bool(int(self.item['vobo_solicitante'])) else app.theme_colors['GrayGreen']
    #"theme:SecondaryGreen" if bool(int(self.item['mtto_realizado'])) else "theme:Yellow"
  ############################### FUNCIONES PERSONALIZADAS ########################################

  ############################################ EVENTOS ############################################
  def button_editar_click(self, **event_args):
    if self.label_status.tag:
      datos = {}
      datos['id_solicitud_mtto'] = self.button_editar.tag
      datos['modo'] = "visor"
      self.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_solicitud', datos=datos)

  def link_status_click(self, **event_args):
    if self.label_status.tag:
      datos = {}
      datos['folio'] = self.label_folio.text
      if self.label_status.background == app.theme_colors['GrayGreen']:
        datos['modo'] = "validacion"
      else:
        datos['modo'] = "visor_by_folio"
      self.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_reporte', datos=datos)
    
    
  """def button_editar_click(self, **event_args):
    datos = {}
    if self.check_box_status.checked:
      botones = [("VER REPORTE","ver_reporte")]
    else:
      botones = [("GENERAR REPORTE","generar_reporte"),("PROGRAMAR MTTO","programar")]
    respuesta = alert(title=self.label_equipo.text,buttons=botones)
    if respuesta == "generar_reporte":
      print(self.tag)
      datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE'
      datos['id_solicitud_mtto'] = self.tag
      datos['modo'] = "nuevo"
      self.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo',datos=datos)
    elif respuesta == "programar":
      botones = [("PROGRAMAR", True)]
      dp = DatePicker(format='%Y-%m-%d')
      status = alert(title="SELECCIONE FECHA:",content=dp, buttons=botones)
      if status:
        datos['fecha_programada'] = dp.date
        datos['id_solicitud_mtto'] = self.tag
        self.parent.parent.parent.parent.parent.parent.raise_event('x-programar_mantenimiento',datos=datos)
    elif respuesta == "ver_reporte":
      alert("Aqui va el reporte...",title="FORMULARIO REPORTE")"""

