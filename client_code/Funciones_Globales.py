from anvil import *
import anvil.server

def get_registro(id, clave, base):
    registro_encontrado = None
    for registro in base:
      if registro[clave] == id and registro['registro_principal'] == '1' and registro['activo'] == '1':
        registro_encontrado = registro
        break
    return registro_encontrado

def genera_diccionario(lista_components, llave_tabla):
  diccionario = {}
  valor = None
  for component in lista_components:
    if type(component) in [TextBox, TextArea]:
      valor = component.text
    elif type(component) is DropDown:
      valor = component.selected_value
    elif type(component) is DatePicker:
      valor = component.date
    elif type(component) is RepeatingPanel:
      items = component.items
      ids = []
      for item in items:
        ids.append(item[llave_tabla])
      valor = ids
    diccionario[component.tag] = valor
  return diccionario

#[{'modo':1, 'tag':'id_numero_parte'},{'modo':2, 'tag':'id_numero_parte'}]

def fill_formulario(lista_components, datos, modos):
  for component in lista_components:
    if type(component) in [TextBox, TextArea]:
      component.text = datos[component.tag]
    elif type(component) is DropDown:
      if modos is not None and modos != "":
        for modo in modos:
          if modo['tag'] == component.tag:
            if modo['modo'] == 'modo1':
              component.selected_value = (datos[component.tag], datos[modo['llave']])
      else:
        component.selected_value = datos[component.tag]
    elif type(component) is DatePicker:
      component.date = datos[component.tag]
    elif type(component) is RepeatingPanel:
      component.items = datos['tabla']


def validar_campos(lista_components, datos_antiguos, campos_no_obligatorios, modo, dicc_modos, llave_tabla):
    status = True
    cambios = False
    for textcomponent in lista_components:
      valor = None
      if type(textcomponent) is DropDown:
        valor = textcomponent.selected_value
      elif type(textcomponent) is DatePicker:
        valor = textcomponent.date
      elif type(textcomponent) in [TextBox, TextArea]:
        valor = textcomponent.text
      elif type(textcomponent) is RepeatingPanel:
        valor = textcomponent.items
      if textcomponent.tag not in campos_no_obligatorios: #valida que campos obligatorios no estén vacios
        if valor == "" or valor is None:
          status = False
          textcomponent.role = "outlined-error"
      if modo == "edicion":
        if type(textcomponent) is DropDown:
          if dicc_modos is not None and dicc_modos != "":
            for dic_modo in dicc_modos:
              if dic_modo['tag'] == textcomponent.tag:
                if str(valor[dic_modo['index']]) != datos_antiguos[textcomponent.tag]:
                  cambios = True
          else:
            if str(valor) != datos_antiguos[textcomponent.tag]: #valida que al menos un campos haya sido modificado
              cambios = True
        elif type(textcomponent) is RepeatingPanel:
          filas_similares = 0
          total_suajes = len(eval(datos_antiguos[textcomponent.tag]))
          for row in valor:
            if int(row[llave_tabla]) in eval(datos_antiguos[textcomponent.tag]):
              filas_similares += 1
              #cambios = True
            """else:
              print(f"id:{row[llave_tabla]} si está en datos:{datos_antiguos[textcomponent.tag]}")"""
          #print(f"filas_similares:{filas_similares} de un total de:{ total_filas}")
          if not (filas_similares == total_suajes and len(valor) == total_suajes):
            cambios = True
        else:
          if str(valor) != datos_antiguos[textcomponent.tag]: #valida que al menos un campos haya sido modificado
            cambios = True
      else:
        cambios = True
    print(f"valor de cambios:{cambios}")
    if not status:
      return 3
    if not cambios:
      return 2
    else:
      return 1

def borrar_item(datos, **event_args):
  lista_items = datos['repeating_panel'].items
  id_borrar = None
  for index, item in enumerate(lista_items):
    if int(item[datos['llave']]) == int(datos[datos['llave']]):
      id_borrar = index
      break
  del(lista_items[id_borrar])
  datos['repeating_panel'].items = lista_items
