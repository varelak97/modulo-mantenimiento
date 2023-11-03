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
    self.lista_links = [
      self.link_lunes_pw,
      self.link_lunes_pm,
      self.link_lunes_pt,
      self.link_lunes_ps,
      self.link_lunes_pa,
      self.link_lunes_r,
      self.link_lunes_p,
      self.link_lunes_ok,
      self.link_martes_pw,
      self.link_martes_pm,
      self.link_martes_pt,
      self.link_martes_ps,
      self.link_martes_pa,
      self.link_martes_r,
      self.link_martes_p,
      self.link_martes_ok,
      self.link_miercoles_pw,
      self.link_miercoles_pm,
      self.link_miercoles_pt,
      self.link_miercoles_ps,
      self.link_miercoles_pa,
      self.link_miercoles_r,
      self.link_miercoles_p,
      self.link_miercoles_ok,
      self.link_jueves_pw,
      self.link_jueves_pm,
      self.link_jueves_pt,
      self.link_jueves_ps,
      self.link_jueves_pa,
      self.link_jueves_r,
      self.link_jueves_p,
      self.link_jueves_ok,
      self.link_viernes_pw,
      self.link_viernes_pm,
      self.link_viernes_pt,
      self.link_viernes_ps,
      self.link_viernes_pa,
      self.link_viernes_r,
      self.link_viernes_p,
      self.link_viernes_ok,
      self.link_sabado_pw,
      self.link_sabado_pm,
      self.link_sabado_pt,
      self.link_sabado_ps,
      self.link_sabado_pa,
      self.link_sabado_r,
      self.link_sabado_p,
      self.link_sabado_ok,
      self.link_domingo_pw,
      self.link_domingo_pm,
      self.link_domingo_pt,
      self.link_domingo_ps,
      self.link_domingo_pa,
      self.link_domingo_r,
      self.link_domingo_p,
      self.link_domingo_ok
    ]
    self.set_color_indicadores()
    
  ######################################## FUNCIONES PERSONALIZADS ################################################
  def set_color_indicadores(self):
    for link in self.lista_links:
      if link.text != None and link.text != "":
        #print(f"es diferente de none:{link.text}")
        indicador = link.text.split(': ')
        print(f"el indicador:{indicador}")
        if indicador[1] != '0':
          if indicador[0] == "PW":
            link.background = app.theme_colors['Primary']
            link.foreground = app.theme_colors['White']
          elif indicador[0] == "PM":
            link.background = app.theme_colors['Orange']
            link.foreground = app.theme_colors['White']
          elif indicador[0] == "PT":
            link.background = app.theme_colors['Tertiary Container']
            link.foreground = app.theme_colors['Blue']
          elif indicador[0] == "PS":
            link.background = app.theme_colors['Tertiary']
            link.foreground = app.theme_colors['White']
          elif indicador[0] == "PA":
            link.background = app.theme_colors['Green']
            link.foreground = app.theme_colors['White']
          elif indicador[0] == "P":
            link.background = app.theme_colors['Primary']
            link.foreground = app.theme_colors['White']
          elif indicador[0] == "R":
            link.background = app.theme_colors['Red']
            link.foreground = app.theme_colors['Blue']
          elif indicador[0] == "OK":
            link.background = app.theme_colors['Green']
            link.foreground = app.theme_colors['White']
        else:
          link.background = "#FFFFFF"
          link.foreground = "#FFFFFF"
      else:
        link.background = "#FFFFFF"
        link.foreground = "#FFFFFF"
    
    
  #################################################### EVENTOS ####################################################
  def link_lunes_click(self, **event_args):
    datos = {}
    datos['dia'] = self.link_lunes_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_martes_click(self, **event_args):
    datos = {}
    datos['dia'] = self.link_martes_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_miercoles_click(self, **event_args):
    datos = {}
    datos['dia'] = self.link_miercoles_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_jueves_click(self, **event_args):
    datos = {}
    datos['dia'] = self.link_jueves_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_viernes_click(self, **event_args):
    datos = {}
    datos['dia'] = self.link_viernes_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_sabado_click(self, **event_args):
    datos = {}
    datos['dia'] = self.link_sabado_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_domingo_click(self, **event_args):
    datos = {}
    datos['dia'] = self.link_domingo_numero_dia.text
    datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_lunes_numero_dia_click(self, **event_args):
    print("test")








      

