
class First:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.num = c

    def __repr__(self):
        return 'Name: ' +self.name+ ' Age: ' +str(self.age) + ' Num: ' + str(self.num)

def initial():
    name = input('name : ')
    age = int(input('age : '))
    num = int(input('num :'))
    return [name, age, num]


a = First(*initial())
print(a.__repr__())
