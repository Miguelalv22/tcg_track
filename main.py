from nicegui import ui

with ui.header(elevated=True).style('background-color: #23252e').classes('items-center justify-between'):
    ui.input(placeholder='search poke').style('background-color: white').classes('rounded-lg text-center')
    ui.button('Search', on_click=lambda: ui.notify('You clicked me!')).classes('rounded-lg')

with ui.card().tight().classes('w-60 shadow-lg rounded-lg overflow-hidden'):
    # Card Image
    ui.image('https://images.pokemontcg.io/xy1/1_hires.png').classes('h-55')
    
    # Card Content
    with ui.card_section().classes('p-2'):
        ui.label('Beautiful Mountains').classes('text-2xl font-bold text-gray-800')
        ui.label('Exp.').classes('text-gray-600 mt-2')
        
    # Card Actions / Buttons
    with ui.card_section().classes('bg-gray-50 p-2 flex justify-center gap-2 border-t'):
        ui.button('View Details').classes('text-sm')

ui.run()