import Stacks_Queue

class TreeNode():
    def __init__(self, inKey, inValue):
        self._key = inKey
        self._value = inValue
        self._left = None
        self._right = None

    def __str__(self):
        return ("Key:" + str(self._key) + " Value: " + str(self._value))

class BinarySearchTree():
    def __init__(self):
        self._root = None

    def _findRec(self, key, cur):
        value = None
        if cur == None:
            raise ValueError("Key " + key + " not found")
        elif key == cur._key:
            value = cur._value
        elif key < cur._key:
            value = self._findRec(key, cur._left)
        else:
            value = self._findRec(key, cur._right)
        return value

    def find(self, key):
        return self._findRec(key, self._root)

    def _insertRec(self, key, cur, value):
        if key < cur._key:
            if cur._left == None:
                cur._left = TreeNode(key, value)
            else:
                self._insertRec(key, cur._left, value)
        elif key > cur._key:
            if cur._right == None:
                cur._right = TreeNode(key, value)
            else:
                self._insertRec(key, cur._right, value)

    def insert(self, key, value):
        #if exception is raised it means that the key is not yet in the tree
        if self._root == None:
            self._root = TreeNode(key, value)
        else:
            try:
                self.find(key)
                raise ValueError("Key " + key + " already exists in tree")
            except:
                self._insertRec(key, self._root, value)
#The delete functions
    def _promoteSuccessor(self, curNode):
        successor = curNode

        if curNode._left == None:
            successor = curNode
        else:
            if curNode._left != None:
                successor = self._promoteSuccessor(curNode._left)
                if successor == curNode._left:
                    curNode._left = successor._right
        return successor

    def _deleteNode(self, key, delNode):
        updateNode = None

        if delNode._left == None and delNode._right == None:
            updateNode = None
        elif delNode._left != None and delNode._right == None:
            updateNode = delNode._left
        elif delNode._left == None and delNode._right != None:
            updateNode = delNode._right
        else:
            updateNode = self._promoteSuccessor(delNode._right)
            if updateNode != delNode._right:
                updateNode._right = delNode._right
            updateNode._left = delNode._left
        return updateNode


    def _deleteRec(self, key, curNode):
        updateNode = curNode
        if curNode == None:
            raise Exception("oh no")
        elif key == curNode._key:
            updateNode = self._deleteNode(key, curNode)
        elif key < curNode._key:
            curNode._left = self._deleteRec(key, curNode._left)
        else:
            curNode._right = self._deleteRec(key, curNode._right)

        return updateNode

    def delete(self, key):
        self._deleteRec(key, self._root)

#All other methods for inormation on the tree
    def _preorderRec(self, cur, resultQueue):
        resultQueue.enqueue(cur)
        if cur._left is not None:
            self._preorderRec(cur._left, resultQueue)
        if cur._right is not None:
            self._preorderRec(cur._right, resultQueue)

    def _inorderRec(self, cur, resultQueue):
        if cur._left is not None:
            self._inorderRec(cur._left, resultQueue)
        resultQueue.enqueue(cur)
        if cur._right is not None:
            self._inorderRec(cur._right, resultQueue)

    def _postorderRec(self, cur, resultQueue):
        if cur._left is not None:
            self._postorderRec(cur._left, resultQueue)
        if cur._right is not None:
            self._postorderRec(cur._right, resultQueue)
        resultQueue.enqueue(cur)

    def display(self, order = 'preorder', string = False):
        resultQueue = Stacks_Queue.Queue()
        result = ''
        cur = self._root
        if order == 'preorder':
            self._preorderRec(cur, resultQueue)
        elif order == 'inorder':
            self._inorderRec(cur, resultQueue)
        elif order == 'postorder':
            self._postorderRec(cur, resultQueue)

        if string == True:
            empty = resultQueue.isEmpty()
            while not empty:
                temp = resultQueue.dequeue()
                result = result + temp.__str__() + '\n'
                empty = resultQueue.isEmpty()
            resultQueue = result
        return resultQueue


    def _heightRec(self, curNode):
        if curNode == None:
            height = -1
        else:
            leftHeight = self._heightRec(curNode._left)
            rightHeight = self._heightRec(curNode._right)

        # Get highest of left vs right branches
            if leftHeight > rightHeight:
                height = leftHeight + 1
            else:
                height = rightHeight + 1
        return height

    def height(self):
        return self._heightRec(self._root)

    def _minRec(self, curNode):
        if curNode._left != None:
            minKey = self._minRec(curNode._left)
        else:
            minKey = curNode._key
        return minKey

    def min(self):
        return self._minRec(self._root)

    def max(self):
        return self._root._key

    def _balanceRec(self, curNode):
        if curNode == None:
            result = 0
        else:
            result = self._heightRec(curNode)

        return result

    def balance(self):
        #base case No children at root
        if self._root == None:
            result = 100
        else:
            leftHeight = self._balanceRec(self._root._left)
            rightHeight = self._balanceRec(self._root._right)

            if leftHeight > rightHeight:
                result = rightHeight/leftHeight *100
            else:
                result = leftHeight/rightHeight *100
        return result
