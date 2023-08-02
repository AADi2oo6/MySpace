import random
import pickle
def captcha():
    while True:
        a = random.randint(0,9)
        b= random.randint(0,9)
        c=random.randint(0,9)
        d =random.randint(0,9)
                
        print("--------------------"+"\n"+"||]:'",a,"'=|=.",b,"-+||","\n""||,#%",c,"*&$",d,"{|%)||"+'\n'+'--------------------')

        captcha= input('ENTER sum of all numbers : ')           
        if captcha == str(a+b+c+d):
            break

def data_check(name,pin): # Checks Login Info
    try: 
        f=open(profile_location+name+".txt","r")
        a = f.read()
        f.close()
    except FileNotFoundError:
        return False   
    if str(pin) in a: 
        return True
    else :
        return False
    
def train_no(): # Creates new train no,
    for i in range(1,100000):
        try:
            f=open(train_location+str(i)+".txt","r")
            f.close()
        except FileNotFoundError: 
            no = str(i)
            break
    return no

def formate(name,arival,departure):#gives Name of train along with their timing
    new= str()+name
    if len(name)<=30:
        n = 30 -len(name)
        for i in range(1,n):
            new += " " 
    new+="||| "+arival
    if len(arival)<=15:
        n = 20 -len(arival)
        for i in range(1,n):
            new+=" "
    new+="-"+departure
    if len(departure)<=15:
        n = 20 -len(arival)
        for i in range(1,n):
            new+=" "
    return new

def enter(type,comment,limit): # Take input
    while True:
        try:
            a = type(input(comment+' : '))
            if len(str(a))==limit :
                return a
                break
            else:
                print('DAta out of limit (limit of digits =',limit,' )')
        except ValueError:
            print("Value Error")

profile_location= "C:\\Users\\adish\\Desktop\\Python Project 11\\practical X!!\\profile\\"
train_location= "C:\\Users\\adish\\Desktop\\Python Project 11\\practical X!!\\Trains\\"

import datetime
current_time = datetime.datetime.now()       

wecome = '''
    ==============================================================================================================================
                                                           WELCOME
    ==============================================================================================================================
                         1. LOG IN                                                         2.  RESISTER                  
'''
print(wecome)

log = "incomplete"

while True:  # takes input as 1 or 2 

    choise= input('Enter What to do : ')

    print("--------------------------------------------------------------------------------")

    if choise  in  ("1","2"):
        break

    print("Something went Wrong Try to re Enter !!")

while True: # Main loop

    if choise=="1": # TAKS DATA FOR LOGIN 
        while choise == '1' :
            Name = input("INTER NAME :")
            pin = input("Inter YOur passward : ")
            a = captcha()

            result = data_check(Name,pin) #CHECKS WHETHER DATA IS PRESENT IN SYSTEM OR NOT (RETURNS TRUE OR FALSE)

            if result == True :
                print("Logged success fully")
                log = 'complete'
                break

            if result == False:
                print("Name or Passward is worong ")
                choise = input("Enter (1 : retry),(2: creat account) : ")    
    

    if choise== "2": #TAKES DATA FOR RESISTORING
        
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                               CREATE NEW ACCOUNT")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print()
        
        Name= input("Enter Your full name: ").lower().title()

        contact = enter(int,"Inter Your phone Number", 10)
    
        Email = input('Enter Email : ')


        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("**Passward must contain at least 4 numbers only!!")
        passward = enter(int,"Create Passward : ", 4)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
           
        detail = 'Name : '+Name +" \n" + "Contact: "+str(contact) +" \n"+"Email Id: "+Email +" \n"+ "Passward : "+str(passward)+"\n"

        f=open(profile_location+Name+".txt", 'w')
        f.writelines(detail)
        f.close()
        
        print('-----------------------------------------------------------')
        print("Name : ",Name , "         Contact: ",contact,'\n', "Email Id:",Email) # PRINTS DETAIL AT LAST 
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
        print()
        print("--------------| ACCOUNT CREATED SUCCESSFULLY |--------------")
        log = 'complete'
    
    
    if log == "complete" and choise=='3': # BOOK TICKET

