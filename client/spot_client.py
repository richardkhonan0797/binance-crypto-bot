from binance.spot import Spot
from client.base import Client

class SpotClient(Client):
    def __init__(self, public_key, secret_key):
        self.client = Spot(key=public_key, secret=secret_key)
