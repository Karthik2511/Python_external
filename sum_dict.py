# Function to calculate the sum of values in a dictionary
def sum_of_values(dictionary):
    return sum(dictionary.values())

# Example dictionary
sample_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Calculate the sum
result = sum_of_values(sample_dict)

# Print the result
print("The sum of all values in the dictionary is:", result)
