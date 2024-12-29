# Function to check if a number is a palindrome
def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Function to check if a number is an Armstrong number
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    return number == sum(int(digit) ** num_digits for digit in num_str)

# Main function
def check_palindrome_and_armstrong(number):
    palindrome = is_palindrome(number)
    armstrong = is_armstrong(number)
    
    if palindrome and armstrong:
        return f"{number} is both a Palindrome and an Armstrong number."
    elif palindrome:
        return f"{number} is a Palindrome but not an Armstrong number."
    elif armstrong:
        return f"{number} is an Armstrong number but not a Palindrome."
    else:
        return f"{number} is neither a Palindrome nor an Armstrong number."

# Example Usage
try:
    number = int(input("Enter a number: "))
    result = check_palindrome_and_armstrong(number)
    print(result)
except ValueError:
    print("Invalid input. Please enter an integer.")
