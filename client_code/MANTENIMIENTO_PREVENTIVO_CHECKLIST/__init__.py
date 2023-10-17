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

    self.libro_mttos = app_files.mantenimiento_preventivo
    self.ws_registros_mttos = self.libro_mttos['Registros']
    self.datos_mttos = self.ws_registros_mttos.rows

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
      registro_actualizar = None
      for registro in self.datos_mttos:
        if registro['registro_principal'] == '1' and registro['id_mtto_preventivo'] == self.datos['id_mtto_preventivo']:
          registro['registro_principal'] = 0
          registro_actualizar = dict(registro).copy()
          break
      if registro_actualizar != None:
        datos_actualizar = {
          "status_mantenimiento": "REALIZADO",
          "actividades":respuestas,
          "operacion":"edicion",
          "marca_temporal":datetime.now()
        }
        registro_actualizar.update(**datos_actualizar)
        self.ws_registros_mttos.add_row(**registro_actualizar)
      self.raise_event("x-close-alert",value=True)

  """def button_regresar_click(self, **event_args):
    self.datos['clave_form'] = 'MANTENIMIENTO_PROGRAMA_ANUAL'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""


