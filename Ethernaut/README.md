# Ethernaut CTF

# 1. [Challenge 1](https://ethernaut.openzeppelin.com/level/0x9CB391dbcD447E645D6Cb55dE6ca23164130D008)

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


# 2. [Challenge 2](https://ethernaut.openzeppelin.com/level/0x9CB391dbcD447E645D6Cb55dE6ca23164130D008)

Tasks: \
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


# 3. [Challenge 3](https://ethernaut.openzeppelin.com/level/0x9CB391dbcD447E645D6Cb55dE6ca23164130D008)

Tasks: 
- This is a coin flipping game where you need to build up your winning streak by guessing the outcome of a coin flip. To complete this level you'll need to use your psychic abilities to guess the correct outcome 10 times in a row.

**Solution:** \
Vulnerable Code: 
```

```
