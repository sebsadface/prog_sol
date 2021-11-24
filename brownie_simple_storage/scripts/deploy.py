from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    # account = accounts.load("rinkby_account1")
    # account = accounts.add(config["wallets"]["from_key"])
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(1032234, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()