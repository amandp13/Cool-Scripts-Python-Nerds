class ListNode():
    def __init__(self, data = None):
        self.next = None
        self.prev = None
        self.data = data

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        result = False
        if self.head is None:
            result = True
        return result

    def peekFirst(self):
        return self.head.data

    def peekLast(self):
        return self.tail.data

    def insertFirst(self, data = None):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            #then update listnodes pointers
            self.head.next = temp
            temp.prev = node

    def insertLast(self, data = None):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            self.tail = node
            #then update listnodes pointers
            self.tail.prev = temp
            temp.next = node

    def printList(self):
        point = self.head
        while(point is not None):
            print(point.data)
            point = point.next

    def removeFirst(self):
        temp = None
        if self.isEmpty():
            raise TypeError("List is Empty, cannot remove First")
        elif self.head.next is None: #if there is only one item in list
            temp = self.head.data
            self.head = None
            self.tail = None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
        return temp

    def removeLast(self):
        temp = None
        if self.isEmpty():
            raise TypeError("List is Empty, cannot remove Last")
        elif self.head.next is None: #if there is only one item in list
            temp = self.head.data
            self.head = None
            self.tail = None
        else:
            temp = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        return temp

    #Iterator Functions
    def __iter__(self):
        currNode = self.head
        while currNode is not None:
            yield currNode.data
            currNode = currNode.next