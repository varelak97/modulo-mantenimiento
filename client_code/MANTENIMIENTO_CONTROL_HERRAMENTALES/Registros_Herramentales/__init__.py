from ._anvil_designer import Registros_HerramentalesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..Form_Edicion_Herramental import Form_Edicion_Herramental


class Registros_Herramentales(Registros_HerramentalesTemplate):
  datos = None
  def __init__(self, datos, **properties):
    self.init_components(**properties)
    self.datos = datos
    self.label_title.text = f"HERRAMENTAL {self.datos['codigo_herramental']}"

  #################################################### FUNCIONES PERSONALIZADAS #####################################################
  def abrir_popup_form(self, datos, **event_args):
    #datos['id_usuario_erp'] = self.datos['id_usuario_erp']
    if datos['clave_form'] == "FORMULARIO_REGISTRO_HERRAMENTAL":
      datos.update(self.datos)
      self.abrir_form(Form_Edicion_Herramental(datos))
      
  def abrir_form(self, form_de_interes):
    respuesta = alert(content = form_de_interes, large=True, dismissible=False, buttons=[("REGRESAR", True)], role="wide-modal-content")
    if respuesta == "registro_guardado":
        self.button_actualizar_click()


  
  ############################################################# EVENTOS #############################################################
  def button_registrar_click(self, **event_args):
    datos = {}
    datos['clave_form'] = "FORMULARIO_REGISTRO_HERRAMENTAL"
    datos['modo'] = "nuevo"
    datos['id_herramental'] = self.datos['id_herramental']
    self.abrir_popup_form(datos)

  def button_actualizar_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
