def celsius_to_fahrenheit(celsius):
   
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
  
    return (fahrenheit - 32) * 5/9

def main():
    print("***TEMPERATURE CONVERTOR***")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    
    choice = input("Choose an option 1 or 2 :- ")
    
    if choice == "1":
        temp = float(input("Enter temperature in Celsius:- "))
        converted_temp = celsius_to_fahrenheit(temp)
        print(f"{temp}Celsius is equal to {converted_temp:.2f}Fahrenheit")
    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit:- "))
        converted_temp = fahrenheit_to_celsius(temp)
        print(f"{temp}Fahrenheit is equal to {converted_temp:.2f}Celsius")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()