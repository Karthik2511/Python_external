import sys

# Function to calculate sum of two numbers
def sum_of_elements(a, b):
    return a + b

# Main Program
if len(sys.argv) != 3:
    print("Usage: python script.py <num1> <num2>")
    sys.exit(1)

try:
    # Convert command line arguments to integers
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    
    # Calculate the sum
    result = sum_of_elements(num1, num2)
    
    # Store the sum in a variable and print it
    print(f"The sum of {num1} and {num2} is {result}")
    
except ValueError:
    print("Please provide valid numbers as arguments.")

#cmd