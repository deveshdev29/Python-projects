import random

lower_bound = int(input('Enter the Lower Bound : '))
upper_bound = int(input('Enter the Upper Bound : '))

random_int = random.randint(lower_bound,upper_bound)
print(random_int)
print('------You have 7 chance to guess------')
count = 0
for i in range(7):
    count = count + 1
    guess = int(input(' Enter you guess '))

    if guess < random_int:
        print('----Guess higher----')
    elif guess > random_int:
        print('----Guess Lower----')
    elif guess == random_int:
        print("----That's correct----")
        break