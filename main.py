print("""   GalintavernaDiceRoller V1.0   """)
print("""   Feito por Riel   """)


import random
run = True

print("""
Enter 1 for a D20
Enter 2 for a D12
Enter 3 for a D10
Enter 4 for a D8
Enter 5 for a D6
Enter 6 for a D4
Enter 7 to Exit
""")

while run:
    number = input("Enter number of choice here: ")
    num_dice = int(input("Enter number of dice being rolled: "))
    modifier = int(input("How much to modify the roll by?"))
    end = 0
    total = 0
    while end < num_dice:
        if number == "1":
            roll = int(random.randint(1, 20))
            total += roll
            outcome = total + modifier

        elif number == "2":
            roll = int(random.randint(1, 12))
            total += roll
            outcome = total + modifier

        elif number == "3":
            roll = int(random.randint(1, 10))
            total += roll
            outcome = total + modifier

        elif number == "4":
            roll = int(random.randint(1, 8))
            total += roll
            outcome = total + modifier

        elif number == "5":
            roll = int(random.randint(1, 6))
            total += roll
            outcome = total + modifier

        elif number == "6":
            roll = int(random.randint(1, 4))
            total += roll
            outcome = total + modifier

        end +=1
    if number != "7":
        print("Dice roll: " + str(total) + "+" + str(modifier)+ " = " + str(outcome))
    else:
        run = False