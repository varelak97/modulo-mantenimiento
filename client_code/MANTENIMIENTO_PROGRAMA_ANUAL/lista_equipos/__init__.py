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
    #print(f"los datos:{self.datos}")
    self.repeating_panel_lista_equipos.items = self.fill_lista(self.datos)

  def fill_lista(self, datos):
    items = []
    for equipo in datos['lista_equipos']:
        if equipo['frecuencia'] == datos['frecuencia']:
          datos_equipo = {
            "equipo":equipo['equipo'],
            "fecha_programada":equipo['fecha_programada'],
            "fecha_realizada":equipo['fecha_hora_final'],
            "ver_checklist":True if equipo['operacion'] == "edicion" else False,
            "id_mtto_preventivo":equipo['id_mtto']
          }
          items.append(datos_equipo)
    
    """if datos['tipo'] == "PROGRAMADO":
      for equipo in datos['lista_equipos']:
        if equipo['frecuencia'] == datos['frecuencia']:
          items.append({"equipo":equipo['equipo'],"fecha_programada":equipo['fecha_programada'],"ver_checklist":True if equipo['operacion'] == "edicion" else False,"id_mtto_preventivo":equipo['id_mtto']})
    elif datos['tipo'] == "REALIZADO":
      for equipo in datos['lista_equipos']:
        if equipo['frecuencia'] == datos['frecuencia']:
          items.append({"equipo":equipo['equipo'],"fecha_programada":equipo['fecha_programada'],"fecha_realizada":equipo['fecha_hora_final'],"ver_checklist":True if equipo['operacion'] == "edicion" else False,"id_mtto_preventivo":equipo['id_mtto']})"""
    
    #estaba asi
    """if datos['frecuencia'] == "SEMANAL":
      for equipo in datos['lista_equipos']:
        if equipo['frecuencia'] == "SEMANAL" and datos['tipo'] == "PROGRAMADO":
          items.append({"equipo":equipo['equipo'],"ver_checklist":True if equipo['operacion'] == "edicion" else False,"id_mtto_preventivo":equipo['id_mtto']})
    
    
    if datos['frecuencia'] == "MENSUAL":
      for equipo in datos['lista_equipos']:
        if equipo['frecuencia'] == "MENSUAL" and datos['tipo'] == "PROGRAMADO":
          items.append({"equipo":equipo['equipo'],"ver_checklist":True if equipo['operacion'] == "edicion" else False,"id_mtto_preventivo":equipo['id_mtto']})
    
    
    if datos['frecuencia'] == "TRIMESTRAL":
      for equipo in datos['lista_equipos']:
        if equipo['frecuencia'] == "TRIMESTRAL" and datos['tipo'] == "PROGRAMADO":
          items.append({"equipo":equipo['equipo'],"ver_checklist":True if equipo['operacion'] == "edicion" else False,"id_mtto_preventivo":equipo['id_mtto']})
    
    
    if datos['frecuencia'] == "SEMESTRAL":
      for equipo in datos['lista_equipos']:
        if equipo['frecuencia'] == "SEMESTRAL" and datos['tipo'] == "PROGRAMADO":
          items.append({"equipo":equipo['equipo'],"ver_checklist":True if equipo['operacion'] == "edicion" else False,"id_mtto_preventivo":equipo['id_mtto']})
    
    
    if datos['frecuencia'] == "ANUAL":
      for equipo in datos['lista_equipos']:
        if equipo['frecuencia'] == "ANUAL" and datos['tipo'] == "PROGRAMADO":
          items.append({"equipo":equipo['equipo'],"ver_checklist":True if equipo['operacion'] == "edicion" else False,"id_mtto_preventivo":equipo['id_mtto']})"""
    return items

    
