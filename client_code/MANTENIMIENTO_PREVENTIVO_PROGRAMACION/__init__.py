from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_PROGRAMACIONTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from datetime import datetime, date, timedelta
import calendar

class MANTENIMIENTO_PREVENTIVO_PROGRAMACION(MANTENIMIENTO_PREVENTIVO_PROGRAMACIONTemplate):
  ################################### DEFINICION DE VARIABLES ####################################
  datos = {}
  
  
  lista_areas = [
    "IMPRESIÓN",
    "SUAJE",
    "MANUALES",
    "LÁSER",
    "CALIDAD",
    "REVELADO",
    "ENSAMBLE",
    "ALMACÉN MP", 
  ]
  actividades_equipos_atma_trimestral = [
    {"id":1,"actividad":"DESTAPAR Y LIMPIAR INTERIOR DEL EQUIPO"},
    {"id":3,"actividad":"LIMPIAR SILENCIADORES CON AGUA A PRESIÓN"},
    {"id":6,"actividad":"ENGRASAR TORNILLOS Y RIELES DE DESPLAZAMIENTO"},
    {"id":7,"actividad":"REVISAR TORNILLERÍA: APRETAR O REEMPLAZAR SI ES NECESARIO"},
    {"id":8,"actividad":"REVISAR QUE NO EXISTAN FUGAS DE AIRE DEL SISTEMA NEUMÁTICO"},
    {"id":9,"actividad":"REVISAR CONEXIONES EN EL PANEL DE CONTROL"},
    {"id":10,"actividad":"LIMPIAR PANEL DE CONTROL"},
    {"id":11,"actividad":"VERIFICAR QUE FUNCIONEN PAROS DE EMERGENCIA"},
    {"id":12,"actividad":"REVISAR QUE INDICADOR DE BATERÍA EN PLC NO ESTÉ ENCENDIDO"}
  ]
  actividades_equipos_atma80_710_trimestral = [
    {"id":2,"actividad":"DRENAR CONTENEDOR DE ACEITE DEL SISTEMA NEUMÁTICO"},
    {"id":4,"actividad":"ENGRASAR CHUMACERAS Y RIELES DE DESPLAZAMIENTO"},
    {"id":5,"actividad":"REVISAR EL NIVEL DE ACEITE DE LA CAJA REDUCTORA"}
  ]
  actividades_equipos_suaje_trimestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA EN AREA DE CORREDERAS"},
    {"id":2,"actividad":"REALIZAR LIMPIEZA GENERAL"},
    {"id":3,"actividad":"ENGRASAR CHUMACERAS"},
    {"id":4,"actividad":"LUBRICAR ENGRANES PRINCIPALES"},
    {"id":5,"actividad":"LIMPIAR ANILLO DE CONTACTO DE BOBINA Y VERIFICAR CARBÓN"},
    {"id":6,"actividad":"ASPIRAR PANEL DE CONTROL"},
    {"id":7,"actividad":"VERIFICAR CONEXIONES"},
    {"id":8,"actividad":"REVISAR TORNILLERÍA: APRETAR O REEMPLAZAR SI ES NECESARIO"},
    {"id":9,"actividad":"VERIFICAR ESTADO DE LA BANDA"},
    {"id":10,"actividad":"VERIFICAR QUE BOMBAS DE LUBRICACIÓN FUNCIONEN"},
    {"id":11,"actividad":"LIMPIAR ANILLOS DE CONTACTO DE BOBINA Y VERIFICAR CARBONES"},
    {"id":12,"actividad":"VERIFICAR QUE LOS PAROS DE EMERGENCIA FUNCIONEN"},
    {"id":13,"actividad":"APLICAR ACEITE TRANSMISIÓN EN CONTENEDORES DEL EJE PRINCIPAL"},
    {"id":14,"actividad":"DRENAR CONTENEDORES DE ACEITE USADO"}
  ]
  actividades_equipo_embolsadora_trimestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA GENERAL Y ASPIRAR EL EQUIPO."},
    {"id":2,"actividad":"REALIZAR LIMPIEZA EN LOS RODILLOS DEL EQUIPO."},
    {"id":3,"actividad":"INSPECCIONAR Y DRENAR CONTENEDOR DE AGUA DEL SUMINISTRO."},
    {"id":4,"actividad":"LIMPIAR CABEZAL DE IMPRESIÓN CON ALCOHOL ISOPROPÍLICO."},
    {"id":5,"actividad":"ASPIRAR ÁREA DE TARJETAS ELECTRÓNICAS (CAJA NEGRA)."},
    {"id":6,"actividad":"VERIFICAR EL ESTADO DE LAS CONEXIONES."},
    {"id":7,"actividad":"LIMPIAR Y LUBRICAR EJES DE MOVIMIENTO DE PLANCHA SELLADORA."},
    {"id":8,"actividad":"LUBRICAR RODILLOS DEL SISTEMA DESENROLLADOR."},
    {"id":9,"actividad":"REVISAR QUE NO EXISTAN FUGAS DE AIRE DEL SISTEMA NEUMÁTICO"},
    {"id":10,"actividad":"ASPIRAR REGULADOR DE VOLTAJE."}
  ]
  actividades_equipos_laser_semanal = [
    {"id":1,"actividad":"QUITAR FILTROS DE AIRE DE EQUIPO Y LIMPIAR ÁREA DE FILTROS."},
    {"id":2,"actividad":"INSTALAR FILTROS DE AIRE LIMPIOS (LAVAR EN CASO DE NO TENER)."},
    {"id":3,"actividad":"LAVAR FILTROS DE AIRE DESINSTALADOS CON AGUA Y JABÓN."},
    {"id":4,"actividad":"REVISAR TRAMPA DE TUBO DE EXTRACTOR DE AIRE."},
    {"id":5,"actividad":"VERIFICAR QUE ESTE LIBRE DE OBJETOS LIMPIAR EN CASO DE REQUERIR)"}
  ]
  actividades_equipos_laser_mensual = [
    {"id":1,"actividad":"ABRIR COMPUERTA DE TUBO LÁSER, ASPIRAR Y REALIZAR LIMPIEZA."},
    {"id":2,"actividad":"VERIFICAR EL ESTADO DE LAS CONEXIONES"},
    {"id":3,"actividad":"RETIRAR TUBO DE EXTRACTOR Y ASPIRAR EN LA SALIDA DEL EQUIPO."},
    {"id":4,"actividad":"RETIRAR MESA DE CORTE Y REALIZAR LIMPIEZA."},
    {"id":5,"actividad":"ASPIRAR INTERIOR DEL EQUIPO."},
    {"id":6,"actividad":"LUBRICAR TORNILLOS DE DESPLAZAMIENTO DEL EJE Z."},
    {"id":7,"actividad":"VERIFICAR ESTADO DE LAS BANDAS Y SU TENSIÓN."},
    {"id":8,"actividad":"ASPIRAR REGULADOR."},
    {"id":9,"actividad":"VERIFICAR LA ALINEACIÓN DEL EJE X."},
  ]
  actividades_equipo_mimaki_mensual = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO."},
    {"id":2,"actividad":"LUBRICAR RIELES Y TORNILLOS DE DESPLAZAMIENTO."},
    {"id":3,"actividad":"ASPIRAR EL INTERIOR DEL EQUIPO."},
    {"id":4,"actividad":"REVISAR TANQUE DE RESIDUOS, VACIAR SI REQUIERE."},
    {"id":5,"actividad":"APLICAR 5 GOTAS DE SOLVENTE EN AGUJERO DE CHAROLA NEGRA"},
    {"id":6,"actividad":"INSPECCIONAR VÍDRIO DE LÁMPARA, LIMPIAR SI REQUIERE."},
    {"id":7,"actividad":"INSPECCIONAR WIPER Y REALIZAR LIMPIEZA."},
    {"id":8,"actividad":"APLICAR 5 GOTAS DE SOLVENTE WIPER."},
    {"id":9,"actividad":"VERIFICAR QUE FUNCIONE EL PARO DE EMERGENCIA."},
  ]
  actividades_equipo_mesa_coordenadas_trimestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO."},
    {"id":2,"actividad":"LIMPIAR Y ENGRASAR RIELES DE DESPLAZAMIENTO."},
    {"id":3,"actividad":"RETIRAR TAPA DE SPOT Y ASPIRAR EL ÁREA."},
    {"id":4,"actividad":"VERIFICAR EL ESTADO DE LAS CONEXIONES."}
  ]
  actividades_equipos_probadores_electricos_mensual = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA DE TARJETA ELECTRONICA."},
    {"id":2,"actividad":"VERIFICAR QUE LOS PINES ESTEN EN BUEN ESTADO."},
    {"id":3,"actividad":"VERIFICAR LA CONTINUIDAD DE CADA PIN CON MULTÍMETRO."}
  ]
  actividades_equipo_probador_electrico_2_mensual = [
    {"id":4,"actividad":"COMPARAR VALOR DE RESISTENCIA MOSTRADO EN PANTALLA CONTRA"},
    {"id":5,"actividad":"EL VALOR OBTENIDO CON MULTÍMETRO DIGITAL EN CADA PIN."},
    {"id":6,"actividad":"USAR ADITAMENTO CON RESISTENCIA DE 47 OHMS."}
  ]
  actividades_equipo_insoladora_semestral = [
    {"id":1,"actividad":"QUITAR TAPAS FRONTALES DEL EQUIPO (INFERIOR Y NEGRA)."},
    {"id":2,"actividad":"ASPIRAR EL INTERIOR DEL EQUIPO."},
    {"id":3,"actividad":"VERIFICAR EL ESTADO DE LAS CONEXIONES."},
    {"id":4,"actividad":"LIMPIAR PAREDES INTERIORES NEGRAS CON UNA TRAPO Y AGUA."},
    {"id":5,"actividad":"LIMPIAR TURBINA IZQUIERDA Y DERECHA."},
    {"id":6,"actividad":"LIMPIAR LÁMPARA Y REFLECTOR UV CON ALCOHOL ISOPROPÍLICO."},
    {"id":7,"actividad":"GIRAR 1/4 DE VUELTA LÁMPARA UV."},
    {"id":8,"actividad":"LIMPIAR SENSOR DE LUZ."},
    {"id":9,"actividad":"LIMPIAR LADO INTERNO DEL VÍDRIO ."},
    {"id":10,"actividad":"ASPIRAR LOS VENTILADORES (NEGROS CUADRADOS) DEL INTERIOR."}
  ]
  actividades_equipo_afilador_raseros_trimestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO."},
    {"id":2,"actividad":"LUBRICAR RIELES DE DESPLAZAMIENTO."},
    {"id":3,"actividad":"ABRIR COMPUERTA DE RUEDA DIAMANTE Y ASPIRAR."},
    {"id":4,"actividad":"ABRIR COMPUERTA DE RUEDA DIAMANTE Y ASPIRAR."},
    {"id":5,"actividad":"LIMPIAR RUEDA DE DIAMANTE."},
    {"id":6,"actividad":"VACIAR CONTENIDO DEL FILTRO DE LA ASPIRADORA INTERNA."}
  ]
  actividades_equipo_sps_mensual = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO."},
    {"id":2,"actividad":"APLICAR GRASA EN LOS PUNTOS MARCADOS CON AMARILLO."},
    {"id":3,"actividad":"APLICAR ACEITE EN LOS PUNTOS MARCADOS CON ROJO."},
    {"id":4,"actividad":"VERIFICAR NIVEL DE ACEITE DE TRANSMISIÓN, RELLENAR SI REQUIERE."},
    {"id":5,"actividad":"VERIFICAR NIVEL DE GRASA EN EL SISTEMA DE LUBRICACIÓN."},
    {"id":6,"actividad":"VERIFICAR NIVEL DE ACEITE DEL SISTEMA RASERO-ENTINTADOR."},
    {"id":7,"actividad":"REALIZAR LIMPIEZA GENERAL DE TURBINA DE VACIO."},
    {"id":8,"actividad":"LIMPIAR FILTROS DE TURBINA DE VACIO."},
    {"id":9,"actividad":"ASPIRAR PARRILLA NEGRA PARA ENFRIAMIENTO DE TURBINA DE VACIO."},
    {"id":10,"actividad":"VERIFICAR QUE FUNCIONEN PAROS DE EMERGENCIA."}
  ]
  actividades_equipo_offset_trimestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO."},
    {"id":2,"actividad":"ASPIRAR PANEL DE CONTROL Y ÁREA DE COMPRESOR."},
    {"id":3,"actividad":"VERIFICAR EL ESTADO DE LAS CONEXIONES."},
    {"id":4,"actividad":"ASPIRAR ÁREA DE ENTRADA DE PAPEL."},
    {"id":5,"actividad":"DESARMAR Y LIMPIAR EL TINTERO."},
    {"id":6,"actividad":"LUBRICAR PARTES MOVILES CON ACEITE PARA TRANSMISIÓN."},
    {"id":7,"actividad":"VERIFICAR QUE PAROS DE EMERGENCIA FUNCIONEN."}
  ]
  actividades_equipo_embosadora_trimestral = [
    {"id":1,"actividad":"LUBRICAR LOS 4 POSTES CON GRASA."},
    {"id":2,"actividad":"LUBRICAR CHUMACERAS DEL MOTOR."},
    {"id":3,"actividad":"REALIZAR LIMPIEZA GENERAL."},
    {"id":4,"actividad":"ASPIRAR PANEL DE CONTROL."},
    {"id":5,"actividad":"VERIFICAR CONEXIONES."},
    {"id":6,"actividad":"REVISAR TORNILLERÍA: APRETAR O REEMPLAZAR SI ES NECESARIO."}
  ]
  actividades_equipo_pickAndPlace_3_trimestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO."},
    {"id":2,"actividad":"ENGRASAR TORNILLOS Y RIELES DE DESPLAZAMIENTO."},
    {"id":3,"actividad":"ASPIRAR REGULADOR DE VOLTAJE."},
  ]
  actividades_equipo_horno_1_semanal = [
    {"id":1,"actividad":"ENGRASAR CHUMACERA DE  MOTOR DE CAMARA DE CALOR."},
    {"id":2,"actividad":"ENGRASAR LAS 2 CHUMACERAS DE TURBINA CAMARA DE CALOR."},
    {"id":3,"actividad":"ENGRASAR CHUMACERA DE  MOTOR DE CAMARA DE ENFRIAMIENTO."},
    {"id":4,"actividad":"REALIZAR LIMPIEZA EXTERNA DE MOTORES."}
  ]
  actividades_equipo_horno_1_mensual = [
    {"id":1,"actividad":"LAVAR FILTROS DE AIRE CON AGUA A PRESIÓN."},
    {"id":2,"actividad":"ASPIRAR PANEL DE CONTROL."},
    {"id":3,"actividad":"VERIFICAR CONEXIONES EN EL PANEL DE CONTROL."},
    {"id":4,"actividad":"ASPIRAR COMPUERTA CON VENTILAS PARA TRANSFORMADOR."},
    {"id":5,"actividad":"ENGRASAR LAS 2 CHUMACERAS DE CADA RODILLO DE LA BANDA."},
    {"id":6,"actividad":"REVISAR CENTRADO DE BANDA, AJUSTAR EN CASO DE REQUERIR."}
  ]
  actividades_equipo_horno_1_semestral = [
    {"id":1,"actividad":"QUITAR TAPAS SECCIÓN DE CALOR (SC) Y SECCIÓN UV (SUV)."},
    {"id":2,"actividad":"LIMPIAR TAPAS SC Y SU CON ALCOHOL Y AGUA 50/50"},
    {"id":3,"actividad":"DESINSTALAR TERMOPAR Y TAPAS INTERNAS DE SC."},
    {"id":4,"actividad":"DESINSTALAR BANDA."},
    {"id":5,"actividad":"LAVAR TAPAS INTERNAS DE SC CON AGUA A PRESIÓN."},
    {"id":6,"actividad":"LAVAR BANDA CON AGUA A PRESIÓN"},
    {"id":7,"actividad":"LIMPIAR PAREDES INTERNAS DE SC CON ALCOHOL Y AGUA 50/50"},
    {"id":8,"actividad":"LIMPIAR TURBINA DE SECCIÓN DE CALOR"},
    {"id":9,"actividad":"LIMPIAR PAREDES INTERNAS DE SECCIÓN SUV"},
    {"id":10,"actividad":"LIMPIAR REFLECTOR Y LÁMPARA CON ALCOHOL ISOPROPÍLICO"},
    {"id":11,"actividad":"REVISAR CONEXIONES DE RESISTENCIAS APRETAR SI ES NECESARIO."},
    {"id":12,"actividad":"QUITAR TAPA SECCIÓN DE ENFRIAMIENTO (SE)"},
    {"id":13,"actividad":"LIMPIAR TAPA SE CON ALCOHOL Y AGUA 50/50"},
    {"id":14,"actividad":"LIMPIAR PAREDES INTERNAS DE SE CON ALCOHOL Y AGUA 50/50"},
    {"id":15,"actividad":"LIMPIAR TURBINA SE"},
    {"id":16,"actividad":"INSTALAR BANDA"},
    {"id":17,"actividad":"INSTALAR TAPAS INTERNAS SC Y TERMOPAR."},
    {"id":18,"actividad":"NSTALAR TAPAS PRINCIPALES SC Y SUV"},
    {"id":19,"actividad":"INSTALAR TAPA SE"},
    {"id":20,"actividad":"AJUSTAR BANDA"},
    {"id":21,"actividad":"VERIFICAR QUE FUNCIONEN LOS 2 PAROS DE EMERGENCIA."},
    {"id":22,"actividad":"ASPIRAR ÁREA DE TRANSFORMADOR"}
  ]
  actividades_equipo_horno_2_semestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA DE LOS 3 VENTILADORES"},
    {"id":2,"actividad":"LAVAR LAS 2 TAPAS CON VENTILAS USAR AGUA A PRESIÓN."},
    {"id":3,"actividad":"QUITAR TAPA SUPERIOR ASPIRAR AREA DE LÁMPARA."},
    {"id":4,"actividad":"ASPIRAR EL PANEL DE CONTROL."},
    {"id":5,"actividad":"VERIFICAR CONEXIONES EN PANEL DE CONTROL."},
    {"id":6,"actividad":"LIMPIAR LÁMPARA Y REFLECTOR CON ALCOHOL ISOPROPÍLICO."},
    {"id":7,"actividad":"ENGRASAR LAS 2 CHUMACERAS DE CADA RODILLO."},
    {"id":8,"actividad":"ENGRASAR LAS 2 CHUMACERAS DEL EXTRACTOR."},
    {"id":9,"actividad":"VERIFICAR EL ESTADO DE BANDA DEL EXTRACTOR."}
  ]
  actividades_equipo_horno_3_semestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA DEL ABANICO DE VENTILACIÓN."},
    {"id":2,"actividad":"ASPIRAR EL INTERIOR DEL EQUIPO."},
    {"id":3,"actividad":"QUITAR TAPA SUPERIOR ASPIRAR AREA DE LÁMPARA."},
    {"id":4,"actividad":"LIMPIAR LÁMPARA Y REFLECTOR CON ALCOHOL ISOPROPÍLICO."},
    {"id":5,"actividad":"VERIFICAR CONEXIONES."}
  ]
  actividades_equipo_horno_4_semestral = [
    {"id":1,"actividad":"ABRIR PANEL DE CONTROL Y ASPIRARLO."},
    {"id":2,"actividad":"VERIFICAR CONEXIONES EN PANEL DE CONTROL."},
    {"id":3,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO."},
    {"id":4,"actividad":"VERIFICAR EL VOLTAJE DE SUMINISTRO."}
  ]
  actividades_equipo_horno_5_semestral = [
    {"id":1,"actividad":"QUITAR TAPA SUPERIOR Y REFLECTOR. ASPIRAR AREA DE LÁMPARA."},
    {"id":2,"actividad":"LIMPIAR LÁMPARA Y REFLECTOR CON ALCOHOL ISOPROPÍLICO."},
    {"id":3,"actividad":"ASPIRAR EL PANEL DE CONTROL."},
    {"id":4,"actividad":"VERIFICAR CONEXIONES EN PANEL DE CONTROL."},
    {"id":5,"actividad":"ASPIRAR ÁREA DE TRANSFORMADOR."},
    {"id":6,"actividad":"ASPIRAR ÁREA DE EXTRACTOR EN SALIDA DE DUCTO(INTERNAMENTE)."},
    {"id":7,"actividad":"ENGRASAR LAS 2 CHUMACERAS DE CADA RODILLO."},
    {"id":8,"actividad":"ASPIRAR PARTE INFERIOR DE ENTRADA Y SALIDA DE BANDAS."},
    {"id":9,"actividad":"VERIFICAR QUE FUNCIONE PARO DE EMERGENCIA."}
  ]
  actividades_equipo_pickAndPlace_2_trimestral = [
    {"id":1,"actividad":"DESTAPAR Y ASPIRAR INTERIOR DEL EQUIPO."},
    {"id":2,"actividad":"LIMPIAR FILTRO DE AIRE DE ATRÁS CON AGUA A PRESIÓN."},
    {"id":3,"actividad":"ENGRASAR TORNILLOS Y RIELES DE DESPLAZAMIENTO."},
    {"id":4,"actividad":"ASPIRAR REGULADOR DE VOLTAJE."},
    {"id":5,"actividad":"QUITAR TAPA SUPERIOR Y ASPIRAR."},
    {"id":6,"actividad":"LAVAR FILTRO DE AIRE SUPERIOR."},
    {"id":7,"actividad":"VERIFICAR QUE FUNCIONEN PAROS DE EMERGENCIA."}
  ]
  actividades_equipos_laminadoras_semestral = [
    {"id":1,"actividad":"ABRIR PANEL DE CONTROL Y ASPIRARLO."},
    {"id":2,"actividad":"VERIFICAR CONEXIONES EN PANEL DE CONTROL."},
    {"id":3,"actividad":"ENGRASAR CHUMACERAS."},
    {"id":4,"actividad":"VERIFICAR EL ESTADO DE LA BANDA."},
    {"id":5,"actividad":"VERIFICAR QUE CUENTE CON GUARDA Y/O SENSOR DE SEGURIDAD."},
    {"id":6,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO."},
    {"id":7,"actividad":"VERIFICAR EL ESTADO DE TORNILLOS EN BASES DE ROLLOS."},
    {"id":8,"actividad":"(REEMPLAZAR SI REQUIERE)"},
    {"id":9,"actividad":"VERIFICAR EL ESTADO DE LLAVE ALLEN."},
    {"id":10,"actividad":"(REEMPLAZAR SI REQUIERE)."}
  ]
  actividades_equipo_troqueladora_manual_semestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO"},
    {"id":2,"actividad":"ENGRASAR CHUMACERA Y RIEL DE DESPLAZAMIENTO."},
    {"id":3,"actividad":"REVISAR TORNILLERÍA: APRETAR O REEMPLAZAR SI ES NECESARIO."},
    {"id":4,"actividad":"VERIFICAR CORRECTO GRAPADO DE CONECTORES."}
  ]
  actividades_equipos_dispensadores_semestral = [
    {"id":1,"actividad":"ABRIR TAPA DE EQUIPO Y REALIZAR LIMPIEZA INTERNA."},
    {"id":2,"actividad":"VERIFICAR EL ESTADO DE LAS CONEXIONES."},
    {"id":3,"actividad":"VERIFICAR QUE NO EXISTAN FUGAS DE AIRE."},
    {"id":4,"actividad":"LIMPIAR EXTERIOR DE EQUIPO, CABLES Y MANGUERAS."},
    {"id":5,"actividad":"REALIZAR LIMPIEZA AL PEDAL DEL EQUIPO."}
  ]
  actividades_equipos_guillotinas_semestral = [
    {"id":1,"actividad":"REALIZAR LIMPIEZA GENERAL DEL EQUIPO."},
    {"id":2,"actividad":"ENGRASAR TORNILLOS DE DESPLAZAMIENTO Y PARTES MOBILES."},
    {"id":3,"actividad":"VERIFICAR EL ESTADO DE LA CUCHILLA."},
    {"id":4,"actividad":"REVISAR TORNILLERÍA: APRETAR O REEMPLAZAR SI ES NECESARIO."},
    {"id":5,"actividad":"REVISAR NIVEL DE ACEITE DEL SISTEMA HIDRÁULICO. RELLENAR EN CASO DE REQUERIR CON ACEITE SAE-46"},
    {"id":6,"actividad":"REVISAR EL ESTADO DE LAS CONEXIONES."},
    {"id":7,"actividad":"REVISAR QUE FUNCIONE EL SISTEMA DE BLOQUEO DE LA PALANCA DE ACTIVACIÓN DE LA CUCHILLA"}
  ]
  actividades_equipo_hojeadora_trimestral = [
    {"id":1,"actividad":"ASPIRAR Y LIMPIAR INTERIOR DEL EQUIPO."},
    {"id":2,"actividad":"ENGRASAR CHUMACERAS"},
    {"id":3,"actividad":"REVISAR TORNILLERÍA: APRETAR O REEMPLAZAR SI ES NECESARIO."},
    {"id":4,"actividad":"LIMPIAR Y ASPIRAR PANEL DE CONTROL."},
    {"id":5,"actividad":"REVISAR CONEXIONES EN EL PANEL DE CONTROL."},
    {"id":6,"actividad":"REVISAR PRESIÓN DE SUMINISTRO (RANGO ENTRE 0.4 Y 0.6 MPA)"}
  ]

  libro_mttos_preventivos = None
  ws_mtto_preventivos = None
  ws_mttos_preventivos_vista = None
  #mttos_preventivos_registros = None
  #registro_seleccionado = None

  libro_equipos = None
  ws_equipos_vista = None
  ws_equipos_registros = None
  
  
  def __init__(self, datos, **properties):
    self.init_components(**properties)
  ########################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos

    self.set_event_handler('x-guardar_fecha_excluida', self.guardar_fecha_excluida)
    self.set_event_handler('x-eliminar_fecha_excluida', self.eliminar_fecha_excluida)
    self.set_event_handler('x-editar_fecha_excluida', self.editar_fecha_excluida)

    self.set_event_handler('x-enable_disable_guardar', self.enable_disable_guardar)

    self.libro_mttos_preventivos = app_files.mantenimiento_preventivo
    self.ws_mtto_preventivos = self.libro_mttos_preventivos['Registros']
    self.ws_mttos_preventivos_vista = self.libro_mttos_preventivos['Consulta']
    
    
    #self.registros_totales = self.ws_registros_totales.rows

    self.libro_equipos = app_files.mantenimiento_lista_equipos
    self.ws_equipos_vista = self.libro_equipos['Vista']
    self.ws_equipos_registros = self.libro_equipos['Registros']

    self.repeating_panel_equipos.items = self.get_lista_equipos(self.ws_equipos_vista.rows)

    self.label_titulo.text = f"PROGRAMACIÓN ANUAL DE MANTENIMIENTO PREVENTIVO {datetime.today().year}"

  ################################ FUNCIONES PERSONALIZADS ########################################
  def editar_fecha_excluida(self, **event_args):
    self.button_agregar_fecha.enabled = False
    self.button_generar_calendario.enabled = False
    filas = self.repeating_panel_fechas_excluidas.get_components()
    for fila in filas:
      componentes_fila = fila.get_components()
      componentes_fila[3].enabled = False #boton editar
      componentes_fila[4].enabled = False #boton borrar
  
  def guardar_fecha_excluida(self, **event_args):
    fechas_excluidas = self.repeating_panel_fechas_excluidas.items
    self.repeating_panel_fechas_excluidas.items = fechas_excluidas
    self.button_agregar_fecha.enabled = True
    self.button_generar_calendario.enabled = True
    
  def eliminar_fecha_excluida(self, indice, **event_args):
    fechas_excluidas = self.repeating_panel_fechas_excluidas.items
    fechas_excluidas.pop(indice)
    for index, fecha in enumerate(fechas_excluidas):
      fecha['index'] = index + 1
    self.repeating_panel_fechas_excluidas.items = fechas_excluidas
    #self.button_agregar_fecha.enabled = True
    
  def enable_disable_guardar(self, id_equipo, status, **event_args):
    self.button_generar_calendario.enabled = status
    for fila in self.repeating_panel_equipos.get_components():
      componentes_fila = fila.get_components()
      if componentes_fila[12].text != id_equipo:
        componentes_fila[0].enabled = status
    
  def get_lista_equipos(self, equipos):
    lista_equipos = []
    for equipo in list(equipos).copy():
      temp = dict(equipo)
      temp['semanal'] = ""
      temp['mensual'] = ""
      temp['trimestral'] = ""
      temp['semestral'] = ""
      temp['anual'] = ""
      lista_equipos.append(temp)
    return lista_equipos

  def get_actividades(self, equipo, area, frecuencia_mtto):
    actividades = None
    if area == "IMPRESIÓN":
      if equipo == "IMPRESORA MIMAKI":
        actividades = self.actividades_equipo_mimaki_mensual
      elif equipo == "SPS":
        actividades = self.actividades_equipo_sps_mensual
      elif equipo == "IMPRESORA OFFSET":
        actividades = self.actividades_equipo_offset_trimestral
      elif equipo == "HORNO 1":
        if frecuencia_mtto == "SEMANAL":
          actividades = self.actividades_equipo_horno_1_semanal
        elif frecuencia_mtto == "MENSUAL":
          actividades = self.actividades_equipo_horno_1_mensual
        elif frecuencia_mtto == "SEMESTRAL":
          actividades = self.actividades_equipo_horno_1_semestral
      elif equipo == "HORNO 2":
        actividades = self.actividades_equipo_horno_2_semestral
      elif equipo == "HORNO 3":
        actividades = self.actividades_equipo_horno_3_semestral
      elif equipo == "HORNO 4":
        actividades = self.actividades_equipo_horno_4_semestral
      elif equipo == "HORNO 5":
        actividades = self.actividades_equipo_horno_5_semestral
      elif equipo == "ATMA 80" or equipo == "ATMA 710":
        self.actividades_equipos_atma_trimestral += self.actividades_equipos_atma80_710_trimestral
        self.actividades_equipos_atma_trimestral = sorted(self.actividades_equipos_atma_trimestral, key=lambda d: d['id']) 
        actividades = self.actividades_equipos_atma_trimestral
      else:
        for index,actividad in enumerate(self.actividades_equipos_atma_trimestral):
          actividad['id'] = index + 1
        actividades = self.actividades_equipos_atma_trimestral
    ################################################# SUAJE ########################################################
    elif area == "SUAJE":
      if equipo == "EMBOSADORA":
        actividades = self.actividades_equipo_embosadora_trimestral
      else:
        actividades = self.actividades_equipos_suaje_trimestral
    ################################################# MANUALES ########################################################
    elif area == "MANUALES":
      actividades = self.actividades_equipo_embolsadora_trimestral
    ################################################# LASER ########################################################
    elif area == "LÁSER":
      if frecuencia_mtto == "SEMANAL":
        actividades = self.actividades_equipos_laser_semanal
      elif frecuencia_mtto == "MENSUAL":
        actividades = self.actividades_equipos_laser_mensual
    ################################################# CALIDAD ########################################################
    elif area == "CALIDAD":
      if equipo == "MESA DE COORDENADAS X-Y":
        actividades = self.actividades_equipo_mesa_coordenadas_trimestral
      elif equipo != "PROBADOR ELÉCTRICO 2 (CC015)":
        self.actividades_equipos_probadores_electricos_mensual += self.actividades_equipo_probador_electrico_2_mensual
        actividades = self.actividades_equipos_probadores_electricos_mensual
      else:
        actividades = self.actividades_equipos_probadores_electricos_mensual
    ################################################# REVELADO ########################################################
    elif area == "REVELADO":
      if equipo == "INSOLADORA":
        actividades = self.actividades_equipo_insoladora_semestral
      elif equipo == "AFILADOR DE RASEROS":
        actividades = self.actividades_equipo_afilador_raseros_trimestral
    ################################################# ENSAMBLE ########################################################
    elif area == "ENSAMBLE":
      if equipo == "PICK&PLACE 2":
        actividades = self.actividades_equipo_pickAndPlace_2_trimestral
      elif equipo == "PICK&PLACE 3":
        actividades = self.actividades_equipo_pickAndPlace_3_trimestral
      elif equipo == "TROQUELADORA MANUAL":
        actividades = self.actividades_equipo_troqueladora_manual_semestral
      elif equipo == "DISPENSADORES":
        actividades = self.actividades_equipos_dispensadores_semestral
      else:
        actividades = self.actividades_equipos_laminadoras_semestral
    ################################################# ALMACEN MP ########################################################
    elif area == "ALMACÉN MP":
      if equipo == "HOJEADORA":
        actividades = self.actividades_equipo_hojeadora_trimestral
      else:
        actividades = self.actividades_equipos_guillotinas_semestral
    return actividades

  def generar_programa_anual(self, equipo, area, fecha_inicial, frecuencia, id_mtto_preventivo):
    dias_offset = {
      "SEMANAL":7,
      "MENSUAL":31,
      "TRIMESTRAL":93,
      "SEMESTRAL":186,
      "ANUAL":365
    }
    fechas_excluir = self.repeating_panel_fechas_excluidas.items
    fecha = fecha_inicial
    anio_actual = datetime.today().year
    while fecha.year == anio_actual:
      temp = fecha
      if fechas_excluir != None:
        for fecha_excluir in fechas_excluir:
          fecha_inicial = fecha_excluir['fecha_inicial']
          fecha_final = fecha_excluir['fecha_final']
          if fecha_inicial != "":
            if fecha_final != "":
              if fecha > fecha_inicial and fecha < fecha_final:
                resta_lim_inferior = fecha - fecha_inicial
                resta_lim_superior = fecha_final - fecha_inicial
                if resta_lim_inferior > resta_lim_superior:
                  fecha = fecha_final - timedelta(days=1)
                elif resta_lim_inferior < resta_lim_superior:
                  fecha = fecha_inicial - timedelta(days=-1)
                else:
                  fecha = fecha_final - timedelta(days=1)
      #agrega offset si dia cae en sabado o domingo
      if fecha.weekday() == 5:
        fecha += timedelta(days = 2)
      elif fecha.weekday() == 6:
        fecha += timedelta(days = 1)
      
      dict_mtto = {
        "id_mtto_preventivo": id_mtto_preventivo,
        "fecha_programada":fecha,
        "area":area,
        "equipo":equipo,
        "frecuencia":frecuencia,
        "status_mantenimiento":"PROGRAMADO",
        "actividades":self.get_actividades(equipo, area, frecuencia),
        "id_usuario_registrador":self.datos['id_usuario_erp'],
        "usuario_registrador":"ALFREDO VARELA CELESTINO",
        "operacion":"creacion",
        "marca_temporal":datetime.now(),
        "comentarios":"",
        "registro_principal": 1
      }
      id_mtto_preventivo += 1
      self.ws_mtto_preventivos.add_row(**dict_mtto)
      fecha = temp
      fecha += timedelta(days = dias_offset[frecuencia])
    return id_mtto_preventivo
  ############################################ EVENTOS ############################################
  def button_generar_calendario_click(self, **event_args):
    equipos_programados = self.repeating_panel_equipos.items
    status = False
    registros_vista_mttos = self.ws_mttos_preventivos_vista.rows
    id_mtto_preventivo = max([int(row['id_mtto_preventivo']) for row in registros_vista_mttos]) + 1 if len(registros_vista_mttos) > 0 else 1
    with Notification("Insertando registros en la base de datos...", title="GENERANDO PROGRAMA ANUAL", style="info"):
      for equipo in equipos_programados:
        if equipo['semanal'] != "":
          id_mtto_preventivo = self.generar_programa_anual(equipo['equipo'], equipo['area'], equipo['semanal'], "SEMANAL", id_mtto_preventivo)
          status = True
        if equipo['mensual'] != "":
          id_mtto_preventivo = self.generar_programa_anual(equipo['equipo'], equipo['area'], equipo['mensual'], "MENSUAL", id_mtto_preventivo)
          status = True
        if equipo['trimestral'] != "":
          id_mtto_preventivo = self.generar_programa_anual(equipo['equipo'], equipo['area'], equipo['trimestral'], "TRIMESTRAL", id_mtto_preventivo)
          status = True
        if equipo['semestral'] != "":
          id_mtto_preventivo = self.generar_programa_anual(equipo['equipo'], equipo['area'], equipo['semestral'], "SEMESTRAL", id_mtto_preventivo)
          status = True
    if status: 
      Notification("Programa anual generado correctamente!", title="'ÉXITO!'", style="success")
    else: 
      alert("Por favor, llene al menos las fechas de un equipo", title="ERROR AL GUARDAR!", buttons=[("ACEPTAR", "ACEPTAR")])

  def button_agregar_fecha_click(self, **event_args):
    self.button_agregar_fecha.enabled = False
    self.button_generar_calendario.enabled = False
    fechas_excluidas = self.repeating_panel_fechas_excluidas.items if self.repeating_panel_fechas_excluidas.items != None else []
    indice = len(fechas_excluidas)
    fechas_excluidas.append({'index':indice + 1,'fecha_inicial':"", 'fecha_final':""})
    self.repeating_panel_fechas_excluidas.items = fechas_excluidas
    filas = self.repeating_panel_fechas_excluidas.get_components()
    for fila in filas:
      componentes_fila = fila.get_components()
      label_indice = int(componentes_fila[0].text) - 1
      datepicker_fecha_1 = componentes_fila[5].get_components()[0]
      datepicker_fecha_2 = componentes_fila[6].get_components()[0]
      label_fecha_1 = componentes_fila[1]
      label_fecha_2 = componentes_fila[2]
      boton_editar = componentes_fila[3]
      boton_eliminiar = componentes_fila[4]


      if label_indice == indice:
        datepicker_fecha_1.visible = True
        datepicker_fecha_2.visible = True
        label_fecha_1.visible = False
        label_fecha_2.visible = False
        boton_editar.icon = "fa:check"
      else:
        boton_editar.enabled = False
      
      boton_eliminiar.enabled = False
      
      #label_indice = int(componentes_fila[0].text) - 1
      #componentes_fila[2].enabled = False #boton editar
      #componentes_fila[4].enabled = False #boton borrar
      #if label_indice == indice:
      #  componentes_fila[3].visible = True #column panel de textbox y su boton"""
    
    
    """numero_anio = datetime.today().year
    total_dias = 366 if self.anio_bisiesto(anio_actual) else 365

    for numero_mes in range(1, 4):
      inicio_mes = 1 if numero_mes != 1 else 2
      total_dias_mes = calendar.monthrange(numero_anio, numero_mes)[1]
      for numero_dia in range(inicio_mes, int(total_dias_mes) + 1):
        fecha_dia = date(numero_anio,numero_mes,numero_dia)"""
      
    """dias_fin_semana = [5,6]
    lista_mttos_programados = []
    index = 1
    for equipo in self.lista_equipos:
      for frecuencia in equipo['FRECUENCIA']:
        if frecuencia == "SEMANAL":
          pass
        dict_mtto = {
          "id_mtto_preventivo": index,
          "fecha_programada":f"{self.datos['anio']}-{self.datos['mes']}-{self.datos['dia']}",
          "area":equipo['AREA'],
          "equipo":equipo['EQUIPO'],
          "frecuencia":frecuencia,
          "status_mantenimiento":"PROGRAMADO",
          "actividades":self.get_actividades(equipo, frecuencia),
          "id_usuario_registrador":self.datos['id_usuario_erp'],
          "usuario_registrador":"pendiente",
          "operacion":"creacion",
          "marca_temporal":datetime.now(),
          "comentarios":"",
          "registro_principal": 1
        }
        index += 1
        lista_mttos_programados.append(dict_mtto)
    print(lista_mttos_programados)"""
    
  """def button_guardar_click(self, **event_args):
    with Notification("Registrando en la base de datos...",title="GUARDANDO."):
      dict_mtto = {
        "id_mtto_preventivo":(max([int(item['id_mtto_preventivo']) for item in self.registros_totales]) + 1) if len(self.registros_totales) > 0 else 1,
        "fecha_programada":f"{self.datos['anio']}-{self.datos['mes']}-{self.datos['dia']}",
        "area":self.drop_down_area.selected_value,
        "equipo":self.drop_down_equipo.selected_value['EQUIPO'],
        "frecuencia":self.drop_down_frecuencia.selected_value,
        "status_mantenimiento":"PROGRAMADO",
        "actividades":self.get_actividades(self.drop_down_equipo.selected_value, self.drop_down_frecuencia.selected_value),
        "id_usuario_registrador":self.datos['id_usuario_erp'],
        "usuario_registrador":"pendiente",
        "operacion":"creacion",
        "marca_temporal":datetime.now(),
        "comentarios":"",
        "registro_principal": 1
      }
      self.ws_registros_totales.add_row(**dict_mtto)
    Notification("Registro guardado correctamente.", title="GUARDADO.", style="success").show()
    self.raise_event("x-close-alert",value="registro_guardado")"""

  

  """def drop_down_area_change(self, **event_args):
    area_seleccionada = self.drop_down_area.selected_value
    if area_seleccionada != None:
      equipos_area = []
      frecuencias = []
      self.drop_down_equipo.enabled = True
      
      for item in self.lista_equipos:
        if item[1]["AREA"] == area_seleccionada:
          equipos_area.append(item)
      
      self.drop_down_equipo.items = equipos_area
      self.button_guardar.enabled = False
      self.drop_down_frecuencia.selected_value = None
      self.drop_down_frecuencia.enabled = False
    else:
      self.drop_down_equipo.enabled = False
      self.drop_down_equipo.selected_value = None
      self.drop_down_frecuencia.enabled = False
      self.drop_down_frecuencia.selected_value = None
      self.button_guardar.enabled = False

  def drop_down_equipo_change(self, **event_args):
    equipo_seleccionado = self.drop_down_equipo.selected_value
    if equipo_seleccionado != None:
      lista_frecuencia_mtto = equipo_seleccionado["FRECUENCIA"]
      if len(lista_frecuencia_mtto) == 1:
        self.drop_down_frecuencia.items = lista_frecuencia_mtto
        self.drop_down_frecuencia.selected_value = lista_frecuencia_mtto[0]
        self.drop_down_frecuencia.enabled = False
        self.button_guardar.enabled = True
      else:
        self.drop_down_frecuencia.items = lista_frecuencia_mtto
        self.drop_down_frecuencia.enabled = True
    else:
      self.drop_down_frecuencia.selected_value = None
      self.drop_down_frecuencia.enabled = None
      self.button_guardar.enabled = False

  def drop_down_frecuencia_change(self, **event_args):
    if self.drop_down_frecuencia.selected_value != None:
      self.button_guardar.enabled = True
    else:
      self.button_guardar.enabled = False"""

    
