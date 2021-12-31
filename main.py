import os

# Modules import
from dotenv import load_dotenv
from pathlib import Path
from client.spot_client import SpotClient

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

if __name__ == '__main__':
    client = SpotClient(public_key=os.environ.get("EXCHANGE_PUBLIC_KEY"), secret_key=os.environ.get("EXCHANGE_SECRET_KEY"))

    print(client.get_account())