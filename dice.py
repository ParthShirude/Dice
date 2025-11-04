import random

line = '-' * 100
loop = True

while loop:
    dice = str(input("Do you want to roll the dice(y/n): ").lower())
    if (dice == "y" or dice == "yes"):
        while (dice == "y" or dice == "yes"):
            ran = print("(",random.randint(1,6),",",random.randint(1,6),")")
            print(line)
            dice = str(input("Do you want to roll the dice(y/n): ").lower().strip())

            if (dice == "n" or dice == "no"):
                print("Thanks! for Playing with us !!!!!!")
                print(line)
                loop = False
                break
    
            elif (dice != "y"and"yes"and"n"and"no"):
                print("Invalid Input please try again")
                print(line)
                continue

    elif (dice == "n" or dice == "no"):
        print("Thanks! for Playing with us !!!!!!")
        print(line)
        break
        
    else: 
        print("Invalid Input please try again")
        print(line)