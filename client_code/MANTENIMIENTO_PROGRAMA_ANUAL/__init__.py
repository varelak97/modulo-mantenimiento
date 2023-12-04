from ._anvil_designer import MANTENIMIENTO_PROGRAMA_ANUALTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil_extras import popover
import anvil.server
import anvil.js
import calendar
from datetime import datetime, date
from ..MANTENIMIENTO_PREVENTIVO_REGISTROS import MANTENIMIENTO_PREVENTIVO_REGISTROS
from ..MANTENIMIENTO_PREVENTIVO_CHECKLIST import MANTENIMIENTO_PREVENTIVO_CHECKLIST

class MANTENIMIENTO_PROGRAMA_ANUAL(MANTENIMIENTO_PROGRAMA_ANUALTemplate):
  #################################### DEFINICION DE VARIABLES ####################################
  dias_semana = {
    "1": "lunes",
    "2": "martes",
    "3": "miercoles",
    "4": "jueves",
    "5": "viernes",
    "6": "sabado",
    "7": "domingo"
  }
  meses = [
    ("ENERO", 1),
    ("FEBRERO", 2),
    ("MARZO", 3),
    ("ABRIL", 4),
    ("MAYO", 5),
    ("JUNIO", 6),
    ("JULIO", 7),
    ("AGOSTO", 8),
    ("SEPTIEMBRE", 9),
    ("OCTUBRE", 10),
    ("NOVIEMBRE", 11),
    ("DICIEMBRE", 12),
  ]

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
    ("ATMA 57",{"EQUIPO":"ATMA 57","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 71",{"EQUIPO":"ATMA 71","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 70",{"EQUIPO":"ATMA 70","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 45",{"EQUIPO":"ATMA 45","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 710",{"EQUIPO":"ATMA 710","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("ATMA 80",{"EQUIPO":"ATMA 80","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("HORNO 1",{"EQUIPO":"HORNO 1","AREA":"IMPRESIÓN","FRECUENCIA":["SEMANAL","MENSUAL","SEMESTRAL"]}),
    ("HORNO 2",{"EQUIPO":"HORNO 2","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 3",{"EQUIPO":"HORNO 3","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 4",{"EQUIPO":"HORNO 4","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("HORNO 5",{"EQUIPO":"HORNO 5","AREA":"IMPRESIÓN","FRECUENCIA":["SEMESTRAL"]}),
    ("IMPRESORA MIMAKI",{"EQUIPO":"IMPRESORA MIMAKI","AREA":"IMPRESIÓN","FRECUENCIA":["MENSUAL"]}),
    ("IMPRESORA OFFSET",{"EQUIPO":"IMPRESORA OFFSET","AREA":"IMPRESIÓN","FRECUENCIA":["TRIMESTRAL"]}),
    ("SPS",{"EQUIPO":"SPS","AREA":"IMPRESIÓN","FRECUENCIA":["MENSUAL"]}),
    ("SUAJADORA 1",{"EQUIPO":"SUAJADORA 1","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 2",{"EQUIPO":"SUAJADORA 2","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 3",{"EQUIPO":"SUAJADORA 3","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("SUAJADORA 4",{"EQUIPO":"SUAJADORA 4","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("EMBOSADORA",{"EQUIPO":"EMBOSADORA","AREA":"SUAJE","FRECUENCIA":["TRIMESTRAL"]}),
    ("LÁSER V-460",{"EQUIPO":"LÁSER V-460","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("LÁSER M-300",{"EQUIPO":"LÁSER M-300","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("LÁSER VLS-360",{"EQUIPO":"LÁSER VLS-360","AREA":"LÁSER","FRECUENCIA":["SEMANAL","MENSUAL"]}),
    ("MESA DE COORDENADAS X-Y",{"EQUIPO":"MESA DE COORDENADAS X-Y","AREA":"CALIDAD","FRECUENCIA":["TRIMESTRAL"]}),
    ("PROBADOR ELÉCTRICO 2 (CC015)",{"EQUIPO":"PROBADOR ELÉCTRICO 2 (CC015)","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("PROBADOR ELÉCTRICO 3 (C0025)",{"EQUIPO":"PROBADOR ELÉCTRICO 3 (C0025)","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("PROBADOR ELÉCTRICO 4 (C0028)",{"EQUIPO":"PROBADOR ELÉCTRICO 4 (C0028)","AREA":"CALIDAD","FRECUENCIA":["MENSUAL"]}),
    ("INSOLADORA",{"EQUIPO":"INSOLADORA","AREA":"REVELADO","FRECUENCIA":["TRIMESTRAL"]}),
    ("AFILADOR DE RASEROS",{"EQUIPO":"AFILADOR DE RASEROS","AREA":"REVELADO","FRECUENCIA":["TRIMESTRAL"]}),
    ("LAMINADORA 1",{"EQUIPO":"LAMINADORA 1","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("LAMINADORA 2",{"EQUIPO":"LAMINADORA 2","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("LAMINADORA 3",{"EQUIPO":"LAMINADOR 3","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("PICK&PLACE 2",{"EQUIPO":"PICK&PLACE 2","AREA":"ENSAMBLE","FRECUENCIA":["TRIMESTRAL"]}),
    ("TROQUELADORA MANUAL",{"EQUIPO":"TROQUELADORA MANUAL","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("DISPENSADORES",{"EQUIPO":"DISPENSADORES","AREA":"ENSAMBLE","FRECUENCIA":["SEMESTRAL"]}),
    ("PICK&PLACE 3",{"EQUIPO":"PICK&PLACE 3","AREA":"ENSAMBLE","FRECUENCIA":["TRIMESTRAL"]}),
    ("GUILLOTINA 1",{"EQUIPO":"GUILLOTINA 1","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("GUILLOTINA 2",{"EQUIPO":"GUILLOTINA 2","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
    ("GUILLOTINA 3",{"EQUIPO":"GUILLOTINA 3","AREA":"ALMACÉN MP","FRECUENCIA":["SEMESTRAL"]}),
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
  
  datos = {}
  libro_mttos = None
  ws_consulta_mttos = None
  registros_consulta_mttos = None
  ws_registros_totales = None
  numero_registros = None
  
  def __init__(self, datos, **properties):
    self.datos = datos
    fecha_actual = date.today()
    self.drop_down_mes.items = self.meses
    self.drop_down_mes.selected_value = self.drop_down_mes.items[fecha_actual.month - 1][1]
    self.drop_down_anio.selected_value = str(fecha_actual.year)
    self.drop_down_equipos.items = self.lista_equipos
    self.drop_down_areas.items = self.lista_areas
    self.libro_mttos = app_files.mantenimiento_preventivo
    self.ws_consulta_mttos = self.libro_mttos['Consulta']
    self.ws_registros_totales = self.libro_mttos['Registros']
    self.llenar_calendario()
    
    self.init_components(**properties)
    ######################## CARGA DE DATOS E INICIALIZACION DE VARIABLES #########################
    self.set_event_handler('x-actualizar_form_activo', self.actualizar_form_activo)
    self.set_event_handler('x-actualizar_calendario', self.llenar_calendario)
    #self.set_event_handler('x-show_lista_equipos', self.show_lista_equipos)
  
  ################################ FUNCIONES PERSONALIZADS ########################################
  """def show_lista_equipos(self, datos, **event_args):
    print(f"datos recibidos:{datos}")
    mes = self.drop_down_mes.selected_value
    anio = self.drop_down_anio.selected_value
    items = None
    if datos['modo'] == "dia":
      items = self.get_datos_actuales(anio, mes, datos['dia'], datos['tipo'], datos['frecuencia'])
    elif datos['modo'] == "todos":
      items = self.registros_consulta_mttos
    return items

  def get_datos_actuales(self, anio, mes, dia, tipo, frecuencia):
    registros_dia_seleccionado = []
    for item in self.registros_consulta_mttos:
      fecha_seleccionada = item['fecha_programada'].split('-')
      if int(fecha_seleccionada[0]) == int(anio) and int(fecha_seleccionada[1]) == int(mes) and int(fecha_seleccionada[2]) == int(dia):
        if tipo == item['status_mantenimiento']:
          if frecuencia == item['frecuencia']:
            registros_dia_seleccionado.append(item)
          elif tipo == "todas":
            registros_dia_seleccionado.append(item)
        elif tipo == "todos":
          registros_dia_seleccionado.append(item)
    return registros_dia_seleccionado"""
    
  def actualizar_form_activo(self, datos, **event_args):
    
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      datos['mes'] = self.drop_down_mes.selected_value
      datos['anio'] = self.drop_down_anio.selected_value
      datos.update(self.datos)
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos))
    elif datos['clave_form'] == "MANTENIMIENTO_PREVENTIVO_CHECKLIST":
      datos.update(self.datos)
      print(f"abriendo checklist:{self}")
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_CHECKLIST(datos))
    
    #estaba asi:
    """datos['mes'] = self.drop_down_mes.selected_value
    datos['anio'] = self.drop_down_anio.selected_value
    datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == 'MANTENIMIENTO_PREVENTIVO_REGISTROS':
      self.abrir_form(MANTENIMIENTO_PREVENTIVO_REGISTROS(datos))"""
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("SALIR",True)], role="wide-modal-content")
    if respuesta:
      self.llenar_calendario()
    
  def llenar_calendario(self):
    self.registros_consulta_mttos = self.ws_consulta_mttos.rows
    anio = self.drop_down_anio.selected_value
    mes = self.drop_down_mes.selected_value
    indicadores_mtto_mes = []
    for dia in range(31):
      area = "todas" if self.drop_down_areas.selected_value == None else self.drop_down_areas.selected_value
      tipo = "todos" if self.drop_down_tipo.selected_value == None else self.drop_down_tipo.selected_value
      equipo = "todos" if self.drop_down_equipos.selected_value == None else self.drop_down_equipos.selected_value['EQUIPO']
      indicadores_mtto_mes.append({
        #genera acumuladores
        'W':0,
        'M':0,
        'T':0,
        'S':0,
        'A':0,
        'P':0,
        'R':0,
        'OK':0,
        'area':area,
        'tipo':tipo,
        'equipo':equipo,
        'lista_equipos':[],
        'id_mtto_preventivo':None
      })
      
    for item in self.registros_consulta_mttos:
      dia_prog = int(item['fecha_programada'].split('-')[2])
      mes_prog = int(item['fecha_programada'].split('-')[1])
      #filtra por datos del mes
      if mes_prog == mes:
        self.fill_indicador(dia_prog, indicadores_mtto_mes, item)
    self.card_calendario.visible = False
    mes_calendario = calendar.month(int(anio),mes)[0:-1] #Se descarta el último salto de línea, pues en caso de haber 6 semanas, se toma una 7a inexistente

    prefijos = {"PROGRAMADO":"P","REPROGRAMADO":"R","REALIZADO":"OK-", "todos":"P"}
    renglones_mes = mes_calendario.split('\n')
    items = []
    for i in range(2, len(renglones_mes)):
      dicc = {}
      j = 1
      for k in range(0,len(renglones_mes[i]),3):
        numero_dia = str(renglones_mes[i][k:k+2]).strip()
        if numero_dia != "":
          prefijo = prefijos[indicadores_mtto_mes[int(numero_dia)-1]['tipo']]
          dicc[self.dias_semana[str(j)]] = {
            "numero_dia":numero_dia,
            'P':f"P: {indicadores_mtto_mes[int(numero_dia)-1]['P']}",
            'R':f"R: {indicadores_mtto_mes[int(numero_dia)-1]['R']}",
            'OK':f"OK: {indicadores_mtto_mes[int(numero_dia)-1]['OK']}",
            'W':f"{prefijo}W: {indicadores_mtto_mes[int(numero_dia)-1]['W']}",
            'M':f"{prefijo}M: {indicadores_mtto_mes[int(numero_dia)-1]['M']}",
            'T':f"{prefijo}T: {indicadores_mtto_mes[int(numero_dia)-1]['T']}",
            'S':f"{prefijo}S: {indicadores_mtto_mes[int(numero_dia)-1]['S']}",
            'A':f"{prefijo}A: {indicadores_mtto_mes[int(numero_dia)-1]['A']}",
            'area':indicadores_mtto_mes[int(numero_dia)-1]['area'],
            'equipo':indicadores_mtto_mes[int(numero_dia)-1]['equipo'],
            'lista_equipos':indicadores_mtto_mes[int(numero_dia)-1]['lista_equipos'],
            'tipo':indicadores_mtto_mes[int(numero_dia)-1]['tipo'],
            'id_mtto_preventivo':indicadores_mtto_mes[int(numero_dia)-1]['id_mtto_preventivo']
          }
        j += 1
      items.append(dicc)
    self.repeating_panel_mes_calendario.items = items
    self.card_calendario.visible = True

  def fill_indicador(self, dia_prog, indicadores_mtto_mes, item):
    prefijos_tipo = {"PROGRAMADO":"P","REPROGRAMADO":"R","REALIZADO":"OK"}
    prefijos_frecuencia = {"SEMANAL":"W", "MENSUAL":"M", "TRIMESTRAL":"T", "SEMESTRAL":"S","ANUAL":"A"}
    area = indicadores_mtto_mes[dia_prog-1]['area']
    equipo = indicadores_mtto_mes[dia_prog-1]['equipo']
    tipo = indicadores_mtto_mes[dia_prog-1]['tipo']

    if area == "todas":
      if equipo == "todos":
        if tipo == "todos":
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
        elif tipo == item['status_mantenimiento']: #tipo:selected
          indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] = indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] + 1
          indicadores_mtto_mes[dia_prog-1]["lista_equipos"].append({'equipo':item['equipo'],'frecuencia':item['frecuencia'],'id_mtto':item['id_mtto_preventivo'],'operacion':item['operacion']})
          #indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
      elif equipo == item['equipo']: #equipo:selected
        if tipo == "todos":
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
        elif tipo == item['status_mantenimiento']: #tipo:selected
          indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] = indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] + 1
          indicadores_mtto_mes[dia_prog-1]['id_mtto_preventivo'] = item['id_mtto_preventivo']
    elif area == item['area']: #area:selected
      if equipo == "todos":
        if tipo == "todos":
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
        elif tipo == item['status_mantenimiento']: #tipo:selected
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
      elif equipo == item['equipo']: #equipo:selected
        if tipo == "todos":
          indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] = indicadores_mtto_mes[dia_prog-1][prefijos_tipo[item['status_mantenimiento']]] + 1
        elif tipo == item['status_mantenimiento']: #tipo:selected
          indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] = indicadores_mtto_mes[dia_prog-1][f"{prefijos_frecuencia[item['frecuencia']]}"] + 1
          indicadores_mtto_mes[dia_prog-1]['id_mtto_preventivo'] = item['id_mtto_preventivo']

  def get_actividades(self, equipo_seleccionado, frecuencia_mtto):
    actividades = None
    if equipo_seleccionado['AREA'] == "IMPRESIÓN":
      if equipo_seleccionado['EQUIPO'] == "IMPRESORA MIMAKI":
        actividades = self.actividades_equipo_mimaki_mensual
      elif equipo_seleccionado['EQUIPO'] == "SPS":
        actividades = self.actividades_equipo_sps_mensual
      elif equipo_seleccionado['EQUIPO'] == "IMPRESORA OFFSET":
        actividades = self.actividades_equipo_offset_trimestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 1":
        if frecuencia_mtto == "SEMANAL":
          actividades = self.actividades_equipo_horno_1_semanal
        elif frecuencia_mtto == "MENSUAL":
          actividades = self.actividades_equipo_horno_1_mensual
        elif frecuencia_mtto == "SEMESTRAL":
          actividades = self.actividades_equipo_horno_1_semestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 2":
        actividades = self.actividades_equipo_horno_2_semestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 3":
        actividades = self.actividades_equipo_horno_3_semestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 4":
        actividades = self.actividades_equipo_horno_4_semestral
      elif equipo_seleccionado['EQUIPO'] == "HORNO 5":
        actividades = self.actividades_equipo_horno_5_semestral
      elif equipo_seleccionado['EQUIPO'] == "ATMA 80" or equipo_seleccionado['EQUIPO'] == "ATMA 710":
        self.actividades_equipos_atma_trimestral += self.actividades_equipos_atma80_710_trimestral
        self.actividades_equipos_atma_trimestral = sorted(self.actividades_equipos_atma_trimestral, key=lambda d: d['id']) 
        actividades = self.actividades_equipos_atma_trimestral
      else:
        for index,actividad in enumerate(self.actividades_equipos_atma_trimestral):
          actividad['id'] = index + 1
        actividades = self.actividades_equipos_atma_trimestral
    ################################################# SUAJE ########################################################
    elif equipo_seleccionado['AREA'] == "SUAJE":
      if equipo_seleccionado['EQUIPO'] == "EMBOSADORA":
        actividades = self.actividades_equipo_embosadora_trimestral
      else:
        actividades = self.actividades_equipos_suaje_trimestral
    ################################################# MANUALES ########################################################
    elif equipo_seleccionado['AREA'] == "MANUALES":
      actividades = self.actividades_equipo_embolsadora_trimestral
    ################################################# LASER ########################################################
    elif equipo_seleccionado['AREA'] == "LÁSER":
      if frecuencia_mtto == "SEMANAL":
        actividades = self.actividades_equipos_laser_semanal
      elif frecuencia_mtto == "MENSUAL":
        actividades = self.actividades_equipos_laser_mensual
    ################################################# CALIDAD ########################################################
    elif equipo_seleccionado['AREA'] == "CALIDAD":
      if equipo_seleccionado['EQUIPO'] == "MESA DE COORDENADAS X-Y":
        actividades = self.actividades_equipo_mesa_coordenadas_trimestral
      elif equipo_seleccionado['EQUIPO'] != "PROBADOR ELÉCTRICO 2 (CC015)":
        self.actividades_equipos_probadores_electricos_mensual += self.actividades_equipo_probador_electrico_2_mensual
        actividades = self.actividades_equipos_probadores_electricos_mensual
      else:
        actividades = self.actividades_equipos_probadores_electricos_mensual
    ################################################# REVELADO ########################################################
    elif equipo_seleccionado['AREA'] == "REVELADO":
      if equipo_seleccionado['EQUIPO'] == "INSOLADORA":
        actividades = self.actividades_equipo_insoladora_semestral
      elif equipo_seleccionado['EQUIPO'] == "AFILADOR DE RASEROS":
        actividades = self.actividades_equipo_afilador_raseros_trimestral
    ################################################# ENSAMBLE ########################################################
    elif equipo_seleccionado['AREA'] == "ENSAMBLE":
      if equipo_seleccionado['EQUIPO'] == "PICK&PLACE 2":
        actividades = self.actividades_equipo_pickAndPlace_2_trimestral
      elif equipo_seleccionado['EQUIPO'] == "PICK&PLACE 3":
        actividades = self.actividades_equipo_pickAndPlace_3_trimestral
      elif equipo_seleccionado['EQUIPO'] == "TROQUELADORA MANUAL":
        actividades = self.actividades_equipo_troqueladora_manual_semestral
      elif equipo_seleccionado['EQUIPO'] == "DISPENSADORES":
        actividades = self.actividades_equipos_dispensadores_semestral
      else:
        actividades = self.actividades_equipos_laminadoras_semestral
    ################################################# ALMACEN MP ########################################################
    elif equipo_seleccionado['AREA'] == "ALMACÉN MP":
      if equipo_seleccionado['EQUIPO'] == "HOJEADORA":
        actividades = self.actividades_equipo_hojeadora_trimestral
      else:
        actividades = self.actividades_equipos_guillotinas_semestral
    return actividades
  
  #################################################### EVENTOS ####################################################
  def drop_down_mes_change(self, **event_args):
    self.llenar_calendario()

  def drop_down_anio_change(self, **event_args):
    self.llenar_calendario()

  def drop_down_areas_change(self, **event_args):
    self.drop_down_equipos.selected_value = None
    self.drop_down_tipo.selected_value = None
    if self.drop_down_areas.selected_value != None:
      lista_filtrada = []
      for equipo in self.lista_equipos:
        if self.drop_down_areas.selected_value == equipo[1]['AREA']:
          lista_filtrada.append(equipo)
      self.drop_down_equipos.items = lista_filtrada
    else:
      self.drop_down_equipos.items = self.lista_equipos
    self.llenar_calendario()
        

  def drop_down_equipos_change(self, **event_args):
    self.drop_down_tipo.selected_value = None
    self.llenar_calendario()

  def drop_down_tipo_change(self, **event_args):
    self.llenar_calendario()

  def button_borrar_click(self, **event_args):
    self.drop_down_areas.selected_value = None
    self.drop_down_equipos.selected_value = None
    self.drop_down_tipo.selected_value = "PROGRAMADO"
    self.llenar_calendario()

  def button_programar_click(self, **event_args):
    for equipo in self.lista_equipos:
      nombre_equipo = equipo['EQUIPO']
      area = equipo['AREA']
      frecuencia = equipo['FRECUENCIA']
      
      pass

  
   
  ##################################################### PRUEBAS #####################################################
    """self.datos['clave_form'] = 'MANTENIMIENTO_VERIFICACION_MTTO_PREVENTIVO'
    self.datos['modo'] = 'nuevo'
    self.parent.raise_event('x-actualizar_form_activo', datos=self.datos)"""

    
    """"lista = [["nombre","edad"],["ALFREDO VARELA",'33'],["FERNANDO CORTES",'31'],["MARIO GONZALES",'45']]
    
    datos = anvil.js.call('SUPERSQL',f"SELECT * FROM ? WHERE edad < 40",lista)
    print(datos)""""

    #print(anvil.js.call('prueba',lista))

    

