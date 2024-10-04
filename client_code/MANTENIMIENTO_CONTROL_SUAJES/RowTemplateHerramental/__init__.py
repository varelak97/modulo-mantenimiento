from ._anvil_designer import RowTemplateHerramentalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..opciones_herramentales import opciones_herramentales
from ..opciones_inspecciones import opciones_inspecciones
from datetime import datetime

class RowTemplateHerramental(RowTemplateHerramentalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    datos = {
      'id_herramental': self.item['id_herramental'],
      'id_inspeccion': self.item['id_inspeccion'],
      'status_visual': self.item['status_visual'],
      'status_dimensional': self.item['status_dimensional'],
      'cliente': self.item['cliente'],
      'id_cliente': self.item['id_cliente'],
      'codigo_herramental': self.item['codigo_herramental'],
      'descripcion': self.item['descripcion'],
      'tipo_suaje': self.item['tipo_suaje'],
      'contador': self.item['contador'],
      'vida_util':self.item['vida_util']
    }

    if int(self.item['contador']) >= int(self.item['vida_util']):
      self.label_alerta.icon = "fa:exclamation-circle"
      self.label_alerta.background = app.theme_colors['Red']
      self.label_alerta.foreground = app.theme_colors['Yellow']
      self.link_alerta.popover(content=opciones_inspecciones(datos), title="REPORTES DE INSPECCIÓN", trigger="click", max_width="700px")
    elif int(self.item['contador']) >= int(self.item['alerta']):
      self.label_alerta.icon = "fa:warning"
      self.label_alerta.foreground = app.theme_colors['Primary']
      self.label_alerta.background = app.theme_colors['Yellow']
    else:
      self.label_alerta.icon = "fa:check"
      self.label_alerta.foreground = app.theme_colors['Primary']
      self.label_alerta.background = app.theme_colors['SecondaryGreen']
    #if int(self.item['contador']) >= int(self.item['vida_util']):
    self.button_editar.popover(content=opciones_herramentales(self.button_editar.tag),title=self.label_codigo_herramental.text, trigger="click",max_width="450px")

  def button_ver_click(self, **event_args):
    datos = {
      "id_herramental": self.button_editar.tag,
      "codigo_herramental": self.label_codigo_herramental.text,
      "tipo_suaje": self.label_tipo_suaje.text,
      "clave_form": "REGISTROS_HERRAMENTAL"
    }
    self.button_editar.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_form', datos=datos)
    #abrir herramental

  def button_ubicar_click(self, **event_args):
    anvil.server.call('led_on', int(self.button_ubicar.tag))

  def link_alerta_click(self, **event_args):
    """if int(self.item['contador']) >= int(self.item['vida_util']):
      datos = {
        'cliente':self.label_cliente.text,
        'id_cliente': self.label_cliente.tag,
        'codigo_herramental': self.label_codigo_herramental.text,
        'descripcion': self.label_descripcion.text,
        'id_herramental': self.button_editar.tag,
        'tipo_suaje': self.label_tipo_suaje.text,
        'vida_util': self.item['vida_util'],
        'contador': self.label_contador.text,
        'clave_form': 'FORM_INSPECCION_SUAJE', 
        'modo':'validacion'
      }
      self.button_editar.parent.parent.parent.parent.parent.parent.raise_event('x-validar_reporte', datos=datos)"""
