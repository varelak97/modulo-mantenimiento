from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CHECKLISTTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from datetime import date,datetime
#import anvil.server

class MANTENIMIENTO_PREVENTIVO_CHECKLIST(MANTENIMIENTO_PREVENTIVO_CHECKLISTTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  libro_mttos = None
  ws_registros_mttos = None
  datos_mttos = None
  registro_equipo = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos
    
    self.libro_mttos = app_files.mantenimiento_preventivo
    self.ws_registros_mttos = self.libro_mttos['Registros']
    self.datos_mttos = self.ws_registros_mttos.rows
    
    for registro in self.datos_mttos:
      if registro['registro_principal'] == '1' and registro['id_mtto_preventivo'] == self.datos['id_mtto_preventivo']:
        self.registro_equipo = registro
        break
    self.label_titulo.text = f"CHECKLIST MTTO PREVENTIVO {self.registro_equipo['equipo']}"
    lista = list(eval(self.registro_equipo['actividades']))
    if datos['modo'] == "checklist":
      for item in lista:
        item['si'] = False
        item['no'] = False
        item['na'] = False
    
    self.repeating_panel_registros.items = lista
    
    if datos['modo'] == "ver_checklist":
      self.button_guardar.enabled = False
      for row in self.repeating_panel_registros.get_components():
        componentes_row = row.get_components()
        componentes_row[2].enabled = False
        componentes_row[3].enabled = False
        componentes_row[4].enabled = False
  ################################ FUNCIONES PERSONALIZADS ########################################
      
  

  ############################################ EVENTOS ############################################
  def button_guardar_click(self, **event_args):
    respuestas = self.repeating_panel_registros.items
    total_respuestas = len(respuestas)
    respuestas_contestadas = 0
    lista_row_panels = self.repeating_panel_registros.get_components()
    for index, row_panel in enumerate(lista_row_panels):
      group_value = row_panel.get_components()[2].get_group_value()
      if group_value != None:
        respuestas_contestadas += 1
        respuestas[index][group_value] = True
    if respuestas_contestadas < total_respuestas:
      alert(title="ERROR!",content="checklist incompleto.")
    else:
      print("guardando...")
      self.registro_equipo['registro_principal'] = 0
      registro_actualizar = dict(self.registro_equipo).copy()
      datos_actualizar = {
        "status_mantenimiento": "REALIZADO",
        "actividades":respuestas,
        "operacion":"edicion",
        "marca_temporal":datetime.now()
      }
      registro_actualizar.update(**datos_actualizar)
      self.ws_registros_mttos.add_row(**registro_actualizar)
      self.raise_event("x-close-alert",value="registro_guardado")

  """def button_regresar_click(self, **event_args):
    self.datos['clave_form'] = 'MANTENIMIENTO_PROGRAMA_ANUAL'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""


