import anvil.email
import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import anvil.pdf
import requests
import json

url_google_script = "https://script.google.com/macros/s/AKfycby7I-YoZiKYZ9tBJlFiDtqke6q5Pt5KK2VCx870Du629ye0RiecKBlgR5hHgtzl3Dc/exec"

@anvil.server.callable
def crear_pdf(datos):
  #respuesta =  json.loads(requests.post(url_google_script, data=datos).text)['respuesta']
  respuesta = requests.post(url_google_script, data=datos)
  return respuesta.json()
  
"""def crear_pdf(datos):
  media_object = anvil.pdf.render_form('MANTENIMIENTO_PREVENTIVO_CHECKLIST', datos)
  return media_object"""
