from ._anvil_designer import A_mainTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.js.window
from ..MANTENIMIENTO_LISTA_EQUIPOS import MANTENIMIENTO_LISTA_EQUIPOS
from ..MANTENIMIENTO_PROGRAMA_ANUAL import MANTENIMIENTO_PROGRAMA_ANUAL
from ..MANTENIMIENTO_PREVENTIVO_REGISTROS import MANTENIMIENTO_PREVENTIVO_REGISTROS
from ..MANTENIMIENTO_PREVENTIVO_CHECKLIST import MANTENIMIENTO_PREVENTIVO_CHECKLIST
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES
from ..MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS import MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS

class A_main(A_mainTemplate):
  form_activo = None
  datos = {
    'id_usuario_erp': None,
    'clave_form': None,
  }

  """"PROGRAMA ANUAL DE MANTENIMIENTOS",
    "REPORTE DE MTTOS PREVENTIVOS",
    "REPORTES DE MTTOS PREVENTIVOS CORRECTIVOS PROGRAMADOS",
    "SOLICITUDES DE MANTENIMIENTO PREVENTIVO CORRECTIVO","""

  lista_mttos = [
    "LISTA GENERAL DE EQUIPOS",
    "LLENAR SOLICITUD DE MTTO PREVENTIVO CORRECTIVO" ############ BORRAR ###########
  ]
  def __init__(self, datos, **properties):
    ################################# INICIALIZACION DE VARIABLES #################################
    self.drop_down_menu_areas.items = self.lista_mttos
    self.datos.update(datos)
    
    self.init_components(**properties)
  
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.content_panel.visible = True

    if self.datos['id_usuario_erp'] == 58 or self.datos['id_usuario_erp'] == 884 or self.datos['id_usuario_erp'] == 0:
      self.datos['clave_form'] = "MANTENIMIENTO_LISTA_EQUIPOS"
      self.drop_down_menu_areas.visible = True
      self.actualizar_form_activo(self.datos)
    else:
      self.datos['clave_form'] = "MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES"
      self.drop_down_menu_areas.visible = False
      self.actualizar_form_activo(self.datos)
      
      
  ################################### FUNCIONES PERSONALIZADAS ####################################
  def actualizar_form_activo(self, datos, **event_args):
    #datos['id_usuario_erp'] = 18
    if datos['clave_form'] == "MANTENIMIENTO_LISTA_EQUIPOS":
      self.abrir_form(MANTENIMIENTO_LISTA_EQUIPOS(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PROGRAMA_ANUAL':
      self.abrir_form(MANTENIMIENTO_PROGRAMA_ANUAL(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CHECKLIST':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CHECKLIST(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REPORTE(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES':
      datos['modo'] = "nuevo"
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS(datos))

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

    if area_seleccionada == "LISTA GENERAL DE EQUIPOS":
      self.datos['clave_form'] = 'MANTENIMIENTO_LISTA_EQUIPOS'
      self.actualizar_form_activo(self.datos)
    elif area_seleccionada == "PROGRAMA ANUAL DE MANTENIMIENTOS":
      self.datos['clave_form'] = 'MANTENIMIENTO_PROGRAMA_ANUAL'
      self.actualizar_form_activo(self.datos)
    elif area_seleccionada == "REPORTE DE MTTOS PREVENTIVOS":
      self.datos['modo'] = "todos"
      self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
      self.actualizar_form_activo(self.datos)
    elif area_seleccionada == "REPORTES DE MTTOS PREVENTIVOS CORRECTIVOS PROGRAMADOS":
      self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_REGISTROS'
      self.actualizar_form_activo(self.datos)
    elif area_seleccionada == "SOLICITUDES DE MANTENIMIENTO PREVENTIVO CORRECTIVO":
      self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES_REGISTROS'
      self.actualizar_form_activo(self.datos)
    elif area_seleccionada == "LLENAR SOLICITUD DE MTTO PREVENTIVO CORRECTIVO":
      self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CORRECTIVO_SOLICITUDES'
      self.actualizar_form_activo(self.datos)

  def link_cerrar_sesion_click(self, **event_args):
    anvil.js.window.location.reload()
