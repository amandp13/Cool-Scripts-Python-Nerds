from BinaryTree import TreeNode, BinarySearchTree

if __name__ == "__main__":
    print("Testing node creation")
    myNode = TreeNode(1, "one")
    print(myNode)


    print("Testing the Binary Search Tree:")
    myTree = BinarySearchTree()
    myTree.insert('D', "D-Data")
    myTree.insert('B', "B-Data")
    myTree.insert('C', "C-Data")
    myTree.insert('A', "A-Data")
    myTree.insert('F', "F-Data")
    myTree.insert('E', "E-Data")
    myTree.insert('G', "G-Data")


    print('printing list in preorder:')
    print(myTree.display(order = 'preorder', string = True))
    print('printing list in inorder:')
    print(myTree.display(order = 'inorder', string = True))
    print('printing list in postorder:')
    print(myTree.display(order = 'postorder', string = True))

    print("testing for min:")
    print(myTree.min())

    print("testing for max:")
    print(myTree.max())

    print("testing for height:")
    print(myTree.height())

    print('testing balance: Should be 100')
    print(myTree.balance())

    myTree.insert('W', "W-Data")
    myTree.insert('X', "X-Data")
    myTree.insert('Z', "Z-Data")

    print('testing balance: Should be 25')
    print(myTree.balance())

    print("testing delete method")
    print("before")
    print(myTree.display(order = 'preorder', string = True))
    myTree.delete('W')
    print("after: (deleting W)")
    print(myTree.display(order = 'preorder', string = True))
