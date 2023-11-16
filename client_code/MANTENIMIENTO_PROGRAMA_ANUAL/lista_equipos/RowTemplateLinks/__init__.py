from ._anvil_designer import RowTemplateLinksTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil_extras import popover

class RowTemplateLinks(RowTemplateLinksTemplate):
  ###################################################### VARIABLES GLOBALES #####################################################
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    ################################################ INICIALIZACION DE VARIABLES ################################################
  

  ################################################## FUNCIONES PERSONALIZADAS ###################################################

    
  ########################################################### EVENTOS ###########################################################
  def button_llenar_checklist_click(self, **event_args):
    #print(self.parent.parent.parent.popper.parent.tag)
    datos = {}
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CHECKLIST'
    datos['modo'] = "checklist"
    datos['id_mtto_preventivo'] = self.label_equipo.tag
    self.parent.parent.parent.popper.pop("hide")
    self.parent.parent.parent.popper.parent.parent.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def button_ver_checklist_click(self, **event_args):
    datos = {}
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CHECKLIST'
    datos['modo'] = "ver_checklist"
    datos['id_mtto_preventivo'] = self.label_equipo.tag
    self.parent.parent.parent.popper.pop("hide")
    self.parent.parent.parent.popper.parent.parent.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)
