import random
import os

items = [
    'Yes', 'No',
    'Rather yes', 'Rather no',
    'I dont know'
]

def start():
    random.shuffle(items)

    for i in items:
        if items.index(i) < 10:
            print(f'''
|-----|
|     |
|  {items.index(i)}  |
|     |
|-----|
    ''')
        else:
            print(f'''
|-----|
|     |
| {items.index(i)}  |
|     |
|-----|
    ''')

    choice = int(input('Your choice --> '))

    if choice < 0 or choice > len(items) - 1:
        print(f'\u001b[31;1mMust choice a number 0 - {len(items) - 1}')
    else:
        print(f'\u001b[37;1mYour result: {items[choice]}')


print('''

\u001b[33;1mThis is a simple divination program.
\u001b[32;1m
[1] - start
[2] - quit

''')

c = int(input('\u001b[37;1mchoice --> '))
if c == 1:
    os.system('clear||cls')
    start()
elif c == 2:
    quit()
else:
    print('\u001b[31;1mWrong number')
