from nicegui import ui
from pages.home import create_home
from pages.card_collection import create_card_collection

@ui.page('/')
def home():
    create_home()

@ui.page('/card-collection')
def collection():
     create_card_collection()

ui.run()