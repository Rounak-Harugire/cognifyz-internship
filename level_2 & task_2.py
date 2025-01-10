import random

def number_guesser():
    
    print("*** WELCOME TO NUMBER GUESSER GAME! ***")
    
    try:
        lower_bound = int(input("Enter the lower bound of the range :- "))
        upper_bound = int(input("Enter the upper bound of the range :- "))
        
        if lower_bound >= upper_bound:
            print("Invalid range! The lower bound must be less than the upper bound")
            return
    except ValueError:
        print("Invalid input! Please enter numeric values for the range")
        return
    
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    print(f"I've chosen a number between {lower_bound} and {upper_bound} Try to guess it!")
    
    while True:
        try:
        
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again")
            elif guess > target_number:
                print("Too high! Try again")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts")
                break
        except ValueError:
            print("Invalid input! Please enter a numeric value")

if __name__ == "__main__":
    number_guesser()