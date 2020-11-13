
class Stack:
    def __init__(self):
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

    # push()
    def push(self, pushValue):
        self.list.append(pushValue)
        return "The element has been successfully inserted"

    # pop()
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    # peek()
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    # Delete Stack
    def delete(self):
        # self.list = None # Return False for isEmpty()
        self.list = []  # Return True for isEmpty()
        return "Entire Stack deleted"


# s = Stack()
# print(s.list)
# print(s.__str__())
customStack = Stack()

print(customStack.isEmpty())

print(customStack.push(1))
print(customStack.push(2))
print(customStack.push(3))
# print(customStack.isEmpty())

# print(customStack)

# print(customStack.pop())
customStack.pop()
print(customStack.isEmpty())
# print(customStack)

print(customStack.peek())

print(customStack.delete())
# print(customStack)
print(customStack.isEmpty())
