from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_CHECKLISTTemplate
from anvil import *

class MANTENIMIENTO_PREVENTIVO_CHECKLIST(MANTENIMIENTO_PREVENTIVO_CHECKLISTTemplate):
  datos = {}
  items_actividades_maquinas = [
    {"id":1,"actividad":"DESTAPAR Y LIMPIAR INTERIOR DEL EQUIPO"},
    {"id":2,"actividad":"DRENAR CONTENEDOR DE ACEITE DEL SISTEMA NEUMÁTICO"},
    {"id":3,"actividad":"LIMPIAR SILENCIADORES CON AGUA A PRESIÓN"},
    {"id":4,"actividad":"ENGRASAR CHUMACERAS Y RIELES DE DESPLAZAMIENTO"},
    {"id":5,"actividad":"REVISAR EL NIVEL DE ACEITE DE LA CAJA REDUCTORA"},
    {"id":6,"actividad":"ENGRASAR CHUMACERAS Y RIELES DE DESPLAZAMIENTO"},
    {"id":7,"actividad":"REVISAR EL NIVEL DE ACEITE DE LA CAJA REDUCTORA"},
    {"id":8,"actividad":"ENGRASAR TORNILLOS Y RIELES DE DESPLAZAMIENTO"},
    {"id":9,"actividad":"REVISAR TORNILLERÍA: APRETAR O REEMPLAZAR SI ES NECESARIO"},
    {"id":10,"actividad":"REVISAR QUE NO EXISTAN FUGAS DE AIRE DEL SISTEMA NEUMÁTICO"},
    {"id":11,"actividad":"REVISAR CONEXIONES EN EL PANEL DE CONTROL"},
    {"id":12,"actividad":"LIMPIAR PANEL DE CONTROL"},
    {"id":13,"actividad":"VERIFICAR QUE FUNCIONEN PAROS DE EMERGENCIA"},
    {"id":14,"actividad":"REVISAR QUE INDICADOR DE BATERÍA EN PLC NO ESTÉ ENCENDIDO"}
  ]
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.datos = datos
    self.repeating_panel_registros.items = self.items_actividades_maquinas
