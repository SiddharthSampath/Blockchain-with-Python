from block import Block
class Blockchain:
    """
    Blockchain : Contains a list of blocks, chained together
    using cryptography

    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def addBlock(self,data):

        block = Block.  mineBlock(self.chain[-1],data)
        self.chain.append(block)

    def __repr__(self):
        return f"Blockchain : {self.chain}"

def main():
    blockchain = Blockchain()
    blockchain.addBlock("one")
    blockchain.addBlock("two")
    print(blockchain)

if __name__ == "__main__":
     main()