from ._anvil_designer import Form_Inspeccion_DimensionalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ... import Funciones_Globales


class Form_Inspeccion_Dimensional(Form_Inspeccion_DimensionalTemplate):
  ws_herramentales = None
  ss_reporte_suajes = None
  reporte_suajes = None
  ss_vista_clientes = None
  vista_clientes = None
  ss_vista_suajes = None
  vista_suajes = None
  ss_suajes = None
  suajes = None
  registro_actual = {}
  datos = None
  modos_botones = None
  status_botones = None
  lista_componentes = None
  lista_componentes_validacion = None
  campos_no_obligatorios = None

  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.set_ini_config(datos)
    self.get_datos()

  ############################################# FUNCIONES PERSONALIZADAS #############################################
  def set_ini_config(self, datos):
    self.datos = datos
    self.ws_herramentales = app_files.control_herramentales
    self.ss_reporte_suajes = self.ws_herramentales['REVISION_SUAJES']
    self.ss_vista_clientes = self.ws_herramentales['VISTA_CLIENTES']
    self.ss_vista_suajes = self.ws_herramentales['VISTA_HERRAMENTALES']
    self.ss_suajes = self.ws_herramentales['HERRAMENTALES']
    
    self.lista_componentes = [
      self.text_box_cliente,
      self.text_box_codigo_suaje,
      self.text_box_tipo_suaje,
      self.text_area_descripcion,
      self.text_box_revisor,
      self.text_area_medidas,
      self.button_medidas_bien,
      self.button_medidas_mal
    ]
    self.lista_componentes_validacion = [
      self.text_area_medidas,
      self.button_medidas_bien
    ]
    self.modos_botones = [
      {'tag':'medidas_bien','modo':True,'llave':'status_medidas'},
      {'tag':'medidas_mal','modo':False,'llave':'status_medidas'},
    ]
    self.status_botones = [
      {'tag':"medidas_bien", "valor": None, 'llave':'status_medidas'}
    ]
    self.campos_no_obligatorios = ["comentarios_medidas"]

  def get_datos(self):
    self.reporte_suajes = self.ss_reporte_suajes.rows
    self.suajes = self.ss_suajes.rows
    
    if self.datos['modo'] in ['edicion', 'visor', 'nuevo_insp']:
      self.vista_clientes = self.ss_vista_clientes.rows
      self.vista_suajes = self.ss_vista_suajes.rows
      for row in self.reporte_suajes:
        if self.datos['id_inspeccion'] == row['id_inspeccion'] and row['registro_principal'] == '1':
          self.registro_actual = row
          break
      dicc_registro_actual = dict(self.registro_actual)
      for suaje in self.vista_suajes:
        if dicc_registro_actual['id_herramental'] == suaje['id_herramental']:
          dicc_registro_actual['codigo_herramental'] = suaje['codigo_herramental']
          dicc_registro_actual['descripcion'] = suaje['descripcion']
          dicc_registro_actual['id_cliente'] = suaje['id_cliente']
          dicc_registro_actual['tipo_suaje'] = suaje['tipo_suaje']
          break
      for cliente in self.vista_clientes:
        if dicc_registro_actual['id_cliente'] == cliente['id_cliente']:
          dicc_registro_actual['cliente'] = cliente['cliente']
          break
      #if self.datos['modo'] != 'nuevo_insp':
      Funciones_Globales.fill_formulario(self.lista_componentes,dicc_registro_actual, self.modos_botones)
    elif self.datos['modo'] == 'nuevo':
      self.text_box_revisor.text = self.datos['nombre_usuario']
      self.text_box_cliente.text = self.datos['cliente']
      self.text_box_codigo_suaje.text = self.datos['codigo_herramental']
      self.text_box_tipo_suaje.text = self.datos['tipo_suaje']
      self.text_area_descripcion.text = self.datos['descripcion']
    
    if self.datos['modo'] == 'visor':
      self.disable_inputs()
      self.button_guardar.visible = False

  def disable_inputs(self):
    for input in self.lista_componentes:
      input.enabled = False
    
  def guarda_datos(self, modo):
    datos_form = Funciones_Globales.genera_diccionario(self.lista_componentes_validacion, None)
    dicc_nuevo_registro = dict(self.registro_actual)
    dicc_nuevo_registro.update(datos_form)
    if self.datos['modo'] == 'nuevo':
      dicc_nuevo_registro['id_inspeccion'] = max([int(item['id_inspeccion']) for item in self.reporte_suajes]) + 1 if len(self.reporte_suajes) > 0 else 0
    dicc_nuevo_registro['id_usuario_registrador'] = self.datos['id_usuario_erp']
    dicc_nuevo_registro['nombre_usuario'] = self.datos['nombre_usuario']
    dicc_nuevo_registro['status_medidas'] = int(self.status_botones[0]['valor'])
    
    if self.datos['modo'] in ["nuevo", "nuevo_insp"]: #antes validacion
      dicc_nuevo_registro['id_herramental'] = self.datos['id_herramental']
      dicc_nuevo_registro['status_dimensional'] = 1
      if self.datos['modo'] == 'nuevo':
        dicc_nuevo_registro['status_visual'] = 0
      dicc_nuevo_registro['registro_principal'] = 1
    if self.datos['modo'] != "nuevo":
      self.registro_actual['registro_principal'] = 0
    if self.datos['modo'] in ['nuevo', 'nuevo_insp']:
      confirmacion_uso = alert("¿Se puede seguir utilizando este suaje?", title="INSPECCIÓN DIMENSIONAL", buttons=[("SI", True), ("NO", False)])
      if confirmacion_uso:
        dicc_nuevo_registro['status_dimensional'] = 2
      else:
        with Notification("Enviando notificación al jefe de Diseño", title="NOTIFICACIÓN DE CAMBIO DE SUAJE", style="notification"):
          text = f"CLIENTE: {self.text_box_cliente.text}\n"
          text += f"CODIGO DE SUAJE: {self.text_box_codigo_suaje.text}\n"
          text += f"TIPO DE SUAJE: {self.text_box_tipo_suaje.text}\n"
          text += f"DESCRIPCIÓN: {self.text_area_descripcion.text}\n"
          text += "\nCORROBORAR MEDIDAS CON PLANOS DE DIBUJO DE DISEÑO:\n"
          text += f"{self.text_area_medidas.text}\n"
          anvil.server.call('enviar_mail', "a.varela@ensel.org", f"SOLICITUD DE CAMBIO DE SUAJE, CLIENTE: {self.text_box_cliente.text}", text)
    self.ss_reporte_suajes.add_row(**dicc_nuevo_registro)

  ###################################################### EVENTOS #####################################################
  def button_guardar_click(self, **event_args):
    if self.button_medidas_bien.background == app.theme_colors['Primary']:
      self.status_botones[0]['valor'] = True
    elif self.button_medidas_mal.background == app.theme_colors['Red']:
      self.status_botones[0]['valor'] = False
      
    status = Funciones_Globales.validar_campos( self.lista_componentes_validacion, self.registro_actual, self.campos_no_obligatorios, self.datos['modo'], self.status_botones, None)
    if status == 1:
      mensaje = "Actualizando registros..." if self.datos['modo'] == 'edicion' else "Guardando registro..."
      titulo = "ACTUALIZANDO." if self.datos['modo'] == 'edicion' else "GUARDANDO."
      with Notification(mensaje, title=titulo, style="notification"):
        self.guarda_datos(self.datos['modo'])
        self.raise_event("x-close-alert",value="registro_guardado")
    elif status == 2:
      alert("No hay cambios que guardar.", title="ERROR!")
    elif status == 3:
      alert("faltan campos por llenar!", title="ERROR!")

  def button_medidas_bien_click(self, **event_args):
    self.button_medidas_bien.background = app.theme_colors['Primary']
    self.button_medidas_bien.foreground = app.theme_colors['On Primary']
    
    self.button_medidas_mal.background = app.theme_colors['LightGray']
    self.button_medidas_mal.foreground = app.theme_colors['Secondary']

    self.status_botones[0]['valor'] = True

  def button_medidas_mal_click(self, **event_args):
    self.button_medidas_bien.background = app.theme_colors['LightGray']
    self.button_medidas_bien.foreground = app.theme_colors['Secondary']
    
    self.button_medidas_mal.background = app.theme_colors['Red']
    self.button_medidas_mal.foreground = app.theme_colors['On Primary']

    self.status_botones[0]['valor'] = False
