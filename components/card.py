from nicegui import ui

def create_card():
    with ui.link(target='/card-info', new_tab=False):    
        with ui.image('https://picsum.photos/640/360').classes('w-[20%] h-30 shadow-lg rounded-lg m-1 justify-items-stretch'):
            with ui.row().classes('justify-self-end p-1 rounded-full m-1'):
                ui.icon('check_circle', color='green').classes('text-3xl')