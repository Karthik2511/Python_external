# Sample list
my_list = [10, 20, 30, 40, 50]

# 1. Accessing the first element
first_element = my_list[0]
print(f"First Element: {first_element}")

# 2. Accessing the last element
last_element = my_list[-1]
print(f"Last Element: {last_element}")

# 3. Finding the middle element
middle_index = len(my_list) // 2  # Integer division for the middle index
middle_element = my_list[middle_index]
print(f"Middle Element: {middle_element}")

# 4. Concatenating two lists
another_list = [60, 70, 80]
concatenated_list = my_list + another_list
print(f"Concatenated List: {concatenated_list}")

# 5. Deleting an element at a specific index (using `del`)
del my_list[1]  # Delete the element at index 1
print(f"List after deleting element at index 1: {my_list}")

# 6. Removing an element by value (using `remove`)
my_list.remove(40)  # Remove first occurrence of 40
print(f"List after removing 40: {my_list}")

# 7. Length of the list
length_of_list = len(my_list)
print(f"Length of the list: {length_of_list}")

# 8. Slicing a list (getting a subset)
sliced_list = my_list[1:4]  # Getting elements from index 1 to 3
print(f"Sliced List (1 to 3): {sliced_list}")
