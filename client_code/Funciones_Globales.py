from anvil import *

def fill_formulario(lista_components, datos):
  for component in lista_components:
    if type(component) in [TextBox, TextArea]:
      component.text = datos[component.tag]
    elif type(component) is DropDown:
      component.selected_value = datos[component.tag]


def validar_campos(lista_components, datos_proveedor, campos_no_obligatorios, modo):
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
        if valor != datos_proveedor[textcomponent.tag]: #valida que al menos un campos haya sido modificado
          cambios = True
      else:
        cambios = True
    if not status:
      return 3
    if not cambios:
      return 2
    else:
      return 1
