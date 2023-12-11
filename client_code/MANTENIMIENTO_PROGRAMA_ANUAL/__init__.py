from ._anvil_designer import MANTENIMIENTO_PROGRAMA_ANUALTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil_extras import popover
import anvil.server
import anvil.js
import calendar
from datetime import datetime, date
from ..MANTENIMIENTO_PREVENTIVO_REGISTROS import MANTENIMIENTO_PREVENTIVO_REGISTROS
from ..MANTENIMIENTO_PREVENTIVO_CHECKLIST import MANTENIMIENTO_PREVENTIVO_CHECKLIST
from ..MANTENIMIENTO_PREVENTIVO_PROGRAMACION import MANTENIMIENTO_PREVENTIVO_PROGRAMACION

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
    ("ATMA 57",{"equipo":"ATMA 57","area":"IMPRESIÓN"}),
    ("ATMA 71",{"equipo":"ATMA 71","area":"IMPRESIÓN"}),
    ("ATMA 70",{"equipo":"ATMA 70","area":"IMPRESIÓN"}),
    ("ATMA 45",{"equipo":"ATMA 45","area":"IMPRESIÓN"}),
    ("ATMA 710",{"equipo":"ATMA 710","area":"IMPRESIÓN"}),
    ("ATMA 80",{"equipo":"ATMA 80","area":"IMPRESIÓN"}),
    ("HORNO 1",{"equipo":"HORNO 1","area":"IMPRESIÓN"}),
    ("HORNO 2",{"equipo":"HORNO 2","area":"IMPRESIÓN"}),
    ("HORNO 3",{"equipo":"HORNO 3","area":"IMPRESIÓN"}),
    ("HORNO 4",{"equipo":"HORNO 4","area":"IMPRESIÓN"}),
    ("HORNO 5",{"equipo":"HORNO 5","area":"IMPRESIÓN"}),
    ("IMPRESORA MIMAKI",{"equipo":"IMPRESORA MIMAKI","area":"IMPRESIÓN"}),
    ("IMPRESORA OFFSET",{"equipo":"IMPRESORA OFFSET","area":"IMPRESIÓN"}),
    ("SPS",{"equipo":"SPS","area":"IMPRESIÓN"}),
    ("SUAJADORA 1",{"equipo":"SUAJADORA 1","area":"SUAJE"}),
    ("SUAJADORA 2",{"equipo":"SUAJADORA 2","area":"SUAJE"}),
    ("SUAJADORA 3",{"equipo":"SUAJADORA 3","area":"SUAJE"}),
    ("SUAJADORA 4",{"equipo":"SUAJADORA 4","area":"SUAJE"}),
    ("EMBOSADORA",{"equipo":"EMBOSADORA","area":"SUAJE"}),
    ("LÁSER V-460",{"equipo":"LÁSER V-460","area":"LÁSER"}),
    ("LÁSER M-300",{"equipo":"LÁSER M-300","area":"LÁSER"}),
    ("LÁSER VLS-360",{"equipo":"LÁSER VLS-360","area":"LÁSER"}),
    ("MESA DE COORDENADAS X-Y",{"equipo":"MESA DE COORDENADAS X-Y","area":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 2 (CC015)",{"equipo":"PROBADOR ELÉCTRICO 2 (CC015)","area":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 3 (C0025)",{"equipo":"PROBADOR ELÉCTRICO 3 (C0025)","area":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 4 (C0028)",{"equipo":"PROBADOR ELÉCTRICO 4 (C0028)","area":"CALIDAD"}),
    ("INSOLADORA",{"equipo":"INSOLADORA","area":"REVELADO"}),
    ("AFILADOR DE RASEROS",{"equipo":"AFILADOR DE RASEROS","area":"REVELADO"}),
    ("LAMINADORA 1",{"equipo":"LAMINADORA 1","area":"ENSAMBLE"}),
    ("LAMINADORA 2",{"equipo":"LAMINADORA 2","area":"ENSAMBLE"}),
    ("LAMINADORA 3",{"equipo":"LAMINADOR 3","area":"ENSAMBLE"}),
    ("PICK&PLACE 2",{"equipo":"PICK&PLACE 2","area":"ENSAMBLE"}),
    ("TROQUELADORA MANUAL",{"equipo":"TROQUELADORA MANUAL","area":"ENSAMBLE"}),
    ("DISPENSADORES",{"equipo":"DISPENSADORES","area":"ENSAMBLE"}),
    ("PICK&PLACE 3",{"equipo":"PICK&PLACE 3","area":"ENSAMBLE"}),
    ("GUILLOTINA 1",{"equipo":"GUILLOTINA 1","area":"ALMACÉN MP"}),
    ("GUILLOTINA 2",{"equipo":"GUILLOTINA 2","area":"ALMACÉN MP"}),
    ("GUILLOTINA 3",{"equipo":"GUILLOTINA 3","area":"ALMACÉN MP"}),
    ("HOJEADORA",{"equipo":"HOJEADORA","area":"ALMACÉN MP"}),
    ("EMBOLSADORA",{"equipo":"EMBOLSADORA","area":"MANUALES"}),
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
    #self.set_event_handler('x-show_lista_equipos', self.show_lista_equipos)
  
  ################################ FUNCIONES PERSONALIZADS ########################################
  """def show_lista_equipos(self, datos, **event_args):
    print(f"datos recibidos:{datos}")
    mes = self.drop_down_mes.selected_value
    anio = self.drop_down_anio.selected_value
    items = None
    if datos['modo'] == "dia":
      items = self.get_datos_actuales(anio, mes, datos['dia'], datos['tipo'], datos['frecuencia'])
    elif datos['modo'] == "todos":
      items = self.registros_consulta_mttos
    return items

  def get_datos_actuales(self, anio, mes, dia, tipo, frecuencia):
    registros_dia_seleccionado = []
    for item in self.registros_consulta_mttos:
      fecha_seleccionada = item['fecha_programada'].split('-')
      if int(fecha_seleccionada[0]) == int(anio) and int(fecha_seleccionada[1]) == int(mes) and int(fecha_seleccionada[2]) == int(dia):
        if tipo == item['status_mantenimiento']:
          if frecuencia == item['frecuencia']:
            registros_dia_seleccionado.append(item)
          elif tipo == "todas":
            registros_dia_seleccionado.append(item)
        elif tipo == "todos":
          registros_dia_seleccionado.append(item)
    return registros_dia_seleccionado"""
    
  def actualizar_form_activo(self, datos, **event_args):
    
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      datos['mes'] = self.drop_down_mes.selected_value
      datos['anio'] = self.drop_down_anio.selected_value
      datos.update(self.datos)
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos), "normal")
    elif datos['clave_form'] == "MANTENIMIENTO_PREVENTIVO_CHECKLIST":
      datos.update(self.datos)
      print(f"abriendo checklist:{self}")
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CHECKLIST(datos), "normal")
    
    #estaba asi:
    """datos['mes'] = self.drop_down_mes.selected_value
    datos['anio'] = self.drop_down_anio.selected_value
    datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos))"""
      
  def abrir_form(self, form_de_interes, modo):
    role = "wide-modal-content" if modo == "normal" else "wide-modal-content-bigger"
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("SALIR",False)], role=role)
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
      equipo = "todos" if self.drop_down_equipos.selected_value == None else self.drop_down_equipos.selected_value['equipo']
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
        'lista_equipos':[],
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

    prefijos = {"PROGRAMADO":"P","REPROGRAMADO":"R","REALIZADO":"OK-", "todos":"P"}
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
            'A':f"{prefijo}A: {indicadores_mtto_mes[int(numero_dia)-1]['A']}",
            'area':indicadores_mtto_mes[int(numero_dia)-1]['area'],
            'equipo':indicadores_mtto_mes[int(numero_dia)-1]['equipo'],
            'lista_equipos':indicadores_mtto_mes[int(numero_dia)-1]['lista_equipos'],
            'tipo':indicadores_mtto_mes[int(numero_dia)-1]['tipo'],
            'id_mtto_preventivo':indicadores_mtto_mes[int(numero_dia)-1]['id_mtto_preventivo']
          }
        j += 1
      items.append(dicc)
    self.repeating_panel_mes_calendario.items = items
    self.card_calendario.visible = True

  def fill_indicador(self, dia_prog, indicadores_mtto_mes, item):
    prefijos_tipo = {"PROGRAMADO":"P","REPROGRAMADO":"R","REALIZADO":"OK"}
    prefijos_frecuencia = {"SEMANAL":"W", "MENSUAL":"M", "TRIMESTRAL":"T", "SEMESTRAL":"S","ANUAL":"A"}
    area = indicadores_mtto_mes[dia_prog-1]['area']
    equipo = indicadores_mtto_mes[dia_prog-1]['equipo']
    tipo = indicadores_mtto_mes[dia_prog-1]['tipo']

    if area == "todas":
      if equipo == "todos":
        if tipo == "todos":
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
        elif tipo == item['status_mantenimiento']: #tipo:selected
          indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] = indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] + 1
          indicadores_mtto_mes[dia_prog-1]["lista_equipos"].append({'equipo':item['equipo'],'frecuencia':item['frecuencia'],'id_mtto':item['id_mtto_preventivo'],'operacion':item['operacion']})
          #indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
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
    self.drop_down_tipo.selected_value = "PROGRAMADO"
    if self.drop_down_areas.selected_value != None:
      lista_filtrada = []
      for equipo in self.lista_equipos:
        if self.drop_down_areas.selected_value == equipo[1]['area']:
          lista_filtrada.append(equipo)
      self.drop_down_equipos.items = lista_filtrada
    else:
      self.drop_down_equipos.items = self.lista_equipos
    self.llenar_calendario()
        

  def drop_down_equipos_change(self, **event_args):
    self.drop_down_tipo.selected_value = "PROGRAMADO"
    self.llenar_calendario()

  def drop_down_tipo_change(self, **event_args):
    self.llenar_calendario()

  def button_borrar_click(self, **event_args):
    self.drop_down_areas.selected_value = None
    self.drop_down_equipos.selected_value = None
    self.drop_down_tipo.selected_value = "PROGRAMADO"
    self.llenar_calendario()

  def button_programar_click(self, **event_args):
    datos = {}
    datos.update(self.datos)
    #self.actualizar_form_activo()
    self.abrir_form(MANTENIMIENTO_PREVENTIVO_PROGRAMACION(datos), "bigger")
    """for equipo in self.lista_equipos:
      nombre_equipo = equipo['EQUIPO']
      area = equipo['AREA']
      frecuencia = equipo['FRECUENCIA']
      
      pass"""

  
   
  ##################################################### PRUEBAS #####################################################
    """self.datos['clave_form'] = 'MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO'
    self.datos['modo'] = 'nuevo'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""

    
    """"lista = [["nombre","edad"],["ALFREDO VARELA",'33'],["FERNANDO CORTES",'31'],["MARIO GONZALES",'45']]
    
    datos = anvil.js.call('SUPERSQL',f"SELECT * FROM ? WHERE edad < 40",lista)
    print(datos)""""

    #print(anvil.js.call('prueba',lista))

    

