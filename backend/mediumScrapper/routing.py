from channels.routing import route
from mediumScrapper.consumer import ws_connect, ws_disconnect
from .wsgi import *

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]
