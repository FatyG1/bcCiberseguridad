# Pares or nones exercise: game of pares or nones
import random

userChoice = ""
userNum = 0
machineNum = 0

def paresNones():
    player()
    machine()
    result = (userNum + machineNum) % 2
  
    if userChoice == "pares":
        if result == 0:
            print("You win!")
        else:
             print("You lose. Try again!")
    if userChoice == "nones":    
        if result != 0:
            print("You win!")
        else:
            print("You lose. Try again...")
          
def player():
    global userChoice
    global userNum
    try:
        userChoice = input("Choose pares o nones \n").lower()
        userNum = int(input("Insert number beetwen 0 and 5: \n"))
        while userChoice != "pares" and userChoice != "nones":
             userChoice = input("You need to choose pares or nones. \n")
        while userNum < 0 or userNum > 5:
            userNum = int(input("Insert number beetwen 0 and 5: \n"))
    except (ValueError):
        print("That was no valid number. Try again...")
        userNum = int(input("Insert number beetwen 0 and 5: \n"))
        print()

def machine():
    global machineNum
    machineNum = (random.randint(1,5))
    if userChoice == "pares":
        print("The machine chooses nones and the number ", machineNum)
    else:
         print("The machine chooses pares and the number ", machineNum)
    
paresNones()