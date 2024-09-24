from ._anvil_designer import opciones_inspeccionesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class opciones_inspecciones(opciones_inspeccionesTemplate):
  datos = None

  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos
    self.set_config()

  ################################################# FUNCIONES PERSONALIZADAS #################################################
  def set_config(self):
    if self.datos['id_inspeccion'] is None:
      self.button_visual_ver.foreground = app.theme_colors['LightGray']
      self.button_dimensional_ver.foreground = app.theme_colors['LightGray']
    else:
      config_ciclo = True
      if self.datos['status_visual'] == '0':
        self.button_visual_ver.foreground = app.theme_colors['LightGray']
        config_ciclo = False
      if self.datos['status_dimensional'] == '0':
        self.button_dimensional_ver.foreground = app.theme_colors['LightGray']
        config_ciclo = False 
      if config_ciclo:
        self.button_ciclo.visible = True
        self.label_ciclo.visible = True
      
      """if self.datos['status_visual'] == '1':
        self.button_visual_ver.foreground = app.theme_colors['Primary']
      else:
        self.button_visual_ver.foreground = app.theme_colors['LightGray']
      if self.datos['status_dimensional'] == '1':
        self.button_dimensional_ver.foreground = app.theme_colors['Primary']
      else:
        self.button_dimensional_ver.foreground = app.theme_colors['LightGray']"""
    
    
    
  def abrir_form(self, modo, clave_form):
    """datos  = {
      'id_inspeccion': self.datos['id_inspeccion'],
      'modo': modo,
      'clave_form': clave_form
    }"""
    self.datos['modo'] = modo
    self.datos['clave_form'] = clave_form
    
    self.popper.pop("hide")
    self.popper.parent.parent.parent.parent.parent.parent.raise_event('x-abrir_form', datos=self.datos)

  ########################################################## EVENTOS #########################################################

  def button_visual_editar_click(self, **event_args):
    if self.datos['id_inspeccion'] is None:
      self.abrir_form('nuevo', 'FORM_INSPECCION_VISUAL')
    else:
      if self.datos['status_visual'] == '0':
        self.abrir_form('nuevo_insp', 'FORM_INSPECCION_VISUAL')
      else:
        self.abrir_form('edicion', 'FORM_INSPECCION_VISUAL')

  def button_visual_ver_click(self, **event_args):
    if self.datos['status_visual'] == '1':
      self.abrir_form('visor', 'FORM_INSPECCION_VISUAL')

  def button_dimensional_editar_click(self, **event_args):
    if self.datos['id_inspeccion'] is None:
      print("ejecuta inspeccion dimensional como nuevo")
      self.abrir_form('nuevo', 'FORM_INSPECCION_DIMENSIONAL')
    else:
      if self.datos['status_dimensional'] == '0':
        print("ejecuta inspeccion dimensional como nueva inspeccion")
        self.abrir_form('nuevo_insp', 'FORM_INSPECCION_DIMENSIONAL')
      else:
        print(f"ejecuta inspeccion dimensional como edicion con status visual:{self.datos['status_dimensional']}")
        self.abrir_form('edicion', 'FORM_INSPECCION_DIMENSIONAL')

  def button_dimensional_ver_click(self, **event_args):
    if self.datos['status_dimensional'] == '1':
      self.abrir_form('visor', 'FORM_INSPECCION_DIMENSIONAL')
    
  def button_ciclo_click(self, **event_args):
    self.popper.pop("hide")
    contenido = ColumnPanel()
    input_ciclo = TextBox(type="number", role="outlined")
    descripcion = Label(text=f"Ciclo actual: {self.datos['vida_util']}\nIngrese próximo ciclo:")
    contenido.add_component(descripcion)
    contenido.add_component(input_ciclo)
    
    respuesta = alert(contenido, title="PRÓXIMO CICLO DE REVISIÓN", buttons=[("GUARDAR", True)])
    if respuesta:
      if int(self.datos['vida_util']) >= input_ciclo.text:
        alert("Debe ingresar un ciclo mayor al actualmente registrado!", title="ERROR!")
      else:
        datos = {
          "id_herramental" : self.datos['id_herramental'],
          "nuevo_ciclo" : input_ciclo.text
        }
        self.popper.parent.parent.parent.parent.parent.parent.raise_event('x-actualizar_ciclo', datos=datos)

