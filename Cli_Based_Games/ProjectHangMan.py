# import time //time.sleep(100)
import random
with open('word_list.txt', 'r') as f:
    words1 = f.read().splitlines()
# Returns any random word
sec = random.choice(words1)
print(f'The Word Length is {len(sec)} ')

d = list(set(list(sec)))
trys = 0
trys = int(input('How many tries do u want to guess the word:'))
used = []

if trys < len(sec):
    print(f'''You won't be able to guess the word in {trys} Chances....''')
    trys = int(input('How many tries do u want to guess the word : '))
    if trys < len(sec):
        trys = len(sec)

def check():
    flag = False
    for k in sec:
        if k not in used:
            flag = False
            break
        else:
            flag = True
    return flag



while (trys):

    if check():
        print(' \n Awsome , You won The Game In Advance!')
        exit(0)
    print('\n'+'-'*50)
    print(f'\n{trys} Chances left .')
    c = input('\n guess a letter : ')
    if len(c) > 1 or len(c) == 0:
        print('\n No cheating!')
    else:
        if c[0] in sec:
            print(' Good ')
            used.append(c[0])
            for i in sec:
                if i in used:
                    print(i, end='.')
                else:
                    print('_', end='.')
        else:
            print(' Hmmmm , Nope ')
            for i in sec:
                if i in used:
                    print(i, end='.')
                else:
                    print('_', end='.')
    trys -= 1


if check():
    print('\n Good , You Win!')
else:
    print('\n Sorry, Better luck Next Time.')
    print(f'The word was : {sec}')
