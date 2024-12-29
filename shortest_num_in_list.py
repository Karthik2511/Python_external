numbers = input("Enter numbers separated by spaces: ").split()

# Find the number with the shortest length
shortest_number = min(numbers, key=len)

print(f"The shortest number is: {shortest_number}")
