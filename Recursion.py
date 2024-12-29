# Recursive function to calculate sum of a given range
def sum_range(start, end):
    if start > end:
        return 0
    else:
        return start + sum_range(start + 1, end)

# Input the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Call the recursive function and print the result
result = sum_range(start, end)
print(f"The sum of numbers from {start} to {end} is: {result}")
