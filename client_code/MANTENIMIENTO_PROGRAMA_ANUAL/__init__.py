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

  lista_areas = [
    "IMPRESIÓN",
    "SUAJE",
    "MANUALES",
    "LÁSER",
    "CALIDAD",
    "REVELADO",
    "ENSAMBLE",
    "ALMACÉN MP"
  ]
  
  lista_equipos = [
    ("ATMA 57",{"EQUIPO":"ATMA 57","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 71",{"EQUIPO":"ATMA 71","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 70",{"EQUIPO":"ATMA 70","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 45",{"EQUIPO":"ATMA 45","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 710",{"EQUIPO":"ATMA 710","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 80",{"EQUIPO":"ATMA 80","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("HORNO 1",{"EQUIPO":"HORNO 1","AREA":"IMPRESIÓN","FRECUENCIA":["SEMANAL","MENSUAL","SEMESTRAL"]}),
    ("HORNO 2",{"EQUIPO":"HORNO 2","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 3",{"EQUIPO":"HORNO 3","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 4",{"EQUIPO":"HORNO 4","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 5",{"EQUIPO":"HORNO 5","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("IMPRESORA MIMAKI",{"EQUIPO":"IMPRESORA MIMAKI","AREA":"IMPRESIÓN","FRECUENCIA":["MENSUAL"]}),
    ("IMPRESORA OFFSET",{"EQUIPO":"IMPRESORA OFFSET","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("SPS",{"EQUIPO":"SPS","AREA":"IMPRESIÓN","FRECUENCIA":["MENSUAL"]}),
    ("SUAJADORA 1",{"EQUIPO":"SUAJADORA 1","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 2",{"EQUIPO":"SUAJADORA 2","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 3",{"EQUIPO":"SUAJADORA 3","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 4",{"EQUIPO":"SUAJADORA 4","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("EMBOSADORA",{"EQUIPO":"EMBOSADORA","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("LÁSER V-460",{"EQUIPO":"LÁSER V-460","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("LÁSER M-300",{"EQUIPO":"LÁSER M-300","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("LÁSER VLS-360",{"EQUIPO":"LÁSER VLS-360","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("MESA DE COORDENADAS X-Y",{"EQUIPO":"MESA DE COORDENADAS X-Y","AREA":"CALIDAD","FRECUENCIA":["TRIMESTRAL"]}),
    ("PROBADOR ELÉCTRICO 2 (CC015)",{"EQUIPO":"PROBADOR ELÉCTRICO 2 (CC015)","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("PROBADOR ELÉCTRICO 3 (C0025)",{"EQUIPO":"PROBADOR ELÉCTRICO 3 (C0025)","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("PROBADOR ELÉCTRICO 4 (C0028)",{"EQUIPO":"PROBADOR ELÉCTRICO 4 (C0028)","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("INSOLADORA",{"EQUIPO":"INSOLADORA","AREA":"REVELADO","FRECUENCIA":["TRIMESTRAL"]}),
    ("AFILADOR DE RASEROS",{"EQUIPO":"AFILADOR DE RASEROS","AREA":"REVELADO","FRECUENCIA":["TRIMESTRAL"]}),
    ("LAMINADORA 1",{"EQUIPO":"LAMINADORA 1","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("LAMINADORA 2",{"EQUIPO":"LAMINADORA 2","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("LAMINADORA 3",{"EQUIPO":"LAMINADOR 3","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("PICK&PLACE 2",{"EQUIPO":"PICK&PLACE 2","AREA":"ENSAMBLE","FRECUENCIA":["TRIMESTRAL"]}),
    ("TROQUELADORA MANUAL",{"EQUIPO":"TROQUELADORA MANUAL","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("DISPENSADORES",{"EQUIPO":"DISPENSADORES","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("PICK&PLACE 3",{"EQUIPO":"PICK&PLACE 3","AREA":"ENSAMBLE","FRECUENCIA":["TRIMESTRAL"]}),
    ("GUILLOTINA 1",{"EQUIPO":"GUILLOTINA 1","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("GUILLOTINA 2",{"EQUIPO":"GUILLOTINA 2","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("GUILLOTINA 3",{"EQUIPO":"GUILLOTINA 3","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("HOJEADORA",{"EQUIPO":"HOJEADORA","AREA":"ALMACÉN MP","FRECUENCIA":["TRIMESTRAL"]}),
    ("EMBOLSADORA",{"EQUIPO":"EMBOLSADORA","AREA":"MANUALES","FRECUENCIA":["TRIMESTRAL"]}),
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
    self.drop_down_areas.items = self.lista_areas
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
    for dia in range(31):
      area = "todas" if self.drop_down_areas.selected_value == None else self.drop_down_areas.selected_value
      tipo = "todos" if self.drop_down_tipo.selected_value == None else self.drop_down_tipo.selected_value
      equipo = "todos" if self.drop_down_equipos.selected_value == None else self.drop_down_equipos.selected_value['EQUIPO']
      indicadores_mtto_mes.append({
        #genera acumuladores
        'W':0,
        'M':0,
        'T':0,
        'S':0,
        'A':0,
        'P':0,
        'R':0,
        'OK':0,
        'area':area,
        'tipo':tipo,
        'equipo':equipo,
        'id_mtto_preventivo':None
      })
      
    for item in self.registros_consulta_mttos:
      dia_prog = int(item['fecha_programada'].split('-')[2])
      mes_prog = int(item['fecha_programada'].split('-')[1])
      #filtra por datos del mes
      if mes_prog == mes:
        self.fill_indicador(dia_prog, indicadores_mtto_mes, item)
    self.card_calendario.visible = False
    mes_calendario = calendar.month(int(anio),mes)[0:-1] #Se descarta el último salto de línea, pues en caso de haber 6 semanas, se toma una 7a inexistente

    prefijos = {"PROGRAMADO":"P","REPROGRAMADO":"R","REALIZADO":"OK", "todos":"P"}
    renglones_mes = mes_calendario.split('\n')
    items = []
    for i in range(2, len(renglones_mes)):
      dicc = {}
      j = 1
      for k in range(0,len(renglones_mes[i]),3):
        numero_dia = str(renglones_mes[i][k:k+2]).strip()
        if numero_dia != "":
          prefijo = prefijos[indicadores_mtto_mes[int(numero_dia)-1]['tipo']]
          dicc[self.dias_semana[str(j)]] = {
            "numero_dia":numero_dia,
            'P':f"P: {indicadores_mtto_mes[int(numero_dia)-1]['P']}",
            'R':f"R: {indicadores_mtto_mes[int(numero_dia)-1]['R']}",
            'OK':f"OK: {indicadores_mtto_mes[int(numero_dia)-1]['OK']}",
            'W':f"{prefijo}W: {indicadores_mtto_mes[int(numero_dia)-1]['W']}",
            'M':f"{prefijo}M: {indicadores_mtto_mes[int(numero_dia)-1]['M']}",
            'T':f"{prefijo}T: {indicadores_mtto_mes[int(numero_dia)-1]['T']}",
            'S':f"{prefijo}S: {indicadores_mtto_mes[int(numero_dia)-1]['S']}",
            'A':f"{prefijo}A: {indicadores_mtto_mes[int(numero_dia)-1]['A']}"
          }
        j += 1
      items.append(dicc)
    print(items)
    """for index,item in enumerate(items):
      print(f"dia:{index+1} --- {item}\n")"""
    self.repeating_panel_mes_calendario.items = items
    self.card_calendario.visible = True

  def fill_indicador(self, dia_prog, indicadores_mtto_mes, item):
    prefijos_tipo = {"PROGRAMADO":"P","REPROGRAMADO":"R","REALIZADO":"OK"}
    prefijos_frecuencia = {"SEMANAL":"S", "MENSUAL":"M", "TRIMESTRAL":"T", "SEMESTRAL":"S","ANUAL":"A"}
    area = indicadores_mtto_mes[dia_prog-1]['area']
    equipo = indicadores_mtto_mes[dia_prog-1]['equipo']
    tipo = indicadores_mtto_mes[dia_prog-1]['tipo']

    if area == "todas":
      if equipo == "todos":
        if tipo == "todos":
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
        elif tipo == item['status_mantenimiento']: #tipo:selected
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
      elif equipo == item['equipo']: #equipo:selected
        if tipo == "todos":
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
        elif tipo == item['status_mantenimiento']: #tipo:selected
          indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] = indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] + 1
          indicadores_mtto_mes[dia_prog-1]['id_mtto_preventivo'] = item['id_mtto_preventivo']
    elif area == item['area']: #area:selected
      if equipo == "todos":
        if tipo == "todos":
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
        elif tipo == item['status_mantenimiento']: #tipo:selected
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
      elif equipo == item['equipo']: #equipo:selected
        if tipo == "todos":
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
        elif tipo == item['status_mantenimiento']: #tipo:selected
          indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] = indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] + 1
          indicadores_mtto_mes[dia_prog-1]['id_mtto_preventivo'] = item['id_mtto_preventivo']
  #################################################### EVENTOS ####################################################
  def drop_down_mes_change(self, **event_args):
    self.llenar_calendario()

  def drop_down_anio_change(self, **event_args):
    self.llenar_calendario()

  def drop_down_areas_change(self, **event_args):
    self.drop_down_equipos.selected_value = None
    self.drop_down_tipo.selected_value = None
    if self.drop_down_areas.selected_value != None:
      lista_filtrada = []
      for equipo in self.lista_equipos:
        if self.drop_down_areas.selected_value == equipo[1]['AREA']:
          lista_filtrada.append(equipo)
      self.drop_down_equipos.items = lista_filtrada
    else:
      self.drop_down_equipos.items = self.lista_equipos
    self.llenar_calendario()
        

  def drop_down_equipos_change(self, **event_args):
    self.drop_down_tipo.selected_value = None
    self.llenar_calendario()

  def drop_down_tipo_change(self, **event_args):
    self.llenar_calendario()

  def button_borrar_click(self, **event_args):
    self.drop_down_areas.selected_value = None
    self.drop_down_equipos.selected_value = None
    self.drop_down_tipo.selected_value = None
    self.llenar_calendario()

  
   
  ##################################################### PRUEBAS #####################################################
    """self.datos['clave_form'] = 'MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO'
    self.datos['modo'] = 'nuevo'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""

    
    """"lista = [["nombre","edad"],["ALFREDO VARELA",'33'],["FERNANDO CORTES",'31'],["MARIO GONZALES",'45']]
    
    datos = anvil.js.call('SUPERSQL',f"SELECT * FROM ? WHERE edad < 40",lista)
    print(datos)""""

    #print(anvil.js.call('prueba',lista))

    

