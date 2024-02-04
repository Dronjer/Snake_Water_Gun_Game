import random

win = 0
draw = 0
lose = 0
k = 0
lis = ['Snake', 'Water', 'Gun']

def cmptr_choice(x):
  a = random.choice(x)
  return a


while k<4:    
    b = input('Enter the word Snake, Water, and Gun: ')
    j = cmptr_choice(lis)
    print(f'The user input is: {j}')

    if b not in lis:
        print('Invalid Input')
    elif b == lis[0] and j == lis[1]:
        print('User won the game')
        win += 1
    elif b == lis[1] and j == lis[2]:
        print('User won the game')
        win += 1
    elif b == lis[2] and j == lis[0]:
        print('User won the game')
        win += 1
    elif b == j:
        print('Same input by both user and computer')
        draw += 1
    else:
        print('Computer won the game')
        lose += 1        
    k = k + 1

print(f'The number of games won, loss, and drawn are respectively: {win}, {lose}, {draw}')
if win > lose:
    print()
    print('User won the game')
elif win == lose:
    print()
    print('The game is drawn')
else:
    print()
    print('Computer won the game, Better luck next time')


