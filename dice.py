import random

response = input("Press Y to start and N to stop: ")

while response == "Y":
    number = random.randint(1,6)
    if number == 1:
        print("The Number Is 1")

    if number == 2:
        print("The Number Is 2")

    if number == 3:
        print("The Number Is 3")

    if number == 4:
        print("The Number Is 4")

    if number == 5:
        print("The Number Is 5")

    if number == 6:
        print("The Number Is 6")

while response == "N":
    print("Ok No Rolling Dice For You :)")