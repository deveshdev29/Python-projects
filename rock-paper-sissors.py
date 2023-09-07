import random

def game(comp,you):
    if comp=='rock':
        if you=='rock':
            print('----Draw----')
        elif you=='paper':
            print('----You win----')
        else:
            print('----Sorry, You Lost----')
    if comp=='paper':
        if you=='rock':
            print('----Sorry, You Lost----')
        elif you=='paper':
            print('----Draw----')
        else:
            print('----You win----')
    if comp=='scissor':
        if you=='rock':
            print('----You win----')
        elif you=='paper':
           print('----Sorry, You Lost----')
        else:
           print('----Draw----')


print("Computer's turn.....Done")
comp=random.randint(1,3)
if comp==1:
    comp='rock'
elif comp==2:
    comp='paper'
else:
    comp='scissor'

print("rock")
print('paper')
print('scissor')
you = input('Your turn : ')

game(comp,you)
print(f'Computer choose {comp}')
print(f'You Choose {you}')