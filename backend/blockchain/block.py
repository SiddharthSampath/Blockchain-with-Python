import time
from backend.util.crypto_hash import crypto_hash
from backend.config import MINE_RATE
from backend.util.hex_to_binary import hex_to_bin
GENESIS_DATA = {"timestamp" : 1, 
                "last_hash" : "genesis_last_hash", 
                "hash" : "genesis_hash", 
                "data" : [],
                "difficulty" : 3,
                "nonce" : "genesis_nonce"}

class Block:
    """
    Block : Contains a list of transactions stored in a blockchain
    to support cryptocurrency
    """
    def __init__(self,timestamp,last_hash,hash,data,difficulty,nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce


    def __repr__(self):
        return (f"(Block : "
         f"{self.timestamp}, "
         f"{self.last_hash}, "
         f"{self.hash}, "
         f"{self.data}, " 
         f"{self.difficulty}, "
         f"{self.nonce} )"
        )
    
    @staticmethod
    def mine_block(last_block, data):
        """
        Function to create a new block using the last block and current data 
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp,last_hash,data,difficulty,nonce)
        while hex_to_bin(hash)[0:difficulty] != '0' *difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp,last_hash,data,difficulty,nonce)
            

        return Block(timestamp,last_hash,hash,data,difficulty,nonce)

    @staticmethod
    def genesis():
        """
        Creates the genesis block of the Blockchain 
        """
        return Block(**GENESIS_DATA)

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        Adjust the difficulty of mining based on mine rate.
        Increased by one if mining is too quick
        Decreased by one if mining is too slow
        """
        if new_timestamp - last_block.timestamp < MINE_RATE:
            return last_block.difficulty + 1
        
        if last_block.difficulty - 1 > 0:
            return last_block.difficulty - 1
        
        return 1


def main():
    gen = Block.genesis()
    block = Block.mine_block(gen, "test")
    #print(gen)
    print(block)

if __name__ == "__main__":
    main()