import random


def r_num(a, b):
    """ generate a random number b/w a,b """
    return random.randint(a, b)


x = 0
y = 100
tryes = 6
num = 0
flag = 0
level = 1


def rules():
    """ Print Rule of the game """
    print('\n----- Rule -----')
    print(f'** You have {tryes} tries in this level **')
    print('----------------')


def debug():
    """ Print all global variable values """
    print('\n------Settings------')
    print(f'Tryes : {tryes}')
    print(f'level : {level}')
    print(f'from : {x} to {y*level}')
    print(f'Flag : {flag}')
    print('---------------------\n')


def engine():
    """ Core of the game """
    global num
    num = r_num(x, y*level)
    print(f'** level :  {level} **\n** i am thinking of number b/w {x} and {y*level} **')
    # print(f'debug : ans {num}')
    for i in range(tryes):

        try:
            n = int(input(f'take a guess : '))
        except:
            print(f'\n\t**You are wasting your chances {name} !!**\n')
            continue
        if n == num:
            global flag
            flag = 1
            break
        elif n > num:
            print('**Too high**\n')
        else:
            print('**Too low**\n')


def evaluate():
    """ Evaluate if player won the game or not """
    if flag == 1:
        global level,tryes
        print(f' --- {random.choice(cong)}, {name} you have won level {level} of the game --- ')
        level +=1
        tryes += 2

    else:
        print(f'** I was thinking of {num} **\n** Better luck next time **\n**You came till level {level} **')
        exit(0)


option = 'y'
name = input('Enter your name : ')

greet = ['Hi', 'Hello', 'Ahola', 'Greetings']
cong = ['congratulation', 'Awsome', 'Great', 'Bravo']
bye = ['bye', 'farewell', 'see u later']

print(f'** {random.choice(greet)} {name}, Welcome to the guessing game !! **\n')

# debug()

while option == 'y':
    rules()
    engine()
    # debug()
    evaluate()
    # debug()
    o = input(f'{name}, Would you like to try level {level} [y/n] : ')
    if o == 'n' or o == 'N' or o == 'no' or o == 'NO':
        print(f'** All right , {random.choice(bye)} {name} **')
        # debug()
        exit(0)
    else:

        option = 'y'
        flag = 0
        # debug()
