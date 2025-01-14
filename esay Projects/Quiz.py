intro = input('Enter you Name : ')
a = input('Press Enter to Start Quiz Test: ')

Q = [
    {
        "question":"Question 1: Which of the following is not true about dictionary keys?"
,
        "options": '''
         1) More than one key is not allowed.
         2) Keys must be immutable.
         3) Keys must be integers.
         4) When duplicate keys encountered, the last assignment wins.  ''',
        "answer": 1
    },
    {
        "question": '''Question 2: What is the output of following code?
                list1=[4, 3, 7, 6, 4, 9, 5, 0, 3, 2]
                l1=list1[1:10:3]
                print(l1)''',
        "options": '''
         1) [3, 7, 6]
         2) [3, 4, 0]
         3) [3, 6, 9]
         4) [7, 9, 2]''',
        "answer": 2
    }
]
print(type(Q))
score = 0
for question in Q:
    print(question["question"])
    print("Options: ",question["options"])
    option = int(input("Your answer: "))
    
    if option == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print('Name of contestant:', intro)
print('score: ',score,' out of 2.')