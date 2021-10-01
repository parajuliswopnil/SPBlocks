from main import TransactionBlocks, TransactionChain
import time
from pprint import pprint

transaction_block = TransactionBlocks(time.time())
transaction_chain = TransactionChain(transaction_block)
transaction_chain.add_blocks(1)
transaction_chain.add_blocks(2)
transaction_chain.add_blocks(3)
pprint(transaction_chain.get_block_chain())