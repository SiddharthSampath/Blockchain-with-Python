from backend.blockchain.block import Block,GENESIS_DATA
import time
from backend.config import MINE_RATE,SECOND
from backend.util.hex_to_binary import hex_to_bin
def test_mine_block():
    gen = Block.genesis()
    data = 'test'
    block = Block.mine_block(gen,data)

    assert isinstance(block, Block)
    assert block.last_hash == gen.hash
    assert block.data == data
    assert hex_to_bin(block.hash)[0:block.difficulty] == '0'* block.difficulty

def test_genesis_block():
     genesis = Block.genesis()
     assert isinstance(genesis, Block)

     for key,val in GENESIS_DATA.items():
         assert getattr(genesis,key) == val

def test_quickly_mined_block():
    last_block = Block.mine_block(Block.genesis(),'test1')
    mined_block = Block.mine_block(last_block,'test2')

    assert mined_block.difficulty == last_block.difficulty + 1

def test_slowly_mined_block():
    last_block = Block.mine_block(Block.genesis(),'test1')
    time.sleep(MINE_RATE / SECOND)
    mined_block = Block.mine_block(last_block,'test2')

    assert mined_block.difficulty == last_block.difficulty - 1

def test_difficulty_limits_at_1():
    last_block = Block(time.time_ns(),
                        'last_block_hash',
                        'last_block_last_hash',
                        'test1',
                        1,
                        0)
    time.sleep(MINE_RATE/SECOND)
    mined_block = Block.mine_block(last_block,'test2')

    assert mined_block.difficulty == 1