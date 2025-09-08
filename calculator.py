# #Simple 2 number calculator

# operator = input("Enter an operator(+ - * /): ")
# num1 = float(input("Enter 1st number: "))
# num2 = float(input("Enter 2nd number: "))

# if operator == "+":
#     result = num1 + num2
#     print(round(result,3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result,3))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result,3))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result,3))
# else:
#     print(f"{operator} is not valid operator")
    

#Simple calculator with menu
import math
while True:
    print("\n===== Calculator Menu =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Quit")
    
    choice = input("Enter your choice (1-9): ")

    if choice == "9":
        print("Exiting... Goodbye!")
        break
    if choice in ["7", "8"]:
        num = float(input("Enter a number: "))
        if choice == "7":
            if num < 0:
                print("Error: Cannot take square root of negative number")
            else:
                print("Result:", math.sqrt(num))
        elif choice == "8":
            if num < 0 or not num.is_integer():
                print("Error: Factorial only works for non-negative integers")
            else:
                print("Result:", math.factorial(int(num)))
    else:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        if choice == "1":
            print("Result:",num1 + num2,)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero")
            else:
                print("Result:", round(num1 / num2, 3))
        elif choice == "5":
            print("Result:", num1 ** num2)
        elif choice == "6":
            print("Result:", num1 % num2)
        else:
            print("Invalid choice, please try again.")
            
            
            
            
            