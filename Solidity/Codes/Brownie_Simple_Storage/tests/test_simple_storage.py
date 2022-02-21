from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert stored_value == expected


def test_updating_deploy():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    update_value = simple_storage.store(expected, {"from": account})
    updated_stored_value = simple_storage.retrieve()
    # Assert
    assert updated_stored_value == expected
