from time import timezone
from utility.printable import Printable


class Block(Printable):
    def __init__(self, index, previous_hash, transactions, proof, timestamp=timezone):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
