from brownie import accounts, Contract, SimpleToken

# token address from which we have to recover funds
# check etherscan to find the address
INSTANCE_ADDRESS = "0x6C2D0a90becd1A964AC98E9E25ce8b69832D4865"
ACCOUNT = 'straul'

def get_account():
    account = accounts.load(ACCOUNT)
    return account


def recover(account):
    token_contract = Contract.from_abi("token", INSTANCE_ADDRESS, SimpleToken.abi)
    token_contract.destroy(account.address, {'from': account})

def main():
    account = get_account()
    recover(account)