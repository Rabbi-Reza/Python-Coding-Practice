
# Use queue module as a FIFO queue
import queue as q

# create
customQueue = q.Queue(maxsize=3)
# print(customQueue)

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
