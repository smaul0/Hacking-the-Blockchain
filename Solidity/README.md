# Lesson 1: [Simple Storage Contract](https://github.com/smaul0/Hacking-the-Blockchain/tree/main/Solidity/Codes/SimpleStorage)
💻 Code: https://github.com/smaul0/Hacking-the-Blockchain/blob/main/Solidity/Codes/SimpleStorage/SimpleStorage.sol
### [Remix](https://remix.ethereum.org/)

### Basic Solidity
- Versioning
- Compiling
- Contract Declaration
- [Types & Declaring Variables](https://docs.soliditylang.org/en/v0.8.6/types.html)
  - `uint256`, `int256`, `bool`, `string`, `address`, `bytes32`
- Default Initializations
- Comments
- Functions
- Deploying a Contract
- Calling a public state-changing Function
- [Visibility](https://docs.soliditylang.org/en/v0.7.3/contracts.html#visibility-and-getters)
- Scope
- View & Pure Functions
- Structs
- Intro to Storage
- Arrays - Dynamic & Fixed sized
- Compiler Errors and Warnings
- Memory
- Mappings
- SPDX License
- Recap
### Deploying to a "Live" network
- A testnet or mainnet
- [Find a faucet here](https://docs.chain.link/docs/link-token-contracts/#rinkeby)
- Connecting Metamask
- Interacting with Deployed Contracts
- The EVM


# Lesson 2: [Storage Factory](https://github.com/smaul0/Hacking-the-Blockchain/tree/main/Solidity/Codes/StorageFactory)
💻 Code: https://github.com/smaul0/Hacking-the-Blockchain/tree/main/Solidity/Codes/StorageFactory
### Inheritance, Factory Pattern, and Interacting with External Contracts
- Factory Pattern
- Imports
- Deploy a Contract From a Contract
- Interact With a Deployed Contract


# Lesson 3: [Fund Me](https://github.com/smaul0/Hacking-the-Blockchain/tree/main/Solidity/Codes/FundMe)
💻 Code: https://github.com/smaul0/Hacking-the-Blockchain/tree/main/Solidity/Codes/FundMe
### Payable, msg.sender, msg.value, Units of Measure
- Payable
- [Wei/Gwei/Eth Converter](https://eth-converter.com/)
- msg.sender & msg.value
### Chainlink Oracles
- Decentralized Oracle Network Chainlink
  - Blockchains can't make API calls
  - Centralized Nodes are Points of Failure
- [data.chain.link](https://data.chain.link/)
- Getting External Data with Chainlink Oracles
  - [Chainlink](https://docs.chain.link/)
  - [Faucets and Contract Addresses](https://docs.chain.link/docs/link-token-contracts/)
    - [Kovan](https://docs.chain.link/docs/link-token-contracts/#kovan)
  - [Getting Price Information](https://docs.chain.link/docs/get-the-latest-price/)
### Importing from NPM and Advanced Solidity
- Decimals/Floating Point Numbers in Solidity
- latestRoundData
- Importing from NPM  in Remix
- Interfaces
  - Introduction to ABIs
- [Getting Price Feed Addresses](https://docs.chain.link/docs/reference-contracts/)
- getPrice
- Tuples
  - Unused Tuple Variables
- Matching Units (WEI/GWEI/ETH)
- getConversionRate
- Matching Units (Continued)
- SafeMath & Integer Overflow
  - using keyword
  - [Libraries](https://docs.soliditylang.org/en/v0.8.6/contracts.html#libraries)
  - SafeMath PSA
- Setting a Threshold
- Require
- Revert
- Withdraw Function 
- Transfer
- Balance
- this
- Contract Owners
- Constructor
- ==
- Modifiers
- Resetting
- for loop
- Array Length
- Forcing a Transaction
