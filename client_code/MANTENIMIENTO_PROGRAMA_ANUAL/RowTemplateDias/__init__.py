from ._anvil_designer import RowTemplateDiasTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class RowTemplateDias(RowTemplateDiasTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  lista_labels = None
  lista_labels_generales = None
  def __init__(self, **properties):
    self.init_components(**properties)
    """self.lista_labels = [
      self.label_lunes_pw,
      self.label_lunes_pm,
      self.label_lunes_pt,
      self.label_lunes_ps,
      self.label_lunes_pa,
      self.label_lunes_rg,
      self.label_lunes_pg,
      self.label_lunes_okg,
      self.label_martes_pw,
      self.label_martes_pm,
      self.label_martes_pt,
      self.label_martes_ps,
      self.label_martes_pa,
      self.label_martes_rg,
      self.label_martes_pg,
      self.label_martes_okg,
      self.label_miercoles_pw,
      self.label_miercoles_pm,
      self.label_miercoles_pt,
      self.label_miercoles_ps,
      self.label_miercoles_pa,
      self.label_miercoles_rg,
      self.label_miercoles_pg,
      self.label_miercoles_okg,
      self.label_jueves_pw,
      self.label_jueves_pm,
      self.label_jueves_pt,
      self.label_jueves_ps,
      self.label_jueves_pa,
      self.label_jueves_rg,
      self.label_jueves_pg,
      self.label_jueves_okg,
      self.label_viernes_pw,
      self.label_viernes_pm,
      self.label_viernes_pt,
      self.label_viernes_ps,
      self.label_viernes_pa,
      self.label_viernes_rg,
      self.label_viernes_pg,
      self.label_viernes_okg,
      self.label_sabado_pw,
      self.label_sabado_pm,
      self.label_sabado_pt,
      self.label_sabado_ps,
      self.label_sabado_pa,
      self.label_sabado_rg,
      self.label_sabado_pg,
      self.label_sabado_okg,
      self.label_domingo_pw,
      self.label_domingo_pm,
      self.label_domingo_pt,
      self.label_domingo_ps,
      self.label_domingo_pa,
      self.label_domingo_rg,
      self.label_domingo_pg,
      self.label_domingo_okg
    ]
    self.set_color_indicadores()"""
    
  ######################################## FUNCIONES PERSONALIZADS ################################################
  def set_color_indicadores(self):
    for label in self.lista_labels:
      if label.text != None:
        indicador = label.text.split(': ')
        print(f"el indicador:{indicador}")
        if indicador[1] != '0':
          if indicador[0] == "PW":
            label.background = app.theme_colors['Primary']
            label.foreground = app.theme_colors['White']
          elif indicador[0] == "PM":
            label.background = app.theme_colors['Orange']
            label.foreground = app.theme_colors['White']
          elif indicador[0] == "PT":
            label.background = app.theme_colors['Tertiary Container']
            label.foreground = app.theme_colors['Blue']
          elif indicador[0] == "PS":
            label.background = app.theme_colors['Tertiary']
            label.foreground = app.theme_colors['White']
          elif indicador[0] == "PA":
            label.background = app.theme_colors['Green']
            label.foreground = app.theme_colors['White']
          elif indicador[0] == "P":
            label.background = app.theme_colors['Primary']
            label.foreground = app.theme_colors['White']
          elif indicador[0] == "R":
            label.background = app.theme_colors['Red']
            label.foreground = app.theme_colors['Blue']
          elif indicador[0] == "OK":
            label.background = app.theme_colors['Green']
            label.foreground = app.theme_colors['White']
        else:
          label.background = "#FFFFFF"
          label.foreground = "#FFFFFF"
      else:
        label.background = "#FFFFFF"
        label.foreground = "#FFFFFF"
    
    
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

  def link_lunes_numero_dia_click(self, **event_args):
    print("test")








      

