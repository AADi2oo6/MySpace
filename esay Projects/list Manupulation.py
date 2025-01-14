while True:
    password=input('Enter your password:')
    if password=='LIST@123':
        print('''
             ******************************************************************************
                                          WELCOME TO LIST MANIPULATION
             ******************************************************************************
            ''')
        lis=list(eval(input("Enter a list of numbers:")))
        print("The original list is:",lis)
        choice ='yes'
        while choice=='yes':
            opt=int(input('''What do you want to do with the list :-
                      1.To know the total number of elements
                      2.Arrange the list in increasing order
                      3.Arrange the list in decreasing order
                      4.To know the minimum and maximum number of the list
                      5.To know the sum of all the elements
                      6.To know the index of an element
                      7.To add a new element
                      8.To remove an element
                      9. To check an element is present or not
                      10.Reverse the list
                      11. Empty the list
                      Enter your Option:'''))
            if opt==1:
                  print("Total elements present in the list are:",len(lis))
            elif opt==2:
                lis.sort()
                print('List arranged in increasing order is :',lis)
            elif opt==3:
                lis1=sorted(lis,reverse=True)
                print('List arranged in decreasing order is :',lis1)
            elif opt==4:
                print('Minimum value :',min(lis),'\nMaximum value:',max(lis))
            elif opt==5:
                print('Sum of all elements :',sum(lis))
            elif opt==6:
                n=int(input('Enter the element whose index you wants to know:'))
                i=lis.index(n)
                print('Index of',n, 'is:',i)
            elif opt==7:
                ele=int(input("Enter an element to add:"))
                ans=int(input('''How do you want to add the element
                                            1. At the end of the list
                                            2. At a particular position
                                            Enter your choice:'''))
                if ans==1:
                    lis.append(ele)
                    print("The new list is:",lis)
                else:
                    pos=int(input("At which position you want to add the element:"))
                    lis .insert(pos,ele)
                    print("The new list is:",lis)
            elif opt==8:
                num=int(input('Which element you want to remove? :'))
                if num not in lis:
                        print('Entered element is not present in the list')
                else:
                    lis.remove(num)
                    print('The new list is:',lis)
            elif opt==9:
                sub=int(input('Enter an element to check:'))
                if sub in lis:
                    print("Element is present at",lis.index(sub),"position")
                else:
                    print("Element is not present")
            elif opt==10:
                list=lis[::-1]
                lis=list
                print("Reversed list is:",lis)
            elif opt==11:
                lis.clear()
                print('Empty list:',lis)
            choice=input('Do you want to continue?yes/no')
        print("Thank you for using our app. Have a nice day:) ")
        break
    else:
         print('Please enter a valid password')
   

    
     
        


       
    
            
                      


    
        

