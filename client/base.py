class Client:
    def __init__(self, public_key, secret_key):
        self.client = None
        self.account = self.get_account()

    def get_account(self):
        return self.client.account()
