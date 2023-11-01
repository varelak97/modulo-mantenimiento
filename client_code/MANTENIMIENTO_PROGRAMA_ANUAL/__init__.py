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
  lista_equipos = [
    "ATMA 57",
    "ATMA 71",
    "ATMA 70",
    "ATMA 45",
    "ATMA 710",
    "ATMA 80",
    "HORNO 1",
    "HORNO 2",
    "HORNO 3",
    "HORNO 4",
    "HORNO 5",
    "IMPRESORA MIMAKI",
    "IMPRESORA OFFSET",
    "SPS",
    "SUAJADORA 1",
    "SUAJADORA 2",
    "SUAJADORA 3",
    "SUAJADORA 4",
    "EMBOSADORA",
    "LÁSER V-460",
    "LÁSER M-300",
    "LÁSER VLS-360",
    "MESA DE COORDENADAS X-Y",
    "PROBADOR ELÉCTRICO 2 (CC015)",
    "PROBADOR ELÉCTRICO 3 (C0025)",
    "PROBADOR ELÉCTRICO 4 (C0028)",
    "INSOLADORA",
    "AFILADOR DE RASEROS",
    "LAMINADORA 1",
    "LAMINADORA 2",
    "LAMINADORA 3",
    "PICK&PLACE 2",
    "TROQUELADORA MANUAL",
    "DISPENSADORES",
    "PICK&PLACE 3",
    "GUILLOTINA 1",
    "GUILLOTINA 2",
    "GUILLOTINA 3",
    "HOJEADORA",
    "EMBOLSADORA"
  ]
  datos = {}
  libro_mttos = None
  ws_consulta_mttos = None
  registros_consulta_mttos = None
  ws_registros_totales = None
  numero_registros = None
  
  def __init__(self, datos, **properties):
    self.datos = datos
    fecha_actual = date.today()
    self.drop_down_mes.items = self.meses
    self.drop_down_mes.selected_value = self.drop_down_mes.items[fecha_actual.month - 1][1]
    self.drop_down_anio.selected_value = str(fecha_actual.year)
    self.drop_down_equipos.items = self.lista_equipos
    self.libro_mttos = app_files.mantenimiento_preventivo
    self.ws_consulta_mttos = self.libro_mttos['Consulta']
    self.ws_registros_totales = self.libro_mttos['Registros']
    self.llenar_calendario()
    
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.set_event_handler('x-actualizar_calendario', self.llenar_calendario)
    
  
  ################################ FUNCIONES PERSONALIZADS ########################################
  def actualizar_form_activo(self, datos, **event_args):
    datos['mes'] = self.drop_down_mes.selected_value
    datos['anio'] = self.drop_down_anio.selected_value
    datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    datos['modo'] = "dia"
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content")
    if respuesta:
      self.llenar_calendario()
    
  def llenar_calendario(self):
    self.registros_consulta_mttos = self.ws_consulta_mttos.rows
    anio = self.drop_down_anio.selected_value
    mes = self.drop_down_mes.selected_value
    indicadores_mtto_mes = []

    #genera acumuladores
    for dia in range(31):
      indicadores_mtto_mes.append({
        """'P-SEMANAL':0,
        'P-MENSUAL':0,
        'P-TRIMESTRAL':0,
        'P-SEMESTRAL':0,
        'P-ANUAL':0,
        'R-SEMANAL':0,
        'R-MENSUAL':0,
        'R-TRIMESTRAL':0,
        'R-SEMESTRAL':0,
        'R-ANUAL':0,
        'OK-SEMANAL':0,
        'OK-MENSUAL':0,
        'OK-TRIMESTRAL':0,
        'OK-SEMESTRAL':0,
        'OK-ANUAL':0,
        'PROGRAMADO':0,
        'REPROGRAMADO':0,
        'REALIZADO':0"""
      })
    for item in self.registros_consulta_mttos:
      dia_prog = int(item['fecha_programada'].split('-')[2])
      mes_prog = int(item['fecha_programada'].split('-')[1])
      if mes_prog == mes:
        #todos los equipos
        if self.drop_down_equipos.selected_value == None:
          #todos los tipos programados, reprogramados, realizados
          if self.drop_down_tipo.selected_value == None:
            #suma_actual = indicadores_mtto_mes[dia_prog-1]['status_mantenimiento']
            indicadores_mtto_mes[dia_prog-1][item['status_mantenimiento']] = indicadores_mtto_mes[dia_prog-1][item['status_mantenimiento']] + 1 if item['status_mantenimiento'] in indicadores_mtto_mes[dia_prog-1].keys() else 0  
          #programados o reprogramados o realizados
          elif self.drop_down_tipo.selected_value == item['status_mantenimiento']:
            prefijos = [{"PROGRAMADOS":"P","REPROGRAMADOS":"R","REALIZADOS":"OK"}]
            if item['status_mantenimiento'] == self.drop_down_tipo.selected_value:
              prefijo_item = prefijos[self.drop_down_tipo.selected_value]
              #mttos programados semanal, mensual, trimestral, semestral, anual
              suma_actual = indicadores_mtto_mes[dia_prog-1][f"{prefijo_item}-{item['frecuencia']}"]
              indicadores_mtto_mes[dia_prog-1][f"P-{item['frecuencia']}"] = suma_actual + 1
              #mttos reprogramados semanal, mensual, trimestral, semestral, anual
              suma_actual = indicadores_mtto_mes[dia_prog-1][f"R-{item['frecuencia']}"]
              indicadores_mtto_mes[dia_prog-1][f"R-{item['frecuencia']}"] = suma_actual + 1
              #mttos realizados semanal, mensual, semestral, anual
              suma_actual = indicadores_mtto_mes[dia_prog-1][f"OK-{item['frecuencia']}"]
              indicadores_mtto_mes[dia_prog-1][f"OK-{item['frecuencia']}"] = suma_actual + 1



            
            
            """#mttos programados semanal, mensual, trimestral, semestral, anual
            suma_actual = indicadores_mtto_mes[dia_prog-1][f"P-{item['frecuencia']}"]
            indicadores_mtto_mes[dia_prog-1][f"P-{item['frecuencia']}"] = suma_actual + 1
            #mttos reprogramados semanal, mensual, trimestral, semestral, anual
            suma_actual = indicadores_mtto_mes[dia_prog-1][f"R-{item['frecuencia']}"]
            indicadores_mtto_mes[dia_prog-1][f"R-{item['frecuencia']}"] = suma_actual + 1
            #mttos realizados semanal, mensual, semestral, anual
            suma_actual = indicadores_mtto_mes[dia_prog-1][f"OK-{item['frecuencia']}"]
            indicadores_mtto_mes[dia_prog-1][f"OK-{item['frecuencia']}"] = suma_actual + 1"""

        else:
          pass
          """if item['equipo'] == self.drop_down_equipos.selected_value:
            suma_actual = indicadores_mtto_mes[dia_prog-1][item['frecuencia']]
            indicadores_mtto_mes[dia_prog-1][item['frecuencia']] = suma_actual + 1"""
      
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
            "W":indicadores_mtto_mes[int(numero_dia) -1]['SEMANAL'],
            "M":indicadores_mtto_mes[int(numero_dia) -1]['MENSUAL'],
            "T":indicadores_mtto_mes[int(numero_dia) -1]['TRIMESTRAL'],
            "S":indicadores_mtto_mes[int(numero_dia) -1]['SEMESTRAL'],
            "A":indicadores_mtto_mes[int(numero_dia) -1]['ANUAL']
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

  def drop_down_equipos_change(self, **event_args):
    self.llenar_calendario()

  def drop_down_tipo_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  
   
  ##################################################### PRUEBAS #####################################################
    """self.datos['clave_form'] = 'MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO'
    self.datos['modo'] = 'nuevo'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""

    
    """"lista = [["nombre","edad"],["ALFREDO VARELA",'33'],["FERNANDO CORTES",'31'],["MARIO GONZALES",'45']]
    
    datos = anvil.js.call('SUPERSQL',f"SELECT * FROM ? WHERE edad < 40",lista)
    print(datos)""""

    #print(anvil.js.call('prueba',lista))

    

