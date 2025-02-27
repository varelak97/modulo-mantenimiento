import anvil.email
import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import anvil.pdf

@anvil.server.callable
def crear_pdf():
  media_object = anvil.pdf.render_form('MANTENIMIENTO_PREVENTIVO_CHECKLIST', 42, name="CHECLIKST_MTTO")
  return media_object
