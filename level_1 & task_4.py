def calculator():
    
    print("Welcome to the Basic Calculator!")
    

    try:
        num1 = float(input("Enter the first number :- "))
        operator = input("Enter an operator (+, -, *, /, %) :- ")
        num2 = float(input("Enter the second number :- "))
    except ValueError:
        print("Invalid input! Please enter numeric values for the numbers")
        return
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed")
            return
    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            print("Error: Modulo by zero is not allowed")
            return
    else:
        print("Invalid operator! Please use one of +, -, *, /, %")
        return
    
    print(f"The result of {num1} {operator} {num2} is: {result}")

if __name__ == "__main__":
    calculator()