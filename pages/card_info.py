from nicegui import ui
from components.header import create_header

def create_card_info():
    create_header()
    with ui.row().classes('w-full border-b border-gray-300 pb-4'):
        ui.label('Nombre y algo mas de info')

    with ui.row().classes('w-full border-b border-gray-300 pb-4'):
        ui.image('https://picsum.photos/640/360').classes('w-[100%] shadow-lg m-1 justify-items-stretch')