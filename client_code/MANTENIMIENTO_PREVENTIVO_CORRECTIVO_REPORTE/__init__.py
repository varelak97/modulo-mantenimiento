from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
from datetime import datetime, date

class MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTETemplate):
  ################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  libro_solicitudes_mtto = None
  ws_solicitudes_mtto = None
  solicitudes_mtto = None
  solicitud_registro_actual = None
  
  libro_mtto_corr_prev = None
  ws_mtto_corr_prev = None
  mtto_corr_prev_todos = None
  mtto_corr_prev_reporte = None

  libro_equipos = None
  ws_equipos_vista = None
  registros_equipos_vista = None
  ws_areas_vista = None
  registros_areas_vista = None

  """lista_areas = [
    "IMPRESIÓN",
    "SUAJE",
    "MANUALES",
    "LÁSER",
    "CALIDAD",
    "REVELADO",
    "ENSAMBLE",
    "ALMACÉN MP",
    "SERVICIOS GENERALES"
  ]
  lista_equipos = [
    ("ATMA 57",{"EQUIPO":"ATMA 57","AREA":"IMPRESIÓN"}),
    ("ATMA 71",{"EQUIPO":"ATMA 71","AREA":"IMPRESIÓN"}),
    ("ATMA 70",{"EQUIPO":"ATMA 70","AREA":"IMPRESIÓN"}),
    ("ATMA 45",{"EQUIPO":"ATMA 45","AREA":"IMPRESIÓN"}),
    ("ATMA 710",{"EQUIPO":"ATMA 710","AREA":"IMPRESIÓN"}),
    ("ATMA 80",{"EQUIPO":"ATMA 80","AREA":"IMPRESIÓN"}),
    ("HORNO 1",{"EQUIPO":"HORNO 1","AREA":"IMPRESIÓN"}),
    ("HORNO 2",{"EQUIPO":"HORNO 2","AREA":"IMPRESIÓN"}),
    ("HORNO 3",{"EQUIPO":"HORNO 3","AREA":"IMPRESIÓN"}),
    ("HORNO 4",{"EQUIPO":"HORNO 4","AREA":"IMPRESIÓN"}),
    ("HORNO 5",{"EQUIPO":"HORNO 5","AREA":"IMPRESIÓN"}),
    ("IMPRESORA MIMAKI",{"EQUIPO":"IMPRESORA MIMAKI","AREA":"IMPRESIÓN"}),
    ("IMPRESORA OFFSET",{"EQUIPO":"IMPRESORA OFFSET","AREA":"IMPRESIÓN"}),
    ("SPS",{"EQUIPO":"SPS","AREA":"IMPRESIÓN"}),
    ("SUAJADORA 1",{"EQUIPO":"SUAJADORA 1","AREA":"SUAJE"}),
    ("SUAJADORA 2",{"EQUIPO":"SUAJADORA 2","AREA":"SUAJE"}),
    ("SUAJADORA 3",{"EQUIPO":"SUAJADORA 3","AREA":"SUAJE"}),
    ("SUAJADORA 4",{"EQUIPO":"SUAJADORA 4","AREA":"SUAJE"}),
    ("EMBOSADORA",{"EQUIPO":"EMBOSADORA","AREA":"SUAJE"}),
    ("LÁSER V-460",{"EQUIPO":"LÁSER V-460","AREA":"LÁSER"}),
    ("LÁSER M-300",{"EQUIPO":"LÁSER M-300","AREA":"LÁSER"}),
    ("LÁSER VLS-360",{"EQUIPO":"LÁSER VLS-360","AREA":"LÁSER"}),
    ("MESA DE COORDENADAS X-Y",{"EQUIPO":"MESA DE COORDENADAS X-Y","AREA":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 2 (CC015)",{"EQUIPO":"PROBADOR ELÉCTRICO 2 (CC015)","AREA":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 3 (C0025)",{"EQUIPO":"PROBADOR ELÉCTRICO 3 (C0025)","AREA":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 4 (C0028)",{"EQUIPO":"PROBADOR ELÉCTRICO 4 (C0028)","AREA":"CALIDAD"}),
    ("INSOLADORA",{"EQUIPO":"INSOLADORA","AREA":"REVELADO"}),
    ("AFILADOR DE RASEROS",{"EQUIPO":"AFILADOR DE RASEROS","AREA":"REVELADO"}),
    ("LAMINADORA 1",{"EQUIPO":"LAMINADORA 1","AREA":"ENSAMBLE"}),
    ("LAMINADORA 2",{"EQUIPO":"LAMINADORA 2","AREA":"ENSAMBLE"}),
    ("LAMINADORA 3",{"EQUIPO":"LAMINADORA 3","AREA":"ENSAMBLE"}),
    ("PICK&PLACE 2",{"EQUIPO":"PICK&PLACE 2","AREA":"ENSAMBLE"}),
    ("TROQUELADORA MANUAL",{"EQUIPO":"TROQUELADORA MANUAL","AREA":"ENSAMBLE"}),
    ("DISPENSADORES",{"EQUIPO":"DISPENSADORES","AREA":"ENSAMBLE"}),
    ("PICK&PLACE 3",{"EQUIPO":"PICK&PLACE 3","AREA":"ENSAMBLE"}),
    ("GUILLOTINA 1",{"EQUIPO":"GUILLOTINA 1","AREA":"ALMACÉN MP"}),
    ("GUILLOTINA 2",{"EQUIPO":"GUILLOTINA 2","AREA":"ALMACÉN MP"}),
    ("GUILLOTINA 3",{"EQUIPO":"GUILLOTINA 3","AREA":"ALMACÉN MP"}),
    ("HOJEADORA",{"EQUIPO":"HOJEADORA","AREA":"ALMACÉN MP"}),
    ("EMBOLSADORA",{"EQUIPO":"EMBOLSADORA","AREA":"MANUALES"})
  ]"""
  lista_equipos = None

  lista_text_components = None
  lista_drop_downs = None
  lista_date_pickers = None
  lista_radio_buttons = None

  def __init__(self, datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.set_event_handler('x-guardar_comentario', self.guardar_comentario)
    self.set_event_handler('x-eliminar_comentario', self.eliminar_comentario)
    self.set_event_handler('x-editar_comentario', self.editar_comentario)
    
    self.lista_drop_downs = [
      self.drop_down_area,
      self.drop_down_equipo,
      self.drop_down_refaccion,
      self.drop_down_servicio,
      self.drop_down_tipo_mantenimiento
    ]
    self.lista_text_components = [
      self.text_box_folio,
      self.text_box_persona_ejecuta_mtto,
      self.text_box_persona_recibe_conformidad,
      self.text_area_descripcion_falla,
      self.text_area_actividades
    ]
    self.lista_date_pickers = [
      self.date_picker_fecha_hora_solicitud,
      self.date_picker_fecha_hora_inicial,
      self.date_picker_fecha_hora_final
    ]

    self.lista_radio_buttons = [
      self.radio_button_deterioro,
      self.radio_button_incumplimiento,
      self.radio_button_mal_uso,
      self.radio_button_omision
    ]
    
    self.datos = datos

    self.libro_equipos = app_files.mantenimiento_lista_equipos
    self.ws_equipos_vista = self.libro_equipos['VISTA_EQUIPOS']
    self.registros_equipos_vista = self.ws_equipos_vista.rows
    self.ws_areas_vista = self.libro_equipos['VISTA_AREAS']
    self.registros_areas_vista = self.ws_areas_vista.rows

    self.libro_mtto_corr_prev = app_files.mantenimiento_correctivo_preventivo_programado
    self.ws_mtto_corr_prev = self.libro_mtto_corr_prev['Registros']
    self.mtto_corr_prev_todos = self.ws_mtto_corr_prev.rows

    self.drop_down_area.items = self.get_lista_areas()
    self.lista_equipos = self.get_lista_equipos()
    self.drop_down_equipo.items = self.lista_equipos

    self.llenar_reporte()
    
  ################################ FUNCIONES PERSONALIZADS ########################################
  def get_lista_areas(self):
    equipos_tuplas = []
    for fila in self.registros_areas_vista:
      if(fila['nivel'] == '1'):
        equipos_tuplas.append(fila['area'])
    return equipos_tuplas
  def get_lista_equipos(self):
    equipos_tuplas = []
    for fila in self.registros_equipos_vista:
      equipos_tuplas.append((fila['equipo'],{"equipo":fila['equipo'],"AREA":fila['area']}))
    return equipos_tuplas
    
  def editar_comentario(self, **event_args):
    self.button_agregar_comentario.enabled = False
    filas = self.repeating_panel_comentarios.get_components()
    for fila in filas:
      componentes_fila = fila.get_components()
      componentes_fila[2].enabled = False #boton editar
      componentes_fila[4].enabled = False #boton borrar
  
  def guardar_comentario(self, datos, **event_args):
    print("entro a guardar comentario")
    comentarios = self.repeating_panel_comentarios.items
    comentarios[datos['indice']]['comentario'] = datos['comentario']
    self.repeating_panel_comentarios.items = comentarios
    self.button_agregar_comentario.enabled = True
    
  def eliminar_comentario(self, indice, **event_args):
    comentarios = self.repeating_panel_comentarios.items
    comentarios.pop(indice)
    for index, comentario in enumerate(comentarios):
      comentario['index'] = index + 1
    self.repeating_panel_comentarios.items = comentarios
    self.button_agregar_comentario.enabled = True
    
  def llenar_reporte(self):
    if self.datos['modo'] == "nuevo":
      self.libro_solicitudes_mtto = app_files.mantenimiento_solicitudes
      self.ws_solicitudes_mtto = self.libro_solicitudes_mtto['Registros']
      self.solicitudes_mtto = self.ws_solicitudes_mtto.rows
      #self.solicitud_registro_actual = self.solicitudes_mtto[int(datos['id_renglon'])]
      for item in self.solicitudes_mtto:
        if item['id_solicitud_mtto'] == self.datos['id_solicitud_mtto'] and item['registro_principal'] == '1':
          self.solicitud_registro_actual = item
          break
      
      self.date_picker_fecha_hora_solicitud.date = self.solicitud_registro_actual['fecha_reporte']
      self.text_box_folio.text = self.solicitud_registro_actual['folio']
      self.drop_down_area.selected_value = self.solicitud_registro_actual['area']
      self.text_box_persona_recibe_conformidad.text = self.solicitud_registro_actual['persona_reporta']
      self.text_box_persona_ejecuta_mtto.text = self.datos['nombre_usuario']
      self.drop_down_area_change()
      for item in self.drop_down_equipo.items:
        if item[1]['EQUIPO'] == self.solicitud_registro_actual['equipo']:
          self.drop_down_equipo.selected_value = item[1]
          break
    elif self.datos['modo'] == "editor":
      for reg in self.mtto_corr_prev_todos:
        if reg['id_mtto_preventivo_correctivo'] == self.datos['id_mtto_preventivo_correctivo'] and reg['registro_principal'] == '1':
          self.mtto_corr_prev_reporte = reg
          break
      self.llenar_campos(self.mtto_corr_prev_reporte)
    elif self.datos['modo'] != "nuevo" and self.datos['modo'] != "editor":
    #elif self.datos['modo'] == "visor" or self.datos['modo'] == "visor_by_folio":
      if self.datos['modo'] == "visor":
        for reg in self.mtto_corr_prev_todos:
          if reg['id_mtto_preventivo_correctivo'] == self.datos['id_mtto_preventivo_correctivo'] and reg['registro_principal'] == '1':
            self.mtto_corr_prev_reporte = reg
            break
      else:
        for reg in self.mtto_corr_prev_todos:
          if reg['folio'] == self.datos['folio'] and reg['registro_principal'] == '1':
            self.mtto_corr_prev_reporte = reg
            break
      self.llenar_campos(self.mtto_corr_prev_reporte)
      self.habilitar_deshabilitar_campos(False)
      if self.datos['modo'] == "validacion":
          self.button_guardar.text = "APROBAR REPORTE"
          self.button_guardar.icon = "fa:check"
          self.button_guardar.background = app.theme_colors['Blue']
          self.button_guardar.foreground = app.theme_colors['White']
          self.button_guardar.enabled = True
          self.button_rechazar.visible = True
      else:
        self.button_guardar.enabled = False
      
      

  def llenar_campos(self, registro):
    self.date_picker_fecha_hora_solicitud.date = registro['fecha_hora_solicitud']
    self.drop_down_area.selected_value = registro['area']
    self.drop_down_area_change()
    self.drop_down_equipo.selected_value = [equipo[1] for equipo in self.lista_equipos if registro['equipo'] in equipo][0]
    self.text_box_folio.text = registro['folio']
    self.text_area_descripcion_falla.text = registro['descripcion_falla']
    self.drop_down_refaccion.selected_value = registro['requiere_refaccion']
    self.drop_down_servicio.selected_value = registro['requiere_servicio']
    self.drop_down_tipo_mantenimiento.selected_value = registro['tipo_mantenimiento']
    self.drop_down_tipo_mantenimiento_change()
    for radio in self.lista_radio_buttons:
      if radio.text == registro['clasificacion_mtto']:
        radio.selected = True
    self.date_picker_fecha_hora_inicial.date = registro['fecha_hora_inicial']
    self.text_area_actividades.text = registro['actividades_mtto']
    self.date_picker_fecha_hora_final.date = registro['fecha_hora_final']
    self.text_box_persona_ejecuta_mtto.text = registro['persona_ejecuta_mtto']
    self.text_box_persona_recibe_conformidad.text = registro['persona_recibe_conformidad']
    self.repeating_panel_comentarios.items = eval(registro['comentarios_mantenimiento']) if registro['comentarios_mantenimiento'] != "" else None

  def valida_campos(self):
    status = True
    respuesta = {}
    for item in self.lista_text_components:
      if item.text == "":
        status = False
      else:
        respuesta[item.tag] = item.text
    for index,item in enumerate(self.lista_drop_downs):
      if item.selected_value == None:
        status = False
      else:
        if index == 1:
          respuesta[item.tag] = item.selected_value['EQUIPO']
        else:
          respuesta[item.tag] = item.selected_value
    for item in self.lista_date_pickers:
      if item.date == None:
        status = False
      else:
        respuesta[item.tag] = item.date
    if self.radio_button_mal_uso.get_group_value() == None:
      status = False
    else:
      respuesta['clasificacion_mtto'] = self.radio_button_mal_uso.get_group_value()

    if not status:
      return status
    return respuesta

  def habilitar_deshabilitar_campos(self, estado):
    for item in self.lista_date_pickers:
      item.enabled = estado
    for item in self.lista_drop_downs:
      item.enabled = estado
    for item in self.lista_radio_buttons:
      item.enabled = estado
    for item in self.lista_text_components:
      item.enabled = estado
    self.data_row_panel_comentarios.visible = estado
    for row in self.repeating_panel_comentarios.get_components():
      componentes_row = row.get_components()
      componentes_row[1].enabled = estado
      componentes_row[2].enabled = estado
  ############################################ EVENTOS ############################################

  def drop_down_tipo_mantenimiento_change(self, **event_args):
    if self.drop_down_tipo_mantenimiento.selected_value == "CORRECTIVO":
      self.column_panel_tipo_mtto.visible = True
      self.column_panel_clasificacion.visible = True
      self.label_titulo_mtto_preventivo_correctivo.text = "MANTENIMIENTO PREVENTIVO CORRECTIVO"
    elif self.drop_down_tipo_mantenimiento.selected_value == "PREVENTIVO PROGRAMADO":
      self.column_panel_tipo_mtto.visible = True
      self.column_panel_clasificacion.visible = False
      self.label_titulo_mtto_preventivo_correctivo.text = "MANTENIMIENTO PREVENTIVO PROGRAMADO"
    else:
      self.column_panel_tipo_mtto.visible = False
      self.column_panel_clasificacion.visible = False
      self.label_titulo_mtto_preventivo_correctivo.text = "TIPO DE MANTENIMIENTO"

  def drop_down_area_change(self, **event_args):
    area_seleccionada = self.drop_down_area.selected_value
    if area_seleccionada != None:
      equipos_area = []
      for item in self.lista_equipos:
        if item[1]["AREA"] == area_seleccionada:
          equipos_area.append(item)
      self.drop_down_equipo.items = equipos_area
      #self.label_titulo_area.text = area_seleccionada
    else:
      self.drop_down_equipo.enabled = False
      self.drop_down_equipo.selected_value = None
      #self.label_titulo_area.text = "AREA"
      #self.button_enviar.enabled = False
      #self.text_area_anomalia.enabled = False

  def button_guardar_click(self, **event_args):
    respuesta = self.valida_campos()
    if respuesta == False:
      alert("Por favor, llene todos los campos!",title="ERROR!")
    else:
      if self.datos['modo'] == "nuevo":
        with Notification("Guardando reporte...", title="GUARDANDO.", style="info"):
          respuesta['id_mtto_preventivo_correctivo'] = (max([int(item['id_mtto_preventivo_correctivo']) for item in self.mtto_corr_prev_todos]) + 1) if len(self.mtto_corr_prev_todos) > 0 else 1
          respuesta['descripcion_problema'] = self.solicitud_registro_actual['descripcion_anomalia']
          respuesta['comentarios_mantenimiento'] = self.repeating_panel_comentarios.items if self.repeating_panel_comentarios.items != None else ""
          respuesta['id_usuario_registrador'] = self.datos['id_usuario_erp']
          respuesta['usuario_registrador'] = self.datos['nombre_usuario']
          respuesta['operacion'] = "creacion"
          respuesta['marca_temporal'] = datetime.now()
          respuesta['comentarios'] = "reporte generado"
          respuesta['registro_principal'] = 1
          self.ws_mtto_corr_prev.add_row(**respuesta)
          
          registro_solicitud_editado = dict(self.solicitud_registro_actual).copy() #self.solicitud_registro_actual['mtto_realizado'] = 1 
          self.solicitud_registro_actual['registro_principal'] = 0

          registro_solicitud_editado['id_usuario_registrador'] = self.datos['id_usuario_erp']
          registro_solicitud_editado['usuario_registrador'] = self.datos['nombre_usuario']
          registro_solicitud_editado['operacion'] = "edicion"
          registro_solicitud_editado['marca_temporal'] = datetime.now()
          registro_solicitud_editado['mtto_realizado'] = 1
          self.ws_solicitudes_mtto.add_row(**registro_solicitud_editado)
          ##################### seguir aqui!!!!!!!!!!!!!!!!! ##############################
      elif self.datos['modo'] == "editor":   
        alert("mod editor")
        with Notification("Actualizando reporte...", title="GUARDANDO.", style="info"):
          registro_edicion = dict(self.mtto_corr_prev_reporte).copy() 
          self.mtto_corr_prev_reporte['registro_principal'] = 0
          registro_edicion.update(respuesta)
          registro_edicion['marca_temporal'] = datetime.now()
          registro_edicion['comentarios_mantenimiento'] = self.repeating_panel_comentarios.items if self.repeating_panel_comentarios.items != None else ""
          registro_edicion['id_usuario_registrador'] = self.datos['id_usuario_erp']
          registro_edicion['usuario_registrador'] = self.datos['nombre_usuario']
          registro_edicion['operacion'] = "edicion"
          registro_edicion['comentarios'] = "reporte editado"
          self.ws_mtto_corr_prev.add_row(**registro_edicion)
      elif self.datos['modo'] == "validacion":
        with Notification("Validando cierre de reporte...", title="GUARDANDO.", style="info"):
          self.libro_solicitudes_mtto = app_files.mantenimiento_solicitudes
          self.ws_solicitudes_mtto = self.libro_solicitudes_mtto['Registros']
          self.solicitudes_mtto = self.ws_solicitudes_mtto.rows
          solicitud_actual = None
          for solicitud in self.solicitudes_mtto:
            if solicitud['folio'] == self.datos['folio'] and int(solicitud['registro_principal']) == 1:
              solicitud_actual = solicitud
              break
          if solicitud_actual != None:
            cierre_solicitud = dict(solicitud_actual).copy()
            solicitud_actual['registro_principal'] = 0
            cierre_solicitud['vobo_solicitante'] = 1
            cierre_solicitud['marca_temporal'] = datetime.now()
            cierre_solicitud['id_usuario_registrador'] = self.datos['id_usuario_erp']
            cierre_solicitud['usuario_registrador'] = self.datos['nombre_usuario']
            cierre_solicitud['operacion'] = "edicion"
            cierre_solicitud['comentarios'] = "solicitud cerrada"
            self.ws_solicitudes_mtto.add_row(**cierre_solicitud)         
      if self.datos['modo'] == "validacion":
        Notification("Solicitud validada y cerrada correctamente!", title="ÉXITO!", style="success").show()
      else:
        Notification("Reporte guardado correctamente!", title="ÉXITO!", style="success").show()
      self.raise_event("x-close-alert",value="registro_guardado")

  def button_rechazar_click(self, **event_args):
    texto = TextArea()
    respuesta = alert(title="MOTIVO DEL RECHAZO:", content = texto, large=True, buttons=[("ENVIAR COMENTARIOS",True), ("SALIR", False)])
    if respuesta:
      alert(f"enviando correo con texto:{texto.text} y folio:{self.text_box_folio.text}")
      titulo = "REPORTE DE MANTENIMIENTO RECHAZADO"
      texto = f"folio del reporte: {self.text_box_folio.text}\nMotivo del rechazo:\n{texto.text}"
      with Notification("Enviando correo a jefe de mantenimiento...", title="ENVIANDO.", style="info"):
        anvil.server.call('enviar_mail','a.varela@ensel.org', titulo, texto)
      Notification("Correo enviado correctamente!", title="ÉXITO!", style="success").show()
      self.raise_event("x-close-alert",value="registro_guardado")


  
  def button_agregar_comentario_click(self, **event_args):
    self.button_agregar_comentario.enabled = False
    comentarios = self.repeating_panel_comentarios.items if self.repeating_panel_comentarios.items != None else []
    indice = len(comentarios)
    comentarios.append({'index':indice + 1,'comentario':""})
    self.repeating_panel_comentarios.items = comentarios
    filas = self.repeating_panel_comentarios.get_components()
    for fila in filas:
      componentes_fila = fila.get_components()
      label_indice = int(componentes_fila[0].text) - 1
      componentes_fila[1].enabled = False #boton editar
      componentes_fila[2].enabled = False #boton borrar
      if label_indice == indice:
        componentes_fila[3].visible = True #column panel de textbox y su boton


      



