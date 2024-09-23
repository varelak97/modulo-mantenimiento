from ._anvil_designer import Form_Inspeccion_DimensionalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class Form_Inspeccion_Dimensional(Form_Inspeccion_DimensionalTemplate):
  ws_herramentales = None
  ss_reporte_suajes = None
  reporte_suajes = None
  ss_vista_clientes = None
  vista_clientes = None
  ss_vista_suajes = None
  vista_suajes = None
  ss_suajes = None
  suajes = None
  registro_actual = {}
  datos = None
  modos_botones = None
  status_botones = None
  lista_componentes = None
  lista_componentes_validacion = None
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
    self.ss_suajes = self.ws_herramentales['HERRAMENTALES']
    
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
    self.lista_componentes_validacion = [
      self.text_area_filo,
      self.text_area_union,
      self.text_area_estado,
      self.button_filo_bien,
      self.button_union_bien,
      self.button_estado_bien
    ]
    self.modos_botones = [
        {'tag':'filo_bien','modo':True,'llave':'status_filo'},
        {'tag':'union_bien','modo':True,'llave':'status_union'},
        {'tag':'estado_bien','modo':True,'llave':'status_estado'},
        {'tag':'filo_mal','modo':False,'llave':'status_filo'},
        {'tag':'union_mal','modo':False,'llave':'status_union'},
        {'tag':'estado_mal','modo':False,'llave':'status_estado'}
      ]
    self.status_botones = [
      {'tag':"filo_bien", "valor": None, 'llave':'status_filo'},
      {'tag':"union_bien", "valor": None, 'llave':'status_union'},
      {'tag':"estado_bien", "valor": None, 'llave':'status_estado'}
    ]
    self.campos_no_obligatorios = ["comentarios_filo", "comentarios_union", "comentarios_estado"]

  def get_datos(self):
    if self.datos["modo"] == "edicion":
      self.reporte_suajes = self.ss_reporte_suajes.rows
    self.vista_suaje = self.ss_vista_suaje.rows
    for suaje in self.vista_suaje:
      if suaje["id_herramental"] == self.datos["id_herramental"]:
        pass

  ###################################################### EVENTOS #####################################################

  def button_medidas_bien_click(self, **event_args):
    self.button_filo_bien.background = app.theme_colors["Primary"]
    self.button_filo_bien.foreground = app.theme_colors["On Primary"]

    self.button_filo_mal.background = app.theme_colors["LightGray"]
    self.button_filo_mal.foreground = app.theme_colors["Secondary"]

  def button_medidas_mal_click(self, **event_args):
    self.button_filo_bien.background = app.theme_colors["LightGray"]
    self.button_filo_bien.foreground = app.theme_colors["Secondary"]

    self.button_filo_mal.background = app.theme_colors["Red"]
    self.button_filo_mal.foreground = app.theme_colors["On Primary"]

  def button_union_bien_click(self, **event_args):
    self.button_union_bien.background = app.theme_colors["Primary"]
    self.button_union_bien.foreground = app.theme_colors["On Primary"]

    self.button_union_mal.background = app.theme_colors["LightGray"]
    self.button_union_mal.foreground = app.theme_colors["Secondary"]

  def button_union_mal_click(self, **event_args):
    self.button_union_bien.background = app.theme_colors["LightGray"]
    self.button_union_bien.foreground = app.theme_colors["Secondary"]

    self.button_union_mal.background = app.theme_colors["Red"]
    self.button_union_mal.foreground = app.theme_colors["On Primary"]

  def button_estado_bien_click(self, **event_args):
    self.button_estado_bien.background = app.theme_colors["Primary"]
    self.button_estado_bien.foreground = app.theme_colors["On Primary"]

    self.button_estado_mal.background = app.theme_colors["LightGray"]
    self.button_estado_mal.foreground = app.theme_colors["Secondary"]

  def button_estado_mal_click(self, **event_args):
    self.button_estado_bien.background = app.theme_colors["LightGray"]
    self.button_estado_bien.foreground = app.theme_colors["Secondary"]

    self.button_estado_mal.background = app.theme_colors["Red"]
    self.button_estado_mal.foreground = app.theme_colors["On Primary"]
