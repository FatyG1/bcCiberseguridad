# Calculator exercise: ask the user for two number and an operation

print("      CALCULATOR")
print()
def calculator():
    menu = " +: sum\n -: sub \n /: division\n *: multiplication\n %: rest\n q: exit"
    print(menu)
    op = input("Insert operator: ")
    while op != "q":
        try:
            num1 = float(input("Insert number 1: "))
            num2 = float(input("insert number 2: "))
            dictionary = { "+" : num1 + num2, "-" : num1 - num2, "/" : num1 / num2, "*" : num1 * num2, "%" : num1 % num2}          
            print(num1, op, num2, " = ", dictionary[op])
        except (ZeroDivisionError, ValueError):
            print("That was no valid number. Try again...")
            print()
        except KeyError:
            print("That was no valid operator. Try again...")
            print()
        print(menu)
        print()
        op = input("Insert operator: ")

calculator()

