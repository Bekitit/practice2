import random
print("     gussing game")
correct_num = random.randint(1,100)
while True:
    user = int(input("Enter a number 1-100:  "))
    if user > correct_num:
        print("To high please try again")
    elif user < correct_num:
        print("To low please try again")
    else:
        print("You Guess it right")
        break        
    
