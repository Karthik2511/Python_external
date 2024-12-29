# Recursive function to sum even numbers
def sum_even(n):
    if n <= 0:  # Base case: if n is 0 or negative, return 0
        return 0
    elif n % 2 == 0:  # If n is even, add it to the sum
        return n + sum_even(n - 2)
    else:
        return sum_even(n - 1)  # If n is odd, skip it and check the next number

# Main program
try:
    num = int(input("Enter a number: "))
    result = sum_even(num)
    print(f"The sum of even numbers up to {num} is {result}")
except ValueError:
    print("Please enter a valid integer.")
