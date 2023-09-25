from ._anvil_designer import A_mainTemplate
from anvil import *

class A_main(A_mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
