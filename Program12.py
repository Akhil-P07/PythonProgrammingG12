from random import randint

op = input("Roll dice? (y/n): ")
if op == "y":
    dice = randint(1,6)
    print("Value of dice:", dice)
