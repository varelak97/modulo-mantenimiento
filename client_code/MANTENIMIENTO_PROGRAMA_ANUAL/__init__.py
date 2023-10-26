from ._anvil_designer import MANTENIMIENTO_PROGRAMA_ANUALTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.js
import calendar
from datetime import datetime, date
from ..MANTENIMIENTO_PREVENTIVO_REGISTROS import MANTENIMIENTO_PREVENTIVO_REGISTROS

class MANTENIMIENTO_PROGRAMA_ANUAL(MANTENIMIENTO_PROGRAMA_ANUALTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  dias_semana = {
    "1": "lunes",
    "2": "martes",
    "3": "miercoles",
    "4": "jueves",
    "5": "viernes",
    "6": "sabado",
    "7": "domingo"
  }
  meses = [
    ("ENERO", 1),
    ("FEBRERO", 2),
    ("MARZO", 3),
    ("ABRIL", 4),
    ("MAYO", 5),
    ("JUNIO", 6),
    ("JULIO", 7),
    ("AGOSTO", 8),
    ("SEPTIEMBRE", 9),
    ("OCTUBRE", 10),
    ("NOVIEMBRE", 11),
    ("DICIEMBRE", 12),
  ]
  datos = {}
  libro_mttos = None
  ws_consulta_mttos = None
  registros_consulta_mttos = None
  #ws_registros_totales = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.datos = datos
    fecha_actual = date.today()
    self.drop_down_mes.items = self.meses
    self.drop_down_mes.selected_value = self.drop_down_mes.items[fecha_actual.month - 1][1]
    self.drop_down_anio.selected_value = str(fecha_actual.year)
    self.libro_mttos = app_files.mantenimiento_preventivo
    self.ws_consulta_mttos = self.libro_mttos['Consulta']
    self.registros_consulta_mttos = self.ws_consulta_mttos.rows
    self.llenar_calendario()
  
  ################################ FUNCIONES PERSONALIZADS ########################################
  def actualizar_form_activo(self, datos, **event_args):
    datos['mes'] = self.drop_down_mes.selected_value
    datos['anio'] = self.drop_down_anio.selected_value
    datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos))
      
  def abrir_form(self, form_de_interes):
     alert(content = form_de_interes, large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content")
    
  def llenar_calendario(self):
    anio = self.drop_down_anio.selected_value
    mes = self.drop_down_mes.selected_value
    
    indicadores_mtto_mes = []
    for dia in range(31):
      indicadores_mtto_mes.append({'SEMANAL':0,'MENSUAL':0,'TRIMESTRAL':0,'SEMESTRAL':0,'ANUAL':0})
    for item in self.registros_consulta_mttos:
      dia_prog = int(item['fecha_programada'].split('-')[2])
      mes_prog = int(item['fecha_programada'].split('-')[1])
      if mes_prog == mes:
        suma_actual = indicadores_mtto_mes[dia_prog-1][item['frecuencia']]
        indicadores_mtto_mes[dia_prog-1][item['frecuencia']] = suma_actual + 1
      
    self.card_calendario.visible = False
    mes_calendario = calendar.month(int(anio),mes)[0:-1] #Se descarta el último salto de línea, pues en caso de haber 6 semanas, se toma una 7a inexistente
    
    renglones_mes = mes_calendario.split('\n')
    items = []
    for i in range(2, len(renglones_mes)):
      dicc = {}
      j = 1
      for k in range(0,len(renglones_mes[i]),3):
        numero_dia = str(renglones_mes[i][k:k+2]).strip()
        if numero_dia != "":
          dicc[self.dias_semana[str(j)]] = {
            "numero_dia":numero_dia,
            "SEMANAL":indicadores_mtto_mes[int(numero_dia) -1]['SEMANAL'],
            "MENSUAL":indicadores_mtto_mes[int(numero_dia) -1]['MENSUAL'],
            "TRIMESTRAL":indicadores_mtto_mes[int(numero_dia) -1]['TRIMESTRAL'],
            "SEMESTRAL":indicadores_mtto_mes[int(numero_dia) -1]['SEMESTRAL'],
            "ANUAL":indicadores_mtto_mes[int(numero_dia) -1]['ANUAL']
          }
        j += 1
      items.append(dicc)
    self.repeating_panel_mes_calendario.items = items
    self.card_calendario.visible = True

  #################################################### EVENTOS ####################################################
  def drop_down_mes_change(self, **event_args):
    self.llenar_calendario()

  def drop_down_anio_change(self, **event_args):
    self.llenar_calendario()
   
  ##################################################### PRUEBAS #####################################################
    """self.datos['clave_form'] = 'MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO'
    self.datos['modo'] = 'nuevo'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""

    
    """"lista = [["nombre","edad"],["ALFREDO VARELA",'33'],["FERNANDO CORTES",'31'],["MARIO GONZALES",'45']]
    
    datos = anvil.js.call('SUPERSQL',f"SELECT * FROM ? WHERE edad < 40",lista)
    print(datos)""""

    #print(anvil.js.call('prueba',lista))
    

