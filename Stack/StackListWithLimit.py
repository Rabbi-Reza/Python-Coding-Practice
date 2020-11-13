
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty()
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull()
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # push()
    def push(self, pushValue):
        if self.isFull():
            print("The Stack is Full")
        else:
            self.list.append(pushValue)
            print("The element has been successfully inserted")

    # pop()
    def pop(self):
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            self.list.pop()
            print("The element has been successfully deleted")

    # peek()
    def peek(self):
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            print("Peek value is: " + str(self.list[len(self.list) - 1]))
            # return self.list[len(self.list) - 1]

    # Delete Stack
    def delete(self):
        self.list = []
        print("Entire Stack deleted")


stackWithLimit = Stack(4)

print(stackWithLimit.isEmpty())
print(stackWithLimit.isFull())

stackWithLimit.push(1)
stackWithLimit.push(3)
stackWithLimit.push(7)
stackWithLimit.push(9)
stackWithLimit.push(13)
stackWithLimit.push(27)
# print(stackWithLimit)

stackWithLimit.pop()
# print(stackWithLimit)

stackWithLimit.peek()
