from backend.blockchain.blockchain import Blockchain
import time
from backend.config import SECOND

times = []

blockchain = Blockchain()
for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    time_to_mine = end_time - start_time
    time_to_mine = time_to_mine / SECOND
    times.append(time_to_mine)

    average_time = sum(times) / len(times)

    print(f'Block Number : {i}')
    print(f'Time to mine block : {time_to_mine}s')
    print(f'Average time to mine block : {average_time}s')
    print(f'Block Difficulty : {blockchain.chain[-1].difficulty}')
    

    

