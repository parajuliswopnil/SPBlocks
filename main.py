import hashlib
import json
import time
from pprint import pprint


class InvalidBlockException(Exception):
    pass


class TransactionBlocks:
    def __init__(self, data=None):
        self.data = data
        self.timestamp = time.time()


class TransactionChain:
    def __init__(self):
        self.blocks = None
        self.block_chain = [self.initial_block()]

    def initial_block(self):
        data = {'previous_block': 'initial_block',
                'timestamp': time.time(),
                'data': None,
                'block_index': 0}
        block_signature = self.get_signature(data)
        data['block_signature'] = block_signature
        return data

    def add_blocks(self):
        previous_block: str = self.block_chain[-1].get('block_signature')
        block_index: int = self.block_chain[-1].get('block_index') + 1
        data = {'previous_block': previous_block,
                'timestamp': self.blocks.timestamp,
                'data': self.blocks.data,
                'block_index': block_index}
        block_signature = self.get_signature(data)
        data['block_signature'] = block_signature
        self.block_chain.append(data)
        self.check_blockchain_validity()

    def get_block_chain(self):
        return self.block_chain

    def get_signature(self, _data: dict):
        data = json.dumps(_data).encode('utf-8')
        hash = hashlib.sha256()
        hash.update(data)
        return hash.hexdigest()

    def get_last_block(self):
        return self.block_chain[-1]

    def check_blockchain_validity(self):
        if len(self.block_chain) > 1:
            for i in range(len(self.block_chain) - 1):
                if self.block_chain[i].get('block_signature') != self.block_chain[i + 1].get('previous_block'):
                    raise InvalidBlockException


if __name__ == '__main__':
    transaction_chain = TransactionChain()
    transaction_chain.blocks = TransactionBlocks(1)
    transaction_chain.add_blocks()
    transaction_chain.blocks = TransactionBlocks(2)
    transaction_chain.add_blocks()
    pprint(transaction_chain.get_block_chain())
    pprint(transaction_chain.get_last_block())
