from backend.blockchain.block import Block,GENESIS_DATA

def test_mine_block():
    gen = Block.genesis()
    data = 'test'
    block = Block.mine_block(gen,data)

    assert isinstance(block, Block)
    assert block.last_hash == gen.hash
    assert block.data == data

def test_genesis_block():
     genesis = Block.genesis()
     assert isinstance(genesis, Block)

     for key,val in GENESIS_DATA.items():
         assert getattr(genesis,key) == val

