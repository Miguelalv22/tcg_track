from nicegui import ui
from components.header import create_header
from components.card import create_card

def create_card_collection():
      var = 0
      create_header() 
      with ui.row().classes('w-full border-b border-gray-300 pb-4'):
            ui.label(f'Total {var}')
      with ui.element('div').classes('w-full'):
            create_card()
            create_card()
            create_card()
            create_card()
            create_card()
            create_card()
