class NotEnoughBalanceException(Exception):
    pass


class SPCoin:
    def __init__(self):
        self.total_supply = 50

    def mint_coin(self, wallet_id, mint_amount):
        previous_balance = wallet_id.get('balance')
        wallet_id['balance'] = previous_balance + mint_amount
        self.total_supply = self.total_supply - mint_amount

    def transfer_coin(self, _from, _to, _amount):
        if _from['balance'] < _amount:
            raise NotEnoughBalanceException
        else:
            _from['balance'] = _from['balance'] - _amount
            _to['balance'] = _to['balance'] + _amount
            _from['balance'] = _from['balance'] + _amount / self.total_supply
            self.total_supply = self.total_supply - _amount / self.total_supply


