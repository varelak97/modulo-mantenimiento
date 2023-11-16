from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CHECKLISTTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from datetime import date,datetime

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
    self.set_event_handler('x-editar_comentario', self.editar_comentario)
    
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
    
    self.repeating_panel_registros.items = lista
    
    if datos['modo'] == "ver_checklist":
      self.text_box_nombre.text = self.registro_equipo['persona_ejecuta_mtto']
      self.date_picker_fecha_hora_inicio.date = self.registro_equipo['fecha_hora_inicio']
      self.date_picker_fecha_hora_termino.date = self.registro_equipo['fecha_hora_final']
      self.repeating_panel_comentarios.items = eval(self.registro_equipo['comentarios_mantenimiento'])#self.get_comentarios(self.registro_equipo['comentarios_mantenimiento'])
      self.disable_componentes_form()
        #componentes_row[4].enabled = False
  ################################ FUNCIONES PERSONALIZADS ########################################
  def disable_componentes_form(self):
    self.data_row_panel_input.visible = False
    self.text_box_nombre.enabled = False
    self.date_picker_fecha_hora_inicio.enabled = False
    self.date_picker_fecha_hora_termino.enabled = False
    self.button_guardar.enabled = False
    for row in self.repeating_panel_registros.get_components():
      componentes_row = row.get_components()
      componentes_row[2].enabled = False
      componentes_row[3].enabled = False
    for row in self.repeating_panel_comentarios.get_components():
      componentes_row = row.get_components()
      componentes_row[2].enabled = False
      
  def editar_comentario(self, indice, **event_args):
    items = self.repeating_panel_comentarios.items
    self.text_area_comentario.text = items[indice-1]['comentario']
    self.button_add.icon = "fa:save"
    self.button_add.tag = indice
    self.button_add.enabled = True
    
  """def get_comentarios(self, comentarios):
    dict_comentarios = eval(comentarios)
    for index,comentario in enumerate(dict_comentarios):
      comentario['index'] = index + 1
    return dict_comentarios"""
    
  def validar_campos(self):
    validacion = True
    if self.text_box_nombre.text == None or self.text_box_nombre.text == "":
      validacion = False
    if self.date_picker_fecha_hora_inicio.date == None:
      validacion = False
    if self.date_picker_fecha_hora_termino.date == None:
      validacion = False
    """if self.text_area_comentarios.text == None or self.text_area_comentarios.text == "":
      validacion = False"""
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
      validacion = False
    else:
      if validacion:
        return respuestas
    return validacion

  ############################################ EVENTOS ############################################
  def button_guardar_click(self, **event_args):
    respuesta = self.validar_campos()
    if respuesta == False:
       alert(title="ERROR!",content="Faltan campos por llenar.")
    else:
      with Notification("Guardando registro en la base de datos...",title="GUARDANDO."):
        self.registro_equipo['registro_principal'] = 0
        registro_actualizar = dict(self.registro_equipo).copy()
        datos_actualizar = {
          "persona_ejecuta_mtto":self.text_box_nombre.text,
          "fecha_hora_inicio":self.date_picker_fecha_hora_inicio.date,
          "status_mantenimiento": "REALIZADO",
          "actividades":respuesta,
          "fecha_hora_final":self.date_picker_fecha_hora_termino.date,
          "comentarios_mantenimiento":self.repeating_panel_comentarios.items,
          "operacion":"edicion",
          "marca_temporal":datetime.now()
        }
        registro_actualizar.update(**datos_actualizar)
        self.ws_registros_mttos.add_row(**registro_actualizar)
      Notification("Registro guardao correctamente.",title="ÉXITO", style="success").show()
      self.raise_event("x-close-alert",value="registro_guardado")

  """def button_regresar_click(self, **event_args):
    self.datos['clave_form'] = 'MANTENIMIENTO_PROGRAMA_ANUAL'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""

  def button_add_click(self, **event_args):
    comentarios = None
    if self.button_add.icon == "fa:plus":
      if self.text_area_comentario.text != "":
        comentarios = self.repeating_panel_comentarios.items if self.repeating_panel_comentarios.items != None else []
        comentarios.append({'index':len(comentarios)+1,'comentario':self.text_area_comentario.text})
    else:
      if self.text_area_comentario.text != "":
        comentarios = self.repeating_panel_comentarios.items
        comentarios[self.button_add.tag-1]['comentario'] = self.text_area_comentario.text
        self.button_add.icon = "fa:plus"
    
    if comentarios != None:
      self.repeating_panel_comentarios.items = comentarios
      self.text_area_comentario.text = ""
      self.button_add.enabled = False

  def text_area_comentario_change(self, **event_args):
    if self.text_area_comentario.text == "":
      self.button_add.enabled = False
    else:
      self.button_add.enabled = True
    


