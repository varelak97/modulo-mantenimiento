from ._anvil_designer import Form_Inspeccion_visualTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ... import Funciones_Globales

class Form_Inspeccion_visual(Form_Inspeccion_visualTemplate):
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
      self.text_area_filo,
      self.text_area_union,
      self.text_area_estado,
      self.button_estado_bien,
      self.button_estado_mal,
      self.button_filo_bien,
      self.button_filo_mal,
      self.button_union_bien,
      self.button_union_mal
    ]
    self.lista_componentes_validacion = [
      self.text_area_filo,
      self.text_area_union,
      self.text_area_estado,
      self.button_filo_bien,
      self.button_union_bien,
      self.button_estado_bien
    ]
    self.modos_botones = [
        {'tag':'filo_bien','modo':True,'llave':'status_filo'},
        {'tag':'union_bien','modo':True,'llave':'status_union'},
        {'tag':'estado_bien','modo':True,'llave':'status_estado'},
        {'tag':'filo_mal','modo':False,'llave':'status_filo'},
        {'tag':'union_mal','modo':False,'llave':'status_union'},
        {'tag':'estado_mal','modo':False,'llave':'status_estado'}
      ]
    self.status_botones = [
      {'tag':"filo_bien", "valor": None, 'llave':'status_filo'},
      {'tag':"union_bien", "valor": None, 'llave':'status_union'},
      {'tag':"estado_bien", "valor": None, 'llave':'status_estado'}
    ]
    self.campos_no_obligatorios = ["comentarios_filo", "comentarios_union", "comentarios_estado"]

  def get_datos(self):
    self.reporte_suajes = self.ss_reporte_suajes.rows
    self.suajes = self.ss_suajes.rows
    
    if self.datos['modo'] in ['edicion', 'visor']:
      self.vista_clientes = self.ss_vista_clientes.rows
      self.vista_suajes = self.ss_vista_suajes.rows
      for row in self.reporte_suajes:
        if self.datos['id_inspeccion'] == row['id_inspeccion']:
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
    dicc_nuevo_registro['id_inspeccion'] = max([int(item['id_inspeccion']) for item in self.reporte_suajes]) + 1 if self.datos['modo'] == 'edicion' else 0
    dicc_nuevo_registro['id_usuario_registrador'] = self.datos['id_usuario_erp']
    dicc_nuevo_registro['nombre_usuario'] = self.datos['nombre_usuario']
    dicc_nuevo_registro['status_filo'] = int(self.status_botones[0]['valor'])
    dicc_nuevo_registro['status_union'] = int(self.status_botones[1]['valor'])
    dicc_nuevo_registro['status_estado'] = int(self.status_botones[2]['valor'])
    
    if self.datos['modo'] == 'validacion':
      dicc_nuevo_registro['id_herramental'] = self.datos['id_herramental']
      dicc_nuevo_registro['status_visual'] = 1
      dicc_nuevo_registro['registro_principal'] = 1
    else:
      self.registro_actual['registro_principal'] = 0
    if self.datos['modo'] == 'validacion':
      confirmacion_uso = alert("¿Se puede seguir utilizando este suaje?", title="INSPECCIÓN VISUAL", buttons=[("SI", True), ("NO", False)])
      if confirmacion_uso:
        alert(f"valor de confirmacion.{confirmacion_uso}")
        if int(self.datos['vida_util']) <= int(self.datos['contador']):
          alert(f"valor de vida util:{self.datos['vida_util']} y valor de contador:{self.datos['contador']}")
          input = TextBox(type='number', role='outlined', background='On Primary')
          respuesta = alert(input, title="INGRESE PRÓXIMO CICLO PARA REVISIÓN:", buttons=[("GUARDAR", True),("IGNORAR", False)])
          if respuesta:
            with Notification("Actualizando ciclo para próxima revisión", title="PRÓXIMO CICLO DE REVISIÓN", style="notification"):
              for suaje in self.suajes:
                if self.datos['id_herramental'] == suaje['id_herramental']:
                  suaje['vida_util'] = input.text
                  break
        else:
          alert(f"no mayor y valor de vida util:{self.datos['vida_util']} y valor de contador:{self.datos['contador']}")
        
      else:
        if not confirmacion_uso:
          with Notification("Enviando notificación al jefe de Diseño", title="NOTIFICACIÓN DE CAMBIO DE SUAJE", style="notification"):
            text = f"CLIENTE: {self.text_box_cliente.text}\n"
            text += f"CODIGO DE SUAJE: {self.text_box_codigo_suaje.text}\n"
            text += f"TIPO DE SUAJE: {self.text_box_tipo_suaje.text}\n"
            text += f"DESCRIPCIÓN: {self.text_area_descripcion.text}\n"
            text += "\nREVISIÓN DE FILO EN PLECAS:\n"
            text += f"{self.text_area_filo.text}\n"
            text += "\nREVISIÓN DE UNIÓN EN PLECAS:\n"
            text += f"{self.text_area_union.text}\n"
            text += "\nREVISIÓN DE BUEN ESTADO DE PLECAS:\n"
            text += f"{self.text_area_estado.text}\n"
            anvil.server.call('enviar_mail', "a.varela@ensel.org", f"SOLICITUD DE CAMBIO DE SUAJE, CLIENTE: {self.text_box_cliente.text}", text)
    self.ss_reporte_suajes.add_row(**dicc_nuevo_registro)
  ###################################################### EVENTOS #####################################################
  def button_guardar_click(self, **event_args):
    status = Funciones_Globales.validar_campos( self.lista_componentes_validacion, self.registro_actual, self.campos_no_obligatorios, self.datos['modo'], self.status_botones, None)
    if status == 1:
      mensaje = "Actualizando registros..." if self.datos['modo'] in ['edicion', 'validacion'] else "Guardando registro..."
      titulo = "ACTUALIZANDO." if self.datos['modo'] in ['edicion', 'validacion'] else "GUARDANDO."
      with Notification(mensaje, title=titulo, style="notification"):
        self.guarda_datos(self.datos['modo'])
    elif status == 2:
      alert("No hay cambios que guardar.", title="ERROR!")
    elif status == 3:
      alert("faltan campos por llenar!", title="ERROR!")

  def button_filo_bien_click(self, **event_args):
    self.button_filo_bien.background = app.theme_colors['Primary']
    self.button_filo_bien.foreground = app.theme_colors['On Primary']
    
    self.button_filo_mal.background = app.theme_colors['LightGray']
    self.button_filo_mal.foreground = app.theme_colors['Secondary']

    self.status_botones[0]['valor'] = True

  def button_filo_mal_click(self, **event_args):
    self.button_filo_bien.background = app.theme_colors['LightGray']
    self.button_filo_bien.foreground = app.theme_colors['Secondary']
    
    self.button_filo_mal.background = app.theme_colors['Red']
    self.button_filo_mal.foreground = app.theme_colors['On Primary']

    self.status_botones[0]['valor'] = False

  def button_union_bien_click(self, **event_args):
    self.button_union_bien.background = app.theme_colors['Primary']
    self.button_union_bien.foreground = app.theme_colors['On Primary']
    
    self.button_union_mal.background = app.theme_colors['LightGray']
    self.button_union_mal.foreground = app.theme_colors['Secondary']

    self.status_botones[1]['valor'] = True

  def button_union_mal_click(self, **event_args):
    self.button_union_bien.background = app.theme_colors['LightGray']
    self.button_union_bien.foreground = app.theme_colors['Secondary']
    
    self.button_union_mal.background = app.theme_colors['Red']
    self.button_union_mal.foreground = app.theme_colors['On Primary']

    self.status_botones[1]['valor'] = False

  def button_estado_bien_click(self, **event_args):
    self.button_estado_bien.background = app.theme_colors['Primary']
    self.button_estado_bien.foreground = app.theme_colors['On Primary']
    
    self.button_estado_mal.background = app.theme_colors['LightGray']
    self.button_estado_mal.foreground = app.theme_colors['Secondary']

    self.status_botones[2]['valor'] = True

  def button_estado_mal_click(self, **event_args):
    self.button_estado_bien.background = app.theme_colors['LightGray']
    self.button_estado_bien.foreground = app.theme_colors['Secondary']
    
    self.button_estado_mal.background = app.theme_colors['Red']
    self.button_estado_mal.foreground = app.theme_colors['On Primary']

    self.status_botones[2]['valor'] = False

