from brownie import accounts, config, network, SimpleStorage


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    update_store_value = simple_storage.store(15, {"from": account})
    update_store_value.wait(1)
    print(f"updated stored value {simple_storage.retrieve()}")


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["form_key"])


def main():
    deploy_simple_storage()
