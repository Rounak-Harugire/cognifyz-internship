import re

def password_strength_checker(password):
    
    min_length = 8

    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if len(password) < min_length:
        return "Weak: Password must be at least 8 characters long"

    if all([has_upper, has_lower, has_digit, has_special]):
        return "Strong: Your password is very secure!"
    elif (has_upper + has_lower + has_digit + has_special) >= 3:
        return "Moderate: Your password could be stronger by including a mix of uppercase, lowercase, digits, and special characters"
    else:
        return "Weak: Your password lacks the necessary complexity."

if __name__ == "__main__":
    user_password = input("Enter your password :- ")
    result = password_strength_checker(user_password)
    print(result)