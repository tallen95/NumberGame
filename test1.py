import random

print("Guess the Number!")
cont= True
while cont == True :
    
    user_Range = int(input("Choose a number you would like to pick between: "))
    init_Num = random.randint(1,user_Range)
    
    user_Num = int(input('Think of a number between 1 and ' + str(user_Range) +': '))
    
    if init_Num == user_Num:
        print("You are correct!!!")
    else :
        print("Incorrect")
        print("The random number was: ", init_Num)
        print("Your number was: ", user_Num)
        
    cont = input("Would you like to play again? (Y/N): ")
    if cont.lower() == "y":
        cont = True
    else:
        cont = False
        print("Thanks for playing!")
        
    
    
    
