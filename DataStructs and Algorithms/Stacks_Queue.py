from LinkList import LinkedList

class Stack():
    def __init__(self, size = 100):
        self.size = size
        self.stack = LinkedList()
        self.count = 0


    def getCount(self):
        return self.count

    def isEmpty(self):
        result = False
        if self.count == 0:
            result = True
        return result

    def isFull(self):
        result = False
        if self.count == self.size:
            result = True
        return result

    def push(self, value):
        if self.isFull():
            raise IndexError("Cannot push, size of stack is full")
        else:
            #print(self.stack)
            self.stack.insertLast(value)
            self.count = self.count + 1

    def pop(self):
        topVal = self.top()
        self.count = self.count - 1
        self.stack.removeLast()
        return topVal

    def top(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            topVal = self.stack.peekLast()
            #topVal = self.stack[self.count - 1]
        return topVal

class Queue():
    def __init__(self, size = 100):
        self.count = 0
        self.size = size
        self.queue = LinkedList()

    def getCount(self):
        return self.count

    def isEmpty(self):
        result = False
        if self.count == 0:
            result = True
        return result

    def isFull(self):
        result = False
        if self.count == self.size:
            result = True
        return result

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            frontVal = self.queue.peekFirst()
        return frontVal

    def enqueue(self, value):
        if self.isFull():
            raise IndexError("Cannot enqueue, size of queue is full")
        else:
            #self.queue[self.count] = value
            self.queue.insertLast(value)
            self.count = self.count + 1

    def dequeue(self):
        frontVal = self.queue.removeFirst()
        self.count = self.count - 1
        return frontVal
