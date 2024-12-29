# Using the ** operator
def exponential_using_operator(base, exponent):
    return base ** exponent

# Using the math.exp() function for e^x
import math
def exponential_using_math(base):
    return math.exp(base)

# Get user input
number = float(input("Enter a number: "))
exponent = float(input("Enter the exponent (if needed): "))

# Calculate the exponential using the ** operator
result_operator = exponential_using_operator(number, exponent)
print(f"{number} raised to the power of {exponent} is: {result_operator}")

# Calculate the exponential using math.exp() (only for e^x)
result_math_exp = exponential_using_math(number)
print(f"e raised to the power of {number} is: {result_math_exp}")
