import web3 as w3
import random

def main():
    hash = w3.Web3.keccak(text="transferOwnership(address)")[:4]

    suffix = "(address,uint)"

    xhash = ""
    while xhash != hash:
        _method = ""

        xhash = w3.Web3.keccak(text=_method+suffix)[:4]