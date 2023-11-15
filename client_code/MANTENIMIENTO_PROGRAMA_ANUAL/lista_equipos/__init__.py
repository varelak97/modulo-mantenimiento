from ._anvil_designer import lista_equiposTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class lista_equipos(lista_equiposTemplate):
  datos = {}
  def __init__(self, datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.datos = datos
    #fill_lista(self.datos)
    self.repeating_panel_lista_equipos.items = self.fill_lista(self.datos)

  def fill_lista(self, datos):
    items = []
    if datos['frecuencia'] == "SEMANAL":
      for equipo in datos['lista_equipos']:
        if equipo['frecuencia'] == "SEMANAL" and datos['tipo'] == "PROGRAMADO":
          items.append({"equipo":equipo['equipo'],"ver_checklist":True if equipo['operacion'] == "edicion" else False})
    return items

    
