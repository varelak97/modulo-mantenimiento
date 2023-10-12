from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server

class RowTemplate1(RowTemplate1Template):
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

    # Any code you write here will run before the form opens.

  def link_click(self, **event_args):
    respuesta = alert(buttons=[("PROGRAMAR MANTENIMIENTO PREVENTIVO","programar"),("REALIZAR CHECKLIST DE MTTO PREVENTIVO","checklist")])
    #po = self.tag
    
    if respuesta == "programar":
      datos = {}
      datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO'
      self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)
    elif respuesta == "checklist":
      datos = {}
      datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_CHECKLIST'
      datos['actividades'] = self.actividades_equipo_hojeadora_trimestral
      self.parent.parent.parent.parent.parent.raise_event('x-actualizar_form_activo', datos=datos)

  def link_lunes_click(self, **event_args):
    pass
      

