# Function to check if there is a common element between two lists
def check_common_element(list1, list2):
    for element in list1:
        if element in list2:
            return True  # Return True if a common element is found
    return False  # Return False if no common elements are found

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

# Check if there is a common element
result = check_common_element(list1, list2)

# Print the result
print(result)
