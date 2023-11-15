from ._anvil_designer import RowTemplateLinksTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class RowTemplateLinks(RowTemplateLinksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_llenar_checklist_click(self, **event_args):
    print(self.parent.parent.parent.parent.parent)

  def button_ver_checklist_click(self, **event_args):
    alert(self.parent.parent.parent.parent)
