my_list = [10, 20, 30, 40, 50]

# Inserting an element at a specific position
my_list.insert(2, 25)  # Insert 25 at index 2
print("List after insertion:", my_list)

# Deleting an element by value
my_list.remove(40)  # Remove the first occurrence of 40
print("List after deletion (by value):", my_list)

# Deleting an element by index
del my_list[1]  # Delete element at index 1
print("List after deletion (by index):", my_list)
