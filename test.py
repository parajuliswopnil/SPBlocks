import hashlib
import json
import time
from pprint import pprint


class InvalidBlockException(Exception):
    pass

class TransactionBlocks:
    def __init__(self, timestamp, data):
        self.timestamp = timestamp
        self.data = data


class TransactionChain:
    def __init__(self, transaction: TransactionBlocks):
        self.transaction = transaction
        self.blocks = [self.initial_block()]

    def initial_block(self):
        data = {'previous_block': 'initial_block',
                'timestamp': self.transaction.timestamp,
                'data': None}
        block_signature = self.get_signature(data)
        data['block_signature'] = block_signature
        return data

    def get_blocks_data(self, block_data):
        previous_block: str = self.blocks[-1].get('block_signature')

        data = {'previous_block': previous_block,
                'timestamp': self.transaction.timestamp,
                'data': block_data}
        block_signature = self.get_signature(data)
        data['block_signature'] = block_signature
        self.blocks.append(data)

    def get_block_chain(self):
        return self.blocks

    def get_signature(self, _data: dict):
        data = json.dumps(_data).encode('utf-8')
        hash = hashlib.sha256()
        hash.update(data)
        return hash.hexdigest()

    def check_blockchain_validity(self):
        if len(self.blocks) > 1:
            for i in range(len(self.blocks) - 1):
                if self.blocks[i].get('block_signature') != self.blocks[i + 1].get('block_signature'):
                    raise InvalidBlockException


transaction_block = TransactionBlocks(time.time(), 1)
transaction_chain = TransactionChain(transaction_block)


transaction_chain.get_blocks_data(1)
transaction_chain.get_blocks_data(2)

pprint(transaction_chain.get_block_chain())






