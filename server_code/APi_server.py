import anvil.email
import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import anvil.http

@anvil.server.callable
def turn_on_led():
  resp = anvil.http.request(url ="http://192.168.2.154/led1on", method="GET")
  return resp
