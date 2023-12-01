from ._anvil_designer import opciones_edicionTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class opciones_edicion(opciones_edicionTemplate):
  id_solicitud = None
  def __init__(self, id_solicitud, status, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.id_solicitud = id_solicitud
    if status:
      self.button_editar_solicitud.visible = False
      self.button_generar_reporte.visible = False
      self.button_programar.visible = False

  def button_ver_solicitud_click(self, **event_args):
    datos = {}
    datos['id_solicitud_mtto'] = self.id_solicitud
    datos['modo'] = "visor"
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_solicitud', datos=datos)

  def button_editar_solicitud_click(self, **event_args):
    datos = {}
    datos['id_solicitud_mtto'] = self.id_solicitud
    datos['modo'] = "editor"
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_solicitud', datos=datos)

  def button_generar_reporte_click(self, **event_args):
    datos = {}
    datos['id_solicitud_mtto'] = self.id_solicitud
    datos['modo'] = "nuevo"
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE'
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def button_programar_click(self, **event_args):
    self.popper.pop("hide")
    datos = {}
    botones = [("PROGRAMAR", True)]
    dp = DatePicker(format='%Y-%m-%d')
    status = alert(title="SELECCIONE FECHA:",content=dp, buttons=botones)
    if status:
      datos['fecha_programada'] = dp.date
      datos['id_solicitud_mtto'] = self.popper.tag
      self.popper.parent.parent.parent.parent.parent.parent.parent.raise_event('x-programar_mantenimiento',datos=datos)
      #self.parent.parent.parent.parent.parent.parent.raise_event('x-programar_mantenimiento',datos=datos)


