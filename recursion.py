# Recursive function to calculate factorial
def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Parameters:
    n (int): The number to find the factorial of.
    
    Returns:
    int: Factorial of the given number.
    """
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Main Program
try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
