import random
print('---------------------------------------------------------------')
print('''             STONE, PAPER AND SEASSOR GAME''')
print('---------------------------------------------------------------')
rounds =int(input('Enter no. of Rounds you want to play: '))
mood = 1
while mood <=rounds:
    print('================================================================')
    p = 'YOu Win'
    print('---------------------------------------------------------------')
    player=int(input('Enter 0 for stone, 1 for paper, 2 for seassor: '))
    print('---------------------------------------------------------------')
    comp= random.randint(0,2)
    if player ==0 and comp == 1 :
        p = 'You Lose'
    elif player== 1 and comp == 2:
        p = 'You Lose'
    elif player==2 and comp ==0:
        p = 'You Lose'
    elif player==comp:
        p = 'Match Drow'
    
    if comp == 1 :
        comp= 'paper'
    if comp ==0:
        comp='stone'
    elif comp ==2 :
        comp= 'seassor'
    if player == 0:
        player = 'stone'
    elif player == 1:
        player = 'paper'
    elif player == 2:
        player = 'seassor'
    print('---------------------------------------------------------------')
    print('player: ',player)
    print('computer: ',comp)
    print('---------------------------------------------------------------')

    print('                         ',p )
    print('---------------------------------------------------------------')
    mood = mood +1
    if mood > rounds:
        break
    mood = int(input('Enter 1 to continue and 0 to Exit: '))
    if mood == 0:
        break
    

    print('================================================================')

    
    
    
