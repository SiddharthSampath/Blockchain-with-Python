import time
from crypto_hash import crypto_hash


class Block:
    """
    Block : Contains a list of transactions stored in a blockchain
    to support cryptocurrency
    """
    def __init__(self,timestamp,last_hash,hash,data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data


    def __repr__(self):
        return (f"(Block : "
         f"{self.timestamp} : "
         f"{self.last_hash} : "
         f"{self.hash} : "
         f"{self.data})"
        )
    
    @staticmethod
    def mineBlock(lastBlock, data):
        """
        Function to create a new block using the last block and current data 
        """
        timestamp = time.time_ns()
        last_hash = lastBlock.hash
        hash = crypto_hash(timestamp,last_hash,data)

        return Block(timestamp,last_hash,hash,data)

    @staticmethod
    def genesis():
        """
        Creates the genesis block of the Blockchain 
        """
        return Block("1","last_hash_genesis","genesis_hash",[])

def main():
    gen = Block.genesis()
    block = Block.mineBlock(gen, "test")
    print(gen)
    print(block)

if __name__ == "__main__":
    main()