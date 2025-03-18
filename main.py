import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Blockchainni sinab ko'ramiz
my_blockchain = Blockchain()
my_blockchain.add_block(Block(1, "", "Birinch block", time.time()))
my_blockchain.add_block(Block(2, "", "Ikkinchi block", time.time()))

for block in my_blockchain.chain:
    print(f"Block {block.index} [Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}]")