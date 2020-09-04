import requests
#import termcolor
#import pyfiglet
import random

#head = termcolor.colored(pyfiglet.print_figlet('Joke Machine'),'red',attrs = ['blink'])


url = "https://icanhazdadjoke.com/search"
term = input('enter a topic : ')
res = requests.get(url, headers={"Accept": "application/json"}, params={"term": term })
data = res.json()
if len(data['results']) == 0:
    print("No jokes available ! for ",term)
else:
    print(str(len(data['results'])) +' jokes available')
    p = random.choice(data['results'])
    print("Here's a joke : " + str(p['joke']))
