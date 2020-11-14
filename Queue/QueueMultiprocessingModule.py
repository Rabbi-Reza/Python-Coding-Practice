
# Use multiprocessing.Queue as a FIFO queue
from multiprocessing import Queue

# create
customQueue = Queue(maxsize=3)

# isEmpty
print(customQueue.empty())

# check queue size ( No of elements )
print(customQueue.qsize())

# enQueue
customQueue.put(4)
customQueue.put(1)
customQueue.put(7)
# print(customQueue.qsize())

# isFull
print(customQueue.full())

# deQueue
print(customQueue.get())
