from ._anvil_designer import MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class MANTENIMIENTO_PREVENTIVO_REGISTROS(MANTENIMIENTO_PREVENTIVO_REGISTROSTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
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
    ("ATMA 57",{"EQUIPO":"ATMA57","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 71",{"EQUIPO":"ATMA71","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 70",{"EQUIPO":"ATMA70","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 45",{"EQUIPO":"ATMA45","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 710",{"EQUIPO":"ATMA710","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 80",{"EQUIPO":"ATMA80","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("HORNO 1",{"EQUIPO":"HORNO1","AREA":"IMPRESIÓN","FRECUENCIA":["SEMANAL","MENSUAL","SEMESTRAL"]}),
    ("HORNO 2",{"EQUIPO":"HORNO2","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 3",{"EQUIPO":"HORNO3","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 4",{"EQUIPO":"HORNO4","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 5",{"EQUIPO":"HORNO5","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("IMPRESORA MIMAKI",{"EQUIPO":"IMPRESORA_MIMAKI","AREA":"IMPRESIÓN","FRECUENCIA":["MENSUAL"]}),
    ("IMPRESORA OFFSET",{"EQUIPO":"IMPRESORA_OFFSET","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("SPS",{"EQUIPO":"SPS","AREA":"IMPRESIÓN","FRECUENCIA":["MENSUAL"]}),
    ("SUAJADORA 1",{"EQUIPO":"SUAJADORA1","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 2",{"EQUIPO":"SUAJADORA2","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 3",{"EQUIPO":"SUAJADORA3","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 4",{"EQUIPO":"SUAJADORA4","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("EMBOSADORA",{"EQUIPO":"EMBOSADORA","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("LÁSER V-460",{"EQUIPO":"LASER_V-460","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("LÁSER M-300",{"EQUIPO":"LASER_M-300","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("LÁSER VLS-360",{"EQUIPO":"LASER_VLS-360","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("MESA DE COORDENADAS X-Y",{"EQUIPO":"MESA_COORDENADAS_XY","AREA":"CALIDAD","FRECUENCIA":["TRIMESTRAL"]}),
    ("PROBADOR ELÉCTRICO 2 (CC015)",{"EQUIPO":"PROBADOR_ELECTRICO_2","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("PROBADOR ELÉCTRICO 3 (C0025)",{"EQUIPO":"PROBADOR_ELECTRICO_3","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("PROBADOR ELÉCTRICO 4 (C0028)",{"EQUIPO":"PROBADOR_ELECTRICO_4","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("INSOLADORA",{"EQUIPO":"INSOLADORA","AREA":"REVELADO","FRECUENCIA":["TRIMESTRAL"]}),
    ("AFILADOR DE RASEROS",{"EQUIPO":"AFILADOR_RASEROS","AREA":"REVELADO","FRECUENCIA":["TRIMESTRAL"]}),
    ("LAMINADORA 1",{"EQUIPO":"LAMINADORA1","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("LAMINADORA 2",{"EQUIPO":"LAMINADORA2","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("LAMINADORA 3",{"EQUIPO":"LAMINADOR3","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("PICK&PLACE 2",{"EQUIPO":"PICK_PLACE_2","AREA":"ENSAMBLE","FRECUENCIA":["TRIMESTRAL"]}),
    ("TROQUELADORA MANUAL",{"EQUIPO":"TROQUELADORA_MANUAL","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("DISPENSADORES",{"EQUIPO":"DISPENSADORES","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("PICK&PLACE 3",{"EQUIPO":"PICK_PLACE_3","AREA":"ENSAMBLE","FRECUENCIA":["TRIMESTRAL"]}),
    ("GUILLOTINA 1",{"EQUIPO":"GUILLOTINA1","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("GUILLOTINA 2",{"EQUIPO":"GUILLOTINA2","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("GUILLOTINA 3",{"EQUIPO":"GUILLOTINA3","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("HOJEADORA",{"EQUIPO":"HOJEADORA","AREA":"ALMACÉN MP","FRECUENCIA":["TRIMESTRAL"]}),
    ("EMBOLSADORA",{"EQUIPO":"EMBOLSADORA","AREA":"MANUALES","FRECUENCIA":["TRIMESTRAL"]}),
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

  
  def __init__(self,datos, **properties):
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.datos = datos
    self.drop_down_area.items = self.lista_areas
    self.drop_down_equipo.items = self.lista_equipos

  ################################ FUNCIONES PERSONALIZADS ########################################
  
  

  ############################################ EVENTOS ############################################
  def button_programar_click(self, **event_args):
    self.outlined_card_equipo.visible = True
    self.button_programar.visible = False
    """ self.datos['clave_form'] = 'MANTENIMIENTO_PREVENTIVO'
    self.datos['modo'] = 'nuevo'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""

  def button_cancelar_click(self, **event_args):
    self.outlined_card_equipo.visible = False
    self.button_programar.visible = True
    self.button_guardar.enabled = False
    self.drop_down_area.selected_value = None
    self.drop_down_equipo.selected_value = None
    self.drop_down_frecuencia.selected_value = None

  def drop_down_area_change(self, **event_args):
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
      self.button_guardar.enabled = False


