from ._anvil_designer import RowTemplateRegistroHerramentalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class RowTemplateRegistroHerramental(RowTemplateRegistroHerramentalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    if self.item['status'] == "1":
      self.label_status.icon = "fa:check"
      self.label_status.background = app.theme_colors["SecondaryGreen"]
    else:
      self.label_status.icon = "fa:clock-o"
      self.label_status.background = app.theme_colors["Yellow"]

  
########################################################## EVENTOS ##########################################################
  def link_status_click(self, **event_args):
    if int(self.item['status']) == 0:
      respuesta = alert("¿Confirma que desea marcar como terminado?", title="CONFIRMACIÓN", buttons=(("ACEPTAR", True),("CANCELAR", False)))
      if respuesta:
        datos = {}
        datos['id_registro'] = self.button_editar.tag
        datos['id_herramental'] = self.label_codigo_herramental.tag
        self.parent.parent.parent.parent.parent.raise_event("x-actualizar_status", datos = datos)

  def button_editar_click(self, **event_args):
    datos = {}
    datos['id_registro'] = self.button_editar.tag
    datos['id_herramental'] = self.label_codigo_herramental.tag
    self.parent.parent.parent.parent.parent.raise_event("x-abrir_form", datos = datos)
        
