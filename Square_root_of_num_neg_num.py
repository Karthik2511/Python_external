import math

while True:
    n = float(input("Enter a number (negative to quit): "))
    if n < 0:
        print("Exiting program.")
        break
    print(f"Square root: {math.sqrt(n):.2f}")
