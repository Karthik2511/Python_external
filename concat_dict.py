# Function to concatenate two dictionaries
def concatenate_dicts(dict1, dict2):
    # Using the update() method to merge dict2 into dict1
    dict1.update(dict2)
    return dict1

# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Concatenate dictionaries
result = concatenate_dicts(dict1, dict2)

# Print the result
print("Concatenated Dictionary:", result)
