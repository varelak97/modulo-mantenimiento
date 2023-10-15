from ._anvil_designer import RowTemplateDiasTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class RowTemplateDias(RowTemplateDiasTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  actividades_equipo_hojeadora_trimestral = [
    {"id":1,"actividad":"ASPIRAR Y LIMPIAR INTERIOR DEL EQUIPO."},
    {"id":2,"actividad":"ENGRASAR CHUMACERAS"},
    {"id":3,"actividad":"REVISAR TORNILLERÍA: APRETAR O REEMPLAZAR SI ES NECESARIO."},
    {"id":4,"actividad":"LIMPIAR Y ASPIRAR PANEL DE CONTROL."},
    {"id":5,"actividad":"REVISAR CONEXIONES EN EL PANEL DE CONTROL."},
    {"id":6,"actividad":"REVISAR PRESIÓN DE SUMINISTRO (RANGO ENTRE 0.4 Y 0.6 MPA)"}
  ]
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  #################################################### EVENTOS ####################################################
  def link_lunes_click(self, **event_args):
    datos = {}
    datos['dia'] = self.label_lunes_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_martes_click(self, **event_args):
    datos = {}
    datos['dia'] = self.label_martes_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_miercoles_click(self, **event_args):
    datos = {}
    datos['dia'] = self.label_miercoles_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_jueves_click(self, **event_args):
    datos = {}
    datos['dia'] = self.label_jueves_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_viernes_click(self, **event_args):
    datos = {}
    datos['dia'] = self.label_viernes_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_sabado_click(self, **event_args):
    datos = {}
    datos['dia'] = self.label_sabado_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_domingo_click(self, **event_args):
    datos = {}
    datos['dia'] = self.label_domingo_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)







      

