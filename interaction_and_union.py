# Define two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Union of two lists (using set)
union_result = list(set(list1) | set(list2))
print("Union of two lists:", union_result)

# Intersection of two lists (using set)
intersection_result = list(set(list1) & set(list2))
print("Intersection of two lists:", intersection_result)