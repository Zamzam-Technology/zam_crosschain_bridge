import os 
from brownie import BSCSwapAgent, BEP20TokenImpl, accounts

def main():
    owner_account = accounts.add(os.getenv("PRIVATE_KEY"))
    impl_token = BEP20TokenImpl.deploy({'from': owner_account})
    bscAgent = BSCSwapAgent.deploy({'from': owner_account})
    bscAgent.initialize(impl_token.address, 0, owner_account, owner_account, {'from': owner_account})