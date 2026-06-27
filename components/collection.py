from nicegui import ui

def create_collection(name_collection, cover_collection):
    with ui.link(target='/card-collection', new_tab=False).classes('w-[45%] no-underline'):
        with ui.card().tight().classes('shadow-lg rounded-lg'):
            ui.image(f'{cover_collection}').classes('h-30')
            
            with ui.card_section().classes('p-2'):
                ui.label(f'{name_collection}').classes('text-lg font-bold text-gray-800')
