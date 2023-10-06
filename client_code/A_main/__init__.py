from ._anvil_designer import A_mainTemplate
from anvil import *
from ..MANTENIMIENTO_CORRECTIVO import MANTENIMIENTO_CORRECTIVO
from ..MANTENIMIENTO_PREVENTIVO import MANTENIMIENTO_PREVENTIVO
from ..MANTENIMIENTO_PREVENTIVO_PROGRAMADO import MANTENIMIENTO_PREVENTIVO_PROGRAMADO
from ..MANTENIMIENTO_PROGRAMA_ANUAL import MANTENIMIENTO_PROGRAMA_ANUAL
from ..MANTENIMIENTO_CORRECTIVO_HISTORIAL import MANTENIMIENTO_CORRECTIVO_HISTORIAL
from ..MANTENIMIENTO_PREVENTIVO_HISTORIAL import MANTENIMIENTO_PREVENTIVO_HISTORIAL
from ..MANTENIMIENTO_PREVENTIVO_PROGRAMADO_HISTORIAL import MANTENIMIENTO_PREVENTIVO_PROGRAMADO_HISTORIAL

class A_main(A_mainTemplate):
  form_activo = None
  datos = {
    'id_usuario_erp': 18,
    'clave_form':"MANTENIMIENTO_PROGRAMA_ANUAL",
    'test':True
  }
  lista_mttos = [
    "PROGRAMA ANUAL DE MANTENIMIENTOS",
    "MANTENIMIENTOS PREVENTIVOS",
    "MANTENIMIENTOS PREVENTIVOS PROGRAMADOS",
    "MANTENIMIENTOS CORRECTIVOS"
  ]
  def __init__(self, **properties):
    self.drop_down_mantenimientos.items = self.lista_mttos
    
    self.init_components(**properties)
  
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.content_panel.visible = True

    if self.datos['id_usuario_erp'] == 18:
      self.datos['clave_form'] = "MANTENIMIENTO_PROGRAMA_ANUAL"
      self.datos['test'] = True
      self.actualizar_form_activo(self.datos)

  def actualizar_form_activo(self, datos, **event_args):
    if datos['clave_form'] == 'MANTENIMIENTO_PROGRAMA_ANUAL':
      self.abrir_form(MANTENIMIENTO_PROGRAMA_ANUAL(datos))
    elif datos['clave_form'] == 'MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO':
      self.abrir_form(MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO(datos))

  def abrir_form(self, form_de_interes):
    try: #Se utiliza un try porque la primera vez que se abre el form RECUERSOS_HUMANOS no tiene ningún form hijo cargado, entonces levantará un error.
      self.form_activo.remove_from_parent()
    except: #no se necesita para manejar el error, pero el 'except' es obligado a estar cuando se usa un try. ¡NO BORRAR!
      pass
    self.form_activo = form_de_interes
    self.add_component(self.form_activo)