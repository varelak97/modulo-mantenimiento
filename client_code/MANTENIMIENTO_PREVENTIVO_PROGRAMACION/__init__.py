from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_PROGRAMACIONTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from datetime import datetime, date, timedelta
import calendar

class MANTENIMIENTO_PREVENTIVO_PROGRAMACION(MANTENIMIENTO_PREVENTIVO_PROGRAMACIONTemplate):
  ################################### DEFINICION DE VARIABLES ####################################
  datos = {}

  libro_mttos_preventivos = None
  ws_mtto_preventivos = None
  ws_mttos_preventivos_vista = None
  #mttos_preventivos_registros = None
  #registro_seleccionado = None

  libro_equipos = None
  ws_equipos_vista = None
  registros_equipos_vista = None
  ws_actividades_vista = None
  registros_actividades_vista = None
  #ws_equipos_registros = None #no se ocupa en este form

  actividades_equipos = None
  
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
  ########################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos

    self.set_event_handler('x-guardar_fecha_excluida', self.guardar_fecha_excluida)
    self.set_event_handler('x-eliminar_fecha_excluida', self.eliminar_fecha_excluida)
    self.set_event_handler('x-editar_fecha_excluida', self.editar_fecha_excluida)

    self.set_event_handler('x-enable_disable_guardar', self.enable_disable_guardar)

    self.libro_mttos_preventivos = app_files.mantenimiento_preventivo
    self.ws_mtto_preventivos = self.libro_mttos_preventivos['Registros']
    self.ws_mttos_preventivos_vista = self.libro_mttos_preventivos['Consulta']
    
    
    #self.registros_totales = self.ws_registros_totales.rows

    self.libro_equipos = app_files.mantenimiento_lista_equipos
    self.ws_equipos_vista = self.libro_equipos['VISTA_EQUIPOS']
    self.registros_equipos_vista = self.ws_equipos_vista.rows
    #self.ws_equipos_registros = self.libro_equipos['EQUIPOS'] #no se ocupa en este form

    self.ws_actividades_vista = self.libro_equipos['VISTA_ACTIVIDADES']
    self.registros_actividades_vista = self.ws_actividades_vista.rows

    self.actividades_equipos = self.set_actividades(self.registros_equipos_vista, self.registros_actividades_vista)

    self.repeating_panel_equipos.items = self.get_lista_equipos(self.registros_equipos_vista)#self.ws_equipos_vista.rows)

    self.label_titulo.text = f"PROGRAMACIÓN ANUAL DE MANTENIMIENTO PREVENTIVO {datetime.today().year}"

  ################################ FUNCIONES PERSONALIZADS ########################################
  def set_actividades(self, lista_equipos, lista_actividades):
    lista_total_equipos = []
    for equipo in lista_equipos:
      dict_actividades = {}
      actividades_equipo = []
      index = 1
      for actividad in lista_actividades:
        if equipo['area'] == actividad['area']:
          if int(equipo['id_equipo']) in eval(actividad['id_equipos']):
            dict_actividad = {}
            dict_actividad['id'] = index
            dict_actividad['actividad'] = actividad['actividad']
            actividades_equipo.append(dict_actividad)
            index+=1
      dict_actividades['id_equipo'] = equipo['equipo']
      dict_actividades['actividades'] = actividades_equipo
      lista_total_equipos.append(dict_actividades)
    print(f"lo generador de equipos y actividades:{lista_total_equipos}")
          
      
  
  def editar_fecha_excluida(self, **event_args):
    self.button_agregar_fecha.enabled = False
    self.button_generar_calendario.enabled = False
    filas = self.repeating_panel_fechas_excluidas.get_components()
    for fila in filas:
      componentes_fila = fila.get_components()
      componentes_fila[3].enabled = False #boton editar
      componentes_fila[4].enabled = False #boton borrar
  
  def guardar_fecha_excluida(self, **event_args):
    fechas_excluidas = self.repeating_panel_fechas_excluidas.items
    self.repeating_panel_fechas_excluidas.items = fechas_excluidas
    self.button_agregar_fecha.enabled = True
    self.button_generar_calendario.enabled = True
    
  def eliminar_fecha_excluida(self, indice, **event_args):
    fechas_excluidas = self.repeating_panel_fechas_excluidas.items
    fechas_excluidas.pop(indice)
    for index, fecha in enumerate(fechas_excluidas):
      fecha['index'] = index + 1
    self.repeating_panel_fechas_excluidas.items = fechas_excluidas
    #self.button_agregar_fecha.enabled = True
    
  def enable_disable_guardar(self, id_equipo, status, **event_args):
    self.button_generar_calendario.enabled = status
    for fila in self.repeating_panel_equipos.get_components():
      componentes_fila = fila.get_components()
      if componentes_fila[12].text != id_equipo:
        componentes_fila[0].enabled = status
    
  def get_lista_equipos(self, equipos):
    lista_equipos = []
    for index, equipo in enumerate(list(equipos).copy()):
      temp = dict(equipo)
      temp['index'] = index + 1
      temp['semanal'] = ""
      temp['mensual'] = ""
      temp['trimestral'] = ""
      temp['semestral'] = ""
      temp['anual'] = ""
      lista_equipos.append(temp)
    print(f"lo que regresa:{lista_equipos}")
    return lista_equipos

  def get_actividades(self, equipo, id_equipo, area, frecuencia_mtto):
    """actividades = []
    for actividad in self.registros_actividades_vista:
      if id_equipo in eval(actividad[])"""
    """actividades = None
    if area == "IMPRESIÓN":
      if equipo == "IMPRESORA MIMAKI":
        actividades = self.actividades_equipo_mimaki_mensual
      elif equipo == "SPS":
        actividades = self.actividades_equipo_sps_mensual
      elif equipo == "IMPRESORA OFFSET":
        actividades = self.actividades_equipo_offset_trimestral
      elif equipo == "HORNO 1":
        if frecuencia_mtto == "SEMANAL":
          actividades = self.actividades_equipo_horno_1_semanal
        elif frecuencia_mtto == "MENSUAL":
          actividades = self.actividades_equipo_horno_1_mensual
        elif frecuencia_mtto == "SEMESTRAL":
          actividades = self.actividades_equipo_horno_1_semestral
      elif equipo == "HORNO 2":
        actividades = self.actividades_equipo_horno_2_semestral
      elif equipo == "HORNO 3":
        actividades = self.actividades_equipo_horno_3_semestral
      elif equipo == "HORNO 4":
        actividades = self.actividades_equipo_horno_4_semestral
      elif equipo == "HORNO 5":
        actividades = self.actividades_equipo_horno_5_semestral
      elif equipo == "ATMA 80" or equipo == "ATMA 710":
        self.actividades_equipos_atma_trimestral += self.actividades_equipos_atma80_710_trimestral
        self.actividades_equipos_atma_trimestral = sorted(self.actividades_equipos_atma_trimestral, key=lambda d: d['id']) 
        actividades = self.actividades_equipos_atma_trimestral
      else:
        for index,actividad in enumerate(self.actividades_equipos_atma_trimestral):
          actividad['id'] = index + 1
        actividades = self.actividades_equipos_atma_trimestral
    ################################################# SUAJE ########################################################
    elif area == "SUAJE":
      if equipo == "EMBOSADORA":
        actividades = self.actividades_equipo_embosadora_trimestral
      else:
        actividades = self.actividades_equipos_suaje_trimestral
    ################################################# MANUALES ########################################################
    elif area == "MANUALES":
      actividades = self.actividades_equipo_embolsadora_trimestral
    ################################################# LASER ########################################################
    elif area == "LÁSER":
      if frecuencia_mtto == "SEMANAL":
        actividades = self.actividades_equipos_laser_semanal
      elif frecuencia_mtto == "MENSUAL":
        actividades = self.actividades_equipos_laser_mensual
    ################################################# CALIDAD ########################################################
    elif area == "CALIDAD":
      if equipo == "MESA DE COORDENADAS X-Y":
        actividades = self.actividades_equipo_mesa_coordenadas_trimestral
      elif equipo != "PROBADOR ELÉCTRICO 2 (CC015)":
        self.actividades_equipos_probadores_electricos_mensual += self.actividades_equipo_probador_electrico_2_mensual
        actividades = self.actividades_equipos_probadores_electricos_mensual
      else:
        actividades = self.actividades_equipos_probadores_electricos_mensual
    ################################################# REVELADO ########################################################
    elif area == "REVELADO":
      if equipo == "INSOLADORA":
        actividades = self.actividades_equipo_insoladora_semestral
      elif equipo == "AFILADOR DE RASEROS":
        actividades = self.actividades_equipo_afilador_raseros_trimestral
    ################################################# ENSAMBLE ########################################################
    elif area == "ENSAMBLE":
      if equipo == "PICK&PLACE 2":
        actividades = self.actividades_equipo_pickAndPlace_2_trimestral
      elif equipo == "PICK&PLACE 3":
        actividades = self.actividades_equipo_pickAndPlace_3_trimestral
      elif equipo == "TROQUELADORA MANUAL":
        actividades = self.actividades_equipo_troqueladora_manual_semestral
      elif equipo == "DISPENSADORES":
        actividades = self.actividades_equipos_dispensadores_semestral
      else:
        actividades = self.actividades_equipos_laminadoras_semestral
    ################################################# ALMACEN MP ########################################################
    elif area == "ALMACÉN MP":
      if equipo == "HOJEADORA":
        actividades = self.actividades_equipo_hojeadora_trimestral
      else:
        actividades = self.actividades_equipos_guillotinas_semestral"""
    return actividades

  def generar_programa_anual(self, equipo, area, fecha_inicial, frecuencia, id_equipo, id_mtto_preventivo):
    dias_offset = {
      "SEMANAL":1,
      "MENSUAL":1,
      "TRIMESTRAL":3,
      "SEMESTRAL":6,
      "ANUAL":1
    }
    fechas_excluir = self.repeating_panel_fechas_excluidas.items
    fecha = fecha_inicial
    temp = fecha_inicial
    anio_actual = datetime.today().year
    
    while fecha.year == anio_actual:
      dict_mtto = {
        "id_mtto_preventivo": id_mtto_preventivo,
        "fecha_programada":fecha,
        "area":area,
        "equipo":equipo,
        "frecuencia":frecuencia,
        "status_mantenimiento":"PROGRAMADO",
        "actividades":self.get_actividades(equipo, id_equipo, area, frecuencia),
        "id_usuario_registrador":self.datos['id_usuario_erp'],
        "usuario_registrador":"ALFREDO VARELA CELESTINO",
        "operacion":"creacion",
        "marca_temporal":datetime.now(),
        "comentarios":"",
        "registro_principal": 1
      }
      id_mtto_preventivo += 1
      self.ws_mtto_preventivos.add_row(**dict_mtto)

      fecha = temp

      #siguiente fecha
      if frecuencia == "SEMANAL":
        fecha += timedelta(days=7)
      elif frecuencia == "MENSUAL":
        mes_siguiente = fecha.month + 1 
        if mes_siguiente > 12:
          fecha = fecha.replace(month=1, year = anio_actual + 1)
        else:
          fecha = fecha.replace(month=mes_siguiente)
      elif frecuencia == "TRIMESTRAL":
        trimestre_siguiente = fecha.month + 3
        if trimestre_siguiente > 12:
          fecha = fecha.replace(month=1, year = anio_actual + 1)
        else:
          fecha = fecha.replace(month=trimestre_siguiente)
      elif frecuencia == "SEMESTRAL":
        semestre_siguiente = fecha.month + 6
        if semestre_siguiente > 12:
          fecha = fecha.replace(month=1, year = anio_actual + 1)
        else:
          fecha = fecha.replace(month=semestre_siguiente)
      elif frecuencia == "ANUAL":
        mes_anio_siguiente = fecha.month + 12
        if mes_anio_siguiente > 12:
          fecha = fecha.replace(month=1, year = anio_actual + 1)
      
      temp = fecha
      
      #fecha += timedelta(days = dias_offset[frecuencia])
      
      # ******************** excluir fechas ***********************
      if fechas_excluir != None:
        for fecha_excluir in fechas_excluir:
          fecha_inicial = fecha_excluir['fecha_inicial']
          fecha_final = fecha_excluir['fecha_final']
          if fecha_inicial != "":
            if fecha_final != "":
              if fecha > fecha_inicial and fecha < fecha_final:
                resta_lim_inferior = fecha - fecha_inicial
                resta_lim_superior = fecha_final - fecha_inicial
                if resta_lim_inferior > resta_lim_superior:
                  fecha = fecha_final + timedelta(days=1)
                  if fecha.weekday() == 5:
                    fecha += timedelta(days=2)
                  elif fecha.weekday() == 6:
                    fecha += timedelta(days=1)
                elif resta_lim_inferior < resta_lim_superior:
                  fecha = fecha_inicial + timedelta(days=-1)
                  if fecha.weekday() == 5:
                    fecha += timedelta(days=-1)
                  elif fecha.weekday() == 6:
                    fecha += timedelta(days=-2)
                else:
                  fecha = fecha_final + timedelta(days=1)
                  if fecha.weekday() == 5:
                    fecha += timedelta(days=2)
                  elif fecha.weekday() == 6:
                    fecha += timedelta(days=1)
            else:
              fecha = fecha_inicial + timedelta(days=1)
              if fecha.weekday() == 5:
                fecha += timedelta(days=2)
              elif fecha.weekday() == 6:
                fecha += timedelta(days=1)
          else:
            if fecha_final != "":
              fecha = fecha_inicial + timedelta(days=1)
              if fecha.weekday() == 5:
                fecha += timedelta(days=2)
              elif fecha.weekday() == 6:
                fecha += timedelta(days=1)
      # ******************** end excluir fechas ***********************
      
      #agrega offset si dia cae en sabado o domingo
      if fecha.weekday() == 5: #sabado
        fecha += timedelta(days = -1)
      elif fecha.weekday() == 6: #domingo
        fecha += timedelta(days = 1)

      #fecha = temp
      
    return id_mtto_preventivo
  ############################################ EVENTOS ############################################
  def button_generar_calendario_click(self, **event_args):
    equipos_programados = self.repeating_panel_equipos.items
    status = False
    registros_vista_mttos = self.ws_mttos_preventivos_vista.rows
    id_mtto_preventivo = max([int(row['id_mtto_preventivo']) for row in registros_vista_mttos]) + 1 if len(registros_vista_mttos) > 0 else 1
    with Notification("Insertando registros en la base de datos...", title="GENERANDO PROGRAMA ANUAL", style="info"):
      for equipo in equipos_programados:
        if equipo['semanal'] != "":
          id_mtto_preventivo = self.generar_programa_anual(equipo['equipo'], equipo['area'], equipo['semanal'], "SEMANAL", equipo['id_equipo'], id_mtto_preventivo)
          status = True
        if equipo['mensual'] != "":
          id_mtto_preventivo = self.generar_programa_anual(equipo['equipo'], equipo['area'], equipo['mensual'], "MENSUAL", equipo['id_equipo'], id_mtto_preventivo)
          status = True
        if equipo['trimestral'] != "":
          id_mtto_preventivo = self.generar_programa_anual(equipo['equipo'], equipo['area'], equipo['trimestral'], "TRIMESTRAL", equipo['id_equipo'], id_mtto_preventivo)
          status = True
        if equipo['semestral'] != "":
          id_mtto_preventivo = self.generar_programa_anual(equipo['equipo'], equipo['area'], equipo['semestral'], "SEMESTRAL", equipo['id_equipo'], id_mtto_preventivo)
          status = True
        if equipo['anual'] != "":
          id_mtto_preventivo = self.generar_programa_anual(equipo['equipo'], equipo['area'], equipo['anual'], "ANUAL", equipo['id_equipo'], id_mtto_preventivo)
          status = True
    if status: 
      Notification("Programa anual generado correctamente!", title="'ÉXITO!'", style="success")
      self.raise_event("x-close-alert",value=True)
    else: 
      alert("Por favor, llene al menos las fechas de un equipo", title="ERROR AL GUARDAR!", buttons=[("ACEPTAR", "ACEPTAR")])

  def button_agregar_fecha_click(self, **event_args):
    self.button_agregar_fecha.enabled = False
    self.button_generar_calendario.enabled = False
    fechas_excluidas = self.repeating_panel_fechas_excluidas.items if self.repeating_panel_fechas_excluidas.items != None else []
    indice = len(fechas_excluidas)
    fechas_excluidas.append({'index':indice + 1,'fecha_inicial':"", 'fecha_final':""})
    self.repeating_panel_fechas_excluidas.items = fechas_excluidas
    filas = self.repeating_panel_fechas_excluidas.get_components()
    for fila in filas:
      componentes_fila = fila.get_components()
      label_indice = int(componentes_fila[0].text) - 1
      datepicker_fecha_1 = componentes_fila[5].get_components()[0]
      datepicker_fecha_2 = componentes_fila[6].get_components()[0]
      label_fecha_1 = componentes_fila[1]
      label_fecha_2 = componentes_fila[2]
      boton_editar = componentes_fila[3]
      boton_eliminiar = componentes_fila[4]


      if label_indice == indice:
        datepicker_fecha_1.visible = True
        datepicker_fecha_2.visible = True
        label_fecha_1.visible = False
        label_fecha_2.visible = False
        boton_editar.icon = "fa:check"
      else:
        boton_editar.enabled = False
      
      boton_eliminiar.enabled = False
      
      #label_indice = int(componentes_fila[0].text) - 1
      #componentes_fila[2].enabled = False #boton editar
      #componentes_fila[4].enabled = False #boton borrar
      #if label_indice == indice:
      #  componentes_fila[3].visible = True #column panel de textbox y su boton"""
    
    
    """numero_anio = datetime.today().year
    total_dias = 366 if self.anio_bisiesto(anio_actual) else 365

    for numero_mes in range(1, 4):
      inicio_mes = 1 if numero_mes != 1 else 2
      total_dias_mes = calendar.monthrange(numero_anio, numero_mes)[1]
      for numero_dia in range(inicio_mes, int(total_dias_mes) + 1):
        fecha_dia = date(numero_anio,numero_mes,numero_dia)"""
      
    """dias_fin_semana = [5,6]
    lista_mttos_programados = []
    index = 1
    for equipo in self.lista_equipos:
      for frecuencia in equipo['FRECUENCIA']:
        if frecuencia == "SEMANAL":
          pass
        dict_mtto = {
          "id_mtto_preventivo": index,
          "fecha_programada":f"{self.datos['anio']}-{self.datos['mes']}-{self.datos['dia']}",
          "area":equipo['AREA'],
          "equipo":equipo['EQUIPO'],
          "frecuencia":frecuencia,
          "status_mantenimiento":"PROGRAMADO",
          "actividades":self.get_actividades(equipo, frecuencia),
          "id_usuario_registrador":self.datos['id_usuario_erp'],
          "usuario_registrador":"pendiente",
          "operacion":"creacion",
          "marca_temporal":datetime.now(),
          "comentarios":"",
          "registro_principal": 1
        }
        index += 1
        lista_mttos_programados.append(dict_mtto)
    print(lista_mttos_programados)"""
    
  """def button_guardar_click(self, **event_args):
    with Notification("Registrando en la base de datos...",title="GUARDANDO."):
      dict_mtto = {
        "id_mtto_preventivo":(max([int(item['id_mtto_preventivo']) for item in self.registros_totales]) + 1) if len(self.registros_totales) > 0 else 1,
        "fecha_programada":f"{self.datos['anio']}-{self.datos['mes']}-{self.datos['dia']}",
        "area":self.drop_down_area.selected_value,
        "equipo":self.drop_down_equipo.selected_value['EQUIPO'],
        "frecuencia":self.drop_down_frecuencia.selected_value,
        "status_mantenimiento":"PROGRAMADO",
        "actividades":self.get_actividades(self.drop_down_equipo.selected_value, self.drop_down_frecuencia.selected_value),
        "id_usuario_registrador":self.datos['id_usuario_erp'],
        "usuario_registrador":"pendiente",
        "operacion":"creacion",
        "marca_temporal":datetime.now(),
        "comentarios":"",
        "registro_principal": 1
      }
      self.ws_registros_totales.add_row(**dict_mtto)
    Notification("Registro guardado correctamente.", title="GUARDADO.", style="success").show()
    self.raise_event("x-close-alert",value="registro_guardado")"""

  

  """def drop_down_area_change(self, **event_args):
    area_seleccionada = self.drop_down_area.selected_value
    if area_seleccionada != None:
      equipos_area = []
      frecuencias = []
      self.drop_down_equipo.enabled = True
      
      for item in self.lista_equipos:
        if item[1]["AREA"] == area_seleccionada:
          equipos_area.append(item)
      
      self.drop_down_equipo.items = equipos_area
      self.button_guardar.enabled = False
      self.drop_down_frecuencia.selected_value = None
      self.drop_down_frecuencia.enabled = False
    else:
      self.drop_down_equipo.enabled = False
      self.drop_down_equipo.selected_value = None
      self.drop_down_frecuencia.enabled = False
      self.drop_down_frecuencia.selected_value = None
      self.button_guardar.enabled = False

  def drop_down_equipo_change(self, **event_args):
    equipo_seleccionado = self.drop_down_equipo.selected_value
    if equipo_seleccionado != None:
      lista_frecuencia_mtto = equipo_seleccionado["FRECUENCIA"]
      if len(lista_frecuencia_mtto) == 1:
        self.drop_down_frecuencia.items = lista_frecuencia_mtto
        self.drop_down_frecuencia.selected_value = lista_frecuencia_mtto[0]
        self.drop_down_frecuencia.enabled = False
        self.button_guardar.enabled = True
      else:
        self.drop_down_frecuencia.items = lista_frecuencia_mtto
        self.drop_down_frecuencia.enabled = True
    else:
      self.drop_down_frecuencia.selected_value = None
      self.drop_down_frecuencia.enabled = None
      self.button_guardar.enabled = False

  def drop_down_frecuencia_change(self, **event_args):
    if self.drop_down_frecuencia.selected_value != None:
      self.button_guardar.enabled = True
    else:
      self.button_guardar.enabled = False"""

    
