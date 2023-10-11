from ._anvil_designer import A_mainTemplate
from anvil import *
from ..MANTENIMIENTO_CORRECTIVO import MANTENIMIENTO_CORRECTIVO
from ..MANTENIMIENTO_PREVENTIVO import MANTENIMIENTO_PREVENTIVO
from ..MANTENIMIENTO_PREVENTIVO_PROGRAMADO import MANTENIMIENTO_PREVENTIVO_PROGRAMADO
from ..MANTENIMIENTO_PROGRAMA_ANUAL import MANTENIMIENTO_PROGRAMA_ANUAL
from ..MANTENIMIENTO_CORRECTIVO_REGISTROS import MANTENIMIENTO_CORRECTIVO_REGISTROS
from ..MANTENIMIENTO_PREVENTIVO_REGISTROS import MANTENIMIENTO_PREVENTIVO_REGISTROS
from ..MANTENIMIENTO_PREVENTIVO_PROGRAMADO_REGISTROS import MANTENIMIENTO_PREVENTIVO_PROGRAMADO_REGISTROS
from ..MANTENIMIENTO_PREVENTIVO_CHECKLIST import MANTENIMIENTO_PREVENTIVO_CHECKLIST

class A_main(A_mainTemplate):
  ############################### DECLARACIÓN DE VARIABLES GLOBALES #############################
  ################################# INICIALIZACION DE VARIABLES #################################
  form_activo = None
  datos = {
    'id_usuario_erp': 18,
    'clave_form':"MANTENIMIENTO_PROGRAMA_ANUAL",
    'test':True
  }
  lista_mttos = [
    "PROGRAMA ANUAL DE MANTENIMIENTOS",
    "MANTENIMIENTOS PREVENTIVOS",
    "MANTENIMIENTOS PREVENTIVOS PROGRAMADOS",
    "MANTENIMIENTOS CORRECTIVOS"
  ]
  def __init__(self, **properties):
    ################################# INICIALIZACION DE VARIABLES #################################
    self.drop_down_menu_areas.items = self.lista_mttos
    
    self.init_components(**properties)
  
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.content_panel.visible = True

    if self.datos['id_usuario_erp'] == 18:
      self.datos['clave_form'] = "MANTENIMIENTO_PROGRAMA_ANUAL"
      self.datos['test'] = True
      self.actualizar_form_activo(self.datos)
      
  ################################### FUNCIONES PERSONALIZADAS ####################################
  def actualizar_form_activo(self, datos, **event_args):
    if datos['clave_form'] == 'MANTENIMIENTO_PROGRAMA_ANUAL':
      self.abrir_form(MANTENIMIENTO_PROGRAMA_ANUAL(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_CORRECTIVO':
      self.abrir_form(MANTENIMIENTO_CORRECTIVO(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_CORRECTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_CORRECTIVO_REGISTROS(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_PROGRAMADO':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_PROGRAMADO(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_PROGRAMADO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_PROGRAMADO_REGISTROS(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CHECKLIST':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CHECKLIST(datos))

  def abrir_form(self, form_de_interes):
    try: #Se utiliza un try porque la primera vez que se abre el form RECUERSOS_HUMANOS no tiene ningún form hijo cargado, entonces levantará un error.
      self.form_activo.remove_from_parent()
    except: #no se necesita para manejar el error, pero el 'except' es obligado a estar cuando se usa un try. ¡NO BORRAR!
      pass
    self.form_activo = form_de_interes
    self.add_component(self.form_activo)

  ########################################### EVENTOS ###########################################

  def drop_down_menu_areas_change(self, **event_args):
    area_seleccionada = self.drop_down_menu_areas.selected_value

    if area_seleccionada == "PROGRAMA ANUAL DE MANTENIMIENTOS":
      self.datos['clave_form'] = 'MANTENIMIENTO_PROGRAMA_ANUAL'
      self.actualizar_form_activo(self.datos)
    elif area_seleccionada == "MANTENIMIENTOS PREVENTIVOS":
      self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
      self.actualizar_form_activo(datos=self.datos)
    elif area_seleccionada == "MANTENIMIENTOS PREVENTIVOS PROGRAMADOS":
      self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_PROGRAMADO_REGISTROS'
      self.actualizar_form_activo(self.datos)
    elif area_seleccionada == "MANTENIMIENTOS CORRECTIVOS":
      self.datos['clave_form'] = 'MANTENIMIENTO_CORRECTIVO_REGISTROS'
      self.actualizar_form_activo(self.datos)

