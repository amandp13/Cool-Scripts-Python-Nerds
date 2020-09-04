class First:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.num = c

    def print(self):
        print(self.name, self.age, self.num)

def initial():
    name = input('name : ')
    age = int(input('age : '))
    num = int(input('num :'))
    return [name, age, num]


a = First(*initial())
a.print()