##############################################################################################################################3333
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                                BOOK TICKET")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print()

        frm = input('FORM :').lower()
        T0 = input("TO: ").lower()
        
        Enter= input('Press enter to check avibility of trains').lower()

        while True: 
            status =0 #if status ==0 prints train not foiund

            if Enter=='again':
                frm = input('FORM :').lower()
                
                T0 = input("TO: ").lower()
                
                Enter= input('Press enter to check avibility of trains !!')

                ########################################################################################3
            print("-----------------------AVILABLE TRAINS------------------------")
            
            avilable = [] # contain train no for avilabale train
            for i in range(1,int(train_no())): #checks and Rerurn data of all trains avilable 
                
                try:
                    f1 =  open(train_location+str(i)+'.txt','r')
                    a = f1.read() # contain all info of train 
                    f1.close()

                    f1 =  open(train_location+str(i)+'.txt','r')
                    b = f1.readlines() # contain all info of train in form of list
                    f1.close()

                except FileNotFoundError:
                    break
                ###################################################################################################

                if T0 in a and frm in a:
                    status+=1   # if status ==0 printst traion not found
                    avilable.append(str(i))
                    print("--------------------------------------------------------------")
                    print("   Train Name       |  Arival Time   |  Departure Time  ")
                    print("--------------------------------------------------------------")
                    print(i,b[0].lower().title()) ######### prints Train Name
            
                    for i in b : # prints Station details
                         
                        if T0 in i.lower() :
                            print(i.title())        

                        if frm in i.lower() :
                            print(i.title())
                            
                        if "avilable seets" in i.lower():
                            print(i.title())
                        
                    print("--------------------------------------------------------------")
                
                
            if status == 0: #prints train not found
                print('''
                {{{{{{{{{{{NO Train found}}}}}}}}}}}
                            ''')
                
            print(avilable)#avilable contaion train no >
            Enter = input('Enter "again" to recheck or "1" to Continue : ')
            
            if Enter=='1' and status > 0:
                
                while True:
                    book = input("Enter Train no. to check Avibility of ticket : ")
                    if book in avilable:
                        break

                
                f = open(train_location+book+'.txt','r')
                seets = f.readlines() # contaion all lines of train in form of list
                f.close()
                print(seets[1])# prints Avilable tickets (present at index 1 of seets)
                Train_name= seets[0]

                date = input('Select date of jurny :')
                req = enter(int,"Select no. of Tickets: ",1) 

                # changes avilable tickets form train
                new = seets[1].replace(seets[1].split()[3],str(int(seets[1].split()[3])-req))##tickets remain after selecting tikets
                seets.pop(1)
                seets.insert(1,new)

                f = open(train_location+book+'.txt','w')
                f.write("")#cleares the data of the train
                f.close()

                for i in seets: #reinter data to the train
                    f = open(train_location+book+'.txt','a')
                    f.writelines(str(i))
                    f.close()
                
                f = open(profile_location+Name+'.txt','r')
                contact = f.readlines()[1].split()[1]
                f.close()
                ticket_detail= "PNR : "+contact+"          Ticket Booked at: [+"+str(current_time)+"+]"

                f = open(profile_location+Name+'.txt','a')
                
                f.writelines('\n'+ticket_detail+'\n'+formate("DATE: "+date,frm.title(),T0.title())+"TRAIN: "+Train_name.upper())
                f.close()

                for r in range(req):
                    passanger=input('Enter name of passager '+str(r+1)+' :  ')
                    gender = input('Enter gender :')
                    age = input('Enter AGe : ')
                    sum = formate('Name : '+passanger.title(),'Gender : '+gender.capitalize(),'Age : '+age)
                    f=open(profile_location+Name+".txt", 'a')
                    f.writelines(sum+'\n')
                    f.close()

                print('______________________Ticket details______________________',"\n")
                f = open(profile_location+Name+'.txt',"r")
                a = f.readlines()
                f.close()
                temp = open("temp.txt",'w+')
                temp.writelines(a[5:])
                temp.seek(0)
                a1 =temp.read()
                temp.close()
                print(a1)
                break

                # f = open(profile_location+Name+'.txt','r')
                # l = f.read()
                # f.close()
                
                # for i in len(l):
                #     if i >=5 :
                #         len = l.index(i)
                #         pass
                # break

    if log == "complete" and choise=='4': 
        pnr = enter(str(),'Enter PNR no : ',10)
        f = open(profile_location+Name+'.txt',"r")
        a = f.readlines()
        f.close()
        temp = open("temp.txt",'w+')
        temp.writelines(a[5:])
        temp.seek(0)
        a1 =temp.read()
        temp.close()
        if pnr in a1:

            print(a1)
        else :
            print('Ticket Not found !!')



    if choise == "exit":
        exit()

    if choise == 'add':
        print("______________________Add New Train______________________")

        train = input("Enter Train Name: ")
        seets= input('Enter Total seats Avilable in Train :')
        num = train_no() # generates unique no for train file
        

        f = open(train_location+num+'.txt', 'a')
        f.writelines(train)
        f.writelines("\n")
        f.writelines("Avilable Seets : "+seets)
        f.writelines("\n")
        f.close()
    
        while True:
            print("----------------------------------------------------------")

            destination= input("Enter its stopages : " )
            
            arival= input("Input Time of arival  : ")
            
            deparure = input("Input Time of departure: ")

            

            print("----------------------------------------------------------")

            
            f = open(train_location+num+'.txt', 'a')
            f.writelines(formate(destination.lower(),"["+arival.lower()+']',"["+deparure.lower()+']'))
            f.writelines("\n")
            # f.writelines("Avilable Seets = ", seets)
            f.close()

            a = input('(Enter "0000" to exit)or("1" to continue )  : ')
            if a == '0000':
                # f = open("C:\\Users\\adish\\Desktop\\Python Project 11\\practical X!!\\Trains\\"+num+'.txt', 'a')
                # f.writelines("Avilable Seets : "+seets)
                # f.close()
                break


    print("""
    ==============================================================================================================================
                                        1. log in     2.Resistor        3. BOOK TICKET       4.  CHECH TICKET                  
    """)
    while True:
        print("-----------------------------------------------------------------------------")
        choise= input('Enter What to do : ')
        print("-----------------------------------------------------------------------------")
        if choise not in  ("3","4",'1','2','add',"exit"):
            print("Something went Wrong Try to re Enter !!")
            continue
        break

        # def account(username,pin):