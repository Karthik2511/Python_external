import copy

# Shallow Copy Example (for Lists)
def shallow_copy(original_list):
    return original_list.copy()

# Deep Copy Example (for Nested Lists)
def deep_copy(original_list):
    return copy.deepcopy(original_list)

# Example with a Custom Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Cloning a Custom Object
def clone_object(original_object):
    return copy.deepcopy(original_object)

# Main Program
if __name__ == "__main__":
    # List Example
    original_list = [1, [2, 3], 4]
    shallow = shallow_copy(original_list)
    deep = deep_copy(original_list)
    
    # Modify the nested list in original
    original_list[1][0] = 'X'
    
    print("Original List:", original_list)
    print("Shallow Copy:", shallow)
    print("Deep Copy:", deep)
    
    # Object Example
    person1 = Person("Alice", 25)
    person2 = clone_object(person1)
    
    print("\nOriginal Object:")
    person1.display()
    print("Cloned Object:")
    person2.display()
    
    # Modify the original object
    person1.name = "Bob"
    print("\nAfter Modifying Original Object:")
    person1.display()
    print("Cloned Object Remains Unchanged:")
    person2.display()
