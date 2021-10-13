pragma solidity ^0.6.0;

import '@openzeppelin/contracts/access/Ownable.sol';

contract Manager is Ownable{

    function withdraw() public {

    }
}

contract Worker {
    function executeTx(address _to, string memory _method, bytes memory args) public returns (bool) {
        _to.call(abi.encodePacked(bytes4(keccak256(abi.encodePacked(_method, "(bytes,bytes,uint64)")))));
        return true;
    }
}

contract Vault is Ownable{
    function deposit () public {}

    function withdraw() public onlyOwner {}
}

// transferOwnership(address)  -> 0xf2fde38b
// _method(address,uint)


