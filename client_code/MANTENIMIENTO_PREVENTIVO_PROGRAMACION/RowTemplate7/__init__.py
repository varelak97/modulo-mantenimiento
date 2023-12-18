from ._anvil_designer import RowTemplate7Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class RowTemplate7(RowTemplate7Template):
  #################################### DEFINICION DE VARIABLES ####################################
  
  def __init__(self, **properties):
    self.init_components(**properties)
    ################################# CARGA DE DATOS E INICIALIZACION DE VARIABLES ################################

    
  ########################################### FUNCIONES PERSONALIZADS #############################################

  #################################################### EVENTOS ####################################################

  def button_editar_click(self, **event_args):
    if self.button_editar.icon == "fa:check":
      self.button_editar.icon = "fa:edit"
      self.label_semanal.visible = True
      self.label_semanal.text = self.date_picker_semanal.date
      self.label_mensual.visible = True
      self.label_mensual.text = self.date_picker_mensual.date
      self.label_trimestral.visible = True
      self.label_trimestral.text = self.date_picker_trimestral.date
      self.label_semestral.visible = True
      self.label_semestral.text = self.date_picker_semestral.date
      self.label_anual.visible = True
      self.label_anual.text = self.date_picker_anual.date
      self.date_picker_semanal.visible = False
      self.date_picker_mensual.visible = False
      self.date_picker_trimestral.visible = False
      self.date_picker_semestral.visible = False
      self.date_picker_anual.visible = False
      self.parent.parent.parent.parent.parent.raise_event('x-enable_disable_guardar', id_equipo = self.label_id_equipo.text)
    else:
      self.button_editar.icon = "fa:check"
      self.label_semanal.visible = False
      self.label_mensual.visible = False
      self.label_trimestral.visible = False
      self.label_semestral.visible = False
      self.label_anual.visible = False
      self.date_picker_semanal.visible = True
      self.date_picker_mensual.visible = True
      self.date_picker_trimestral.visible = True
      self.date_picker_semestral.visible = True
      self.date_picker_anual.visible = True
      self.parent.parent.parent.parent.parent.button_generar_calendario.enabled = False
