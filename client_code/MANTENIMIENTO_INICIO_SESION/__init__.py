from ._anvil_designer import MANTENIMIENTO_INICIO_SESIONTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..REGISTRO_USUARIOS import REGISTRO_USUARIOS
from ..A_main import A_main

class MANTENIMIENTO_INICIO_SESION(MANTENIMIENTO_INICIO_SESIONTemplate):
  libro_usuarios = None
  ws_usuarios = None
  usuarios = None
  def __init__(self, **properties):
    self.init_components(**properties)
    self.libro_usuarios = app_files.usuarios_erp
    self.ws_usuarios = self.libro_usuarios['Registros']

  def button_iniciar_sesion_click(self, **event_args):
    if self.text_box_usuario.text == "" or self.text_box_usuario.text == None:
      alert("Debe ingresar su número de empleado.", title="Error de inicio de sesión!")
    else:
      #with Notification("Buscando usuario...", title="Iniciando sesión."):
        datos = {
          "id_usuario_erp": None, #652
          "password": None,
          "nombre_usuario": None
        }
        self.usuarios = self.ws_usuarios.rows
        for usuario in self.usuarios:
          if usuario['numero_empleado'] == str(self.text_box_usuario.text): #usuario encontrado
            datos['id_usuario_erp'] = self.text_box_usuario.text
            datos['nombre_usuario'] = usuario['nombre_usuario']
            if usuario['password'] != "":
              if usuario['password'] == self.text_box_password.text: #password encontrado
                datos['password'] = self.text_box_password.text
                break
              else:
                datos['password'] = ""
        if(datos['id_usuario_erp'] is not None and datos['password'] != "" and datos['password'] is not None):
          #self.flow_panel_card_inicio_sesion.remove_from_parent()
          open_form(A_main(datos))
        elif datos['id_usuario_erp'] is None:
          Notification("El número de empleado ingresado no existe!", style="danger", title="Error de inicio de sesión").show(3)
          #alert("El número de empleado ingresado no existe!", title="Error de inicio de sesión!")
        else:
          if datos['password'] is None:
            alert(REGISTRO_USUARIOS(datos),large=True, buttons=[("SALIR","SALIR")])
          else:
            Notification("La contraseña ingresada es incorrecta!", style="danger", title="Error de inicio de sesión").show(3)
    
              
