import random
rule= '''-------------------------------------------------------------------------------------------------  
                            ------------------------------                   
                                    Rules to Play
                            ------------------------------

                    >Rules for Easy Level 1: Arrange X in order to Win.
                    >Rules for Medium Level 2: If no one Win You will win
                    >Rules for Hard Level 3: If computer wins YOu Win.
-------------------------------------------------------------------------------------------------      '''
print(rule)
print('-------------------------------------------------------------------------------------------------')
player =input('Enter Symbol of Player: ')
p = player[0]                                # Takes Symbols of Player and Computer from User
comp = input('Select Symbol of Computer:')
c = comp[0]
print('-------------------------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------------------')

mode = input('Select mode 1 for easy,2 for medium & 3 for hard: ') #Decides Level of game

while  mode not in ['1','2','3'] :
    print('''
                    -------------------------------------------------
                    This Mode is Not Avilable Select correct Mode!
                    -------------------------------------------------
         ''')
    mode = input('Select mode 1 for easy,2 for medium & 3 for hard: ')
print('-------------------------------------------------------------------------------------------------')

a='''                                      1 | 2 | 3 
                                     ---|---|---
                                      4 | 5 | 6
                                     ---|---|---
                                      7 | 8 | 9'''

intrest = '1'

note = ""

while intrest == '1':
    
    if mode =='1' :
        rslt1='\U0001F973',"YOU Win",'\U0001F60E'
        rslt2='\U0001F480','You Lose!','\U0001F494'
        rslt3='\U0001F47B','Drow','\U0001F92D'
    elif mode =='3':
        note = 'NOTE: If Computer Wins Then You win'
        rslt1='\U0001F480','You Lose!','\U0001F494'            #  Show Results for Different levels
        rslt2='\U0001F973',"YOU Win",'\U0001F60E'
        rslt3='\U0001F47B','Drow','\U0001F92D'
    elif mode =='2':
        note = 'NOTE: If No one Wins you Will win'
        rslt1='\U0001F480','You Lose!','\U0001F494'
        rslt2='\U0001F480','You Lose!','\U0001F494'
        rslt3='\U0001F973',"YOU Win",'\U0001F60E'

    print(note)
    print('-------------------------------------------------------------------------------------------------')
    start = input('Press Enter to Start : ')
    print('-------------------------------------------------------------------------------------------------')
    if start == '': 
                 
            print('')
            print(a)
            print('')

            no = [1,2,3,4,5,6,7,8,9]

            while len(no)>=0:
                win1= a[38]==a[42]==a[46]==p or a[136]==a[140]==a[144]==p or a[233]==a[237]==a[241]==p
                win2=a[38]==a[136]==a[233]==p or a[42]==a[140]==a[237]==p or a[46]==a[144]==a[241]==p
                win3=a[38]==a[140]==a[241]==p or a[46]==a[140]==a[233]==p                                  
                win4= a[38]==a[42]==a[46]==c or a[136]==a[140]==a[144]==c or a[233]==a[237]==a[241]==c
                win5=a[38]==a[136]==a[233]==c or a[42]==a[140]==a[237]==c or a[46]==a[144]==a[241]==c
                win6=a[38]==a[140]==a[241]==c or a[46]==a[140]==a[233]==c

                if win1 or win2 or win3 :
                    print(rslt1)
                    
                    break
                elif win4 or win5 or win6:
                    print(rslt2)                          #check Condition of winning.
                    
                    break
                elif len(no)==0:
                    print(rslt3)
                    
                    break
                print('-------------------------------------------------------------------------------------------------')
                b = input("Select Your Position : ")# users choise
                
                while b not in a:
                    print("-->Positon Not Avilable!")
                    b = input("Select Correct Position : ")# users choise
                print('-------------------------------------------------------------------------------------------------')

                a = a.replace(b,p)
                n = no.remove(int(b))#removes user input fom list

                if len(no)>0:
                    com = str(random.choice(no))#computers choise
                    a = a.replace(com,c)
                    n = no.remove(int(com))

                print("")
                print(a)
                print("")
    print('-------------------------------------------------------------------------------------------------')

         # Asks What to do next when game overs.
    intrest = input('press ( 0 -> Exit)  or (1 -> Replay) or (2 -> Change mode) or (3 -> Change Symbol): ')     
    while intrest not in ['0','1','2','3']:
        print('''
                    -------------------------------------------------
                      This Key is Not Avilable Select correct Key!
                    -------------------------------------------------
                    ''')
        intrest = input('press ( 0 -> Exit)  or (1 -> Replay) or (2 -> Change mode) or (3 -> Change Symbol): ')

    print('-------------------------------------------------------------------------------------------------')

    while intrest =='0' or intrest =='2' or intrest =='3':                
        
        if intrest =='0': 
            exit()
        elif intrest == '2':
            mode = input('Select mode 1 for easy,2 for medium & 3 for hard: ')
            print('-------------------------------------------------------------------------------------------------')
            
            while  mode not in ['1','2','3'] :
                print('''
                    -------------------------------------------------
                     This Mode is Not Avilable Select correct Mode!
                    -------------------------------------------------
                    ''')
                mode = input('Select mode 1 for easy,2 for medium & 3 for hard: ')
            print('-------------------------------------------------------------------------------------------------')

        elif intrest == '3':
            print('-------------------------------------------------------------------------------------------------')
            player =input('Enter Symbol of Player: ')
            p = player[0]
            comp = input('Select Symbol of Computer:')
            c = comp[0]
            print('-------------------------------------------------------------------------------------------------')
        
        print('-------------------------------------------------------------------------------------------------')
        intrest = input('press ( 0 -> Exit)  or (1 -> Start Game) or (2 -> Change mode) or (3 -> Change Symbol): ')
        while intrest not in ['0','1','2','3']:
            print('''
                            -------------------------------------------------
                            This Key is Not Avilable Select correct Key!
                            -------------------------------------------------
                        ''')
            intrest = input('press ( 0 -> Exit)  or (1 -> Start Game) or (2 -> Change mode) or (3 -> Change Symbol): ')
        print('-------------------------------------------------------------------------------------------------')
    
    # if Player choose replay it Clears the game board
    no = [1,2,3,4,5,6,7,8,9]
    a='''                                      1 | 2 | 3 
                                     ---|---|---
                                      4 | 5 | 6
                                     ---|---|---
                                      7 | 8 | 9'''
        
        
            




