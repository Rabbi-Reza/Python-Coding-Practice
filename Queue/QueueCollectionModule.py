
# Use collection.deque as a FIFO queue
from collections import deque

# create
customQueue = deque(maxlen=3)
print(customQueue)

# enQueue
customQueue.append(1)
customQueue.append(3)
customQueue.append(5)
print(customQueue)

# customQueue.append(9)
# print(customQueue)

# deQueue
print(customQueue.popleft())
print(customQueue)

# delete
customQueue.clear()
print(customQueue)
