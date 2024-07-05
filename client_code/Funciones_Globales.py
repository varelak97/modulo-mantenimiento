from anvil import *
import anvil.server

def get_registro(id, clave, base):
    registro_encontrado = None
    for registro in base:
      if registro[clave] == id and registro['registro_principal'] == '1' and registro['activo'] == '1':
        registro_encontrado = registro
        break
    return registro_encontrado

def genera_diccionario(lista_components):
  diccionario = {}
  valor = None
  for component in lista_components:
    if type(component) in [TextBox, TextArea]:
      valor = component.text
    elif type(component) is DropDown:
      valor = component.selected_value
    elif type(component) is DatePicker:
      valor = component.date
    diccionario[component.tag] = valor
  return diccionario

#[{'modo':1, 'tag':'id_numero_parte'},{'modo':2, 'tag':'id_numero_parte'}]

def fill_formulario(lista_components, datos, tuplas, modo, llave, id_tupla):
  for component in lista_components:
    if type(component) in [TextBox, TextArea]:
      component.text = datos[component.tag]
    elif type(component) is DropDown:
      if tuplas != None:
        for tupla in tuplas:
          component.selected_value = datos[tupla['tag']] = datos[tupla['llave']] 
          """if tupla['modo'] == 1 and tupla['tag'] == component.tag:
            component.selected_value = (datos[component.tag], datos[llave])
          elif tupla['modo'] == 2 and tupla['tag'] == component.tag:
            component.selected_value = (datos[component.tag], id_tupla)"""
      else:
        component.selected_value = datos[component.tag]
    elif type(component) is DatePicker:
      component.date = datos[component.tag]


def validar_campos(lista_components, datos_antiguos, campos_no_obligatorios, modo):
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
      if textcomponent.tag not in campos_no_obligatorios: #valida que campos obligatorios no estén vacios
        if valor == "" or valor is None:
          status = False
          textcomponent.role = "outlined-error"
      if modo == "edicion":
        if str(valor) != datos_antiguos[textcomponent.tag]: #valida que al menos un campos haya sido modificado
          cambios = True
      else:
        cambios = True
    if not status:
      return 3
    if not cambios:
      return 2
    else:
      return 1
