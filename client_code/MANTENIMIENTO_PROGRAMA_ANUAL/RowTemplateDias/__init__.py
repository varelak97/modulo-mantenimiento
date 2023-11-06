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
      self.link_lunes_w,
      self.link_lunes_m,
      self.link_lunes_t,
      self.link_lunes_s,
      self.link_lunes_a,
      self.link_lunes_r,
      self.link_lunes_p,
      self.link_lunes_ok,
      self.link_martes_w,
      self.link_martes_m,
      self.link_martes_t,
      self.link_martes_s,
      self.link_martes_a,
      self.link_martes_r,
      self.link_martes_p,
      self.link_martes_ok,
      self.link_miercoles_w,
      self.link_miercoles_m,
      self.link_miercoles_t,
      self.link_miercoles_s,
      self.link_miercoles_a,
      self.link_miercoles_r,
      self.link_miercoles_p,
      self.link_miercoles_ok,
      self.link_jueves_w,
      self.link_jueves_m,
      self.link_jueves_t,
      self.link_jueves_s,
      self.link_jueves_a,
      self.link_jueves_r,
      self.link_jueves_p,
      self.link_jueves_ok,
      self.link_viernes_w,
      self.link_viernes_m,
      self.link_viernes_t,
      self.link_viernes_s,
      self.link_viernes_a,
      self.link_viernes_r,
      self.link_viernes_p,
      self.link_viernes_ok,
      self.link_sabado_w,
      self.link_sabado_m,
      self.link_sabado_t,
      self.link_sabado_s,
      self.link_sabado_a,
      self.link_sabado_r,
      self.link_sabado_p,
      self.link_sabado_ok,
      self.link_domingo_w,
      self.link_domingo_m,
      self.link_domingo_t,
      self.link_domingo_s,
      self.link_domingo_a,
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








      

