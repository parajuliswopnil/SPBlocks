import json
import hashlib
import time
from pprint import pprint
from main import TransactionBlocks, TransactionChain
from SPCoin import SPCoin


class User:
    def __init__(self, user_data):
        """
        initializes the user wallet
        """
        self.user_data = user_data
        self.user_id = None
        self.wallet_balance = 0
        self.registered_users = list()

    def get_user_id(self):
        """
        :return: returns the user_id
        """
        return self.user_id

    def get_balance(self):
        return self.wallet_balance


class RegisteredUsers:
    def __init__(self):
        self.registered_users = list()
        self.transaction_chain = TransactionChain()
        self.sp_coin = SPCoin()

    def register_users(self, user_data: User):
        user_data.user_data['timestamp'] = time.time()
        user_data.user_data['balance'] = user_data.get_balance()

        def _get_user_id(user_data: dict):
            """
            internal method to get user id from user data
            :param user_data:
            :return: user id
            """
            data = json.dumps(user_data).encode('utf-8')
            hashed_data = hashlib.sha256()
            hashed_data.update(data)
            return hashed_data.hexdigest()

        _user_data = user_data.user_data
        self.user_id = 'US' + _get_user_id(_user_data)
        wallet_data = {self.user_id: _user_data}
        self.registered_users.append(wallet_data)
        self.sp_coin.mint_coin(wallet_id=wallet_data[self.user_id], mint_amount=1)
        self.transaction_chain.blocks = TransactionBlocks(wallet_data)
        self.transaction_chain.add_blocks()
        return wallet_data

    def transfer(self, _from, _to, _amount):
        self.sp_coin.transfer_coin(_from[self.get_wallet_address(_from)], _to[self.get_wallet_address(_to)], _amount)
        wallet_data = {'sender': wallets.get_wallet_address(_from),
                       'receiver': wallets.get_wallet_address(_to),
                       'amount': _amount,
                       'remarks': 'token transfer'}
        self.transaction_chain.blocks = TransactionBlocks(wallet_data)
        self.transaction_chain.add_blocks()

    def get_registered_users(self):
        return self.registered_users

    def get_wallet_address(self, _wallet_data):
        wallet_address = _wallet_data.keys()
        return [*wallet_address][0]


user_data = {
    'wallet_name': 'Swopnil Parajuli'
}
user_data2 = {
    'wallet_name': 'Bigyapti Nepal'
}
user_data3 = {
    'wallet_name': 'Pranil Parajuli'
}

wallets = RegisteredUsers()
user1 = User(user_data)
user2 = User(user_data2)
user3 = User(user_data3)
user1_wallet = wallets.register_users(user1)
print(user1_wallet.keys())
user2_wallet = wallets.register_users(user2)
user3_wallet = wallets.register_users(user3)
wallets.transfer(user1_wallet, user2_wallet, 1)
print('*************************************************************************************************')
pprint(wallets.transaction_chain.get_block_chain())
print('*************************************************************************************************')
pprint(wallets.get_registered_users())
print('*************************************************************************************************')
print(wallets.sp_coin.total_supply)