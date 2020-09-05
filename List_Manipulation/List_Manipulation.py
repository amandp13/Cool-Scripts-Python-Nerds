'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''


def list_manipulation(list1, com, loc, val=0):
    if com == "remove":
        if loc == "end":
            list1.pop()

        else:
            list1.pop(0)

    else:
        if loc == "end":
            list1.append(val)

        else:
            list1.insert(0, val)
    return list1


print(list_manipulation([1, 2, 3, 4], "remove", "end"))
print(list_manipulation([1, 2, 3, 4], "remove", "begining"))
print(list_manipulation([1, 2, 3, 4], "add", "end", 56))
print(list_manipulation([1, 2, 3, 4], "add", "begining", 56))
