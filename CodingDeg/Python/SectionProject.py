# Addition
def add(x, y):
    return x + y
# Subtraction
def subtract(x, y):
    return x - y
# Multiplication
def multiply(x, y):
    return x * y
# Division
def divide(x, y):
    return x / y

while True:
    # user input
    choice = input('''
Please type in the calculation you would like to complete:
1 for addition
2 for subtraction
3 for multiplication
4 for division
''')
    # Check if choice is valid
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
       
        # Check if user wants to stay in program
        next_calculation = input("Try another calculation? (y/n): ")
        if next_calculation == "n":
          print("Don't be a stranger. See ya later!")
          break
    
    else:
        print("Unrecognised command")

