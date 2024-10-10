from ._anvil_designer import MANTENIMIENTO_CONTROL_SUAJESTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil_extras import popover
from ..MANTENIMIENTO_REGISTRO_SUAJES import MANTENIMIENTO_REGISTRO_SUAJES
from .Form_Edicion_Herramental import Form_Edicion_Herramental
from ..MANTENIMIENTO_INSPECCION_SUAJES import MANTENIMIENTO_INSPECCION_SUAJES
from ..MANTENIMIENTO_INSPECCION_SUAJES.Form_Inspeccion_visual import Form_Inspeccion_visual
from ..MANTENIMIENTO_INSPECCION_SUAJES.Form_Inspeccion_Dimensional import Form_Inspeccion_Dimensional


class MANTENIMIENTO_CONTROL_SUAJES(MANTENIMIENTO_CONTROL_SUAJESTemplate):
  datos = None
  ws_herramentales = None
  ss_vista_herramentales = None
  vista_herramentales = None
  ss_herramentales = None
  herramentales = None
  ss_vista_clientes = None
  vista_clientes = None
  ss_vista_reportes = None
  vista_reportes = None
  ss_reportes = None
  reportes = None
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.set_event_handler('x-abrir_form', self.abrir_popup_form)
    self.set_event_handler('x-validar_reporte', self.validar_reporte)
    self.set_event_handler('x-actualizar_reporte', self.actualizar_reporte)
    self.set_event_handler('x-actualizar_ciclo', self.actualizar_ciclo)
    self.button_actualizar_click()

  ############################################# FUNCIONES PERSONALIZADAS ##############################################
  def set_ini_config(self, datos):
    self.datos = datos
    self.ws_herramentales = app_files.control_herramentales
    self.ss_vista_herramentales = self.ws_herramentales['VISTA_HERRAMENTALES']
    self.ss_herramentales = self.ws_herramentales['HERRAMENTALES']
    self.ss_vista_clientes = self.ws_herramentales['VISTA_CLIENTES']
    self.ss_vista_reportes = self.ws_herramentales['VISTA_REVISION_SUAJES']
    self.ss_reportes = self.ws_herramentales['REVISION_SUAJES']

  def get_datos(self):
    self.vista_herramentales = self.ss_vista_herramentales.rows
    self.vista_clientes = self.ss_vista_clientes.rows
    self.vista_reportes = self.ss_vista_reportes.rows
    
    lista_vista_herramentales = []
    for herramental in list(self.vista_herramentales):
      for cliente in self.vista_clientes:
        if herramental['id_cliente'] == cliente['id_cliente']:
          dicc_herramental = dict(herramental)
          dicc_herramental['cliente'] = cliente['cliente']
          lista_vista_herramentales.append(dicc_herramental)   
    
    for herramental in lista_vista_herramentales:
      herramental['id_inspeccion'] = None
      herramental['status_visual'] = '0'
      herramental['status_dimensional'] = '0'
      for reporte in self.vista_reportes:
        if reporte['id_herramental'] == herramental['id_herramental'] and reporte['registro_principal'] == '1':
          herramental['id_inspeccion'] = reporte['id_inspeccion']
          herramental['status_visual'] = reporte['status_visual']
          herramental['status_dimensional'] = reporte['status_dimensional']
          break
        
    self.repeating_panel_herramentales.items = lista_vista_herramentales
    
  def abrir_popup_form(self, datos, **event_args):
    datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    datos['nombre_usuario'] = self.datos['nombre_usuario']
    if datos['clave_form'] == 'REGISTROS_HERRAMENTAL':
      self.abrir_form(MANTENIMIENTO_REGISTRO_SUAJES(datos))
    elif datos['clave_form'] == 'FORM_HERRAMENTAL':
      self.abrir_form(Form_Edicion_Herramental(datos))
    elif datos['clave_form'] == 'FORM_INSPECCION_VISUAL':
      self.abrir_form(Form_Inspeccion_visual(datos))
    elif datos['clave_form'] == 'FORM_INSPECCION_DIMENSIONAL': 
      self.abrir_form(Form_Inspeccion_Dimensional(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", False)], role="wide-modal-content-bigger")
    if respuesta is not False and  respuesta is not None:
      mensaje = "El registro ha sido guardado correctamente" if respuesta == "registro_guardado" else "El registro ha sido actualizado correctamente."
      Notification(mensaje, title="ÉXITO!", style="success").show(3)
      with Notification("Actualizando tabla...", title="ACTUALIZANDO.", style="notification"):
        self.button_actualizar_click()

  def validar_reporte(self, datos, **event_args):
    self.vista_reportes = self.ss_vista_reportes.rows
    reporte_actual = None
    for reporte in self.vista_reportes:
      if reporte['id_herramental'] == datos['id_herramental'] and reporte['registro_principal'] == '1':
        reporte_actual = reporte
        break
    if reporte_actual is not None: #existe un reporte
      if reporte_actual['status_visual'] == '0': #and self.datos['id_usuario_erp'] == xx # HABILITAR PARA QUE SOLO USUARIO ASIGNADO PUEDA HACER REPORTE VISUAL
        datos['visual_modo'] = 'edicion'
        
        datos['id_inspeccion'] = reporte_actual['id_inspeccion']
        self.abrir_popup_form(datos)
      else:
        datos['modo'] = "visor"
        datos['reporte_actual'] = reporte_actual['id_inspeccion']
        return datos
    else: #nio se ha generado reporte
      print("entrando aqui!!")
      #self.abrir_popup_form(datos)

  def actualizar_ciclo(self, datos, **event_args):
    with Notification("Actualizando próximo ciclo de revisión...", title="ACTUALIZANDO.", style="notification"):
      self.herramentales = self.ss_herramentales.rows
      self.reportes = self.ss_reportes.rows
      for reporte in self.reportes:
        if reporte['id_inspeccion'] == datos['id_inspeccion'] and reporte['registro_principal'] == '1':
          reporte['registro_principal'] = 0
          break
      for herramental in self.herramentales:
        if herramental['id_herramental'] == datos['id_herramental']:
          nueva_alerta = (int(datos['nuevo_ciclo']) - int(herramental['vida_util'])) * 0.9 + int(herramental['vida_util'])
          herramental['vida_util'] = datos['nuevo_ciclo']
          herramental['alerta'] = nueva_alerta
          herramental['activo'] = 1 #################probar si funciona
          break
    Notification("Próximo ciclo de revisión actualizado correctamente!", title="ÉXITO!", style="success").show(3)
    self.button_actualizar_click()

  def actualizar_reporte(self, datos, **event_args):
    msg = "Actualizando reporte visual..." if datos['reporte'] == "visual" else "Actualizando reporte dimensional..."
    with Notification(msg, title="ACTUALIZANDO REPORTE...", style="notification"):
      self.reportes = self.ss_reportes.rows
      for reporte in self.reportes:
        if reporte['id_inspeccion'] == datos['id_inspeccion'] and reporte['registro_principal'] == '1':
          if datos['reporte'] == 'visual':
            reporte['status_visual'] = 2
          elif datos['reporte'] == 'dimensional':
            reporte['status_dimensional'] = 2
          break
    notificacion = "Reporte visual actualizado correctamente!" if datos['reporte'] == "visual" else "Reporte dimensional actualizado correctamente!"      
    Notification(notificacion, title="ÉXITO!", style="success").show(3)
    self.button_actualizar_click()
  ###################################################### EVENTOS ######################################################
  def button_actualizar_click(self, **event_args):
    if len(event_args) > 0:
      with Notification("Actualizando tabla...", title="ACTUALIZANDO.", style="notification"):
        self.get_datos()
    else:
      self.get_datos()
    

  def button_nuevo_click(self, **event_args):
    datos = {}
    datos['clave_form'] = 'FORM_HERRAMENTAL'
    datos['modo'] = "nuevo"
    self.abrir_popup_form(datos)
