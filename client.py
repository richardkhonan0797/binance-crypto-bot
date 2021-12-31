from sys import settrace

from binance.spot import Spot


class Client:
    def __init__(self, public_key, secret_key):
        self.client = None
        self.account = self.get_account()

    def get_account(self):
        return self.client.account()


class SpotClient(Client):
    def __init__(self, public_key, secret_key):
        self.client = Spot(key=public_key, secret=secret_key)
