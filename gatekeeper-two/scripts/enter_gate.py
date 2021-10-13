from brownie import GatekeeperHack, accounts

INSTANCE_ADDRESS = "0x87AA318e28ac5167C5aaE14fFD01D8Ac0df99392" # ethernaut level instance
ACCOUNT = 'straul'

def get_account():
    return accounts.load(ACCOUNT)


def deploy_and_hack_gatekeeper(account):
    # deploy gategeeker_hack contract
    gatekeeper_hack = GatekeeperHack.deploy(INSTANCE_ADDRESS, {"from": account, 'value': 1e10})

    return gatekeeper_hack


def main():
    account = get_account()
    gatekeeper_hack = deploy_and_hack_gatekeeper(account)
