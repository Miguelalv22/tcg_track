from nicegui import ui

def create_header():
    with ui.header(elevated=True).style('background-color: #23252e').classes('items-center justify-between'):
        ui.image('https://picsum.photos/id/377/640/360') \
                .classes('rounded-full size-16 cursor-pointer hover:opacity-80 transition') \
                .on('click', lambda: ui.notify('presionada'))
        ui.button('Collections')
        ui.button('Creating')