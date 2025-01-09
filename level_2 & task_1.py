import random

def guessing_game():
    
    print(" *** WELCOME TO NUMBER GUESSING GAME! ***")
    print("I'm thinking of a number between 1 and 100.")
    
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
           
            guess = int(input("Enter your guess :- "))
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"CONGRATULATIONS! You guessed the number {target_number} in {attempts} attempts")
                break
        except ValueError:
            print("Invalid input! Please enter a numeric value between 1 and 100")

if __name__ == "__main__":
    guessing_game()