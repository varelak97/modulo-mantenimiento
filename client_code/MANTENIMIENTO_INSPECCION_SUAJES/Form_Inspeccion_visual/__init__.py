from ._anvil_designer import Form_Inspeccion_visualTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ... import Funciones_Globales

class Form_Inspeccion_visual(Form_Inspeccion_visualTemplate):
  ws_herramentales = None
  ss_reporte_suajes = None
  reporte_suajes = None
  ss_vista_clientes = None
  vista_clientes = None
  ss_vista_suajes = None
  vista_suajes = None
  registro_actual = {}
  datos = None
  modos_botones = None
  lista_componentes = None
  campos_no_obligatorios = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.get_datos()
    
  ############################################# FUNCIONES PERSONALIZADAS #############################################
  def set_ini_config(self, datos):
    self.datos = datos
    self.ws_herramentales = app_files.control_herramentales
    self.ss_reporte_suajes = self.ws_herramentales['REVISION_SUAJES']
    self.ss_vista_clientes = self.ws_herramentales['VISTA_CLIENTES']
    self.ss_vista_suajes = self.ws_herramentales['VISTA_HERRAMENTALES']
    
    self.lista_componentes = [
      self.text_box_cliente,
      self.text_box_codigo_suaje,
      self.text_box_tipo_suaje,
      self.text_area_descripcion,
      self.text_box_revisor,
      self.text_area_filo,
      self.text_area_union,
      self.text_area_estado,
      self.button_estado_bien,
      self.button_estado_mal,
      self.button_filo_bien,
      self.button_filo_mal,
      self.button_union_bien,
      self.button_union_mal
    ]
    self.modos_botones = [
        {'tag':'filo_bien','modo':True,'llave':'status_filo'},
        {'tag':'union_bien','modo':True,'llave':'status_union'},
        {'tag':'estado_bien','modo':True,'llave':'status_estado'},
        {'tag':'filo_mal','modo':False,'llave':'status_filo'},
        {'tag':'union_mal','modo':False,'llave':'status_union'},
        {'tag':'estado_mal','modo':False,'llave':'status_estado'}
      ]
    self.campos_no_obligatorios = ["comentarios", ""]

  def get_datos(self):
    self.reporte_suajes = self.ss_reporte_suajes.rows
    
    if self.datos['modo'] == 'edicion':
      self.vista_clientes = self.ss_vista_clientes.rows
      self.ss_vista_suajes = self.ss_vista_suajes.rows
      for row in self.reporte_suajes:
        if self.datos['id_inspeccion'] == row['id_inspeccion']:
          self.registro_actual = row
          break
      dicc_registro_actual = dict(self.registro_actual)
      for suaje in self.vista_suajes:
        if dicc_registro_actual['id_herramental'] == suaje['id_herramental']:
          dicc_registro_actual['codigo_herramental'] = suaje['codigo_herramental']
          dicc_registro_actual['descripcion'] = suaje['descripcion']
          dicc_registro_actual['id_cliente'] = suaje['id_cliente']
          break
      for cliente in self.vista_clientes:
        if dicc_registro_actual['id_cliente'] == cliente['id_cliente']:
          dicc_registro_actual['cliente'] = cliente['ciente']
          break
      Funciones_Globales.fill_formulario(self.lista_componentes,dicc_registro_actual, self.modos_botones)
    else:
      self.text_box_revisor.text = self.datos['nombre_usuario']
      self.text_box_cliente.text = self.datos['cliente']
      self.text_box_codigo_suaje.text = self.datos['codigo_herramental']
      self.text_box_tipo_suaje.text = self.datos['tipo_suaje']
      self.text_area_descripcion.text = self.datos['descripcion']

  def guarda_datos(self, modo):
    pass
  ###################################################### EVENTOS #####################################################
  def button_guardar_click(self, **event_args):
    dicc_modos = [{'tag':'id_cliente', 'index': 0}]
    status = Funciones_Globales.validar_campos( self.lista_componentes, self.registro_actual, self.campos_no_obligatorios, self.datos['modo'], dicc_modos, None)
    if status == 1:
      self.guarda_datos(self.datos['modo'])
    elif status == 2:
      alert("No hay cambios que guardar.", title="ERROR!")
    elif status == 3:
      alert("faltan campos por llenar!", title="ERROR!")

  def button_filo_bien_click(self, **event_args):
    self.button_filo_bien.background = app.theme_colors['Primary']
    self.button_filo_bien.foreground = app.theme_colors['On Primary']
    
    self.button_filo_mal.background = app.theme_colors['LightGray']
    self.button_filo_mal.foreground = app.theme_colors['Secondary']

  def button_filo_mal_click(self, **event_args):
    self.button_filo_bien.background = app.theme_colors['LightGray']
    self.button_filo_bien.foreground = app.theme_colors['Secondary']
    
    self.button_filo_mal.background = app.theme_colors['Red']
    self.button_filo_mal.foreground = app.theme_colors['On Primary']

  def button_union_bien_click(self, **event_args):
    self.button_union_bien.background = app.theme_colors['Primary']
    self.button_union_bien.foreground = app.theme_colors['On Primary']
    
    self.button_union_mal.background = app.theme_colors['LightGray']
    self.button_union_mal.foreground = app.theme_colors['Secondary']

  def button_union_mal_click(self, **event_args):
    self.button_union_bien.background = app.theme_colors['LightGray']
    self.button_union_bien.foreground = app.theme_colors['Secondary']
    
    self.button_union_mal.background = app.theme_colors['Red']
    self.button_union_mal.foreground = app.theme_colors['On Primary']

  def button_estado_bien_click(self, **event_args):
    self.button_estado_bien.background = app.theme_colors['Primary']
    self.button_estado_bien.foreground = app.theme_colors['On Primary']
    
    self.button_estado_mal.background = app.theme_colors['LightGray']
    self.button_estado_mal.foreground = app.theme_colors['Secondary']

  def button_estado_mal_click(self, **event_args):
    self.button_estado_bien.background = app.theme_colors['LightGray']
    self.button_estado_bien.foreground = app.theme_colors['Secondary']
    
    self.button_estado_mal.background = app.theme_colors['Red']
    self.button_estado_mal.foreground = app.theme_colors['On Primary']

