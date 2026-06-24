from nicegui import ui
from components.header import create_header
from components.collection import create_collection

collections = {
    'fruta': {
        'cover': 'https://picsum.photos/id/377/640/360',
        'cards': {}
    },
    'verdura': {
        'cover': 'https://picsum.photos/id/377/640/360',
        'cards': {}
    },
    'chocolate': {
        'cover': 'https://picsum.photos/id/377/640/360',
        'cards': {}
    }
}

def create_home():
    create_header()
    with ui.row().classes('w-full border-b border-gray-300 pb-4'):
        ui.button("Add Collection")

    with ui.row().classes('w-full flex-wrap justify-evenly'):
        for collection in collections:
            create_collection(collection, collections[collection]['cover'])
    

