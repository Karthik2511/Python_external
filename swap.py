# Function to swap two numbers
def swap_numbers(a, b):
    return b, a  # Swap values and return

# Main program
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Swapping numbers using the function
    num1, num2 = swap_numbers(num1, num2)
    
    print(f"After swapping: \nFirst number: {num1} \nSecond number: {num2}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
