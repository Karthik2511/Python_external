# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # If divisible by any number other than 1 and itself, not prime
    return True

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
