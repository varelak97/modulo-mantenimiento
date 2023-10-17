from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CHECKLISTTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
#import anvil.server

class MANTENIMIENTO_PREVENTIVO_CHECKLIST(MANTENIMIENTO_PREVENTIVO_CHECKLISTTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.set_event_handler('x-actualizar_checklist', self.actualizar_checklist)
    self.datos = datos
    self.label_titulo.text = f"CHECKLIST MTTO PREVENTIVO {datos['equipo']}"
    lista = list(eval(self.datos['actividades']))
    for item in lista:
      item['si'] = False
      item['no'] = False
      item['na'] = False
    
    self.repeating_panel_registros.items = lista

  ################################ FUNCIONES PERSONALIZADS ########################################
  def actualizar_checklist(self, fila, **event_args):
    pass
    #print(self.repeating_panel_registros.items)
    """ lista = self.repeating_panel_registros.items
    for item in lista:
      if item['id'] == fila['id']:
        print("ok")
        if fila['tipo'] == "si":
          item['si'] = True
          break
    self.repeating_panel_registros.items = lista
    print(self.repeating_panel_registros.items)"""
    
      
  

  ############################################ EVENTOS ############################################
  def button_guardar_click(self, **event_args):
    lista_row_panels = self.repeating_panel_registros.get_components()
    for row_panel in lista_row_panels:
      print(f"valor:{row_panel.get_components()[2].get_group_value()}")
      pass
    #print(self.repeating_panel_registros.items)
    self.raise_event("x-close-alert",value=True)

  """def button_regresar_click(self, **event_args):
    self.datos['clave_form'] = 'MANTENIMIENTO_PROGRAMA_ANUAL'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""


