print('''
     ======================================================================================
                                    WELCOME TO UNIT COVVERTOR
     ======================================================================================
    ''')

choice =1
while choice==1:
    opt=int(input('''                        -------------------------------------------------
                        | Opt |      From       |       |      To       |
                        -------------------------------------------------
                        |  1  |  Centimeter(cm) | --->  | Meter(m)      |
                        |  2  |  Meter(m)       | --->  | kelometer(km) |
                        |  3  |  Meter(m)       | --->  | feet(ft)      |
                        |  4  |  gram(g)        | --->  | Kilogram(kg)  |
                        |  5  |  kilogram       | --->  | ton(t)        |
                        |  6  |  kilogram(kg)   | --->  | Pound(pd)     |
                        |  7  |  rupee(Rs)      | --->  | dollor($)     |
                        |  8  |  dollor($)      | --->  | Rupee(Rs)     |
                        -------------------------------------------------
              
              Enter your Option: '''))
    if opt==1:
        unit= float(input('Enter value in Centimeter(cm) : '))
        print(unit,'cm = ',unit/100,'meter')

    elif opt==2:
        unit= float(input('Enter value in meter(m) : '))
        print(unit,'m = ',unit/1000,'Km')

    elif opt==3:
        unit= float(input('Enter value in meter(m) : '))
        print(unit,'m = ',unit*3.28,'ft') 

    elif opt==4:
        unit= float(input('Enter value in gram(g) : '))
        print(unit,'gm = ',unit/1000,'Kg')

    elif opt==5:
        unit= float(input('Enter value in Kilogram(kg) : '))
        print(unit,'kg = ',unit/1000,'ton')
    
    elif opt==6:
        unit= float(input('Enter value in Kilogram(kg) : '))
        print(unit,'kg = ',unit*2.205,'Lbs')
    
    elif opt==7:
        print("NOTE: 1$ = 82.5 Rs.")
        unit= float(input('Enter amount in Rupee(Rs) : '))
        print(unit,'Rs = ',unit*(1/82.5),'$')
    
    elif opt==8:
        print("NOTE: 1$ = 82.5 Rs.")
        unit= float(input('Enter value in dollor($) : '))
        print(unit,'$ = ',unit*82.5,'Rs',)

    choice = int(input("If You Want to continue Enter 1 if not Enter 0 : "))