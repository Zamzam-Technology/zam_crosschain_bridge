import os
from brownie import ETHSwapAgent, accounts

def main():
    owner_account = accounts.add(os.getenv("PRIVATE_KEY"))
    ethAgent = ETHSwapAgent.deploy({'from': owner_account})
    ethAgent.initialize(0, owner_account, {'from': owner_account})