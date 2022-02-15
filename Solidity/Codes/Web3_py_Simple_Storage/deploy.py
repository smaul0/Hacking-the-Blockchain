from web3 import Web3
from solcx import compile_standard, install_solc
import json

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile solidity

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x4De6FA83300514BAabB69DC5cBb5aAb5c91eea7e"
private_key = "0xf7d18df9cdc8b875d6323a7b531cbfc3f1ca2fa7a96814b8e4e8a669baa2b03e"

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# get the latest txn
nonce = w3.eth.getTransactionCount(my_address)

# Build the txn
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)

# send the txn
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send it!
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Working with deployed Contracts
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(f"Initial Stored Value {simple_storage.functions.retrieve().call()}")
