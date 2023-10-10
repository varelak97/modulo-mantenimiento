from ._anvil_designer import MANTENIMIENTO_PREVENTIVOTemplate
from anvil import *

class MANTENIMIENTO_PREVENTIVO(MANTENIMIENTO_PREVENTIVOTemplate):
  datos = {}
  lista_areas = [
    "IMPRESIÓN",
    "SUAJE",
    "MANUALES",
    "LÁSER",
    "CALIDAD",
    "REVELADO",
    "ENSAMBLE",
    "ALMACÉN MP"
  ]
  lista_equipos = [
    ("ATMA 57",{"EQUIPO":"ATMA57","AREA":"IMPRESIÓN"}),
    ("ATMA 71",{"EQUIPO":"ATMA71","AREA":"IMPRESIÓN"}),
    ("ATMA 70",{"EQUIPO":"ATMA70","AREA":"IMPRESIÓN"}),
    ("ATMA 45",{"EQUIPO":"ATMA45","AREA":"IMPRESIÓN"}),
    ("ATMA 710",{"EQUIPO":"ATMA710","AREA":"IMPRESIÓN"}),
    ("ATMA 80",{"EQUIPO":"ATMA80","AREA":"IMPRESIÓN"}),
    ("HORNO 1",{"EQUIPO":"HORNO1","AREA":"IMPRESIÓN"}),
    ("HORNO 2",{"EQUIPO":"HORNO2","AREA":"IMPRESIÓN"}),
    ("HORNO 3",{"EQUIPO":"HORNO3","AREA":"IMPRESIÓN"}),
    ("HORNO 4",{"EQUIPO":"HORNO4","AREA":"IMPRESIÓN"}),
    ("HORNO 5",{"EQUIPO":"HORNO5","AREA":"IMPRESIÓN"}),
    ("IMPRESORA MIMAKI",{"EQUIPO":"IMPRESORA_MIMAKI","AREA":"IMPRESIÓN"}),
    ("IMPRESORA OFFSET",{"EQUIPO":"IMPRESORA_OFFSET","AREA":"IMPRESIÓN"}),
    ("SUAJADORA 1",{"EQUIPO":"SUAJADORA1","AREA":"SUAJE"}),
    ("SUAJADORA 2",{"EQUIPO":"SUAJADORA2","AREA":"SUAJE"}),
    ("SUAJADORA 3",{"EQUIPO":"SUAJADORA3","AREA":"SUAJE"}),
    ("SUAJADORA 4",{"EQUIPO":"SUAJADORA4","AREA":"SUAJE"}),
    ("EMBOSADORA",{"EQUIPO":"EMBOSADORA","AREA":"SUAJE"}),
    ("LÁSER V-460",{"EQUIPO":"LASER_V-460","AREA":"LÁSER"}),
    ("LÁSER M-300",{"EQUIPO":"LASER_M-300","AREA":"LÁSER"}),
    ("LÁSER VLS-360",{"EQUIPO":"LASER_VLS-360","AREA":"LÁSER"}),
    ("MESA DE COORDENADAS X-Y",{"EQUIPO":"MESA_COORDENADAS_XY","AREA":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 2 (CC015)",{"EQUIPO":"PROBADOR_ELECTRICO_2","AREA":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 3 (C0025)",{"EQUIPO":"PROBADOR_ELECTRICO_3","AREA":"CALIDAD"}),
    ("PROBADOR ELÉCTRICO 4 (C0028)",{"EQUIPO":"PROBADOR_ELECTRICO_4","AREA":"CALIDAD"}),
    ("INSOLADORA",{"EQUIPO":"INSOLADORA","AREA":"REVELADO"}),
    ("AFILADOR DE RASEROS",{"EQUIPO":"AFILADOR_RASEROS","AREA":"REVELADO"}),
    ("LAMINADORA 1",{"EQUIPO":"LAMINADORA1","AREA":"ENSAMBLE"}),
    ("LAMINADORA 2",{"EQUIPO":"LAMINADORA2","AREA":"ENSAMBLE"}),
    ("LAMINADORA 3",{"EQUIPO":"LAMINADOR3","AREA":"ENSAMBLE"}),
    ("PICK&PLACE 2",{"EQUIPO":"PICK_PLACE_2","AREA":"ENSAMBLE"}),
    ("TROQUELADORA MANUAL",{"EQUIPO":"TROQUELADORA MANUAL","AREA":"ENSAMBLE"}),
    ("DISPENSADORES",{"EQUIPO":"DISPENSADORES","AREA":"ENSAMBLE"}),
    ("PICK&PLACE 3",{"EQUIPO":"PICK_PLACE_3","AREA":"ENSAMBLE"}),
    ("GUILLOTINA 1",{"EQUIPO":"GUILLOTINA1","AREA":"ALMACÉN MP"}),
    ("GUILLOTINA 2",{"EQUIPO":"GUILLOTINA2","AREA":"ALMACÉN MP"}),
    ("GUILLOTINA 3",{"EQUIPO":"GUILLOTINA3","AREA":"ALMACÉN MP"}),
    ("HOJEADORA",{"EQUIPO":"HOJEADORA","AREA":"ALMACÉN MP"}),
    ("EMBOLSADORA",{"EQUIPO":"EMBOLSADORA","AREA":"MANUALES"}),
  ]
  def __init__(self,datos, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.datos = datos
    self.drop_down_area.items = self.lista_areas
    self.drop_down_equipo.items = self.lista_equipos

  def button_volver_click(self, **event_args):
    self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO_REGISTROS'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)

  def drop_down_area_change(self, **event_args):
    area_seleccionada = self.drop_down_area.selected_value
    equipos_area = []
    self.drop_down_equipo.enabled = True
    
    for item in self.lista_equipos:
      if item[1]["AREA"] == area_seleccionada:
        equipos_area.append(item)
    
    self.drop_down_equipo.items = equipos_area

  def drop_down_equipo_change(self, **event_args):
    print(self.drop_down_equipo.selected_value)



