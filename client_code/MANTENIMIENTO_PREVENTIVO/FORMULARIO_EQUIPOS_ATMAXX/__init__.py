from ._anvil_designer import FORMULARIO_EQUIPOS_ATMAXXTemplate
from anvil import *

class FORMULARIO_EQUIPOS_ATMAXX(FORMULARIO_EQUIPOS_ATMAXXTemplate):
  datos = {}
  items_actividades_maquinas = [
    {"id":1,"actividad":"DESTAPAR Y LIMPIAR INTERIOR DEL EQUIPO"},
    {"id":2,"actividad":"DRENAR CONTENEDOR DE ACEITE DEL SISTEMA NEUMÁTICO"},
    {"id":3,"actividad":"LIMPIAR SILENCIADORES CON AGUA A PRESIÓN"},
    {"id":4,"actividad":"actividad fdre"}
  ]
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.datos = datos
    self.repeating_panel_1.items = self.items
    
    
    # Any code you write here will run before the form opens.
