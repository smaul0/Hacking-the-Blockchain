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


# Lesson 4: [Web3.py Simple Storage](https://github.com/smaul0/Hacking-the-Blockchain/tree/main/Solidity/Codes/Web3_py_Simple_Storage)
💻 Code: https://github.com/smaul0/Hacking-the-Blockchain/tree/main/Solidity/Codes/Web3_py_Simple_Storage
### Installing VSCode, Python, and Web3
- [Developer Bootcamp Setup Instructions (metamask, vscode, python, nodejs..)](https://chain.link/bootcamp/brownie-setup-instructions)
- [VSCode](https://code.visualstudio.com/download)
- Extensions
- Short Cuts:
  - [VSCode Shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings)
- [Python](https://www.python.org/downloads/)
  - Install Troubleshooting
- Terminal
- Making a directory/Folder
- Opening the folder up with VSCode
- Creating a new file
- Syntax Highlights
- Remember to save!
- Setting linting compile version
- VSCode Solidity Settings
  - Formatting & Format on Save
  - Solidity Prettier
  - [Python Black](https://pypi.org/project/black/)
  - [pip](https://pypi.org/project/pip/)
### First Python Script with Web3.py - Deploying a Contract
- Reading our solidity file
- Running a Python Script in the Terminal
- [Windows Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- Compiling in Python
- [py-solc-x](https://pypi.org/project/py-solc-x/)
  - compile_standard
- Colorized Brackets
- JSON ABI 
- Saving Compiled Code
- Formatting JSON
- Deploying in Python
  1. Get Bytecode
  2. Get ABI
  3. Choose Blockchain to Deploy To
    - Local Ganache Chain
      - [Ganache UI](https://www.trufflesuite.com/ganache)
      - [Ganache Command Line](https://github.com/trufflesuite/ganache-cli)
- [Web3.py](https://web3py.readthedocs.io/en/stable/)
- HTTP / RPC Provider
- Private Keys MUST start with "0x"
- Contract Object
- Building a Transaction
- Account Nonce 
- Calling "Constructor"
- Transaction Parameters
- Signing the Transaction
- NEVER put your private key directly in your code
- [Setting Environment Variables (Windows, Linux, MacOS)](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
  - [More on Windows Environment Variables](https://www.youtube.com/watch?v=tqWDiu8a4gc&t=40s)
- Exported Environment Variables Only Last the Duration of the Shell/Terminal
- Private Key PSA
- .env file
- .gitignore
- Loading .env File in Python
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
- Viewing our Transaction / Deployment in Ganache
- Waiting for Block Confirmations
### Interacting with Contract in Python & Web3.py
- 2 Things you always need
  1. Contract Address
  2. Contract ABI
- Getting address from transaction receipt
- Calling a view function with web3.py
  - Call vs Transact
- Updating State with Web3.py
- [ganache-cli](https://github.com/trufflesuite/ganache-cli)
  - Installing Ganache
    - [Install Nodejs](https://nodejs.org/en/)
    - [Install Yarn](https://classic.yarnpkg.com/en/docs/install)
- Working with ganache-cli
- Open a new terminal in the same window
- Deploying to a testnet
- [Infura](https://infura.io/)
- [Alchemy](https://www.alchemy.com/)
- Using Infura RPC URL / HTTP Provider
- [Chain Ids](https://chainlist.org/)


# Lesson 5: [Brownie Simple Storage](https://github.com/smaul0/Hacking-the-Blockchain/tree/main/Solidity/Codes/Brownie_Simple_Storage)
💻 Code: https://github.com/smaul0/Hacking-the-Blockchain/tree/main/Solidity/Codes/Brownie_Simple_Storage
### Brownie Introduction
- Some Users:
  - https://yearn.finance/
  - https://curve.fi/
  - https://badger.finance/
### Installing Brownie
- [Installing Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html)
  - Install pipx
  - pipx install eth-brownie
  - Testing Successful Install
### Brownie Simple Storage Project
- A new Brownie project with `brownie init`
  - Project Basic Explanation
- Adding `SimpleStorage.sol` to the `contracts` folder
- Compiling with `brownie compile`
- Brownie deploy script
  - `def main` is brownie's entry point
- brownie defaults to a `development` `ganache` chain that it creates
- Placing functions outside of the `main` function
- brownie `accounts`
  - 3 Ways to Add Accounts
    1. `accounts[0]`: Brownie's "default" ganache accounts
       - Only works for local ganache 
    2. `accounts.load("...")`: Brownie's encrypted command line (MOST SECURE)
       - Run `brownie accounts new <name>` and enter your private key and a password
    3. `accounts.add(config["wallets"]["from_key"])`: Storing Private Keys as an environment variable, and pulling from our `brownie-config.yaml`
        - You'll need to add `dotenv: .env` to your `brownie-config.yaml` and have a `.env` file
- Importing a Contract
- Contract.Deploy
- View Function Call in Brownie
- State-Changing Function Call in Brownie / Contract Interaction
- `transaction.wait(1)`
### Testing Basics
- `test_simple_storage.py`
- Arrange, Act, Assert
- [`assert`](https://docs.pytest.org/en/6.2.x/assert.html)
- `brownie test`
- `test_updating_storage`
- [Pytest / Brownie Test Tips](https://docs.pytest.org/en/6.2.x/)
- Deploy to a Testnet
- `brownie networks list`
- Development vs Ethereum
  - Development is temporary
  - Ethereum networks persist
- RPC URL / HTTP Provider in Brownie
- The network flag
  - `list index out of range`
- `get_account()`
- `networks.show_active()`
- build/deployments
- Accessing previous deployments
- Interacting with contracts deployed in our brownie project
### [Brownie console]
- `brownie console`


