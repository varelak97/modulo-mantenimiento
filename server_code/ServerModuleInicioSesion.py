import anvil.email
import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server

@anvil.server.callable
def enviar_mail(address, folio):
  anvil.email.send(
    from_name = "ENSEL MANTENIMIENTO",
    to = address,
    subject = "SOLICITUD DE MANTENIMIENTO",
    text= f"Tienes una nueva solicitud de mantenimiento con folio:{folio}"
  )
